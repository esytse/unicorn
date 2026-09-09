# Backlog-Driven Automation

**Status:** Active design  
**Reference date:** 2026-09-09  
**Automation epic:** #120  
**Portfolio epic:** #117  

> GitHub issues are the authoritative execution backlog. Automation may research, monitor, update repository content and operate the governed PR workflow, but it must not place brokerage trades.

## Objective

Automate as much of the `unicorn` research and portfolio operating process as practical with the smallest scheduler footprint.

The initial architecture uses **one scheduled Portfolio Ops Agent**. GitHub—not the scheduler—is the orchestration layer. The scheduler repeatedly reads the backlog, promotes triggered work, selects the highest-value executable item and processes one bounded unit of work.

A second scheduler should be added only when measured queue pressure or latency shows that one worker is insufficient.

## Architecture

```text
Scheduled Portfolio Ops Agent
        |
        v
Read governance + portfolio + backlog
        |
        v
Scan WAITING triggers cheaply
        |
        +---- trigger fires ----> promote to READY
        |
        v
Calculate queue health
        |
        v
Select highest-priority READY item
        |
        v
Claim RUNNING
        |
        v
Execute one bounded work item
        |
        v
Branch -> PR -> Research governance -> merge
        |
        v
Update issue state / next action / follow-up backlog
```

Monthly portfolio review is represented as a recurring/due backlog condition rather than a separate scheduler. Event monitoring is also part of the same run.

## Source of truth

The sources of truth are:

1. `AGENTS.md` — mandatory repository governance;
2. `PORTFOLIO.md` — portfolio objective and capital-allocation framework;
3. this file — automation orchestration protocol;
4. GitHub issues — live execution state and dependencies;
5. canonical research files — research evidence and conclusions;
6. pull requests / Git history — audit record.

Chat history is not an authoritative workflow state.

## Queue states

Every automation-relevant issue should be classifiable into exactly one execution state.

### `EPIC`
Coordination or programme item. Never selected directly for substantive execution.

Examples: Gate-E portfolio programme, cross-theme Top-10 maintenance, automation orchestration.

### `READY`
Executable now. Required inputs are available and no dependency or external event blocks the next action.

### `RUNNING`
Claimed by a worker. A scheduler must mark an item `RUNNING` before substantive work so another worker does not duplicate it.

The issue should record enough run context to determine whether the claim is still live, for example start time and associated branch/PR once created.

### `WAITING`
Blocked on an external event, date or evidence trigger such as:

- earnings release;
- regulatory filing;
- S-4;
- production qualification;
- royalty announcement;
- capital raise;
- major price/evidence threshold.

The trigger must be explicit and testable.

### `BLOCKED`
Blocked on another backlog item or missing prerequisite that is internal to the research process.

### `PARKED`
Intentionally deprioritized. The work may remain useful but should not consume scheduler capacity until explicitly promoted.

### `DONE`
Completion gate met. Normally represented by closing the GitHub issue after final state / links are recorded.

## Priority model

Priority applies within the execution state.

- **P0 — immediate decision / orchestration:** could change a current capital decision in roughly 30 days, or is critical work required to make the automation system safe/reliable.
- **P1 — direct 18-month underwrite:** serious portfolio candidate, material catalyst, or evidence that can change the current ranking/allocation.
- **P2 — discovery / bottleneck migration:** could surface a superior candidate or invalidate an important structural assumption.
- **P3 — background:** useful research without near-term capital consequence.

The worker selects the highest-priority `READY` item. If multiple items share a priority, use catalyst proximity, age and potential portfolio impact as tie-breakers.

Do not choose an intellectually interesting P2/P3 item over an actionable P0/P1 item.

## Machine-readable issue contract

Automation-relevant issues should contain an `## Automation metadata` section using this structure:

