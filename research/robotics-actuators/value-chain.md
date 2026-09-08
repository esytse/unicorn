# Robotics Actuators — End-to-End Value Chain

**Status:** Initial E2E map complete; Gate-A deep dives opened  
**Confidence:** **Medium** on architecture decomposition; **Low-Medium** on preliminary supplier-scarcity scores  
**Last substantive update:** 2026-09-08  
**Parent backlog:** #3

## Executive conclusion

**INTERPRETATION:** Advanced-robot actuation is not one component market. It is a coupled electromechanical stack whose bottleneck can move between **transmission architecture, precision manufacture, sensing, thermal design and actuator industrialization**.

The most important early conclusion is that there is **no single winning humanoid-joint architecture**. Current evidence supports at least four distinct actuation economies:

1. **high-ratio rotary joints** — frameless/high-response motor + strain-wave, cycloidal/RV or precision planetary transmission + bearings + position/torque feedback;
2. **low-ratio / quasi-direct-drive rotary joints** — larger torque motor + lower-ratio planetary or other compact gearing, trading reduction ratio for backdrivability and control bandwidth;
3. **linear joints** — motor + planetary roller screw / ball screw + thrust support + position/force sensing, attractive where high force is required over short stroke;
4. **dexterous hands** — miniature motors/reducers or tendon drives + very high bearing/sensor counts + tactile/force sensing, with a different miniaturization and reliability problem from body joints.

**FACT:** Schaeffler's December 2025 humanoid portfolio model estimates rotary-actuator integration at roughly **25%** of humanoid BOM, linear-actuator integration at roughly **30%**, and the dexterous hand at roughly **20%**. These figures are a supplier estimate rather than an industry standard, but they are useful evidence that the opportunity should not be reduced to harmonic reducers alone.

**FACT:** Schaeffler has disclosed both strain-wave and planetary rotary actuator platforms and linear actuator products, and in 2026 signed supply agreements for humanoid joint actuators with Humanoid and Hexagon Robotics. Humanoid says its five-year agreement makes Schaeffler preferred supplier for more than half of the wheeled platform's joint-actuator demand through 2031 and is expected to represent a **seven-digit number of actuators**.

**INTERPRETATION:** The strongest early hunting ground is therefore **qualified motion conversion + repeatable actuator industrialization**, not simply raw motor content.

---

## 1. End-to-end stack

```text
robot task / payload / duty cycle / safety target
        ↓
body-zone architecture choice
(rotary high-ratio / rotary QDD / linear / hand microactuation)
        ↓
energy storage + DC bus
        ↓
servo drive / inverter / motor-driver IC
        ↓
ELECTRICAL-TO-MECHANICAL CONVERSION
frameless torque motor / BLDC / coreless / stepping motor
        ↓
MOTION CONVERSION / TRANSMISSION
├─ strain-wave reducer
├─ cycloidal / RV / monocrank reducer
├─ precision planetary / low-ratio QDD gearbox
├─ planetary roller screw / inverted roller screw
└─ ball screw / miniature screw / tendon mechanism
        ↓
LOAD SUPPORT + SAFETY
cross-roller / thin-section / angular-contact / miniature bearings
brake / lock / stops / seals / lubrication
        ↓
FEEDBACK
motor/joint encoder or resolver
joint torque / strain sensing
linear force sensing
hand tactile / multi-axis force sensing
        ↓
ACTUATOR INTEGRATION
housing + preload + alignment + thermal path + wiring/connectors
controller firmware / commutation / torque control
        ↓
INDUSTRIALIZATION
precision grinding / gear cutting / forming / heat treatment
bearing fit / winding / magnet placement / assembly
encoder zeroing / torque calibration / backlash setup
EOL dynamometer / noise / thermal / lifetime / shock test
traceability + field reliability
        ↓
robot limb / hand integration
        ↓
system calibration / controls / sim-to-real / fleet feedback
```

