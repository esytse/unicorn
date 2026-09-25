# Repository architecture and lifecycle model

**As of:** 2026-09-25  
**Issue:** #332  
**Status:** CANONICAL repository architecture and authority map

## Purpose and thesis invariant

Unicorn is a thesis-first research system. Repository structure exists to support, never replace, the original chain:

> **Abundant Intelligence → Scarce Complements → Bottleneck Migration → Economic Capture → Capital Allocation**

Discovery therefore starts with architecture/change and scarcity, not a generic stock screen. Repo hygiene must not alter investment conclusions or the frozen #261 corpus.

## Authority rules

1. **One canonical authority per live concept.**
2. **Issues are workflow; documents are durable knowledge.** An issue may coordinate work or preserve execution history, but durable conclusions land in the appropriate document.
3. **Derived views name their upstream authority.** They may rank, index or summarize; they do not become a second live truth.
4. **Historical/frozen material cannot silently become live.** Re-adoption requires an explicit new live artifact/change, not editing history.
5. Git history is the detailed version record. Prefer stable paths/indexes over moves that create reference churn.
6. Superseded material remains discoverable but is explicitly non-current.
7. Cleanup cannot change research conclusions, portfolio rules, or #261 frozen content.

## Lifecycle vocabulary

| Class | Role | Mutation rule |
|---|---|---|
| **CANONICAL** | Sole current authority for a defined live concept | Update in place with evidence/governance; Git preserves versions |
| **DERIVED** | Index, ranking, synthesis or report computed/summarized from authority | Must identify upstream; refresh rather than independently redefine truth |
| **HISTORICAL** | Point-in-time/frozen evidence, validation or superseded snapshot retained for provenance | Do not rewrite into current state; immutable where declared frozen |
| **GUIDANCE** | Human/agent operating instructions, templates and navigation | May evolve, but must point to canonical authorities rather than duplicate mutable conclusions |
| **LOG** | Chronological record of changes/events | Append/record what happened; never treat as current truth |
| **ARCHIVE** | Intentionally retired material retained when Git history alone is insufficient | Non-current; must not be routed to for live decisions |

A document can support another class, but only one artifact owns each live concept. Classification describes authority, not folder location.

## Deterministic issue-state semantics

| State | Meaning | Executable? |
|---|---|---:|
| **READY** | Prerequisites satisfied; concrete next action can start now | yes |
| **RUNNING** | Claimed and actively being executed; owner/context must prevent duplicate execution | no new claim |
| **WAITING** | Needs an external/date/evidence trigger; trigger is explicit | no |
| **BLOCKED** | Needs an internal prerequisite/dependency; dependency is explicit | no |
| **PARKED** | Intentionally deprioritized until an explicit reactivation condition | no |
| **EPIC** | Coordination/parent surface, never a work item itself | no |
| **DONE** | Completion gate satisfied; durable findings recorded; GitHub issue should be closed | no |

Only READY enters the executable queue. RUNNING is excluded unless a stale claim is explicitly recovered. WAITING becomes READY only when its trigger fires; BLOCKED becomes READY only when dependencies resolve; PARKED requires an explicit reactivation decision. Two selections against unchanged repository/issue state must produce the same queue order.

## Canonical source map

| Concept | Canonical source | Derived / supporting views | Lifecycle |
|---|---|---|---|
| Repository purpose / navigation | `README.md` | `CONTRIBUTING.md` | GUIDANCE |
| Agent operating rules | `AGENTS.md` | README workflow summary | GUIDANCE |
| Queue states / scheduler protocol | `AUTOMATION.md` | issue metadata, README summary | live canonical |
| Portfolio mandate / Gate-E operating rules | `PORTFOLIO.md` | company monitors, ranking views | live canonical |
| Cross-theme candidate index | `watchlist.md` | theme rankings | DERIVED; company evidence resolves upstream |
| Live ranked research universe | `research/ranked-universe.md` | watchlist/theme rankings | live canonical |
| Multibagger discovery / reverse-underwrite funnel | `research/unicorn-potential.md` | company files | live canonical |
| Live prospective calibration checkpoints | `research/prediction-calibration-ledger.md` | issue checkpoints | live canonical |
| Wave-5 seed calibration snapshot | `research/decision-outcome-calibration-ledger.md` | none | HISTORICAL |
| Historical Gate-D valuation layer | `research/top10-capital-allocation.md` | none | HISTORICAL |
| Current company evidence/thesis | relevant canonical company/deep-dive file | watchlist, ranking, issue | live canonical per company |
| Theme thesis / value chain | each theme's `thesis.md` / `value-chain.md` | synthesis/deep dives | live canonical per theme |
| Theme research queue/plan | each theme's `research-plan.md` | GitHub issues | durable plan; issue state wins execution |
| Theme ranking | each theme's `synthesis-ranking.md` | watchlist/top-level ranking | DERIVED |
| Historical validation #261 | `research/backtests/261/**` | `SUMMARY.md` entry point | HISTORICAL, frozen |
| Source provenance | `sources/source-register.md` plus recoverable inline sources | citations | canonical provenance |
| Change history | `CHANGELOG.md` | Git history / PRs | LOG |

