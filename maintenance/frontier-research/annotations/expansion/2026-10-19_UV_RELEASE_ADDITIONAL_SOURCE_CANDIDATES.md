# Additional 2026 source-selection evidence — reconciliation of superseded PR #148

## Identity, trigger, history
- Repository: `lostlight530/auto-doc-engine`; evidence-check date: **2026-10-19**; record type: `ADDITIVE_CANDIDATE_EVIDENCE / SOURCE_BOUNDED`.
- Parallel proposal [#148](https://github.com/lostlight530/auto-doc-engine/pull/148) was based on an older `main`. While it was being researched, native Stages I–K, open L, the index correction and other source-selection reconciliations were merged independently.
- **Main's earlier Stage files, Part IDs, month selections, syntheses and A2 index retain authority.** This record selects only source objects not carried as native findings by those prior sampled Stage owners; it does not reclassify the older selections or rewrite their negative space.
- `CURRENT_BRANCH_SOURCE_SHA` at this note's preparation: `31e110d7a6f5c7404c73344712619b499a4758ec`. Later states must be checked separately.

## Distinct upstream versioned candidate objects
| Intended quarter / month | GitHub release published | Exact source | Release-described observation | Interpretation and limitation |
|---|---|---|---|---|
| 2026-Q1 / January | 2026-01-06 | [astral-sh/uv 0.9.22](https://github.com/astral-sh/uv/releases/tag/0.9.22) | Release note introduces a dedicated missing-lockfile diagnostic and filters unusable wheel architectures from lockfiles. | Missing lock, resolver metadata, installation feasibility and reproduction remain separate. This event is distinct from the earlier uv 0.9.23 candidate. |
| 2026-Q2 / April | 2026-04-01 | [astral-sh/uv 0.11.3](https://github.com/astral-sh/uv/releases/tag/0.11.3) | Release expands uv workspace metadata with lock dependencies and describes validation of platform/hash behavior. | Workspace/lock disclosure is not executed-environment evidence. Distinct from existing 0.11.4 and 0.11.6 supplemental records. |
| 2026-Q2 / May | 2026-05-28 | [astral-sh/uv 0.11.17](https://github.com/astral-sh/uv/releases/tag/0.11.17) | Release fixes transitive Git archive lock behavior and preserves Git repository URLs in direct URL metadata. | A source URL is provenance context, not content attestation. Distinct from 0.11.9 and 0.11.15 supplemental versions. |
| 2026-Q3 / July | 2026-07-31 | [astral-sh/uv 0.12.1](https://github.com/astral-sh/uv/releases/tag/0.12.1) | Release introduces lock validation / canonical lock parsing-related fixes and preview checks around metadata-free locks. | Lock parsing, URL constraint handling and realized installation differ. Distinct from native/expanded 0.12.0 source. |

## Executed method and source authority
On **2026-10-19**, the connected GitHub API was used to inspect upstream tagged-release listings and the exact `/repos/{owner}/{repo}/releases/tags/{tag}` release-note bodies for every listed candidate. Dates are the publisher's GitHub published-at timestamps, not repository execution dates. A release notice reports what its issuer says it changed; it is not independent corroboration, downstream adoption, runtime execution, a security test, or proof of semantic equivalence. Retrieval is `SOURCE_BOUNDED`, not an exhaustive field search.

## Analytic delta and counter-reading
The native Stage I–K selections and existing two uv expansion notes remain authoritative; the superseded parallel PR #148 contains four further distinct uv version objects not added to its original registers.

The four release objects form **one uv originating publisher family**. Read together they raise a specific hypothesis: evidence can fail at absent lock, workspace metadata, Git source identity, and parser validation before a converter runs. This is an interpretation across different version events, **not** independent corroboration or a claim that this repository executed uv.

**Strong alternative:** ordinary maintenance and purposive selection may explain these release differences better than any field-wide turning point. The number of upstream versions does not measure progress or independent confirmation. No external contradictory-source search, local experiment, artifact replay, formal methods review or current repository audit was performed for this addendum.

## Disposition / temporal and governance boundary
- `HOLD_FOR_EXPLICIT_STAGE_SELECTION_AMENDMENT`: these are **supplemental candidates**, not silently admitted objects in Stage I–K's original `SOURCE_OBJECT_REGISTER` or `EVIDENCE_CHART`.
- Proposed elevation requires dated Stage study-design amendment or new correction/reconciliation, source IDs, charting and bounded review; preserve the original publication/source-selection snapshot.
- Stage L remains `OPEN / 2026-Q4`; 2026 year remains `YEAR_OPEN`. No local drift established and no runtime or contract change.
- This addendum preserves the provenance of why overlapping PR #148 should **not** be merged; it does not assert independent review.