The value chain is serial: a high-performance reducer does not create a production-ready joint if the motor overheats, encoder drifts, bearing stack loses stiffness or end-of-line calibration cannot be repeated at volume.

---

## 2. Architecture map by robot/body zone

The map below is deliberately probabilistic. Robot OEMs are still iterating rapidly and multiple architectures can serve the same joint.

| Robot / body zone | Current architecture candidates | Why it can win | Main trade-off / falsification | Research status |
|---|---|---|---|---|
| Humanoid shoulder / hip | strain-wave, compact cycloidal/RV, precision planetary integrated rotary actuator | high torque in compact envelope; rigidity and shock resistance matter | weight, reflected inertia, backdrivability and fall loads can shift architecture | #78 |
| Humanoid elbow / wrist / arm | strain-wave and compact planetary common candidates | low backlash, low weight, compact packaging | Chinese strain-wave supply expansion and planetary alternatives reduce single-supplier scarcity | #78 |
| Dynamic humanoid lower limb | QDD / low-ratio planetary **or** linear screw actuator depending robot | backdrivability/control bandwidth vs very high linear force density | no universal architecture; duty cycle and packaging determine winner | #78 / #79 |
| Payload-oriented knee / ankle / leg | planetary roller screw / inverted roller screw / ball screw in some architectures | high axial force and stiffness over short stroke | screw cost, efficiency, stroke and sensing burden; rotary alternatives remain viable | #79 |
| Dexterous hand / fingers | micro geared actuators, micro strain-wave, coreless motors, tendon/cable drives | extreme packaging and force-control requirements | architecture is highly unsettled; reliability and cost may favor simpler hands | #80 |
| Cobots / light industrial arms | strain-wave + integrated torque sensing; some planetary | compact low-backlash joints and force control | supplier base broadening; robot OEM integration | #78 / #81 |
| Heavy industrial robots | cycloidal/RV at large joints; strain-wave at smaller axes | shock load, rigidity, mature installed base | established market may not translate directly to humanoid economics | benchmark |
| Quadrupeds / highly dynamic legged robots | QDD / lower-ratio geared rotary actuators are an important architecture | backdrivability and fast torque control | larger motor/current/thermal burden | #78 |
| Exoskeletons | planetary/QDD and harmonic-drive architectures both used | transparency/safety vs compact torque | no clear universal winner; controller quality matters | benchmark |

**FACT:** A 2026 peer-reviewed comparison of harmonic-drive and planetary actuation units for exoskeletons confirms that transmission choice changes friction, inertia and perceived transparency rather than producing a universally superior architecture.

**FACT:** A 2026 review of humanoid joint modules identifies QDD as especially attractive for dynamic lower-limb locomotion because lower reduction improves backdrivability and control bandwidth.

**OPEN QUESTION:** Which of these architectures survives the cost / reliability / energy-efficiency requirements of multi-shift industrial humanoid deployment rather than prototype demonstrations?

---

## 3. Component / process map and preliminary bottleneck screen

These are **preliminary research-priority scores**, not completed Gate-A conclusions.

