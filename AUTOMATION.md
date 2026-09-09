# Backlog-Driven Automation

**Status:** LIVE  
**Live since:** 2026-09-09  
**Automation epic:** #120  
**Portfolio epic:** #117  
**Deployment:** #121 completed; #122 completed  

> GitHub issues are the authoritative execution backlog. Automation may monitor, research, update repository content and operate the governed PR workflow, but it must not place brokerage trades.

## Objective

Operate the `unicorn` research and Gate-E portfolio loop with the smallest reliable scheduler footprint while notifying the user promptly when attention or action is genuinely warranted.

The live architecture uses **one hourly, alert-first Portfolio Ops scheduler**. GitHub—not the scheduler—is the orchestration layer. The scheduler repeatedly reads current governance and backlog state, checks explicit triggers, promotes triggered work, executes bounded research and measures whether one scheduler remains sufficient.

The scheduler is deliberately **quiet by default**. Routine successful monitoring, unchanged triggers and ordinary backlog maintenance do not generate user notifications.

## Live scheduler

**Name:** Unicorn Portfolio Ops  
**Timing mode:** condition watch  
**Frequency:** hourly from **00:00 through 22:00 Europe/London**  
**Purpose:** fast trigger detection, decision-useful alerts and bounded backlog execution across Asian, European and US market/news cycles.

The hourly cadence exists primarily for **monitoring and notification**, not to launch a full research project every hour.

## Source of truth

Read at runtime, in this order:

1. `AGENTS.md` — mandatory repository governance.
2. `AUTOMATION.md` — this orchestration and alerting contract.
3. `PORTFOLIO.md` — active Gate-E capital-allocation framework.
4. GitHub issue #120 — automation epic / health history.
5. Active GitHub issues containing `## Automation metadata` — live queue, triggers and dependencies.
6. Canonical research files and `sources/source-register.md` — evidence and conclusions.
7. Pull requests / Git history — audit record.

Chat history is not authoritative workflow state.

## Queue states

Every automation-relevant issue must be classifiable into exactly one execution state:

- **`EPIC`** — coordination/programme item; never directly selected for substantive execution.
- **`READY`** — executable now; required inputs exist and no dependency/event blocks it.
- **`RUNNING`** — claimed by a worker; record run/start context and branch/PR where applicable.
- **`WAITING`** — blocked on an explicit external event/date/evidence/price trigger.
- **`BLOCKED`** — blocked on an internal prerequisite or another backlog item.
- **`PARKED`** — intentionally deprioritized; not executable until promoted.
- **`DONE`** — completion gate met; normally close the issue after final links/state are recorded.

## Priority model

- **P0 — immediate decision / portfolio / orchestration consequence.**
- **P1 — direct 18-month underwrite or material catalyst.**
- **P2 — discovery / bottleneck migration that could surface a superior candidate.**
- **P3 — background or historical work without near-term capital consequence.**

Within `READY`, select highest priority first; use catalyst proximity, age and potential portfolio impact as tie-breakers.

Do not choose an intellectually interesting P2/P3 item over an actionable P0/P1 item.

## Machine-readable issue contract

Automation-relevant issues should contain:

```markdown
## Automation metadata
- **State:** WAITING
- **Priority:** P1
- **Type:** EVENT
- **Trigger:** Company files Form S-4
- **Dependencies:** NONE
- **Parent:** #117
- **Next action:** Rebuild fully diluted capitalization after filing.
- **Completion gate:** dilution, recurring economics and 18-month return cases updated.
```

The metadata block is the scheduler contract. The rest of the issue remains human-readable context.

The trigger must be explicit and testable. Do **not** invent a price threshold, thesis condition or action condition merely so automation has something to monitor.

Historical Gate-D / old Gate-C 10/12/15% or four-year price zones are **context only** unless a current Gate-E issue explicitly adopts a new evidence-supported action rule.

## Live Gate-E decision surface

### Programme / recurring
- #117 — `EPIC` P0: aggressive £40k / 18-month portfolio.
- #110 — `EPIC` P1: cross-theme Top-10 hunting universe.
- #120 — `EPIC` P0: automation/orchestration and capacity telemetry.
- #131 — `BLOCKED` P0: construct initial aggressive portfolio after enough company underwrites are current.
- #132 — `WAITING` P1: monthly portfolio re-rank when due.
- #133 — `WAITING` P2: quarterly full-universe challenge when due.

### Current Top-10 company work
- #125 JEM — `READY` P1.
- #126 SUSS MicroTec — `READY` P1.
- #127 Weebit Nano — `READY` P1.
- #86 Laifual Drive — `READY` P1.
- #128 Micronics Japan — `READY` P1.
- #106 BlackBerry/QNX — `WAITING` P0 on Q2 FY2027 / material non-auto evidence.
- #108 FORT Robotics — `WAITING` P1 on S-4/equivalent / transaction change.
- #129 Centrus — `WAITING` P1 on funded-capacity / financing inflection.
- #130 Jinpan — `READY` P1.
- #85 Harmonic Drive — `PARKED` P2.
- #109 QNX vs FORT — `BLOCKED` P1 until both fresh event-driven underwrites exist.