```markdown
## Automation metadata
- **State:** READY
- **Priority:** P1
- **Type:** RESEARCH
- **Trigger:** NONE
- **Dependencies:** NONE
- **Parent:** #117
- **Next action:** Re-underwrite ExampleCo against the March-2028 hurdle.
- **Completion gate:** role + catalyst + downside + entry/add/trim/sell rules recorded.
```

For event-dependent work:

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

Labels may be added later for convenience, but automation must not rely on labels as the sole source of truth unless that migration is explicitly documented.

## Scheduler run algorithm

Each run should follow this order.

### 1. Load context
Read:

- `AGENTS.md`;
- `AUTOMATION.md`;
- `PORTFOLIO.md`;
- relevant active issues;
- relevant canonical research before substantive work.

### 2. Resolve stale claims
Before claiming new work, check `RUNNING` items.

Do not duplicate work if an active branch/PR or recent live claim exists. A stale claim may be returned to `READY` only after verifying that no active work is still in flight.

### 3. Scan triggers cheaply
Check explicit `WAITING` triggers. Do not redo full company research merely to see whether a trigger fired.

If a material trigger fires:

- add the evidence/date/source to the issue;
- change the state to `READY`;
- reprioritize if the event can change a near-term capital decision.

### 4. Calculate queue health
Record or derive the scheduler-sufficiency indicators defined below.

### 5. Select work
Choose the highest-priority executable `READY` item.

Do not select:

- `EPIC`;
- `WAITING` whose trigger has not fired;
- `BLOCKED` with unresolved dependencies;
- `PARKED`;
- a `RUNNING` item already claimed elsewhere.

### 6. Claim before execution
Change state to `RUNNING` before substantive work and record start/run context.

### 7. Execute one bounded substantive unit
The default is **one substantive backlog item per scheduler run**.

Short administrative actions may be batched, but the scheduler should avoid opening many simultaneous research threads that produce partially completed work.

### 8. Use repository governance
For substantive repository updates:

- use a branch;
- update canonical files, sources and changelog where required;
- open a PR with the required audit summary;
- never bypass `Research governance`;
- merge only after required checks pass unless manual review was requested.

### 9. Close or specify the next action
After work:

- mark `DONE` / close the issue if its completion gate is met; or
- set `READY`, `WAITING`, `BLOCKED` or `PARKED` with a concrete next action and trigger/dependency.

Avoid vague states such as “more research needed.”

### 10. Create follow-up backlog selectively
An agent may create a new issue when the new work could materially change:

- portfolio allocation;
- Top-10 ranking;
- bottleneck location/direction;
- evidence confidence;
- catalyst probability/timing;
- an important thesis breaker.

Do not create self-perpetuating research tasks merely because another adjacent question exists.

## Trigger monitoring

A single scheduler can monitor many companies because triggers live in issues, not in separate scheduled tasks.

Examples:

- QNX results published;
- FORT/Newbury Street II S-4 filed;
- Weebit recurring production royalty disclosed;
- JEM/MJC HBM4 production qualification evidence;
- Centrus commercial capacity financing completed;
- candidate enters a defined valuation/price zone;
- bottleneck evidence changes after a standard/architecture/capacity event.

Trigger checks should focus on primary/regulatory/company evidence where practical.

## Portfolio review as backlog

Do not require a separate monthly scheduler initially.

The Portfolio Ops Agent should treat a full portfolio re-rank as due when the last completed monthly review is sufficiently old. The due review becomes or is promoted to a `READY` P0/P1 backlog item and competes normally for execution.

This keeps cadence logic inside the backlog rather than multiplying schedulers.

## Scheduler sufficiency metrics

The system must measure whether one scheduler is enough.

### 1. READY backlog depth
Number of substantive executable `READY` items currently waiting.

Initial healthy range: usually **0–3**. More than five substantive READY items is a capacity warning, not an automatic scale decision.

### 2. Oldest P0/P1 READY age
Elapsed time since the oldest executable high-priority item became READY.

