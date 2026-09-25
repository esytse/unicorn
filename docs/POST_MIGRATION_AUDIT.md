# Post-migration repository audit (#337)

**As of:** 2026-09-25
**Lifecycle:** HISTORICAL
**Compared:** pre-migration `afc41f078fcf4efd6cb0f4b2fd273d95afb5317c` to merged `main` `876719443c5dc154c777d3b7a824a4f533a9825e`

This audit compares the repository itself with [the captured baseline](MIGRATION_334_BASELINE.md), not the migration PR description. The current authority map remains [REPOSITORY_GOVERNANCE.md](REPOSITORY_GOVERNANCE.md).

| Check | Evidence and result |
|---|---|
| Canonical-source inventory | The sole live ranked source moved from `research/top10-unicorn-priority.md` to `research/ranked-universe.md` (Git reports a 100% rename). `PORTFOLIO.md`, the prospective ledger, company/theme evidence and source provenance retained their homes. The authority map declares one live path for each of ranking, portfolio and prospective checkpoints. |
| #261 frozen corpus | All 23 tracked files remain; sorted path/content-hash manifest is `38d748d234da61a72f9f82f7bf062dca614a61caef515490fef0575d6adfac20`, identical to baseline and per-file integrity manifest. |
| Ranking and company classifications | Ranked file SHA-256 is `efd74cba11a75e7cf10b1651f174abba3219c983ac9c2b9be1b19cde930e19ea`, byte-identical to baseline; all 65 live rows therefore retain their rank/state. No company evidence file changed in the migration/navigation diff. |
| Portfolio and transaction rules | `PORTFOLIO.md` changed only ranking-path references. Transaction-rules section SHA-256 remains `7b97a353ca436bac4e84d24e59d8256eddf063aa656a4472d83cb1e2db818d9d`. |
| Prospective validation | `research/prediction-calibration-ledger.md` SHA-256 remains `6e4d86d792d29ae8e7e89017c1bc0202e91bd809313f9e291288f216c9dbf50e`. The historical seed ledger is also byte-identical. #325/#327/#330 remain READY; #326/#328/#329 remain BLOCKED on their stated prerequisites. No v2 experiment was run. |
| References and orphans | Old ranked path is absent. Active repository references route to the new path; only dated `CHANGELOG.md` entries and the pre-migration baseline preserve the former path as history. README links and all Markdown local links pass the integrity scan. The renamed file is linked directly by README, PORTFOLIO, AUTOMATION, watchlist and the authority map. Stable theme/company trees were deliberately retained. |
| Duplicate live state | Ranking and portfolio have one declared live authority each. Theme rankings and watchlist identify their upstream sources; historical Gate-D and completed Gate-E artifacts identify their non-current role. |
| Open-issue execution state | Inspected 36 open issues after #336. All have the eight required metadata fields. No READY issue has an unresolved dependency, no BLOCKED issue lacks one, and EPIC/WAITING/PARKED work is excluded from execution. #337 is the only hygiene issue RUNNING during this audit. |

## Checks

- `python3 -m unittest discover -s scripts -p 'test_*.py'`: 15 passed, including deliberately failing corruption fixtures.
- `python3 scripts/repo_integrity.py`: 0 errors, including Markdown links, authority references, metadata and frozen #261 contents.
- `git diff --check`: clean.
- Research governance CI for migration PR #347 and navigation PR #348: passed before merge. This audit PR must independently pass the same required workflow before merge.

No material residual repository hygiene defect was found. The old `top10` wording in dated changelog entries remains as historical evidence; the live ranking title, path and #110 EPIC now describe an uncapped universe. Current investment conclusions and transaction actions were not reviewed or changed by this structural audit.
