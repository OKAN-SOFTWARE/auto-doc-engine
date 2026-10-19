#!/usr/bin/env python3
"""Provider-neutral, allowlisted, synchronous tool adapter.

Explicitly *not* an MCP server, arbitrary code executor, autonomous planner,
external LLM client, or scientific validation authority. No automatic writes.
"""
from __future__ import annotations

import json
from typing import Any

PROFILE = "auto-doc-engine/tool-adapter"
_SPECS = [
  {
    "name": "document_inspect",
    "description": "Inspect local Markdown links, frontmatter and optional readability without mutating the input documents.",
    "parameters": {
      "type": "object",
      "properties": {
        "docs_dir": {
          "type": "string",
          "description": "Local Markdown folder to inspect"
        },
        "with_readability": {
          "type": "boolean",
          "description": "Include heuristic readability checks"
        }
      },
      "required": [
        "docs_dir"
      ],
      "additionalProperties": False
    }
  },
  {
    "name": "artifact_lineage",
    "description": "Build a caller-declared artifact lineage handoff in memory, without writing a sidecar.",
    "parameters": {
      "type": "object",
      "properties": {
        "artifact_record": {
          "type": "string",
          "description": "Existing auto-doc-engine/artifact-record JSON sidecar"
        },
        "relations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "relation": {
                "type": "string",
                "enum": [
                  "derived-from",
                  "revision-of",
                  "supersedes",
                  "uses",
                  "related-to"
                ]
              },
              "target": {
                "type": "string"
              }
            },
            "required": [
              "relation",
              "target"
            ],
            "additionalProperties": False
          }
        }
      },
      "required": [
        "artifact_record"
      ],
      "additionalProperties": False
    }
  }
]


TOOL_SPECS = {item["name"]: item for item in _SPECS}


def tool_definitions() -> list[dict]:
    """JSON-Schema function declarations usable by a caller-managed Agent."""
    return [{"type": "function", "function": {
        "name": spec["name"], "description": spec["description"],
        "parameters": spec["parameters"],
    }} for spec in _SPECS]


def _check_arguments(name: str, arguments: Any) -> dict:
    if not isinstance(arguments, dict):
        raise ValueError("arguments must be a JSON object")
    schema = TOOL_SPECS[name]["parameters"]
    properties = schema["properties"]
    unknown = set(arguments) - set(properties)
    if unknown:
        raise ValueError("unexpected argument(s): " + ", ".join(sorted(unknown)))
    missing = set(schema.get("required", [])) - set(arguments)
    if missing:
        raise ValueError("missing argument(s): " + ", ".join(sorted(missing)))
    for key, value in arguments.items():
        typ = properties[key]["type"]
        if typ == "string" and (not isinstance(value, str) or not value.strip()):
            raise ValueError(key + " must be a nonempty string")
        if typ == "boolean" and not isinstance(value, bool):
            raise ValueError(key + " must be a boolean")
        if typ == "array" and not isinstance(value, list):
            raise ValueError(key + " must be an array")
    return arguments


def _dispatch(name: str, a: dict) -> Any:
    if name == "document_inspect":
        from core.doctor import run_doctor
        report = run_doctor(a["docs_dir"], with_readability=a.get("with_readability", True))
        return {"report": report.to_dict(), "diagnostic_exit_code": report.exit_code(),
                "meaning": "local document diagnostics, not source verification"}
    if name == "artifact_lineage":
        from core.artifact_lineage import build_artifact_lineage
        relations = a.get("relations", [])
        if any(not isinstance(x, dict) or set(x) != {"relation", "target"}
               or not all(isinstance(v, str) and v.strip() for v in x.values())
               for x in relations):
            raise ValueError("relations must be objects with nonempty relation and target strings")
        return build_artifact_lineage(a["artifact_record"],
                                      relations=[(x["relation"], x["target"]) for x in relations])
    raise ValueError("unknown tool")


def execute_tool_call(name: str, arguments: dict | str) -> dict:
    """Dispatch an allowlisted call and return a stable JSON-serializable envelope.

    String arguments are accepted for model function-call interoperability.
    Domain findings live inside result; status=ok never means scientific truth.
    """
    envelope = {
        "profile": PROFILE, "tool": name, "status": "error",
        "result": None, "error": None,
        "scientific_validity_claim": False,
        "remote_provider_called": False,
    }
    if name not in TOOL_SPECS:
        envelope["error"] = {"code": "UNKNOWN_TOOL", "message": "tool is not allowlisted"}
        return envelope
    try:
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as exc:
                raise ValueError("arguments are not valid JSON") from exc
        checked = _check_arguments(name, arguments)
    except (ValueError, TypeError) as exc:
        envelope["error"] = {"code": "INVALID_ARGUMENT", "message": str(exc)}
        return envelope
    try:
        envelope["result"] = _dispatch(name, checked)
        envelope["status"] = "ok"
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        envelope["error"] = {"code": "EXECUTION_FAILED", "message": str(exc)}
    except Exception as exc:
        # Third-party validators may raise domain-specific exception classes.
        # Preserve a structured failure, never emit a traceback on JSON stdout.
        envelope["error"] = {"code": "INTERNAL_ERROR", "message": type(exc).__name__ + ": " + str(exc)}
    return envelope


def list_tool_names() -> list[str]:
    return sorted(TOOL_SPECS)
