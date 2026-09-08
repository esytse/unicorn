# Physical AI — Research Plan

**Status:** Gate A complete; Gate B merchant-capture research active  
**Parent issue:** #91  
**Last substantive update:** 2026-09-08

## Objective

Identify the **cross-embodiment bottlenecks and merchant profit pools** created as AI moves from digital reasoning into autonomous action in the physical world.

The programme separates:

- **Gate A — Bottleneck Strength:** is the function hard to reproduce/substitute at production scale?
- **Gate B — Investment Capture:** can a supplier/operator retain economics from that bottleneck?
- **Gate C — Capital Allocation:** is expected return attractive at current valuation with tolerable downside?

`research/robotics-actuators/` remains a valid detailed embodiment-hardware substream, not the umbrella thesis.

---

## Research principles

1. **Loop before BOM.** Start with the real-world learning/deployment loop, not component counts.
2. **Cross-embodiment before humanoid-specific.** Compare vehicles, drones, industrial/mobile robots and humanoids.
3. **Real deployment beats demos.** Fleet miles/hours, production programs and field economics outrank showcase capability.
4. **Action data differs from internet data.** Track state/action/outcome alignment, failures, interventions and embodiment context.
5. **Synthetic data is solution and falsification.** It can scale learning while increasing the importance of real calibration anchors.
6. **Closed-loop evaluation matters.** Physical actions change the next state; replay alone is insufficient.
7. **Open models reduce base-model scarcity.** Separate model capability from post-training/data/deployment moats.
8. **Edge constraints are explicit.** Latency, power, thermal, sensor I/O and safe fallback create a distinct physical-AI runtime problem.
9. **Technical constraint ≠ merchant profit pool.** Energy density can bind without creating a robotics-specific battery moat.
10. **Captive moat ≠ investable supplier.** A Tesla/Waymo/Amazon/Figure feedback loop may be powerful while difficult to buy cleanly.
11. **Avoid double counting.** Reuse memory, energy and actuator findings where the bottleneck is already canonical.
12. **Do not capitalize top-down robot-unit forecasts.** Tie economics to deployment and signed/commercial evidence.
13. **Data rights are a Gate-B variable.** A multi-customer platform has no data flywheel if contracts prevent cross-deployment learning.
14. **Safety evidence can create secondary switching costs.** Component substitution can force retraining/revalidation even when hardware is technically multi-source.

---

## Gate-A result — complete

### Validated structural frontier

1. **real deployment feedback / rare failure data — 4.7**
2. **closed-loop safety / policy evaluation — 4.7**
3. **domain-calibrated sim-to-real / digital twin — 4.6**
4. **data-engine curation / replay — 4.6**
5. **safety validation / certification evidence — 4.6**
6. **edge performance-per-watt / latency — 4.5 as system constraint**
7. **fleet operations / continuous learning — 4.5**
8. **manufacturing / calibration / field reliability — 4.4**
9. **embodiment-specific post-training / transfer — 4.4**
10. **precision actuation / motion conversion — 4.4, embodiment-specific**
11. deployment / commissioning — 4.4
12. sensor fusion / calibration — 4.2
13. energy density — 4.2 as system constraint

### Explicit negative / narrowed results

- **General VLA/model weights:** technically important, only ~3.8 current supplier scarcity because open models and rapid diffusion are strong falsification.
- **Merchant edge-accelerator concentration:** ~3.9 despite a 4.5 system constraint; NVIDIA/Qualcomm/custom silicon prevent a single-vendor conclusion.
- **Generic sensors:** no camera/lidar/radar category passes cross-embodiment Gate A; architecture is not converged.
- **Physical-AI-specific battery cells:** ~3.2; real energy constraint, weak robotics-specific supplier scarcity.
- **Generic motors / bearings / encoders:** existing actuator work keeps these below Gate A despite high unit content.

Canonical synthesis: `synthesis-ranking.md`.

---

## Completed Gate-A issues

- **#92** data engines / teleoperation / fleet learning
- **#93** world models / simulation / digital twins / sim-to-real
- **#94** training compute / edge inference / runtime
- **#95** embodied models / VLA / planning / control transfer
- **#96** sensing / perception / localization
- **#97** embodiment hardware / power / industrialization
- **#98** safety / evaluation / deployment / fleet operations
- **#99** common-basis synthesis

Parent #91 can close after the governed umbrella PR lands.

---

# Gate B — active backlog

