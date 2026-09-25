# Documentation corpus audit

**As of:** 2026-09-25  
**Issue:** #338  
**Corpus:** 158 Markdown files on `main` at audit start

## Classification vocabulary

- **CANONICAL** — authoritative live knowledge for a defined concept.
- **DERIVED** — navigation/ranking/index/report derived from canonical evidence.
- **HISTORICAL** — frozen or superseded snapshot retained for provenance.
- **GUIDANCE** — operating/contributor/template instructions.
- **LOG** — chronological record; never current truth.
- **ARCHIVE** — intentionally retired material. No current files require physical archive placement before #332/#334.

## Complete classification by path rule

The rules below cover all 158 Markdown files; exceptions are listed explicitly.

| Path / rule | Count | Classification | Notes |
|---|---:|---|---|
| root Markdown | 7 | mixed, explicit below | operating surfaces |
| `.github/pull_request_template.md` | 1 | GUIDANCE | PR audit template |
| `research/_templates/*.md` | 2 | GUIDANCE | reusable research templates |
| `research/backtests/261/**` | 23 | HISTORICAL | frozen validation corpus; immutable semantics |
| `research/cross-theme/**` | 7 | CANONICAL research evidence, except dated discovery snapshots may become HISTORICAL when superseded | cross-theme structural work |
| `research/energy/**` | 44 | CANONICAL evidence/company/theme docs; `synthesis-ranking.md` DERIVED | theme corpus |
| `research/memory/**` | 25 | CANONICAL evidence/company/theme docs; `synthesis-ranking.md` DERIVED | theme corpus |
| `research/physical-ai/**` | 24 | CANONICAL evidence/company/theme docs; `synthesis-ranking.md` DERIVED | theme corpus |
| `research/robotics-actuators/**` | 10 | CANONICAL evidence/company/theme docs; `synthesis-ranking.md` DERIVED | theme corpus |
| `research/scientific-ai/**` | 3 | CANONICAL research evidence | theme corpus |
| `sources/**` | 2 | CANONICAL provenance/supporting evidence | source records |
| `articles/**` | 1 | DERIVED | publication/output, not research authority |
| root-level `research/*.md` | 9 | mixed, explicit below | cross-theme live/historical surfaces |

### Root files

| File | Classification | Authority |
|---|---|---|
| `README.md` | GUIDANCE | navigation/purpose |
| `AGENTS.md` | GUIDANCE | mandatory agent operating rules |
| `AUTOMATION.md` | CANONICAL | queue/scheduler semantics |
| `CONTRIBUTING.md` | GUIDANCE | contributor workflow |
| `PORTFOLIO.md` | CANONICAL | Gate-E portfolio mandate/rules |
| `watchlist.md` | DERIVED | cross-theme index; company evidence/state must resolve upstream |
| `CHANGELOG.md` | LOG | what changed, never current truth |

### Root-level research files

| File | Classification | Authority |
|---|---|---|
| `prediction-calibration-ledger.md` | CANONICAL | only live prospective calibration ledger |
| `decision-outcome-calibration-ledger.md` | HISTORICAL | Wave-5 seed snapshot |
| `top10-unicorn-priority.md` | CANONICAL | live ranked research universe |
| `unicorn-potential.md` | CANONICAL | multibagger/reverse-underwrite funnel |
| `top10-capital-allocation.md` | HISTORICAL | old Gate-D valuation/downside layer |
| `gate-e-portfolio-construction.md` | HISTORICAL | portfolio construction snapshot; live rules in PORTFOLIO |
| `gate-e-thesis-first-entry-sprint.md` | HISTORICAL | completed sprint artifact |
| `evidence-quality-audit.md` | CANONICAL | current evidence-quality control/audit surface |
| `evidence-quality-corpus-audit.md` | HISTORICAL | corpus audit snapshot |

## Drift findings

1. **Ranking duplication risk:** theme rankings, watchlist and top-level ranking all mention company state. Resolution: top-level ranking owns cross-theme order; theme rankings are derived; company evidence remains in canonical company files.
2. **Portfolio duplication risk:** historical Gate-D and Gate-E construction documents can be mistaken for current action rules. Resolution: `PORTFOLIO.md` + live company monitor/company evidence own current Gate-E semantics.
3. **Calibration duplication:** two ledgers exist. This is already resolved in-file: prediction ledger is live; decision-outcome ledger is historical.
4. **Issue/document duplication:** several issues contain substantial research history. Issues remain workflow/audit surfaces; durable conclusions must land in canonical documents.
5. **Freshness ambiguity:** many research files do not expose an explicit as-of/version header. #340 will define where this is required rather than mechanically adding metadata to all files.
6. **Path churn risk:** the corpus is coherent by theme despite root-level clutter. Physical reorganization should be selective, not aesthetic.

## Audit conclusion

No document is being deleted during this baseline. The corpus is classifiable without losing provenance. The main defect is **authority ambiguity**, not absence of research. Consolidation (#339) should remove competing mutable state before any large path migration.
