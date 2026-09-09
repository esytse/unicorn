# Backlog-Driven Automation

**Status:** Active design  
**Reference date:** 2026-09-09  
**Automation epic:** #120  
**Portfolio epic:** #117  

> GitHub issues are the authoritative execution backlog. Automation may monitor, research, update repository content and operate the governed PR workflow, but it must not place brokerage trades.

## Objective

Automate as much of the `unicorn` research and portfolio operating loop as practical with the smallest scheduler footprint, while ensuring the user is **notified promptly when attention or action is genuinely warranted**.

The initial architecture uses **one alert-first Portfolio Ops scheduler**. GitHub—not the scheduler—is the orchestration layer. The scheduler repeatedly reads the backlog, checks explicit triggers, promotes triggered work, selects bounded executable work and measures whether one scheduler remains sufficient.

The scheduler is deliberately **quiet by default**. Routine successful monitoring, unchanged triggers and ordinary backlog maintenance should not generate user notifications.

## Initial frequency

Run the single scheduler **hourly from 00:00 through 22:00 Europe/London**.

Why this window:
- the universe includes Japan/Hong Kong, Europe and US-listed names;
- hourly is the highest supported scheduler frequency and gives materially better event responsiveness than a daily scan;
- 00:00–22:00 London covers the economically useful part of the Asian, European and US trading/news cycle without requiring a separate scheduler per geography.

This cadence is an initial operating choice, not a permanent rule. Measure alert latency, queue pressure and saturation and change the architecture only when the evidence warrants it.

## Two modes inside one scheduler

The same scheduled run performs two different workloads.

### 1. Monitoring / alert pass — every run
This is cheap and must happen first:
- read explicit `WAITING` triggers and relevant active action conditions;
- check only the minimum fresh public evidence needed to determine whether a trigger fired;
- detect material new filings, earnings, qualification/royalty/funding/capital events, thesis-break evidence and defined price/valuation conditions;
- deduplicate unchanged conditions;
- notify only when the notification contract below is met.

Do **not** redo a full company underwrite merely to test whether an event happened.

### 2. Substantive research / backlog pass — bounded
After monitoring, execute at most **one substantive backlog item per run**, and normally no more than **one non-triggered heavy research item per 24 hours**.

Exceptions are allowed when:
- a P0/P1 trigger has fired and a fresh underwrite is needed to make the alert decision-useful;
- multiple tightly coupled administrative steps are required to complete one governed work item;
- a material portfolio-risk event makes waiting until the next day unreasonable.

The purpose of hourly scheduling is **fast detection and notification**, not to generate 20+ full research projects per day.

## Architecture

```text
Hourly Portfolio Ops scheduler
        |
        v
Read governance + portfolio + backlog
        |
        v
Resolve stale RUNNING claims
        |
        v
Cheap trigger/action scan
        |
        +---- material trigger ----> promote to READY / P0-P1
        |                              |
        |                              +--> decision-useful analysis if needed
        |                              +--> notify if contract met
        |
        v
Calculate queue + alert health
        |
        v
If research budget permits:
select highest-priority READY item
        |
        v
Claim RUNNING -> bounded work
        |
        v
Branch -> PR -> Research governance -> merge
        |
        v
Update issue state / next action / telemetry
```

Monthly portfolio review remains a recurring/due backlog condition rather than a separate scheduler.

## Source of truth

1. `AGENTS.md` — mandatory repository governance.
2. `PORTFOLIO.md` — portfolio objective and capital-allocation framework.
3. `AUTOMATION.md` — orchestration, alerting and scheduler-capacity protocol.
4. GitHub issues — live execution state, triggers and dependencies.
5. Canonical research files — evidence and conclusions.
6. Pull requests / Git history — audit record.

Chat history is not authoritative workflow state.

## Queue states

Every automation-relevant issue must be classifiable into one execution state.

- **`EPIC`** — coordination/programme item; never directly selected for substantive execution.
- **`READY`** — executable now; required inputs exist and no dependency/event blocks it.
- **`RUNNING`** — claimed by a worker; record start context and branch/PR when applicable.
- **`WAITING`** — blocked on an explicit external event/date/evidence/price trigger.
- **`BLOCKED`** — blocked on an internal prerequisite or another backlog item.
- **`PARKED`** — intentionally deprioritized; not executable until promoted.
- **`DONE`** — completion gate met; normally close the issue after final links/state are recorded.

## Priority model

