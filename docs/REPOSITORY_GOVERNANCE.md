# Repository architecture and canonical-source map

**As of:** 2026-09-25  
**Issues:** #331, #333, #338  
**Status:** baseline before structural migration

## Purpose

Unicorn is a research system, not a collection of independent Markdown notes. This map defines which artifact owns each live concept so refactoring can preserve provenance and avoid competing truths.

## Canonical-source rules

1. One live concept has one canonical source.
2. Issues own workflow state; documents own durable knowledge.
3. Derived views may summarize canonical sources but must not silently become authoritative.
4. Historical/frozen records are append-only or immutable according to their own rules.
5. Git history is the detailed version record; do not create version-suffixed duplicates.
6. A move is not allowed until inbound references and regression tests are known.
7. Repo cleanup must not change a research conclusion, portfolio rule or frozen validation result.

## Canonical source map

| Concept | Canonical source | Derived / supporting views | Lifecycle |
|---|---|---|---|
| Repository purpose / navigation | `README.md` | `CONTRIBUTING.md` | live guidance |
| Agent operating rules | `AGENTS.md` | README workflow summary | live guidance |
| Queue states / scheduler protocol | `AUTOMATION.md` | issue metadata, README summary | live canonical |
| Portfolio mandate / Gate-E operating rules | `PORTFOLIO.md` | company monitors, ranking views | live canonical |
| Cross-theme candidate index | `watchlist.md` | theme rankings | **derived index**; not authority for company evidence |
| Live ranked research universe | `research/top10-unicorn-priority.md` | watchlist/theme rankings | live canonical |
| Multibagger discovery / reverse-underwrite funnel | `research/unicorn-potential.md` | company files | live canonical |
| Live prospective calibration checkpoints | `research/prediction-calibration-ledger.md` | issue checkpoints | live canonical |
| Wave-5 seed calibration snapshot | `research/decision-outcome-calibration-ledger.md` | none | historical; no parallel live updates |
| Historical Gate-D valuation layer | `research/top10-capital-allocation.md` | none | historical context |
| Current company evidence/thesis | relevant canonical company/deep-dive file | watchlist, ranking, issue | live canonical per company |
| Theme thesis / value chain | each theme's `thesis.md` / `value-chain.md` | synthesis/deep dives | live canonical per theme |
| Theme research queue/plan | each theme's `research-plan.md` | GitHub issues | research-plan document; GitHub issue state wins for execution |
| Theme ranking | each theme's `synthesis-ranking.md` | watchlist/top-level ranking | derived theme view |
| Historical validation #261 | `research/backtests/261/**` | `SUMMARY.md` as entry point | frozen historical corpus |
| Source provenance | `sources/source-register.md` plus recoverable inline sources | company/deep-dive citations | canonical provenance register |
| Change history | `CHANGELOG.md` | Git history / PRs | log, never current truth |

## Target information architecture

Do **not** bulk-move files yet. The safe target is conceptual first:

- `methodology/` or a methodology index for versioned research rules.
- `discovery/` for architecture-first scans and negative-search records.
- existing theme/company trees for canonical research.
- `portfolio/` or a portfolio index for live allocation/ranking/transaction-rule surfaces.
- `validation/historical/` and `validation/prospective/` conceptually separated.
- monitors remain GitHub issues; durable findings land in canonical documents.
- `archive/` only for genuinely superseded material where Git history alone is insufficient.

Whether these become physical folders is deferred to #332. Stable paths may be preferable to cosmetic moves.

## Migration sequence

1. Finish documentation/backlog baseline (#338/#333).
2. Add integrity tests (#335/#341).
3. Codify target lifecycle/structure (#332).
4. Consolidate duplicate live state (#339).
5. Define lightweight metadata/templates (#340).
6. Migrate only where the benefit exceeds reference churn (#334).
7. Rewrite start-here navigation after paths settle (#336).
8. Run independent post-migration regression audit (#337).

## Known ambiguity to resolve before migration

- `watchlist.md` contains current-status language but is now explicitly a derived index.
- top-level ranking, theme rankings and company files must not independently own the same company state.
- `top10-capital-allocation.md` is historical context, while Gate-E live action semantics belong to `PORTFOLIO.md`, current company files/monitors and the live ranked universe.
- the two calibration ledgers already declare their roles; only `prediction-calibration-ledger.md` is live.
- issue bodies may contain execution history, but completed research conclusions must be reflected in canonical documents.

## Invariants

- #261 frozen prediction/outcome corpus must not change during repo hygiene.
- live portfolio/company conclusions must not change merely because files move.
- every open automation-relevant issue must carry State, Priority, Type, Trigger, Dependencies, Parent, Next action and Completion gate.
- only READY is executable; RUNNING is already claimed; WAITING/BLOCKED/PARKED/EPIC are not selectable.
