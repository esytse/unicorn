# Unicorn Research

A collaborative research repository for identifying emerging companies and technologies with asymmetric upside, especially where structural bottlenecks create durable value.

Git history is the authoritative version record. Do not create duplicate files such as `final-v2.md` or `revised-final.md`; update the canonical document and let Git preserve the history.

## Research streams

- `research/physical-ai/` — umbrella Physical AI value chain: data, simulation, embodied models, edge compute, sensing, deployment and cross-embodiment bottlenecks
- `research/robotics-actuators/` — embodiment-specific actuator / precision-motion substream within Physical AI
- `research/memory/` — AI memory, data movement, interfaces and related bottlenecks
- `research/energy/` — AI/data-centre energy, grid, power-delivery and speed-to-power bottlenecks
- Additional themes can be added under `research/` without creating a new repository

## Key files

- `AGENTS.md` — mandatory operating instructions for any AI agent working in this repository
- `AUTOMATION.md` — canonical live backlog-driven automation, alerting, queue-state and scheduler-capacity protocol
- `CHANGELOG.md` — human-readable record of substantive research changes
- `watchlist.md` — cross-theme research candidates and current status
- `research/top10-unicorn-priority.md` — active stock-aware cross-theme top-10 hunting queue; separates structural upside, evidence quality and current stock attractiveness
- `research/top10-capital-allocation.md` — historical Gate-D valuation/downside layer; useful context but not the current 18-month action framework
- `PORTFOLIO.md` — Gate-E aggressive dynamic portfolio strategy for the £40k / 18-month objective through March 2028; defines concentration, catalyst timing, buy/add/trim/sell/rotation rules and bottleneck migration
- `sources/source-register.md` — source provenance register
- `CONTRIBUTING.md` — simple workflow for collaborators who do not use Git day to day
- `research/_templates/` — reusable structures for new themes and company deep dives

## Default workflow

1. Ask an agent to read `AGENTS.md` before doing anything.
2. The agent researches or updates the requested theme.
3. The agent edits the canonical Markdown files on a branch.
4. The agent updates sources and `CHANGELOG.md` where required.
5. The agent opens a pull request that records what changed, why, evidence, confidence and uncertainty.
6. Automated governance checks run.
7. If the checks pass, the PR can auto-merge. Human approval is not required by default.

Pull requests are primarily an audit trail and safety boundary, not a manual approval queue.

If someone prefers not to formulate an agent prompt directly, GitHub's **Research request** issue template can capture the question and starting context in a structured way.

## Live backlog-driven automation

The live automation architecture is documented in `AUTOMATION.md` and tracked by **#120**.

**Status:** one hourly alert-first **Unicorn Portfolio Ops** scheduler is enabled.  
**Cadence:** hourly from **00:00 through 22:00 Europe/London**.  
**Deployment backlog:** #121 and #122 are complete.  

GitHub issues are the execution queue. The scheduler does not carry one fixed stock list inside its prompt; it reads the current machine-readable issue state at runtime.

Every run first performs a cheap monitoring pass:
1. scans explicit `WAITING` / evidence / action-condition triggers;
2. checks only the minimum fresh evidence needed to determine whether something material changed;
3. promotes fired triggers to `READY` and P0/P1 where justified;
4. emits a user notification only for a new/material `ACTION`, `REASSESS`, `THESIS BREAK`, `CATALYST` or `SYSTEM DEGRADED` condition;
5. deduplicates unchanged conditions so routine monitoring stays quiet.

The hourly cadence exists primarily for **fast detection and useful alerts**, not to launch a full underwrite every hour. Normally no more than one non-triggered heavy research item should be started per rolling 24 hours; P0/P1 trigger-driven analysis can override that limit when needed to make an alert decision-useful.

A useful notification should state what changed, why it matters, the current research-level signal or reassessment need, the relevant current Gate-E condition, the main downside/thesis breaker, the next catalyst and what decision the user needs to make. Actual brokerage execution remains manual.

Epics are coordination surfaces and are not selected directly. Monthly and quarterly reviews are represented as due backlog items (#132 / #133) rather than separate schedulers.

Current Gate-E company work includes:
- #125 JEM
- #126 SUSS MicroTec
- #127 Weebit Nano
- #86 Laifual Drive
- #128 Micronics Japan
- #106 BlackBerry/QNX
- #108 FORT Robotics
- #129 Centrus
- #130 Jinpan
- #85 Harmonic Drive
- #109 QNX vs FORT comparison

The initial portfolio-construction work is #131 and becomes executable when enough current company underwrites exist.

Scheduler sufficiency is measured rather than assumed. Key indicators include:
- in-window P0/P1 alert detection-to-notification latency, target **<=2h**;
- P0/P1 trigger-to-substantive-action latency, target **<=24h**;
- READY backlog depth;
- oldest P0/P1 READY age;
- 7-day Backlog Pressure Ratio;
- substantive-work saturation.

A second scheduler is added only when the documented scale-up thresholds persist. The default split would separate **Alert / Trigger / Triage** from the **Research Worker**, not create one scheduler per stock.

## Example instruction to an agent

> Read `AGENTS.md` and the relevant existing research first. Research the requested bottleneck/company, update the canonical documents with sourced evidence, mark facts vs interpretation vs hypothesis, update the changelog if conclusions change, open a pull request, and merge only after required checks pass.

For backlog-driven work:

> Read `AGENTS.md`, `AUTOMATION.md`, `PORTFOLIO.md`, #120 and the active automation-relevant GitHub backlog. Scan explicit triggers first, notify only when the notification contract is met, then select only a valid `READY` issue, claim it as `RUNNING`, execute bounded work, follow repository governance, and update the issue with its truthful resulting state and next action.

## When to request manual review

Manual review is optional. Ask for it when you specifically want a second pair of eyes before a conclusion enters `main`, for example a major thesis reversal or an unusually consequential decision.

## Research principles

- Evidence before narrative
- Facts, interpretation and hypotheses are clearly separated
- Conflicting evidence is preserved rather than hidden
- Thesis changes are explicit and traceable
- Uncertainty and confidence are recorded
- Sources should be attributable and recoverable
- Portfolio capital is dynamic: holdings must continue to earn their place on remaining-window forward return and evidence, not on cost basis or past conviction
- The active Gate-E mandate is aggressive and catalyst-aware: favour concentrated, evidence-backed setups capable of resolving materially inside the 18-month window
- Historical Gate-D / old Gate-C normalized-return zones are context, not current action rules unless explicitly re-adopted by current Gate-E work
- Bottlenecks are expected to migrate as technology, capacity and supply chains mature; the research universe and portfolio must be re-ranked accordingly
- Automation should be quiet when nothing changed and explicit when a decision may be required
- Automation capacity should be scaled from measured alert latency, queue pressure and throughput, not intuition