| Layer | What matters technically | Supply / substitution hypothesis | Preliminary Bottleneck Strength | Next work |
|---|---|---|---:|---|
| Planetary roller screws / high-force linear conversion | load sharing, thread geometry, precision grinding, preload, speed, life | potentially narrow qualified process capability; architecture-dependent | **4.4** | #79 P2 |
| Precision strain-wave reducer manufacture | flexspline fatigue, tooth profile, concentricity, heat treatment, bearings, life/backlash consistency | historically concentrated but Chinese mass production and alternatives are increasing elasticity | **4.3** | #78 P1 |
| Actuator integration / calibration / high-volume industrialization | tolerance stack, preload, encoder zero, thermal path, torque calibration, yield, traceability | could be more durable than any one component; high vertical-integration risk | **4.3** | #82 P5 |
| Dexterous-hand microactuation / sensing | miniaturization, wiring/tendon wear, bearings, force/tactile calibration | high engineering difficulty but architecture still unsettled | **4.1** | #80 P3 |
| Compact cycloidal/RV | rigidity, shock load, high engaged-tooth count, backlash, weight | strong process know-how; humanoid share not established | **4.1** | #78 P1 |
| Precision planetary / QDD gear stage | efficiency, noise, backlash, tooth load, bearing support | broader gear-making base; integrated design may be harder than gearbox alone | **4.0** | #78 P1 |
| Joint force / torque sensing | drift, overload, calibration, bandwidth, packaging | important for compliance but may be partly substituted by motor-current/model-based estimation | **3.9** | #81 P4 |
| Cross-roller / thin-section / specialized bearings | rigidity, compactness, preload, life, low noise | high content and precision but multiple global suppliers | **3.8** | #81 P4 |
| Frameless torque motors | torque density, cogging, winding fill, magnets, heat rejection | many capable suppliers; customization/integration stronger than motor scarcity | **3.7** | #81 P4 |
| Absolute encoders / resolvers | resolution, latency, compact hollow-shaft geometry, EMI/thermal stability | broad optical/magnetic/inductive supplier options | **3.7** | #81 P4 |
| Thermal / lubrication design | continuous torque, gear/bearing life, motor temperature | critical function but distributed across materials/design rather than obvious merchant chokepoint | **3.6** | #82 P5 |
| Servo drive / power stage | current density, switching losses, control latency, safety | mature semiconductor/power-electronics ecosystem; integration matters | **3.5** | #82 P5 |
| Brakes / mechanical locks | holding safety, energy reduction, fail-safe behavior | joint-dependent and relatively broad supplier base | **3.3** | #82 P5 |

### Initial ranking implication

**HYPOTHESIS:** The leading structural candidates are **roller-screw linear conversion**, **qualified precision reducers**, and **actuator industrialization/calibration**. Motors, bearings and sensors may have excellent content growth without equivalent scarcity.

This is intentionally different from a thematic supplier list. High unit count does not automatically create pricing power.

---

## 4. Architecture-specific transmission economics

### 4.1 Strain-wave gearing

Strengths:
- very high reduction in a compact/light package;
- low backlash and high positioning accuracy;
- hollow-shaft and flat configurations support joint packaging.

Risks:
- flexspline cyclic fatigue and life consistency;
- stiffness / ratcheting / shock-load concerns versus more rigid architectures;
- reflected inertia/backdrivability at high ratios;
- manufacturing barriers may weaken as more suppliers reach production quality.

**FACT:** Harmonic Drive Systems says it pursues materials, structural analysis and repeated endurance testing in the reducer business. It disclosed in 2024 that it was supplying prototype humanoid products to multiple startups and had begun mass production for some customers; its 2026 plan identifies AI robots as a focus development area.

**FACT:** Laifual's 2026 Hong Kong listing document says it was one of two Chinese manufacturers that had achieved deliveries and mass production of harmonic reducers for humanoid robots by end-2025; it reported 21.4% shipment share in China's robotic harmonic-reducer market in 2025 according to CIC.

**INTERPRETATION:** Strain-wave gearing remains a high-quality bottleneck candidate, but **incumbent exclusivity is already being falsified**. Gate A must test process/lifetime consistency and qualification, not rely on old market-share data.

### 4.2 Cycloidal / RV

Strengths:
- high rigidity and shock-load capability;
- multiple engaged elements distribute load;
- strong industrial-robot field history.

Risks:
- size/weight and inertia can be unattractive for distal joints;
- humanoid-specific adoption is less mature.

**FACT:** Nabtesco's 2026 materials position the compact Monocrank series specifically for humanoid shoulder and hip joints and emphasize high rigidity, high torque density and resistance to skipped/ratcheted motion. Nabtesco also offers strain-wave products through Ovalo.

### 4.3 Planetary / QDD

Strengths:
- high efficiency and potentially better backdrivability at lower ratios;
- conventional gear geometry can support scalable industrial production;
- strong fit where dynamic force control matters.

