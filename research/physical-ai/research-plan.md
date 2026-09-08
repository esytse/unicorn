# Physical AI — Research Plan

**Status:** Active Gate-A discovery  
**Parent issue:** #91  
**Last substantive update:** 2026-09-08

## Objective

Identify the **cross-embodiment bottlenecks and profit pools** created as AI moves from digital reasoning into autonomous action in the physical world.

The programme deliberately separates:

- **Gate A — Bottleneck Strength:** is the function hard to reproduce/substitute at production scale?
- **Gate B — Investment Capture:** can a supplier/operator retain economics from that bottleneck?
- **Gate C — Capital Allocation:** is the expected return attractive at current valuation with tolerable downside?

The existing `research/robotics-actuators/` stream remains valid but is now one downstream substream of the broader Physical AI programme.

---

## Core principles

1. **Loop before BOM.** Model the real-world learning/deployment feedback loop before selecting components.
2. **Cross-embodiment before humanoid-specific.** Compare vehicles, drones, industrial/mobile robots and humanoids.
3. **Real deployment beats demos.** Fleet miles, field hours, production agreements and customer deployment matter more than benchmark videos.
4. **Action data differs from internet data.** Track state/action/outcome alignment, failure coverage and embodiment context.
5. **Synthetic data is both solution and falsification.** It can reduce real-data scarcity but still depends on calibration to reality.
6. **Closed-loop evaluation matters.** Open-loop replay is insufficient for systems whose actions change the environment.
7. **Open models reduce model scarcity.** Separate model capability from proprietary post-training/deployment data.
8. **Edge constraints are explicit.** Latency, power, thermal, sensor bandwidth and safe fallback can make onboard inference a distinct bottleneck.
9. **Technical constraint ≠ merchant profit pool.** Batteries can constrain runtime while remaining commodity-like.
10. **Captive moat ≠ investable supplier.** Tesla/Waymo/Amazon-type feedback loops may be powerful but trapped inside vertically integrated operators.
11. **Avoid double counting.** Reuse the memory, energy and actuator research for shared physical infrastructure.
12. **Do not capitalize top-down robot-unit forecasts.** Tie economics to observed deployment and disclosed contracts.

---

## Gate-A scorecard

Score 1–5 on:

- scarcity / reproducibility;
- real-world data dependence;
- supply elasticity;
- switching / revalidation cost;
- cross-embodiment durability;
- safety / failure consequence;
- learning / network effects;
- open-source / standardization risk;
- vertical-integration risk;
- production/deployment evidence.

A score of **≥4.0** warrants focused supplier/profit-pool hunting, but is not a company recommendation.

---

## Execution backlog

### P1 — #92 Data engines / teleoperation / fleet learning

Test:
- real robot/vehicle state-action data;
- human video;
- teleoperation;
- intervention/failure data;
- data curation and replay;
- fleet learning;
- data rights.

Main question: **does deployment create a compounding proprietary data moat, or can video/synthetic/cross-embodiment learning commoditize it?**

### P2 — #93 World models / simulation / sim-to-real

Test:
- generative world models;
- physics simulation;
- digital twins;
- synthetic data;
- closed-loop evaluation;
- safety critics;
- real-to-sim calibration.

Main question: **is value in the generic simulation platform or in domain-calibrated reality correlation and evaluation?**

### P3 — #94 Training compute / edge inference / runtime

Separate:
- generic training compute already covered by memory/energy;
- simulation compute;
- edge AI accelerators;
- deterministic runtime;
- sensor ingest / memory bandwidth;
- local safety / redundancy.

Main question: **does Physical AI create a distinct merchant edge-compute bottleneck despite custom silicon?**

### P4 — #95 Embodied models / VLA / planning / control

Test:
- VLA weights;
- embodied reasoning;
- whole-body policies;
- post-training;
- cross-embodiment transfer;
- high-level vs low-level control.

Main question: **do model weights stay scarce, or does value migrate to data/post-training/deployment?**

### P5 — #96 Sensing / perception / localization

Test:
- cameras;
- lidar/radar/depth;
- tactile/force;
- IMU/proprioception;
- SLAM/localization;
- sensor fusion/calibration.