- **P0 — action / immediate orchestration:** could change a current capital decision or materially threaten the portfolio/research process now.
- **P1 — direct 18-month underwrite:** serious candidate, material catalyst or evidence that can change current allocation/ranking.
- **P2 — discovery / bottleneck migration:** could surface a superior candidate or invalidate an important structural assumption.
- **P3 — background:** useful work without near-term capital consequence.

Within `READY`, select highest priority first; use catalyst proximity, age and potential portfolio impact as tie-breakers.

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

The trigger must be explicit and testable. Do not invent a price threshold, thesis condition or action condition merely so automation has something to monitor.

Labels may be added for convenience, but the metadata block remains the scheduler contract unless a later migration is explicitly documented.

## Notification contract

The scheduler should notify the user when there is a **new or materially changed** condition that plausibly requires attention or a decision.

### Notify: `ACTION`
Use when source-backed evidence indicates a defined research-level **Buy / Add / Trim / Sell** condition is met or a capital-allocation decision is now ripe for the user.

The notification should include, where supported:
- company / instrument;
- what changed;
- current research signal;
- current price/evidence versus the governed condition;
- proposed initial/max size or affected allocation if already defined in the underwrite;
- main downside / thesis breaker;
- next catalyst;
- explicit statement that **no brokerage trade was placed**.

### Notify: `REASSESS`
Use when a major catalyst, price move, valuation change, competitor development or bottleneck migration materially changes expected 18-month attractiveness but the correct action still needs a fresh underwrite.

### Notify: `THESIS BREAK`
Use when credible evidence satisfies or materially approaches a documented thesis-break condition.

### Notify: `CATALYST`
Use when an awaited event fires and is sufficiently material that the user should know even before the full underwrite is finished, for example an S-4, earnings surprise, production royalty, qualification, financing or major dilution event.

Avoid sending a separate catalyst alert if the same run can immediately produce a more useful `ACTION` or `REASSESS` notification.

### Notify: `SYSTEM DEGRADED`
Use when automation failure creates a meaningful risk of missing decision-relevant triggers or when scheduler capacity metrics indicate the alert/research loop is no longer keeping up.

### Stay quiet
Do not notify merely because:
- an hourly scan completed successfully;
- nothing material changed;
- a trigger remains false;
- a routine P2/P3 research item advanced without changing a conclusion;
- the same unchanged alert condition was already surfaced;
- a PR merged with no decision impact.

GitHub should retain the operational/audit evidence even when the user notification remains quiet.

## Notification quality

Notifications are decision surfaces, not news digests. Prefer:

```text
ACTION — ExampleCo
What changed: ...
Why it matters: ...
Research signal: Add / Trim / etc.
Current condition: ...
Main risk / thesis breaker: ...
Next catalyst: ...
Your decision: ...
No trade has been placed.
```

Do not overstate confidence. If evidence is incomplete, say `REASSESS` rather than manufacturing an `ACTION` signal.

## Deduplication

Before notifying, compare the new finding with the most recent persisted issue/automation state.

Do not repeatedly alert on the same unchanged trigger. Re-alert only if there is a material change such as:
- new evidence;
- action state changes;
- price/evidence crosses back through a governed condition;
- severity increases;
- the prior condition resolves and later recurs;
- a new user decision is genuinely required.

## Scheduler run algorithm

1. Read `AGENTS.md`, `AUTOMATION.md`, `PORTFOLIO.md`, active automation-relevant issues and relevant canonical research.
2. Check `RUNNING` items and avoid duplicate work; reclaim only after verifying no active branch/PR/work remains.
3. Perform the cheap trigger/action scan.
4. Promote fired triggers to `READY` and reprioritize to P0/P1 when justified.
5. Perform enough fresh analysis to determine whether a notification contract is met.
6. Notify only for new/material `ACTION`, `REASSESS`, `THESIS BREAK`, `CATALYST` or `SYSTEM DEGRADED` conditions.
7. Calculate alert and queue health.
8. If the substantive-work budget permits, select the highest-priority valid `READY` item.
9. Mark it `RUNNING` before substantive work.
10. Execute one bounded work item using canonical files and source-backed evidence.
11. For repo changes use branch -> PR -> required `Research governance` -> merge; never bypass required checks.
12. Set a truthful resulting state and a concrete next action/trigger/dependency.
13. Create follow-up backlog only when it can materially change allocation, ranking, bottleneck, evidence confidence, catalyst probability/timing or an important thesis breaker.

Avoid vague states such as “more research needed.”

## Trigger examples

