# Robotics Actuators — Research Plan

**Status:** Active discovery programme  
**Parent issue:** #3  
**Last substantive update:** 2026-09-08

## Objective

Identify the actuator functions and suppliers that can become structurally difficult to substitute as advanced robotics moves from prototypes to high-volume industrial deployment.

The programme deliberately separates:

- **Gate A — Bottleneck Strength:** is the function structurally scarce / qualification-heavy?
- **Gate B — Investment Capture:** does a supplier convert the bottleneck into margins, share, backlog, service or total-company earnings?
- **Gate C — Capital Allocation:** is the expected return attractive at the current valuation with tolerable downside?

No company moves directly from thematic relevance to Gate B or C.

---

## Research principles

1. **Architecture before company.** A supplier cannot own a bottleneck if the architecture using its component loses share.
2. **Body zone matters.** Shoulder, wrist, hip, knee, ankle and hand can have different optimal actuator architectures.
3. **Production evidence beats prototype claims.** Supply agreements, mass-production disclosures, field deployments and repeat qualification carry more weight than exhibitions.
4. **Installed reliability matters.** Backlash at time zero is less important than backlash/life/noise/thermal drift after repeated load cycles.
5. **Manufacturing process can be the moat.** Gear patents may expire while heat treatment, grinding, flexspline forming, preload, calibration and yield remain difficult.
6. **Dual-source cost is a key metric.** Ask whether a component can be swapped or whether the entire joint requires redesign/revalidation.
7. **High content is not the same as scarcity.** Bearings, motors and sensors can grow rapidly while remaining competitive/elastic.
8. **Vertical integration is explicit falsification.** Robot OEMs can internalize modules, software, calibration or complete actuators.
9. **Do not capitalize top-down humanoid forecasts.** Use real deployment/supply evidence first.

---

## Gate A scorecard

Each function is scored 1–5 on:

- physical / precision-manufacturing difficulty;
- supply elasticity;
- supplier concentration;
- qualification / switching cost;
- system criticality;
- architecture durability;
- production evidence / field reliability;
- capacity expansion / vertical-integration risk.

A preliminary **≥4.0** score merits focused supplier hunting, but the score is not an investment conclusion.

---

## Execution backlog

### P1 — #78 Rotary reducer architectures

Compare:
- strain-wave;
- cycloidal / RV / Monocrank;
- precision planetary;
- QDD / low-ratio gearing.

Primary questions:
- body-zone share;
- fatigue / rigidity / shock / backlash / backdrivability;
- process moat after patent expiry;
- Chinese supply elasticity;
- customer qualification.

Expected candidate set: Harmonic Drive Systems, Nabtesco, Schaeffler plus evidence-backed Chinese challengers.

### P2 — #79 Linear actuators and screw drives

Compare:
- planetary roller screw;
- inverted roller screw;
- ball screw;
- integrated linear actuator.

Primary questions:
- lower-limb/body-zone adoption;
- thread/roller grinding and matching;
- preload / force sensing;
- supply concentration;
- rotary substitutes.

Expected benchmarks: Schaeffler/Ewellix, Rollvis and evidence-backed listed Asian linear-motion suppliers.

### P3 — #80 Dexterous-hand microactuation

Map:
- micro reducers;
- coreless/DC motors;
- tendon/cable mechanisms;
- miniature bearings;
- tactile/force sensing;
- mechanical locks;
- calibration / assembly.

Primary falsification: simpler grippers / underactuated hands may win on cost and reliability.

### P4 — #81 Common components

Test whether any standalone bottleneck exists in:
- frameless motors;
- magnets / windings;
- encoders/resolvers;
- torque/force sensing;
- cross-roller / thin-section / miniature bearings.

Expected outcome is intentionally uncertain: these may be excellent content-growth layers without high scarcity.

### P5 — #82 Drives, brakes, thermal and industrialization

Test the system-level hypothesis that repeatable actuator production is the durable moat:
- servo/power stage;
- brakes/locks;
- thermal/lubrication;
- integration;
- preload/alignment;
- encoder zero / torque calibration;
- EOL test;
- yield / traceability / field feedback.

Key commercial evidence: Schaeffler/Humanoid seven-digit actuator expectation through 2031.

### P6 — #83 Common-basis synthesis

After #78–#82:
- rank validated bottlenecks;
- map architectures by body zone;
- identify rejected/commoditized layers;
- open only evidence-backed Gate-B company issues;
- update watchlist only when supplier-level evidence warrants.

---

## Current preliminary frontier

Before the deep dives, the strongest hypotheses are:

1. **planetary roller screws / high-force linear conversion — 4.4 preliminary**;
2. **precision strain-wave reducer manufacturing — 4.3 preliminary**;
3. **integrated actuator industrialization / calibration — 4.3 preliminary**;
4. **dexterous-hand microactuation — 4.1 preliminary**;
5. **compact cycloidal/RV — 4.1 preliminary**;
6. **precision planetary/QDD — 4.0 preliminary**.

Motors, sensors, bearings, drives and thermal remain below the provisional 4.0 line until evidence shows narrower supply or stronger switching barriers.

These numbers must be replaced or confirmed by completed deep dives; they are prioritization aids, not findings.

---

## Evidence hierarchy

Prefer, in order:

1. regulatory filings / prospectuses;
2. robot OEM or component supplier signed supply agreements / named deployment evidence;
3. audited annual/interim reports and earnings materials;
4. technical papers / conference data / patents;
5. reputable journalism;
6. industry research where methodology/denominator is visible;
7. supplier marketing only as product-capability evidence, not market-share proof.

Never use anonymous supply-chain rumor as primary qualification evidence.

---

## Completion criteria

### Gate A stream complete when
- #78–#82 are closed with sourced deep dives;
- architecture-specific contradictory evidence is preserved;
- each material layer has an evidence-backed score or explicit rejection;
- #83 produces one common-basis ranking.

### Gate B begins only when
A company has direct evidence that the bottleneck materially affects:
- production/customer qualification;
- revenue/backlog/content;
- pricing/margins/cash;
- durable share/service economics.

### Gate C begins only when
At least two credible Gate-B candidates can be compared on dated valuation, normalized bear/base/bull outcomes, reverse return hurdles and margin of safety.

---

## Re-open triggers after discovery closes

- a major robot OEM discloses a new actuator architecture;
- a supplier wins a named multi-year production programme;
- comparative lifetime/yield data materially changes supplier qualification;
- a new manufacturing process changes reducer/screw economics;
- vertical integration materially changes merchant supplier opportunity;
- valuation creates asymmetric capital-allocation potential in a previously validated candidate.