Historical #114 Gate D and #89 actuator Gate C are closed and must not be selected as current work.

## Two modes inside one scheduler

### 1. Monitoring / alert pass — every run

This happens first and should be cheap:

- resolve stale `RUNNING` claims without duplicating live branches/PRs;
- scan explicit triggers and current action conditions on automation-relevant issues;
- check only the minimum fresh public/company/regulatory/market evidence needed to determine whether a trigger fired;
- detect material filings, earnings, qualification/royalty/funding/capital events, thesis-break evidence and defined current Gate-E price/valuation conditions;
- promote fired work to `READY` and P0/P1 where justified;
- deduplicate unchanged conditions;
- notify only when the notification contract is met.

Do not redo a full company underwrite merely to test whether an event happened.

### 2. Substantive research / backlog pass — bounded

After monitoring:

- normally perform no more than **one non-triggered heavy research item per rolling 24 hours**;
- P0/P1 trigger-driven analysis may override that limit when needed to make an alert decision-useful;
- select only the highest-priority valid `READY` issue;
- never directly execute `EPIC`, unresolved `WAITING`, `BLOCKED`, `PARKED` or already-live `RUNNING` work;
- mark the selected issue `RUNNING` before substantive work;
- complete one bounded unit of work rather than opening many partial investigations.

## Notification contract

Notify only for a **new or materially changed** condition in one of these classes.

### `ACTION`
Use when source-backed current Gate-E evidence indicates a defined research-level **Buy / Add / Trim / Sell / Rotate** condition is met and user judgement is required.

Where supported, include:
- company / instrument;
- what changed;
- why it matters now;
- current research signal;
- current price/evidence versus the documented Gate-E condition;
- proposed initial/max size or affected allocation if already defined;
- main downside / thesis breaker;
- next catalyst;
- explicit user decision required;
- statement that **no brokerage trade was placed**.

### `REASSESS`
Use when evidence, price, catalyst, competitor behaviour or bottleneck migration materially changes the remaining-window case but a fresh underwrite is still required before action.

### `THESIS BREAK`
Use when credible evidence satisfies or materially approaches a documented current thesis breaker.

### `CATALYST`
Use when an awaited material event fires and the user should know promptly even before a full underwrite is completed, for example:
- S-4 / transaction filing;
- earnings result;
- production royalty;
- qualification or major customer evidence;
- financing / funded capacity;
- material dilution or capital action.

Avoid sending a separate catalyst alert if the same run can immediately produce a more useful `ACTION` or `REASSESS` notification.

### `SYSTEM DEGRADED`
Use when automation failure creates a meaningful risk of missing decision-relevant triggers, or when sustained scheduler-capacity evidence shows the alert/research loop is no longer keeping up.

### Stay quiet
Do not notify merely because:
- an hourly scan completed successfully;
- nothing material changed;
- a trigger remains false;
- routine P2/P3 work advanced without decision impact;
- the same unchanged alert condition was already surfaced;
- a PR merged with no decision impact;
- a monthly/quarterly review is materially unchanged.

## Deduplication

Before notifying, compare the new finding with persisted issue/automation history.

Re-alert only when there is a material state change such as:
- new evidence;
- action class changes;
- price/evidence crosses back through a current governed condition;
- severity increases;
- a prior condition resolves and later recurs;
- a genuinely new user decision is required.

## Scheduler run algorithm

Each run should:

1. Read current `AGENTS.md`, `AUTOMATION.md`, `PORTFOLIO.md`, #120 and active automation-relevant issues.
2. Resolve stale `RUNNING` claims; do not duplicate live work.
3. Perform the cheap trigger/action scan.
4. Promote fired triggers to `READY` and reprioritize when justified.
5. Perform enough fresh analysis to determine the alert class.
6. Notify only for new/material `ACTION`, `REASSESS`, `THESIS BREAK`, `CATALYST` or `SYSTEM DEGRADED`.
7. Calculate alert and queue health.
8. If the substantive-work budget permits, select the highest-priority valid `READY` issue.
9. Mark it `RUNNING` before substantive work.
10. Read the relevant canonical research and source material.
11. Use fresh public evidence where needed; distinguish **FACT / INTERPRETATION / HYPOTHESIS / OPEN QUESTION** and preserve uncertainty.
12. For substantive repo changes use branch → PR → required `Research governance` → merge; never bypass checks.
13. Update/close the issue with truthful state, next action, trigger/dependency and completion status.
14. Create follow-up backlog only when it can materially change allocation, ranking, bottleneck direction, evidence confidence, catalyst timing or a thesis breaker.

Avoid vague end states such as “more research needed.”

## Repository governance

For substantive research updates:

- work on a branch, never directly on `main`;
- update canonical documents, not versioned duplicates;
- add/update recoverable sources;
- update `CHANGELOG.md` when required by `AGENTS.md`;
- open a PR with the required audit summary;
- never merge while required checks are pending/failing;
- merge only after `Research governance` passes unless manual review was explicitly requested;
- never bypass governance to clear queue pressure.

## Recurring work lives in the backlog

Do not create separate monthly/quarterly schedulers initially.

- #132 becomes executable when the monthly Gate-E re-rank is due.
- #133 becomes executable when the quarterly full-universe challenge is due.

The hourly scheduler checks these due conditions alongside external triggers.

A recurring review should notify only if it produces a material action/reassessment change.

## Scheduler sufficiency metrics

The system must measure both **alert responsiveness** and **research throughput**.

### 1. In-window P0/P1 alert latency
Elapsed time from a material trigger becoming publicly observable to a decision-useful notification or explicit `REASSESS`.

Initial target during 00:00–22:00 London: **<=2 hours** where trigger time is reasonably knowable.

Events outside the monitoring window are assessed at the next scheduled run and should be reported separately from in-window latency.

### 2. P0/P1 trigger-to-substantive-action latency
Elapsed time from a material trigger to the first substantive governed underwrite/update when required.

Initial target: **<=24 hours**.

### 3. READY backlog depth
Number of substantive executable items waiting.

Initial healthy range: usually **0–3**. More than five is a capacity warning, not an automatic split.

### 4. Oldest P0/P1 READY age
Initial target: **<=48 hours**.

### 5. Backlog Pressure Ratio

```text
Pressure Ratio = new executable work created/promoted over 7 days
                 ------------------------------------------------
                 executable work completed over 7 days
```

Interpretation:
- **<0.8** — spare capacity;
- **0.8–1.0** — healthy/busy;
- **1.0–1.25** — accumulating; monitor;
- **>1.25** — meaningful pressure;
- **>1.5 for two consecutive weeks** — strong evidence more worker capacity may be justified.

If completed work is zero, report denominator failure rather than a misleading finite ratio.

### 6. Substantive-work saturation
Share of substantive-work opportunities that finish while another P0/P1 executable item remains.

Initial warning threshold: **>80%**.

## Scale-up rule

Keep **one scheduler** unless **any two** of these persist for **two weeks**:

1. in-window P0/P1 alert latency >2h;
2. P0/P1 trigger-to-substantive-action latency >24h;
3. oldest P0/P1 READY age >48h;
4. Pressure Ratio >1.25;
5. >5 substantive READY issues;
6. >80% substantive-work saturation.

Do not redesign the architecture because one exceptional event temporarily breaches a threshold.

### Default split if scaling is justified

**Scheduler A — Alert / Trigger / Triage**
- hourly trigger checks;
- notifications;
- issue promotion/reprioritization;
- alert-health telemetry.

**Scheduler B — Research Worker**
- substantive P0/P1 underwrites;
- highest-value READY work;
- governed repository updates.

Do not split by company or theme unless later evidence supports it.

## Automation health record

Record recoverable health evidence in #120 when there is:
- a fired trigger;
- substantive work;
- a meaningful capacity-state change;
- system degradation.

Avoid noisy hourly comments when nothing changed.

Useful telemetry includes:
- run date/time;
- triggers checked/fired;
- notification class and dedup state;
- estimated alert latency;
- READY count;
- oldest P0/P1 READY age;
- 7-day new/completed executable counts;
- Pressure Ratio or denominator warning;
- saturation yes/no;
- item selected/resulting state;
- recommendation: `ONE SUFFICIENT`, `WATCH`, or `SPLIT CANDIDATE`.

## Failure handling

If a required tool/source is unavailable:
- do not fabricate completion;
- record the exact dependency/failure;
- preserve truthful issue state;
- emit `SYSTEM DEGRADED` only when the failure materially threatens decision coverage or alert reliability.

Never mark an issue `DONE` merely because a scheduler run ended.

## Boundaries

Automation may:
- search fresh public information;
- inspect filings/company sources;
- compare evidence and current Gate-E valuation/action conditions;
- update research and portfolio analysis;
- maintain backlog issues;
- create branches/PRs and merge after required checks pass;
- produce research-level Buy/Add/Trim/Sell/Rotate signals, catalyst alerts and thesis-break alerts.

Automation must not:
- place brokerage orders;
- infer that a brokerage transaction occurred;
- fabricate market data/evidence;
- lower evidence standards to pursue the March-2028 objective;
- invent action thresholds;
- force-push protected history;
- bypass required checks;
- silently change watchlist/research conclusions;
- generate backlog or notifications merely to stay busy.

## Deployment state

- **#121 — completed:** active P0/P1 backlog normalized into machine-readable queue states and explicit triggers.
- **#122 — completed:** hourly alert-first Portfolio Ops scheduler deployed and enabled.
- **#120 — active:** collect operational evidence and decide empirically whether one scheduler remains sufficient.

The goal is the **minimum reliable orchestration that keeps the user informed when a decision may be needed, without drowning them in routine monitoring noise**.
