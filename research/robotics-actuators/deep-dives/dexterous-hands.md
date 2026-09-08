# Dexterous Hands — Microactuation, Sensing & Integration Gate A

**Status:** Gate-A screen complete  
**Backlog:** #80  
**Confidence:** **Medium on integration difficulty; Low-Medium on winning architecture**  
**Last substantive update:** 2026-09-08

## Executive conclusion

Dexterous hands are one of the most mechanically dense parts of a humanoid, but **high component count is not the same as supplier scarcity**.

**CONCLUSION:** **Dexterous-hand integration / industrialization passes Gate A narrowly at 4.1/5.** Individual microactuation, bearings and tactile/force sensors do **not** currently pass a 4.0 supplier-scarcity threshold because hand architectures remain highly diverse and there are multiple ways to trade actuator count, tendon routing, linkage, compliance and sensing.

Current scores:

| Function | Bottleneck Strength | Conclusion |
|---|---:|---|
| Hand-level mechanical/electrical integration, routing, calibration and durability | **4.1 / 5** | Gate A passed narrowly |
| High-torque micro actuator / miniature geared drive | **4.0 / 5** | technical Gate A borderline; architecture-dependent |
| Tendon/cable/linkage transmission | **3.8 / 5** | difficult wear/routing problem, but design-specific rather than concentrated supply |
| Fingertip force/tactile sensing | **3.8 / 5** | performance-critical; many sensing technologies / in-house options |
| Miniature bearings | **3.6 / 5** | very high content, broad supplier base |
| Small/coreless/BLDC motors | **3.6 / 5** | packaging/performance critical, broad supply |

The key result is:

> **The hand may create the highest part-count multiplier in the robot without creating the best merchant component bottleneck.**

---

## 1. Why a hand is a different actuator economy

A human-like hand requires some combination of:

```text
motor / micro actuator
→ reducer or tendon/linkage transmission
→ miniature bearings / pivots
→ joints / compliant structures
→ fingertip force / tactile sensing
→ tendon tension / position feedback
→ cable routing / electronics
→ hand controller
→ calibration + grasp control
```

Unlike a shoulder or knee, a hand multiplies these subsystems across many fingers and degrees of freedom while imposing severe limits on:

- diameter and mass;
- noise;
- holding power;
- wire/tendon routing;
- thermal rise;
- backlash / compliance;
- fingertip sensitivity;
- impact resistance;
- serviceability.

Cost also compounds rapidly because every additional active degree of freedom adds actuator, transmission, bearing, sensing, wiring and calibration content.

---

## 2. Direct production-oriented platform evidence — MinebeaMitsumi + HDS

**FACT:** MinebeaMitsumi and Harmonic Drive Systems jointly developed an ultra-compact high-torque geared micro actuator for robot hands.

**FACT:** MinebeaMitsumi's CES/Q3 FY3/2026 materials describe a hand using:
- **11 actuators**;
- **107 bearings** in the disclosed Q3 configuration;
- **5 force sensors**;
- high-response DC motors;
- ultra-compact HarmonicDrive reducers;
- two reduction-ratio actuators per finger to combine speed and gripping force;
- wire-driven fingertips to reduce distal weight;
- a mechanical lock to reduce power while holding;
- strain-gauge / MEMS force sensing capable of detecting force direction, pinch location and slip.

A later product page cites 85 bearings in its current exhibit configuration. This difference itself is evidence that the design is still evolving rather than a fixed industry BOM.

**INTERPRETATION:** The Minebea/HDS hand demonstrates how many precision layers can coexist in one hand, but it should **not** be generalized to every production humanoid.

---

## 3. Strong falsification — radically different hand architectures are credible

### Tendon + linkage

**FACT:** A 2026 Scientific Reports paper demonstrated a 20-DoF humanoid hand with **15 active and 5 passive DoF** using a hybrid tendon-and-linkage system plus thin-film pressure sensors and embedded multi-sensor control.

The design intentionally uses mechanical coupling/passive DoF to reduce actuation burden while retaining grasp capability.

### Schaeffler

**FACT:** Schaeffler's February 2026 humanoid materials describe a dexterous-hand concept with:
- modular fingers;
- **20 DoF**;
- tendon-based actuation;
- integrated tactile sensors;
- in-house transmission and motor drive;
- high vertical integration / scalable forming and production processes.

**INTERPRETATION:** These designs directly falsify the idea that a production dexterous hand must use one micro geared actuator per finger joint or a standard sensor stack.

**THESIS BREAKER:** A commercially successful humanoid may use a much simpler underactuated hand or task-specific gripper, reducing total hand component value dramatically.

---

## 4. Microactuation

### What is hard

Miniature actuators must simultaneously deliver:
- high torque per diameter;
- high response speed;
- low backlash;
- low noise;
- low holding power;
- low heat;
- repeated shock/wear survival.

HDS/Minebea's co-developed unit is only about 13 mm wide in Minebea's CES disclosure and couples a micro reducer with a high-response motor and miniature bearings.

### Why supplier scarcity is capped

Alternative hand architectures can use:
- remote motors + tendons;
- direct small motors;
- conventional micro gearboxes;
- miniature strain-wave reducers;
- underactuated linkages;
- compliant mechanisms.

**INTERPRETATION:** Miniaturization is hard, but architecture substitution reduces the durability of any single microactuator supplier's moat.

**Bottleneck Strength: 4.0 / 5 — borderline.**

---

## 5. Tendons / cables / linkages

Tendon systems move mass out of the fingers and allow small motors to be placed in the palm/forearm.