Main question: **is any sensing layer scarce across embodiments, or only in specific architectures?**

### P6 — #97 Embodiment / power / industrialization

Reuse actuator findings and add:
- batteries / energy density;
- power electronics;
- thermal;
- structures;
- ruggedization;
- production calibration/reliability.

Main question: **which body constraints remain cross-embodiment and which are form-factor-specific?**

### P7 — #98 Safety / deployment / fleet operations

Test:
- critic/evaluation;
- commissioning;
- remote assist;
- OTA deployment;
- fleet orchestration;
- monitoring / maintenance;
- safety/regulatory evidence.

Main question: **does the most durable economic moat appear after training, when systems meet real workflows and failure consequences?**

### Synthesis — #99

After #92–#98:
- replace preliminary scores with common-basis evidence-backed ranking;
- separate technical bottleneck from merchant profit pool;
- identify captive versus merchantizable feedback loops;
- identify layers already captured by memory/energy/actuator streams;
- open company Gate-B issues only for evidence-backed candidates.

---

## Preliminary frontier to test

1. proprietary real-world feedback / rare-failure data — **4.7 preliminary**
2. domain-calibrated closed-loop evaluation / safety critic — **4.7 preliminary**
3. sim-to-real / domain digital twin — **4.6 preliminary**
4. data engine / curation / replay — **4.6 preliminary**
5. edge inference / deterministic runtime — **4.5 preliminary**
6. fleet operations / continuous learning — **4.5 preliminary**
7. physical industrialization / calibration — **4.4 preliminary / partially validated in actuators**
8. embodiment-specific precision actuation — **4.4 validated in humanoid substream**
9. embodiment-specific post-training/control integration — **4.4 preliminary**
10. generic training compute — **4.3, but cross-theme**
11. base VLA weights — ~**4.1 technical / lower supplier scarcity**
12. generic sensors / motors / batteries — generally below the cross-embodiment Gate-A frontier unless a narrower sublayer validates.

---

## Evidence hierarchy

Prefer:

1. regulatory filings / audited financials;
2. fleet/deployment metrics from operators;
3. signed production/customer agreements;
4. primary technical reports and benchmark methodology;
5. platform docs with reproducible architecture information;
6. peer-reviewed or strong conference work;
7. reputable journalism;
8. supplier marketing only as capability evidence.

Avoid anonymous 'supply chain' claims for qualification or market share.

---

## Gate-A completion criteria

The umbrella structural phase is complete when:

- #92–#98 each have a canonical sourced deep dive;
- each major layer has a score or explicit rejection;
- captive vs merchantizable economics are separated;
- #99 produces a common-basis ranking;
- the actuator findings are integrated without duplication;
- memory/energy cross-links avoid double counting.

## Gate-B entry criteria

A company/platform receives a dedicated underwriting issue only when there is direct evidence of at least one of:

- proprietary deployment/data flywheel;
- multi-customer platform adoption;
- qualification / switching cost;
- recurring software/service economics;
- significant backlog / revenue / margin contribution;
- unusually pure public-market exposure to a validated bottleneck.

## Gate-C entry criteria

At least two Gate-B candidates must be comparable on:

- dated valuation;
- normalized earnings/FCF independent of heroic Physical AI forecasts;
- bear/base/bull outcomes;
- 10/12/15% return hurdles;
- capital intensity / dilution;
- thesis breakers.

---

## Existing actuator backlog treatment

Actuator Gate-B issues #85–#89 remain open for audit continuity, but are **parked behind #99**. Resume them early only if #97/#99 confirm embodiment hardware / precision actuation as one of the leading merchant profit pools.

---

## Re-open / reprioritization triggers

- a major operator discloses a large new data/compute deployment;
- open models materially close the gap with proprietary robot brains;
- cross-embodiment transfer becomes demonstrably reliable;
- synthetic data sharply reduces real-world demonstration requirements;
- a merchant platform wins multiple major OEM/fleet deployments;
- edge compute architecture concentrates around a small supplier set;
- regulation/safety frameworks create a new certification bottleneck;
- a hardware architecture standardizes strongly enough to change component scarcity.