A single scheduler can monitor many companies because triggers live in issues:
- QNX results published;
- FORT/Newbury Street II S-4 filed;
- Weebit recurring production royalty disclosed;
- JEM/MJC HBM4 production qualification evidence;
- Centrus commercial capacity financing completed;
- candidate enters a defined valuation/price zone;
- dilution/capital raise exceeds a documented tolerance;
- standards/architecture/capacity evidence changes a bottleneck thesis.

Prefer primary/regulatory/company evidence where practical.

## Portfolio review as backlog

A full portfolio re-rank becomes `READY` when the documented monthly review is due. It competes normally for execution; it does not require another scheduler initially.

A monthly re-rank should notify only when it identifies a material allocation/action/reassessment change. A routine unchanged re-rank stays quiet.

## Scheduler sufficiency metrics

The system must measure both **alert responsiveness** and **research throughput**.

### 1. Alert detection-to-notification latency
Elapsed time from a material external trigger becoming publicly observable to a decision-useful notification or explicit `REASSESS` alert.

Initial target during the scheduled 00:00–22:00 London window: **<=2 hours** for P0/P1 events where the trigger time is reasonably knowable.

Events becoming public outside the monitoring window should be assessed at the next scheduled run and reported separately from in-window latency.

### 2. Trigger-to-substantive-action latency
Elapsed time from a material trigger to the first substantive governed underwrite/update when one is required.

Initial target: **<=24 hours** for P0/P1.

### 3. READY backlog depth
Number of substantive executable items waiting. Initial healthy range: usually **0–3**; >5 is a capacity warning.

### 4. Oldest P0/P1 READY age
Initial target: **<=48 hours**.

### 5. Backlog Pressure Ratio

```text
Pressure Ratio = new executable work created/promoted over 7 days
                 ------------------------------------------------
                 executable work completed over 7 days
```

Interpretation:
- **<0.8** spare capacity;
- **0.8–1.0** healthy/busy;
- **1.0–1.25** accumulating; monitor;
- **>1.25** meaningful pressure;
- **>1.5 for two consecutive weeks** strong evidence that more worker capacity may be justified.

If completed work is zero, report the denominator failure rather than a misleading finite ratio.

### 6. Run saturation
Share of substantive-work opportunities that finish while another P0/P1 executable item still waits. Initial warning threshold: **>80%**.

## Scale-up rule

Start with **one scheduler**.

Consider a second scheduler when **any two** of these persist for **two weeks**:
1. in-window P0/P1 alert latency >2h;
2. P0/P1 trigger-to-substantive-action latency >24h;
3. oldest P0/P1 READY age >48h;
4. Pressure Ratio >1.25;
5. >5 substantive READY issues;
6. >80% substantive-work saturation.

Do not redesign the architecture because one exceptional event temporarily breaches a threshold.

### Default split if scaling is justified

**Scheduler A — Alert / Trigger / Triage**
- hourly event and action-condition checks;
- notifications;
- issue promotion/reprioritization;
- alert-health telemetry.

**Scheduler B — Research Worker**
- substantive P0/P1 underwrites and highest-value READY work;
- governed repository updates.

Do not split by company/theme unless later evidence supports it.

## Automation health record

Persist enough evidence to calculate:
- run date/time;
- trigger items checked / fired;
- notifications emitted and class;
- estimated in-window alert latency;
- READY substantive count;
- oldest P0/P1 READY age;
- 7-day new/completed executable counts and Pressure Ratio;
- saturation yes/no;
- item selected/completed/resulting state;
- scheduler recommendation: `ONE SUFFICIENT`, `WATCH`, or `SPLIT CANDIDATE`.

The storage surface may evolve, but the metric definitions should remain stable enough for trend comparison.

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
- compare evidence and valuation conditions;
- update research/portfolio analysis;
- create and maintain backlog issues;
- create branches/PRs and merge after required checks pass;
- produce research-level Buy/Add/Trim/Sell signals, catalyst alerts and thesis-break alerts.

Automation must not:
- place brokerage orders;
- fabricate market data/evidence;
- lower evidence standards to hit the March-2028 objective;
- invent action thresholds;
- force-push protected history;
- bypass required checks;
- silently change watchlist/research conclusions;
- generate backlog or notifications merely to stay busy.

## Initial rollout

1. **#121 — normalize active backlog**, including explicit event/action triggers.
2. **#122 — deploy one hourly alert-first Portfolio Ops scheduler and measure alert + research capacity** after normalization is sufficient.
3. Run the single-scheduler architecture until telemetry supports keeping it single or splitting alert/triage from substantive research.

The goal is the **minimum reliable orchestration that keeps the user informed when a decision may be needed, without drowning them in routine monitoring noise**.