The engineering challenges are substantial:
- cable stretch and creep;
- routing friction;
- hysteresis;
- fatigue at pulleys/anchors;
- tensioning/preload;
- replacement/service;
- coupled motion and calibration.

But these are usually **robot-design / integration problems**, not a concentrated merchant component market.

**Bottleneck Strength: 3.8 / 5.**

---

## 6. Force and tactile sensing

Dexterous manipulation benefits from sensing:
- normal force;
- shear/slip;
- contact location;
- multi-axis load;
- tendon tension;
- joint position.

**FACT:** MinebeaMitsumi is developing compact strain-gauge and MEMS 3-axis/6-axis fingertip sensors and says worldwide inquiries/orders for its humanoid component portfolio accelerated after CES 2026.

**FACT:** Schaeffler is pursuing integrated tactile sensors and automotive-derived MEMS production.

**FACT:** Current academic hands also demonstrate thin-film pressure sensors and custom multi-sensor systems.

**INTERPRETATION:** This is a technically important layer but currently has **many sensing modalities and high vertical-integration potential**. The robot OEM can trade tactile arrays, force sensors, motor-current estimation, vision and learned contact models.

**Bottleneck Strength: 3.8 / 5.**

Re-open if a specific sensor becomes process-of-record across multiple production humanoid platforms.

---

## 7. Bearings — the content trap

**FACT:** MinebeaMitsumi's 2026 investor materials estimate roughly **30–100 bearings per hand** and **120–200 per body excluding hands** for high-performance humanoids, with one CES hand prototype using more than 100 bearings.

This is enormous unit content.

However:
- miniature ball bearings are produced by multiple capable suppliers;
- bearing sizes/designs can change radically with tendon/linkage architecture;
- not all hands use miniature reducers at every joint;
- bearing content is unlikely to be qualification-concentrated in the same way as a reducer or roller screw.

**CONCLUSION:** Bearings can be an exceptional **volume/content beneficiary** without being a structural bottleneck.

**Miniature-bearing Bottleneck Strength: 3.6 / 5.**

---

## 8. The actual hand bottleneck: integration and durability

Hand integration couples:
- actuator placement;
- tendon/gear routing;
- joint geometry;
- bearing stacks;
- tactile sensing;
- wiring/flex circuits;
- mechanical locks;
- grasp controller;
- calibration;
- thermal / power budget.

Failures can include:
- tendon wear/stretch;
- gear backlash growth;
- wire fatigue;
- sensor drift;
- fingertip impact damage;
- loss of calibration;
- debris/contamination;
- actuator overheating.

**INTERPRETATION:** The hand-level bottleneck is therefore closer to **miniaturized mechatronic system industrialization** than any individual catalog part.

But this function has high **vertical-integration risk**: Schaeffler, MinebeaMitsumi and robot OEMs can integrate substantial portions internally.

### Gate-A score — hand integration

| Dimension | Score | Rationale |
|---|---:|---|
| engineering / packaging difficulty | **4.8** | many DoF / sensors / wires / transmissions in extreme volume constraint |
| supply elasticity | **4.0** | few truly production-mature hands, but many architectures/teams can iterate |
| supplier concentration | **3.4** | no stable merchant supplier structure yet |
| qualification / switching cost | **4.5** | whole grasp/control/mechanical stack changes with hand design |
| system criticality | **4.4** for manipulation tasks | high for general manipulation, lower for task-specific robots |
| architecture durability | **3.5** | underactuation/simple grippers can remove much complexity |
| production evidence | **3.8** | credible platforms exist; mass industrial lifetime evidence remains limited |

**Bottleneck Strength: 4.1 / 5 — Gate A passed narrowly for integration, not individual hand components.**

---

## 9. Supplier implications

### MinebeaMitsumi
Strongest current **component-content** evidence:
- bearings;
- DC/brushless motors;
- force sensors;
- analog signal chain;
- connectors;
- ball screws;
- hand-level demonstrator with HDS.

This makes Minebea a candidate for later Gate-B work if humanoid orders become financially material, but the breadth also means no one component needs to be scarce.

### Harmonic Drive Systems
Has direct micro-reducer/actuator relevance through the Minebea collaboration, but hand architecture substitution adds another risk on top of broader strain-wave competition.

### Schaeffler
Provides important integration/verticalization evidence: a tendon hand, sensors, ball-screw transmission and automotive production technology can be combined inside one group.

No hand-specific company is promoted from #80.

---

## 10. Research implication

#80 materially lowers the priority of hunting individual hand bearings or tactile sensors.

The remaining high-value question moves to #82:

> **If hand-level integration is difficult but not merchant-concentrated, is the broader repeatable actuator/module industrialization process the true architecture-resilient bottleneck?**

#81 should separately test whether any body-level motor/sensor/bearing class escapes the same content-without-scarcity problem.

---

## Sources

- MinebeaMitsumi Q3 FY3/2026 humanoid materials: https://www.minebeamitsumi.com/english/corp/investors/disclosure/financial/p2026/__icsFiles/afieldfile/2026/02/05/e2026_q3_presentation_en.pdf
- MinebeaMitsumi humanoid product platform: https://product.minebeamitsumi.com/en/pickup/humanoidrobot/index.html
- MinebeaMitsumi CES 2026 announcement: https://www.minebeamitsumi.com/english/news/press/2025/1210639_20344.html
- Schaeffler Humanoids at Schaeffler, Feb 2026: https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20260205_humanoids_at_schaeffler.pdf
- Scientific Reports 2026 tendon/linkage dexterous hand: https://doi.org/10.1038/s41598-026-63917-x
- Research 2026 system-level dexterous-hand review: https://doi.org/10.34133/research.1388