Initial target: **<=48 hours**.

### 3. Trigger-to-action latency
Elapsed time from a material external trigger occurring to the first substantive action on the associated issue.

Initial target: **<=24 hours** for P0/P1 triggers.

### 4. Backlog Pressure Ratio

```text
Pressure Ratio = new executable work created/promoted over 7 days
                 ------------------------------------------------
                 executable work completed over 7 days
```

Interpretation:

- **<0.8** — spare capacity;
- **0.8–1.0** — healthy but busy;
- **1.0–1.25** — backlog accumulating; monitor;
- **>1.25** — meaningful capacity pressure;
- **>1.5 for two consecutive weeks** — strong evidence that a second worker may be justified.

If completed work is zero, do not report a misleading finite ratio; report the denominator failure and assess queue age/saturation directly.

### 5. Run saturation
Share of scheduler runs that finish while higher-priority executable work still remains.

A run is “saturated” when it completed its allowed substantive work but another P0/P1 READY item still waits.

Initial warning threshold: **>80% of runs**.

## Scale-up rule

Start with **one scheduler**.

Add a second scheduler only if **any two** of these conditions persist for **two weeks**:

1. P0/P1 READY age >48h;
2. material trigger-to-action latency >24h;
3. Pressure Ratio >1.25;
4. >5 substantive READY issues;
5. >80% run saturation.

Use judgement for a single exceptional market event; do not redesign the architecture because one unusually busy day temporarily breaches a threshold.

### Default two-scheduler split

If evidence supports scaling:

**Scheduler A — Trigger/Triage**
- scans external triggers;
- promotes/ reprioritizes issues;
- computes queue health;
- maintains orchestration state.

**Scheduler B — Research Worker**
- claims and executes the highest-value READY substantive item;
- performs governed repo updates.

Do not split by company or theme unless later evidence shows that is operationally superior.

## Automation health record

Each meaningful scheduler run should make queue-health observations recoverable, preferably in the automation epic or a future dedicated machine-maintained status surface.

Minimum observations:

- run date/time;
- READY substantive count;
- oldest P0/P1 READY age;
- triggers fired and estimated trigger latency;
- 7-day new executable count;
- 7-day completed executable count;
- Pressure Ratio or denominator warning;
- saturation yes/no;
- item selected;
- item completed / resulting state;
- scheduler-scale recommendation: `ONE SUFFICIENT`, `WATCH`, or `SPLIT CANDIDATE`.

The exact storage surface can evolve, but the definitions above should remain stable enough to compare over time.

## Failure handling

If a run cannot complete its item:

- preserve partial factual work only if source-backed and useful;
- record the failure/blocker in the issue;
- set a truthful state (`READY`, `WAITING`, `BLOCKED` or `PARKED`);
- never mark `DONE` because a run ended;
- never bypass governance to clear the queue.

If a required tool, website or source is unavailable, record the missing dependency rather than fabricating completion.

## Boundaries

Automation may:

- search fresh public information;
- inspect filings/company sources;
- compare evidence;
- update research and portfolio analysis;
- create and maintain backlog issues;
- create branches and PRs;
- merge after required checks pass;
- produce research-level Buy/Add/Trim/Sell signals and thesis-break alerts.

Automation must not:

- place brokerage orders;
- fabricate market data/evidence;
- lower evidence standards to hit the March-2028 objective;
- force-push protected history;
- bypass required checks;
- silently change watchlist/research conclusions;
- keep creating backlog simply to stay busy.

## Initial rollout

The rollout is governed by #120.

1. **#121 — normalize active backlog** into the machine-readable queue contract.
2. **#122 — deploy one Portfolio Ops scheduler and measure capacity** after normalization is sufficient.
3. Run the single-scheduler architecture until the scale-up rule provides evidence for or against splitting.

The design goal is not maximum automation complexity. It is the **minimum reliable orchestration needed to keep the research and portfolio decision loop current**.
