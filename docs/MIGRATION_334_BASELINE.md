# Canonical artifact migration baseline (#334)

**As of:** 2026-09-25
**Lifecycle:** HISTORICAL
**Base commit:** `afc41f078fcf4efd6cb0f4b2fd273d95afb5317c`

This records the default branch before the path migration. The [repository authority map](REPOSITORY_GOVERNANCE.md) owns current locations; this file is comparison evidence, not another live source.

| Concept | Before path | SHA-256 of tracked content |
|---|---|---|
| Cross-theme ranking, 65 live company entries | `research/top10-unicorn-priority.md` | `efd74cba11a75e7cf10b1651f174abba3219c983ac9c2b9be1b19cde930e19ea` |
| Portfolio rules/current checkpoint | `PORTFOLIO.md` | `994274d0254c2e194a921362cb5e63431e0f1b0c10503b6f1082be6c5d728816` |
| Prospective calibration ledger | `research/prediction-calibration-ledger.md` | `6e4d86d792d29ae8e7e89017c1bc0202e91bd809313f9e291288f216c9dbf50e` |
| Historical Wave-5 seed | `research/decision-outcome-calibration-ledger.md` | `3731a4b35629843d903b32be119fe0e3ec8713862656ac165b4530a96e0e5c93` |
| Historical Gate-D allocation | `research/top10-capital-allocation.md` | `d66c25ea9f34be62899b94dbad07a46c06ea6efbd77f66c7f950b43458f4e848` |

The transaction-rules section (`## Transaction rules` through the next `## Bottleneck-migration framework` heading) has SHA-256 `7b97a353ca436bac4e84d24e59d8256eddf063aa656a4472d83cb1e2db818d9d`. The 23 tracked files in `research/backtests/261/` have manifest SHA-256 `38d748d234da61a72f9f82f7bf062dca614a61caef515490fef0575d6adfac20` (sorted `path SHA-256` lines). `scripts/frozen-261.json` supplies the per-file CI comparison.

The live ranking states and company classifications are in the ranked file at the base commit. The prospective v2 backlog at capture is #325 READY, #326 BLOCKED, #327 READY, #328 BLOCKED, #329 BLOCKED and #330 READY; #261 is WAITING. None is within the migration's research scope.

Expected migration: move the uniquely authoritative ranked universe to a name without the obsolete Top-10 implication, repair all live references, and keep the ranked file bytes, portfolio transaction section, prospective ledger and #261 corpus identical. Stable theme/company trees remain in place under the architecture's explicit no-aesthetic-moves rule.