Risks:
- lower ratios require larger/higher-current torque motors;
- multi-stage precision gearing can reintroduce backlash, noise and tolerance-stack complexity.

**FACT:** Schaeffler's 2026 humanoid planetary actuator integrates a two-stage planetary gearbox, motor, encoder and controller over 60–250 Nm. Schaeffler has also signed actuator supply partnerships with Humanoid and Hexagon Robotics.

**INTERPRETATION:** Schaeffler is important falsification against a thesis that only specialist harmonic-drive vendors can industrialize humanoid joints.

---

## 5. Linear actuation

A linear actuator typically maps:

```text
motor → gear/drive if needed → roller/ball screw → nut/roller set
→ thrust/radial support → force/position sensing → housing
```

**FACT:** Schaeffler's humanoid portfolio includes inverted roller screws, planetary roller screws, ball-screw drives, bearings, sensors and integrated linear actuators. Its own BOM framework places linear-actuator integration at ~30% of the illustrative humanoid BOM.

**FACT:** Ewellix describes planetary roller screws as high-load, high-speed, high-acceleration, long-life devices with customized/preloaded variants and diameters from 8 to 240 mm.

**HYPOTHESIS:** Planetary roller screws may have stronger manufacturing scarcity than motors or bearings because many precision threaded rollers must share load with controlled geometry and preload. This is the highest-priority falsifiable hypothesis in #79.

**OPEN QUESTION:** Does humanoid architecture converge on roller screws in enough high-value joints for supplier scarcity to matter, or do QDD/rotary architectures prevent scale concentration?

---

## 6. Bearings and sensing

### Bearings

**FACT:** THK and IKO both market cross-roller bearings for high-rigidity, compact robot-joint applications.

**FACT:** MinebeaMitsumi says one humanoid startup uses approximately **170 of its bearings per robot** and its CES 2026 hand prototype used more than 100 bearings. These are company-specific examples, not universal humanoid BOMs.

**INTERPRETATION:** Bearing content can scale enormously with humanoid adoption. However, high content is not yet evidence of structural scarcity; the qualified global bearing base is broad. The research target is narrow classes such as ultra-thin, cross-roller or miniature bearings where robot-specific qualification might matter.

### Position and force feedback

Joint feedback can include:
- motor-side encoder/resolver;
- output-side absolute encoder;
- torque/strain sensing;
- linear force sensing;
- fingertip tactile/multi-axis force sensing.

**FACT:** MinebeaMitsumi is explicitly marketing single-axis torque sensors, multi-axis force sensors and multiple motor/bearing products for humanoids. Schaeffler's platform similarly includes inductive position sensing and MEMS force/torque sensing.

**HYPOTHESIS:** sensing may be a **performance-critical but relatively substitutable** layer unless production calibration, drift/overload performance or process-of-record evidence reveals a narrower supplier set.

---

## 7. Dexterous hands are a separate economy

**FACT:** MinebeaMitsumi and Harmonic Drive Systems co-developed a high-torque micro actuator for a robot hand. The CES 2026 prototype used 11 actuators and more than 100 bearings, with strain/MEMS force sensing and mechanical locking to reduce holding power.

**INTERPRETATION:** Hand economics differ from torso/leg joints:
- part counts are much higher;
- allowable mass and diameter are much lower;
- wire/tendon routing, miniaturized bearings and tactile calibration become dominant;
- cost pressure is severe because fingers multiply every component.

**OPEN QUESTION:** Does the winning hand architecture use one actuator per degree of freedom, underactuated/tendon mechanisms, remote motors or radically simpler grippers? Until that settles, hand component scarcity deserves separate treatment in #80.

---

## 8. Actuator industrialization may be the hidden bottleneck

A production joint is more than a catalog motor + gearbox + encoder.