## Target architecture: conceptual homes and lifecycle

Physical folders are not required when existing stable paths already make authority clear.

| Domain | Live authority / home | Lifecycle |
|---|---|---|
| **Methodology** | methodology rules remain in canonical methodology/control documents indexed from governance/README; Git records revisions until #325 establishes prospective version boundaries | CANONICAL; old versions become HISTORICAL, never parallel live rules |
| **Thesis-first discovery** | cross-theme/theme discovery records under `research/`; start from world/architecture change → scarcity → bottleneck, then companies | CANONICAL evidence; dated scans may become HISTORICAL |
| **Company research** | one canonical company/deep-dive record per company/question | CANONICAL; rankings/watchlist/issues reference it |
| **Live ranked universe** | `research/ranked-universe.md`; universe is uncapped | CANONICAL |
| **Portfolio / Gate E** | `PORTFOLIO.md` owns mandate/construction/transaction rules; company evidence + issue monitors supply current inputs | CANONICAL |
| **Historical validation** | `research/backtests/261/**` for v1 frozen corpus and any explicitly historical validation records | HISTORICAL/frozen |
| **Prospective validation** | `research/prediction-calibration-ledger.md` now; #325 defines the prospective/versioning boundary before methodology changes | CANONICAL prospective record |
| **Monitors / triggers** | GitHub issues + `AUTOMATION.md` semantics | workflow state in issues; durable findings flow back to CANONICAL docs |
| **Evidence / provenance** | `sources/source-register.md` + recoverable inline citations | CANONICAL provenance/support |
| **Derived reports** | rankings/syntheses/articles that explicitly point upstream | DERIVED; regenerable/refreshable |
| **Superseded / historical material** | retain stable path with explicit status or Git history; use archive only where discoverability requires a retained retired artifact | HISTORICAL/ARCHIVE |

## Routing cases

| Task | Route | Why |
|---|---|---|
| Add a new bottleneck discovery | relevant `research/cross-theme/` or theme discovery/thesis artifact, then company discovery if warranted | preserves thesis-first sequence |
| Update a company thesis | that company's canonical deep-dive/company file | one durable authority |
| Find current cross-theme ranking | `research/ranked-universe.md` | sole live cross-theme order |
| Find current portfolio rules | `PORTFOLIO.md` | sole Gate-E mandate/rule authority |
| Record a live monitor | GitHub issue using `AUTOMATION.md` contract | issues own workflow/trigger state |
| Record historical validation | historical validation corpus/record; #261 stays frozen | cannot masquerade as live |
| Record a prospective prediction | `research/prediction-calibration-ledger.md` under the prospective boundary | prevents hindsight rewriting |
| Change/version methodology | update the canonical methodology/control surface only after respecting #325 prospective/version boundary; preserve prior version via Git/HISTORICAL record when materially required | prevents rule changes contaminating validation |

## Navigation and migration policy

Prefer adding authority labels, indexes and references over moving coherent theme/company trees. A move is justified only when it materially removes ambiguity and every inbound reference can be repaired in the same governed batch. No aesthetic bulk migration.

## Invariants

- #261 frozen prediction/outcome corpus is immutable during hygiene.
- Live portfolio/company conclusions do not change merely because authority or paths are clarified.
- Every automation-relevant open issue carries State, Priority, Type, Trigger, Dependencies, Parent, Next action and Completion gate.
- Only READY is executable.
- The ranked universe remains a consequence of thesis-first discovery, not the boundary of discovery.
