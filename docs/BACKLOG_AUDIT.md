# Backlog relevance and execution audit

**As of:** 2026-09-25  
**Issue:** #333  
**Open issues after audit:** 46

## Result

Every open automation-relevant issue now contains the full contract: **State, Priority, Type, Trigger, Dependencies, Parent, Next action, Completion gate**.

State distribution at completion of the audit baseline:

| State | Count | Executable? |
|---|---:|---|
| READY | 5 | yes |
| RUNNING | 3 | already claimed |
| WAITING | 20 | no; external/date/evidence trigger |
| BLOCKED | 10 | no; internal prerequisite |
| PARKED | 4 | no; intentionally deprioritized |
| EPIC | 4 | no; coordination only |

Priority distribution: **P0 15 / P1 23 / P2 8**.

## Relevance rule

An open issue must answer at least one current useful question:
- research/discovery;
- monitoring/catalyst;
- portfolio/capital allocation;
- validation/methodology;
- repository infrastructure/governance.

If it does not, close it as completed/not-planned/duplicate rather than carrying it indefinitely. Age alone is not a reason to close a monitor; a monitor survives only when it has an explicit, decision-relevant trigger.

## Relevance decisions

### Keep active / executable
- #325 prospective validation boundary — required before v2 rule changes.
- #327 durability/shareholder-capture experiment — directly addresses historical PROMOTE weakness.
- #330 discovery coverage/negative-search ledger — protects the original architecture-first thesis.
- #335/#341 integrity/documentation test scaffolding — safety net before migration.

### Cleanup programme currently RUNNING
- #331 architecture/source map.
- #333 backlog normalization/relevance.
- #338 documentation audit.

### Corrected from falsely executable to BLOCKED
- #326 waits for #325.
- #328 waits for #326 and #327.
- #329 waits for #325.
- #332/#334/#336/#337/#339/#340 follow their documented cleanup dependencies.

### Retained as trigger monitors, not routine work
Gate-E/event monitors (#67, #86, #101, #103, #106, #108, #125–#130, #132–#133, #146, #261, #292–#295) remain open only because each has a concrete trigger capable of changing evidence, ranking or allocation.

### Parked rather than consuming research capacity
- #85 Harmonic Drive.
- #87 Schaeffler.
- #88 MinebeaMitsumi.
- #102 merchant-data flywheel.

These remain potentially relevant but do not belong in the executable queue absent their explicit triggers.

### Epics
#110, #117, #120 and #168 remain coordination surfaces and are never selected directly.

## Specific relevance corrections made in this audit

- #67 normalized to a P2 energy trigger monitor.
- #87/#88 parked because humanoid exposure is not yet sufficiently material at group level.
- #101 narrowed to residual independent certification/assurance; generic simulation and QNX work are owned elsewhere.
- #102 parked because the strongest merchant-data candidates remain private/non-cleanly investable.
- #103 narrowed to a low-priority edge/runtime architecture monitor; QNX company work is #106.
- #326/#328/#329 corrected to BLOCKED to match their dependencies.
- #292–#295 and legacy orchestration/discovery issues received complete queue metadata.

## Closure assessment

No additional issue met the standard for immediate closure after the relevance pass. The older ambiguous issues were either narrowed to a non-duplicative question or parked behind a material trigger. This is intentional: **PARKED/WAITING is not a soft READY state**.

Future triage should close an issue when:
1. its question is answered and durable findings are in canonical docs;
2. another issue/document fully owns the same remaining question;
3. the thesis can no longer affect the governed universe/portfolio;
4. its trigger is obsolete with no replacement;
5. the programme it supports has been retired.

## Deterministic queue selection

1. Exclude EPIC, WAITING, BLOCKED and PARKED.
2. Exclude RUNNING unless reclaiming a demonstrably stale claim.
3. Consider READY only.
4. P0 before P1 before P2.
5. Within priority, choose the work with highest marginal decision/portfolio contribution, consistent with AGENTS/AUTOMATION.
6. Respect dependencies and bounded-work limits.
7. With no repo changes, two queue selections must return the same ordering.

## Immediate post-audit queue

The cleanup baseline temporarily takes precedence while live P0/P1 monitors continue to interrupt only when a real trigger fires. After #331/#338/#333 close, proceed to integrity tests and architecture rules before structural migration.