At volume it requires:
- matched tolerance stacks;
- bearing/reducer preload;
- motor concentricity and rotor/stator air gap;
- encoder alignment / zeroing;
- torque/force sensor calibration;
- lubrication quantity and sealing;
- thermal characterization;
- backlash, noise and vibration screening;
- software/firmware parameterization;
- traceability and field-failure feedback.

**FACT:** Schaeffler's Humanoid agreement is expected to cover a seven-digit number of joint actuators through 2031, while Harmonic Drive Systems explicitly emphasizes endurance testing and mechatronic integration of reducers, motors, sensors, drivers and controllers.

**HYPOTHESIS:** If humanoids scale from prototypes to tens/hundreds of thousands of robots, **repeatable actuator yield and qualification** may become a stronger moat than the BOM components individually.

**FALSIFICATION:** Large robot OEMs may vertically integrate joint modules, source components from multiple vendors, and internalize calibration/test. The function can be scarce without creating an independent merchant profit pool.

---

## 9. Supplier landscape — evidence level, not investment ranking

| Supplier | Evidence-backed role | Current evidence | Research treatment |
|---|---|---|---|
| Harmonic Drive Systems | strain-wave reducers + mechatronic actuators | industrial-robot installed base; humanoid prototypes; disclosed mass production for some humanoid customers; AI robots a 2026 focus | #78 benchmark/candidate |
| Nabtesco | RV/cycloidal + compact Monocrank + strain-wave via Ovalo | Monocrank explicitly targeted at humanoid shoulders/hips; mature industrial robot reducer base | #78 benchmark/candidate |
| Schaeffler / Ewellix | planetary/strain-wave rotary, linear screws, bearings, motors, sensors, controllers | Humanoid + Hexagon actuator supply agreements; seven-digit actuator expectation from Humanoid deal | #78/#79/#82 benchmark/candidate |
| Laifual | strain-wave reducers | HK listing document says humanoid deliveries/mass production achieved; #2 China shipment provider in 2025 per CIC | #78 competition/falsification |
| Leaderdrive | strain-wave reducers / modules | direct humanoid product positioning; strong China reducer position; named high-quality humanoid customer evidence needs primary verification | #78 investigation |
| MinebeaMitsumi | bearings, motors, force sensors, screws, electronics | CES/WRC humanoid components; HDS hand collaboration; customer inquiries accelerating | #80/#81 benchmark/candidate |
| THK | cross-roller bearings / linear motion | direct robot-joint bearing applications; humanoid-specific economic exposure not yet proven | #81 benchmark |
| IKO / Nippon Thompson | cross-roller bearings | direct industrial robot joint applications | #81 benchmark |
| Renishaw and other encoder specialists | precision position feedback | technically relevant; direct humanoid production evidence to be verified | #81 research queue |

No company is promoted on this map alone.

---

## 10. Demand evidence and demand risk

**FACT:** Humanoid's May 2026 supply agreement with Schaeffler is expected by Humanoid to cover a seven-digit number of joint actuators through 2031 and more than half of its wheeled-platform joint demand. Reuters separately reported the agreement alongside Humanoid's planned 1,000–2,000-robot deployment at Schaeffler facilities by 2032.

**FACT:** MinebeaMitsumi says worldwide customer orders/inquiries for humanoid components accelerated after CES 2026, while also explicitly cautioning against more aggressive industry unit forecasts and using about **1.4 million humanoids in 2030** internally.

**INTERPRETATION:** There is now credible component-demand evidence beyond prototypes, but forecast dispersion remains enormous. The research should underwrite **supplier qualification and per-robot content** before using top-down humanoid unit forecasts.

**THESIS BREAKER:** If deployed robots remain specialized, wheeled, low-DOF or use simpler grippers, actuator content per robot can be much lower than headline humanoid BOM assumptions.

---

## 11. What is most likely to surprise us

