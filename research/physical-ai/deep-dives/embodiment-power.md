# Physical AI Deep Dive — Embodiment Hardware, Power Density and Field Industrialization

**Issue:** #97  
**Status:** Gate-A initial pass complete  
**Confidence:** Medium-High on industrialization; Medium on energy-density/system constraints  
**Last substantive update:** 2026-09-08

## Executive conclusion

The broader Physical AI view preserves the actuator findings but changes their importance.

**Embodiment-specific precision mechanics can be real bottlenecks without being the dominant cross-Physical-AI profit pool.** The more architecture-resilient physical moat is **repeatable industrialization, calibration, ruggedization and field reliability**.

Energy density is also a real system constraint for mobile embodiments, but **robotics-specific battery-cell or pack scarcity does not currently pass Gate A**.

### Gate-A scores

| Sublayer | Score | Conclusion |
|---|---:|---|
| **Manufacturing / calibration / field reliability** | **4.4** | Pass; cross-embodiment |
| Humanoid precision actuation | **4.4** | Validated in actuator substream; embodiment-specific |
| Ruggedized integration / connectors / harness / environmental reliability | 4.2 | Pass narrowly |
| Energy density as system constraint | 4.2 | Real constraint, not merchant scarcity |
| Thermal / power-density integration | 4.1 | Important, architecture-specific |
| Pack / BMS integration | 3.8 | Broad capability / vertical integration risk |
| Merchant battery-cell scarcity specific to Physical AI | **3.2** | No pass |
| Generic motors / bearings / encoders | mostly <4.0 | Existing actuator negative result |

**Core finding:** the scarce physical layer is less likely to be 'the battery' or 'the motor' and more likely to be the **qualified integrated machine that survives repeated real-world duty at predictable yield, calibration and uptime**.

---

## 1. Existing actuator findings remain valid

The completed `research/robotics-actuators/` programme established:

- qualified precision rotary-transmission manufacture: **4.4/5**;
- planetary roller-screw precision manufacture: **4.4/5**;
- actuator industrialization / calibration: **4.4/5**;
- integrated linear actuators: **4.2/5**;
- dexterous-hand integration: **4.1/5**;
- force/torque sensing: **3.9/5**;
- common motors / encoders / bearings: below Gate A.

These findings are not reversed.

### Physical AI reinterpretation

They are **humanoid/robot-body bottlenecks**, not necessarily the leading cross-embodiment bottlenecks.

An AV, drone, AMR and industrial arm do not share the same reducer or roller screw, but all require:

- repeatable production;
- calibration;
- safety validation;
- thermal/power integration;
- field diagnostics;
- reliability.

That increases the strategic importance of industrialization versus individual mechanical architectures.

---

## 2. Energy density — real constraint, uneven across embodiments

### Drones

Specific energy directly constrains:

- endurance;
- payload;
- range;
- compute/sensor budget.

### Humanoids

Battery mass competes with:

- payload;
- actuator mass;
- thermal hardware;
- runtime.

### AMRs

Can tolerate heavier packs and scheduled charging, so operational optimization can substitute for maximum energy density.

### Autonomous vehicles

Large chassis support large battery packs; energy remains important but is less constraining per unit compute/actuation than in drones/humanoids.

### Industrial arms

Often grid-powered and effectively bypass the battery constraint.

### Conclusion

Energy density scores **4.2/5 as a Physical AI system constraint**, but cross-embodiment universality is incomplete.

---

## 3. Figure F.03 — direct evidence and direct falsification

### FACT

Figure's July 17, 2025 F.03 battery disclosure says:

- battery technology is central to its electromechanical humanoid platform;
- Figure has designed custom packs from F.01 onward;
- across three generations it increased energy density by **94%**;
- the F.03 pack is **2.3 kWh** and enables up to **5 hours** peak-performance runtime;
- the pack supports **2 kW fast charging** with active cooling;
- Figure chose to engineer and manufacture the battery system **in-house at BotQ**.

### INTERPRETATION

This is unusually clean evidence of both sides of the thesis:

1. **energy density matters materially** to humanoid system design;
2. **merchant pack capture is weak enough that a robot OEM can rationally integrate it internally**.

The scarce advantage may therefore be robot-level power/thermal packaging, not an external pack supplier.

---

## 4. Battery cells — likely volume beneficiary, not a robotics-specific moat

Physical AI battery demand will use chemistry/process ecosystems shared with:

- EVs;
- consumer electronics;
- stationary storage;
- drones/power tools.

Robot volumes are not yet sufficient to define a separate cell technology market.

### Why supplier scarcity is weak

- large global cell industry;
- multiple chemistries/form factors;
- robot OEMs can source cells then design packs internally;
- application-specific advantage comes from packaging/BMS/thermal rather than unique cell chemistry in most current systems.

### Score: **3.2/5** for a Physical-AI-specific merchant cell bottleneck.

Do not infer 'millions of robots × battery packs' → structural cell pricing power.

---

## 5. Power electronics / distribution

Physical machines need:

- battery/DC bus;
- BMS;
- motor inverters/drives;
- DC/DC conversion;
- safety isolation;
- current sensing;
- charging;
- regenerative energy handling.

These are technically critical but draw from mature ecosystems in:

- automotive;
- industrial automation;
- drones;
- power electronics.

### Preliminary scores

- motor drives / inverter hardware: **3.6**
- BMS: **3.7**
- robot-level power integration / distribution: **4.0**

Again, integration is more interesting than commodity hardware.

---

## 6. Thermal management

Heat comes from:

- edge compute;
- motors;
- gear/reducer friction;
- battery fast charging/discharging;
- power electronics;
- enclosed electronics.

Thermal limits can reduce:

- sustained torque;
- inference performance;
- battery life;
- runtime;
- component lifetime.