Gate B now asks **where the validated bottlenecks escape captive OEMs and become merchant economics**.

## P1 — #100 Simulation / digital-twin / evaluation platforms

### Why first

Domain-calibrated simulation/evaluation combines:

- 4.6–4.7 structural score;
- cross-embodiment applicability;
- possibility of serving many customers;
- recurring software/engineering/service economics;
- switching cost after virtual-controller / digital-twin validation.

### Required tests

- paid production usage, not demos;
- multi-customer adoption;
- recurring revenue / retention;
- reality correlation / virtual commissioning;
- domain-data ownership;
- open/NVIDIA commoditization;
- total-company earnings sensitivity.

Do not assume generic simulation is scarce.

---

## P2 — #101 Safety runtime / validation / certification platforms

### Why second

NVIDIA Halos provides direct evidence that safety can become a reusable platform across AVs and robotics.

### Required tests

- production OEM design-ins;
- hardware/software pull-through;
- inspection/certification monetization;
- recurring safety/runtime economics;
- switching cost from validated configurations;
- open standards / independent certification as falsification.

---

## P3 — #102 Merchant data / robot-brain / fleet-learning flywheels

### Why potentially highest upside

The data flywheel is the strongest structural moat.

### Why not first

The evidence hurdle for **merchant capture** is much higher:

- customer data rights;
- privacy/IP restrictions;
- OEM insourcing;
- private-company concentration;
- open model substitutes.

A platform passes only if it can demonstrably **learn across customer deployments** and retain the resulting economics.

---

## P4 — #103 Edge compute / deterministic runtime platforms

### Required comparison

- NVIDIA Jetson/IGX/Thor + software/safety stack;
- Qualcomm Dragonwing robotics + mixed-criticality/runtime architecture;
- Tesla/Waymo/custom silicon as disintermediation benchmarks;
- model efficiency as hardware-demand falsification.

Do not promote a semiconductor supplier solely because local compute is essential.

---

# Existing actuator Gate B treatment

Open issues:

- #85 Harmonic Drive Systems
- #86 Laifual Drive
- #87 Schaeffler
- #88 MinebeaMitsumi
- #89 actuator Gate C

These remain open for audit continuity but are **parked behind #100–#103**.

Resume early only if:

- new named high-volume customer evidence appears;
- valuation changes materially;
- #100–#103 fail to produce merchantizable economics;
- new evidence strengthens precision hardware as a superior profit pool.

---

# Gate-B common scorecard

For every platform/company assess:

- structural bottleneck inherited from Gate A;
- **merchant vs captive** value;
- multi-customer production adoption;
- data / learning rights;
- switching / revalidation cost;
- recurring revenue / service;
- gross/operating margin evidence;
- capex / working capital / cash conversion;
- open-source / standardization risk;
- vertical-integration risk;
- total-company revenue/earnings sensitivity;
- public investability / valuation only after operating capture is credible.

A strong Gate-B candidate should normally show a credible **feedback-loop or qualification moat**, not merely high market growth.

---

# Gate C — not yet opened at umbrella level

Gate C begins after at least two credible Gate-B candidates can be compared on:

- dated price / market cap / EV;
- normalized base business independent of heroic Physical AI forecasts;
- explicit Physical AI contribution scenarios tied to production evidence;
- bear/base/bull 3–5 year outcomes;
- reverse 10/12/15% annualized-return hurdles;
- margin-of-safety zones;
- dilution/capex/working-capital effects;
- thesis breakers.

No automatic Gate C from strategic importance.

---

# Evidence hierarchy

Prefer:

1. regulatory filings / audited financials;
2. fleet/deployment metrics from operators;
3. signed production/customer agreements;
4. safety/certification records and standards evidence;
5. primary technical reports / benchmark methodology;
6. platform docs with reproducible architecture information;
7. peer-reviewed / strong conference work;
8. reputable journalism;
9. supplier marketing only as capability evidence.

Avoid anonymous supply-chain claims for production qualification or market share.

---

# Re-open / reprioritization triggers

- cross-embodiment transfer becomes demonstrably reliable or fails materially;
- synthetic data sharply reduces real-data needs;
- a platform wins multiple production OEMs with retained learning rights;
- regulators/customers standardize Physical AI safety evidence;
- edge compute concentrates around a small certified platform set;
- a sensor architecture converges across major embodiments;
- a hardware architecture standardizes enough to alter component scarcity;
- valuation creates a large margin-of-safety opportunity in a previously validated actuator or platform candidate.