1. **Roller screws may outrank harmonic reducers** if lower-limb linear architectures scale and precision manufacturing remains narrow.
2. **The bottleneck may be actuator industrialization rather than the reducer itself** if more gearbox suppliers become good enough but joint calibration/yield remains difficult.
3. **Hands may create the greatest component count but not the best profit pool** if underactuation and simpler end-effectors win on cost/reliability.
4. **Motors and bearings may be excellent volume beneficiaries without being bottlenecks.**
5. **Automotive motion suppliers can enter quickly.** Schaeffler's agreements are direct evidence that incumbent industrial/auto manufacturing expertise can challenge traditional robot-component specialists.

---

## 12. Active backlog

- **#78 P1 — rotary reducer architectures and supplier bottlenecks**
- **#79 P2 — linear actuators / planetary roller screws / ball screws**
- **#80 P3 — dexterous-hand microactuation + tactile/force sensing**
- **#81 P4 — motors / encoders / force sensing / bearings**
- **#82 P5 — servo drives / brakes / thermal / industrialization**
- **#83 P6 — common-basis synthesis and Investment Capture shortlist**

Parent **#3** remains open until the Gate-A/synthesis programme has converted this preliminary map into evidence-backed bottleneck conclusions.

---

## Sources

Primary / company:
- Schaeffler — Humanoids at Schaeffler, Dec 2025: https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20251202_humanoids_at_schaeffler.pdf
- Schaeffler — planetary gear actuator for humanoids, CES 2026: https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88156672
- Schaeffler — partnership with Humanoid, Jan 2026: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88159810
- Schaeffler — partnership with Hexagon Robotics, Apr 2026: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88184988
- Humanoid — May 2026 Schaeffler deployment/supply agreement: https://thehumanoid.ai/humanoid-secures-landmark-deal-with-schaeffler-to-deploy-thousands-of-humanoid-robots/
- Harmonic Drive Systems — R&D / reducer endurance + mechatronics: https://www.hds.co.jp/english/development/structure/diagram/
- Harmonic Drive Systems — 2026 management message / AI robots focus: https://www.hds.co.jp/english/ir/management_policy/top_message/
- Harmonic Drive Systems — humanoid prototype/mass-production disclosure (2024 briefing): https://www.hds.co.jp/Portals/0/files/english/ir/data/investor_event/pdf/E-setsumeikai_20241119%20V2.pdf
- Nabtesco — FY2025 results / Monocrank humanoid reducer: https://www.nabtesco.com/cms/wp-content/uploads/Results_Briefing_Material_for_FY2025_e.pdf
- Nabtesco — 2026 product direction / humanoids: https://www.nabtesco.de/en/the-company/presse-detail/nabtesco-2026-technology-and-service-expertise-from-a-single-source
- MinebeaMitsumi — humanoid component platform / CES 2026: https://www.minebeamitsumi.com/english/news/press/2025/1210639_20344.html
- MinebeaMitsumi — World Robot Conference 2026 humanoid products: https://www.minebeamitsumi.com/english/news/press/2026/1210917_20482.html
- MinebeaMitsumi — humanoid component technical overview: https://tech.minebeamitsumi.com/en/pickup/humanoidrobot/index.html
- Ewellix — planetary roller screws: https://www.ewellix.com/en/products/ball-and-roller-screws/roller-screws/planetary-roller-screws
- THK — cross-roller rings: https://www.thk.com/jp/en/products/cross_roller_ring/cross_roller_ring/
- IKO — crossed roller bearings: https://www.ikont.co.jp/eg/product/needle/ndl0803.html
- Laifual Hong Kong listing document, Jun 2026: https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0622/2026062200047.pdf

Technical / independent:
- Mechatronics 2026 — harmonic vs planetary actuator comparison: https://www.sciencedirect.com/science/article/pii/S095741582600019X
- Intelligent and Sustainable Manufacturing 2026 — humanoid joint-module review / QDD: https://doi.org/10.70322/ism.2026.10019
- Reuters, May 13 2026 — Humanoid/Schaeffler deployment and actuator agreement: https://www.reuters.com/business/humanoid-deploy-up-2000-robots-schaeffler-plants-2026-05-13/