### Why merchant scarcity is limited

Thermal design is highly embodiment-specific:

- passive chassis conduction;
- fans;
- liquid cooling;
- battery active cooling;
- motor thermal paths.

Few universal robotics-specific thermal components dominate.

### Score: **4.1 technical/integration constraint**, lower pure supplier scarcity.

---

## 7. Structures / lightweighting

Physical AI machines trade:

- stiffness;
- mass;
- fatigue life;
- crash/impact tolerance;
- manufacturability;
- cost.

Materials can include:

- aluminum;
- magnesium;
- steel;
- composites;
- engineered polymers.

### Conclusion

Important engineering optimization, but current evidence does not support a broad scarce material profit pool specific to Physical AI.

Score: **3.5/5**.

---

## 8. Ruggedization / connectors / harnessing

Field machines must survive:

- repeated motion;
- vibration;
- shock;
- dust/water;
- connector cycles;
- cable flex;
- thermal cycling;
- accidental impact.

Qualcomm's Physical AI work explicitly notes that conventional robot wiring can fail under repeated motion/stress and discusses future wireless in-robot links as one path to lower wiring complexity.

### INTERPRETATION

This is another example of bottleneck migration:

`more sensors/actuators`
→ more harness/connectors
→ reliability burden
→ architecture may shift to local compute/networked joints/wireless links.

The durable function is ruggedized integration, not necessarily copper cable content.

Score: **4.2/5** for ruggedized system integration / reliability.

---

## 9. Manufacturing and calibration — architecture-resilient physical moat

Production requires repeatability across:

- mechanical tolerances;
- bearing preload;
- gear/screw alignment;
- motor/encoder zero;
- force/torque calibration;
- sensor extrinsics;
- battery/BMS calibration;
- thermal interfaces;
- controller parameters;
- safety limits.

### End-of-line validation can include

- backlash;
- torque/force output;
- noise/vibration;
- thermal soak;
- sensor fusion calibration;
- actuator response;
- battery/charging safety;
- connectivity;
- functional-safety routines.

### Why this survives architecture changes

Whether a robot uses:

- strain-wave or planetary gears;
- roller screw or QDD;
- lidar or vision;
- NVIDIA or Qualcomm compute;

it still needs repeatable production and calibration.

### Score: **4.4/5 — PASS.**

This is the strongest cross-embodiment physical-body function currently validated.

---

## 10. Field reliability / service creates learning data

A deployed physical machine produces:

- component failures;
- calibration drift;
- battery degradation;
- thermal events;
- collision/wear data;
- task failures;
- maintenance interventions.

This links physical industrialization back into the umbrella data thesis:

`production process + field fleet → reliability/failure data → design/calibration changes → better next units`

### INTERPRETATION

A large installed base can create a **manufacturing/reliability feedback loop** analogous to the software data flywheel.

This can favor:

- vertically integrated OEMs;
- module suppliers with many customers;
- field-service platforms with access to failure data.

---

## 11. Contract manufacturing / vertical integration

Merchant capture can leak in two directions:

### OEM insourcing

Figure's battery is an example. Large robot makers may internalize strategically important subsystems.

### Manufacturing outsourcing

If product designs standardize, EMS/contract manufacturers can scale assembly and reduce OEM differentiation.

### Decision rule

A physical supplier deserves Gate B only if it owns one of:

- hard process/yield know-how;
- qualification history;
- proprietary module design;
- field service / installed base;
- multi-OEM learning curve;
- unusually strong total-company exposure.

---

## 12. Cross-embodiment ranking

| Physical layer | Humanoid | AV | Drone | AMR | Industrial arm | Cross-embodiment moat |
|---|---|---|---|---|---|---|
| Industrialization/calibration | High | High | High | High | High | **High** |
| Battery energy density | High | Medium | **Very High** | Medium | Low | Medium |
| Precision actuation | **High** | Low | Medium | Medium | High | Medium-Low |
| Ruggedization/reliability | High | High | High | High | High | **High** |
| Thermal/power integration | High | High | High | Medium | Medium | Medium-High |
| Generic cells | Medium | High content | Medium | Medium | None | Low scarcity |
| Generic motors/bearings | High content | Different stack | Different | High | High | Low scarcity |

---

## 13. Thesis breakers

Raise hardware profit-pool attractiveness if:

- a common actuator/power architecture converges across many robot types;
- one module supplier wins multiple named high-volume OEM programs;
- lifecycle service/spares become substantial recurring revenue;
- manufacturing yield remains difficult despite robot-volume scaling.

Lower it if:

- OEMs vertically integrate batteries/actuators/electronics;
- automotive supply chains commoditize robot hardware quickly;
- contract manufacturing standardizes assembly;
- model/control improvements allow cheaper/lower-spec hardware;
- robot form factors simplify.

---

## 14. Gate-A decision

**PASS — 4.4/5 for manufacturing / calibration / field reliability.**  
**PASS narrowly — 4.2/5 for ruggedized integration.**  
**Technical constraint — 4.2/5 for energy density, but not a merchant-scarcity pass.**  
**NO PASS — 3.2/5 for Physical-AI-specific battery-cell scarcity.**

Existing actuator 4.4/5 sublayers remain valid but are **embodiment-specific rather than umbrella-leading**.

This confirms the user's concern that assuming actuators are the central opportunity would be premature.

No company is promoted to `Watch` from Gate A alone.

## Primary sources

- Figure F.03 Battery Development: https://www.figure.ai/news/f-03-battery-development
- Figure Helix 02: https://www.figure.ai/news/helix-02
- Qualcomm Physical AI architecture: https://www.qualcomm.com/news/onq/2026/02/physical-ai-6g-robotics
- Existing canonical actuator work: `research/robotics-actuators/`
