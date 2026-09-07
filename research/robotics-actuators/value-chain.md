# Robotics Actuators — Value Chain and Bottleneck Map

**Research stream:** Robotics actuators  
**Status:** First evidence-backed value-chain map  
**Confidence:** Medium on architecture / bottleneck topology; Low-to-Medium on company economic capture  
**Last substantive update:** 2026-09-07

## Purpose

Identify where value can become structurally difficult to substitute as advanced robotics scales. The target is not simply “companies that sell robot parts.” The target is a dependency that combines:

- high physical / manufacturing difficulty;
- slow or capital-intensive supply expansion;
- supplier concentration or qualification lock-in;
- high system criticality;
- limited ability for robot OEMs to redesign around it quickly;
- enough supplier revenue sensitivity for robotics growth to matter financially.

The same five-factor Bottleneck Strength framework used in the AI-memory research is applied here on a 1–5 scale:

1. physical / technical difficulty;
2. supply elasticity;
3. supplier concentration;
4. qualification / switching cost;
5. system criticality.

A score around **4/5 or higher** is a candidate structural bottleneck. Company-level Investment Capture still requires separate underwriting.

---

## 1. Actuator system architecture

A high-performance joint is a system, not a gearbox alone. A typical rotary joint can contain:

**motor → drive / power electronics → encoder → transmission / reducer → output bearing → torque / force sensing → brake / lock → thermal path → housing / wiring → calibration and controls.**

Linear joints replace the rotary reducer with a screw / roller-screw / linear transmission and associated bearings.

**FACT:** Schaeffler's 2026 humanoid actuator platform integrates the electric motor, power electronics, high-precision encoder and a configurable transmission; the company explicitly supports **strain-wave, planetary and cycloidal** gearbox architectures. Its CES planetary actuator combines a two-stage planetary gearbox, motor, encoder and controller in a compact unit.

**FACT:** MinebeaMitsumi's humanoid portfolio similarly spans bearings, ball screws, frameless motors, force/torque sensors, motor-driver ICs and cooling. Its FY2026 presentation estimates roughly **120–200 bearings per humanoid body excluding the hands, plus 30–100 per hand**, illustrating how component count can compound even when no single bearing is exotic.

**INTERPRETATION:** The investable opportunity may sit in either a narrow hard-to-make component such as a precision reducer, or in a supplier able to integrate multiple qualified components into an actuator architecture while manufacturing them at automotive-like scale.

---

## 2. Architecture by robot type

### Large industrial robots

Typical load-bearing axes use **high-ratio cycloidal / RV reducers** because stiffness, shock resistance and torque capacity dominate. Smaller wrist axes can use strain-wave gearing. Conventional high-performance servo motors and absolute encoders are well established.

**FACT:** Nabtesco estimates approximately **60% global share** in precision reduction gears for joints of medium-to-large industrial robots. Its RV family emphasizes rigidity, overload resistance, low backlash and positioning accuracy.

### Cobots / lightweight manipulators

Weight, compactness, low backlash and human interaction become more important. **Strain-wave reducers + frameless motors + torque sensing** are common, while low-ratio / quasi-direct-drive designs can be attractive where backdrivability matters.

### Humanoids

There is **no single winning joint architecture yet**.

Current credible designs and supplier roadmaps span:

- strain-wave actuators for compact, high-reduction, low-backlash joints;
- low-ratio planetary / quasi-direct-drive actuators for efficiency and backdrivability;
- cycloidal actuators where impact resistance / torque transparency matter;
- ball-screw / linear actuators where compact linear force transmission is preferred;
- miniature geared / tendon / wire-driven actuators in hands and fingers.

**FACT:** Schaeffler explicitly argues that all three main rotary gearbox types have roles in humanoids: strain-wave for power density / low backlash, planetary for efficiency / backdrivability, and cycloidal for robustness / torque transparency.

**FACT:** Academic QDD work shows the architecture trade-off directly: a high-torque-density motor plus low-ratio gearbox can improve backdrivability and control bandwidth relative to conventional high-ratio actuation, but the lower gear ratio makes motor torque density more demanding.

### Quadrupeds / dynamic legged robots / exoskeletons

Dynamic motion, impact tolerance and backdrivability make **quasi-direct-drive / low-ratio planetary or cycloidal** architectures especially relevant. Here, motor torque density and thermal performance can matter more than extreme reduction ratio.

### Hands

Hands fragment into many small actuators and sensors. Compact motors, miniature bearings, small reducers, tendon/wire transmissions, force/tactile sensing and mechanical locks can dominate. The challenge is integration and manufacturability rather than one universal transmission architecture.

**FACT:** MinebeaMitsumi's CES robot hand used **11 actuators and 85 miniature/small bearings** per hand and combined motors, bearings, force sensing and mechanical locking; the drive unit was jointly developed with Harmonic Drive Systems.

---

## 3. Precision reducers / gearboxes — strongest current bottleneck

### Why they matter

Reducers convert compact high-speed motor output into useful joint torque while controlling backlash, stiffness, inertia, friction, efficiency, shock load and acoustic performance.

A small manufacturing error can appear as joint-position error, vibration, wear or poor force control. This makes precision tooth geometry, thin-wall components, heat treatment, bearings, lubrication and assembly repeatability important.

### Sub-architectures

#### Strain-wave gearing

Strengths:

- high reduction in compact volume;
- near-zero backlash;
- high torque-to-weight / package efficiency;
- large hollow-bore possibilities.

Weaknesses:

- flexspline fatigue / life;
- torsional compliance;
- efficiency and thermal losses at some duty points;
- shock / impact sensitivity versus robust low-ratio alternatives;
- cost and precision manufacturing.

Key suppliers / evidence:

- **Harmonic Drive Systems** — category-defining incumbent; FY2026 speed-reducer sales ¥46.3bn, and Q1 FY2027 consolidated orders rose 55.7% y/y. HDS also supplies robot-actuation technology jointly with MinebeaMitsumi and has longstanding robot-OEM relationships.
- **Leader Harmonious Drive (Leaderdrive)** — official site claims **60%+ domestic Chinese share**, >300,000 strain-wave reducers sold in 2025 and a broader portfolio of reducers, rotary actuators and frameless motors.
- **Schaeffler** — entering with formed strain-wave gearboxes; August 2026 launch says its forming process lowers manufacturing cost by **>25%** and material use by **>75%**, with rollout of mass manufacturing for multiple humanoid manufacturers planned for 2027.
- **Nabtesco** — historically strongest in RV/cycloidal, but launched compact RVmini / Monocrank products to address cobots and humanoids, including low-torque applications.

**Evidence against a permanent monopoly thesis:** Schaeffler's cost-focused entry, Leaderdrive's scale, Chinese supplier growth and Nabtesco's expansion into compact reducers show that the supply base is broadening. Precision reducers can remain difficult without remaining scarce forever.

#### Cycloidal / RV gearing

Strengths:

- high rigidity and shock tolerance;
- high torque capacity;
- low backlash;
- proven reliability in industrial robot load-bearing axes.

**FACT:** Nabtesco estimates ~60% global share in medium/large industrial-robot joint precision reducers and reports more than **14 million** cumulative RV-series units. Its 2025 compact product launch explicitly targets cobots and humanoids.

Humanoid uncertainty: the traditional RV architecture can be heavier than strain-wave or low-ratio planetary options, so penetration into small humanoid joints is not guaranteed.

#### Planetary / QDD

Strengths:

- high efficiency;
- low-ratio versions improve backdrivability and torque transparency;
- mature manufacturing base.

Weakness: delivering humanoid-level precision, low backlash and torque density at low cost can require custom integrated design rather than a commodity planetary gearbox.

### Bottleneck score — precision reducers

| Factor | Score | Rationale |
|---|---:|---|
| Physical difficulty | **4.7** | sub-arc-minute accuracy, stiffness, fatigue/life and compactness are hard simultaneously |
| Supply elasticity | **4.0** | precision machining and qualification take time, but new entrants can scale |
| Supplier concentration | **4.2** | strong incumbents in strain-wave and RV; Chinese / automotive suppliers expanding |
| Qualification / switching | **4.5** | reducer choice affects housing, controls, life, calibration and full joint design |
| System criticality | **5.0** | failure or backlash directly compromises joint safety / precision |
| **Bottleneck Strength** | **4.5/5** | **Gate-A candidate — strongest current layer** |

**CONCLUSION:** Precision reducers are the first layer to underwrite at company level, but the thesis should be **architecture-aware** rather than “harmonic gears win every humanoid joint.”

---

## 4. Integrated actuator module / thermal / calibration — structural but capture is uncertain

As robots scale from prototypes into products, actuator value moves from individual component specifications toward the **integrated joint**:

- motor electromagnetic design;
- gearbox and bearing preload;
- encoder alignment;
- torque sensing;
- power-electronics placement;
- thermal path;
- cable routing / connectors;
- sealing and lubrication;
- firmware and current / torque control;
- end-of-line calibration and life testing.

**FACT:** Schaeffler says a humanoid uses roughly **25–30 actuators** and has developed highly integrated rotary actuator platforms with in-house motor, encoder/controller, bearings and multiple gearbox architectures. It has supply/development partnerships with Humanoid, Hexagon Robotics and VinDynamics.

**FACT:** Reuters reported in May 2026 that Humanoid agreed a five-year supply arrangement under which Schaeffler would be preferred supplier for more than half of its joint actuator demand, totaling at least **one million actuator units through 2031**.

**INTERPRETATION:** The scarce capability could become **industrialization of the complete actuator**, not one subcomponent. Automotive-scale winding, forming, bearing production, electronics assembly and calibration are potential advantages.

**Evidence against:** humanoid OEMs can vertically integrate actuators to optimize mass, cost and controls; architecture churn can make a standardized module obsolete; supplier capture is currently less proven than technical criticality.

### Bottleneck score — integrated joint industrialization

| Factor | Score |
|---|---:|
| Physical difficulty | 4.5 |
| Supply elasticity | 4.0 |
| Supplier concentration | 3.3 |
| Qualification / switching | 4.5 |
| System criticality | 5.0 |
| **Bottleneck Strength** | **4.3/5** |

**CONCLUSION:** This passes the structural screen, but **economic capture is the key uncertainty**. Schaeffler is the clearest public company to test this thesis because it spans all three gearbox architectures and has direct humanoid supply agreements.

---

## 5. High-torque-density frameless motors

Humanoid and cobot joints increasingly embed frameless BLDC / torque motors directly into the joint housing. The design problem is not simply motor availability; it is continuous torque density under a tight thermal envelope.

Important variables:

- copper fill / winding quality;
- magnetic material / rotor topology;
- cogging torque;
- continuous versus peak torque;
- rotor inertia;
- cooling / winding temperature;
- manufacturability at high volume.

**FACT:** Kollmorgen markets TBM/TBM2G frameless motors specifically for compact robot/humanoid joints and says its robotics experience covers hundreds of thousands of robot joints/arms. MinebeaMitsumi is also developing / selling frameless motors into the humanoid ecosystem and says North American order wins are progressing.

**Evidence against bottleneck:** motors have many capable global suppliers, and robot OEMs can custom-design motors. Low-ratio QDD raises the importance of torque density, but it can also encourage vertical integration.

### Bottleneck Strength: **3.8/5 — important enabling layer, not yet a concentrated structural bottleneck.**

Best follow-up: test whether any supplier owns a manufacturing/process advantage in high-volume frameless torque motors rather than treating the whole motor category as scarce.

---

## 6. Ball screws / linear actuators

Linear actuation converts motor rotation into high axial force using ball screws / roller screws / other screw transmissions. Requirements include:

- screw accuracy and surface quality;
- efficiency / friction;
- compact nut design;
- axial load / life;
- thermal stability;
- backlash / preload;
- contamination / lubrication.

**FACT:** MinebeaMitsumi explicitly maps ball screws and frameless motors into humanoid linear actuators and created Minebea Linear Motion after acquiring ball-screw / ball-way capability. NSK identifies ball screws as high-efficiency, high-rigidity precision motion components and has historically targeted robot actuators in its industrial machinery strategy.

**Architecture risk:** linear actuation is not universal. A robot designed around rotary joints can reduce or eliminate this exposure.

### Bottleneck Strength: **3.8/5 today; 4.2/5 optionality if ball-screw linear architectures become common in high-load humanoid joints.**

Candidate suppliers: MinebeaMitsumi, THK, NSK and specialized screw manufacturers. Do not promote until humanoid production sockets are verified.

---

## 7. Precision bearings

Relevant types include:

- thin-section bearings;
- cross-roller bearings;
- miniature ball bearings;
- reducer / wave-generator bearings;
- support bearings for ball screws.

They determine stiffness, friction, runout, life and joint package size.

**FACT:** MinebeaMitsumi estimates 120–200 bearings per humanoid body excluding the hands and 30–100 per hand. Nabtesco integrates main bearings into RV products; cross-roller bearings are commonly used where a compact joint must carry radial, axial and moment loads.

**Evidence against bottleneck:** the total bearing count is large but the qualified supplier base is also broad. Many bearings are likely to become standardized components rather than monopoly-like profit pools.

### Bottleneck Strength: **3.4/5.**

**INTERPRETATION:** Bearings can generate strong **content-per-robot** for a diversified supplier such as MinebeaMitsumi, but high content is not the same as structural scarcity.

---

## 8. Encoders, torque / force sensing and tactile feedback

Closed-loop robot motion depends on accurate position and torque/force feedback.

Layers include:

- motor-side magnetic/optical encoders;
- output-side absolute encoders;
- joint torque sensors / strain gauges;
- six-axis force/torque sensors;
- fingertip/tactile sensors.

**FACT:** MinebeaMitsumi is developing force/torque sensors, including miniature multi-axis sensors, as part of its humanoid platform. Schaeffler integrates high-precision encoders into its actuator architecture.

**Trade-off:** low-backlash / QDD / torque-transparent mechanical architectures can reduce reliance on dedicated output torque sensors or enable sensorless estimation. This is evidence against assuming every sensor becomes mandatory.

### Bottleneck Strength: **3.7/5.**

Potential value can still accrue in tiny high-reliability sensors for hands and compact joints, but supplier concentration / customer lock-in need evidence.

---

## 9. Drives / power electronics / brakes

### Motor drives and power electronics

Requirements include high current density, fast field-oriented control, low switching loss, regenerative energy handling, safety and compact thermal packaging.

Many semiconductor, servo-drive and robot OEMs can supply or vertically integrate this layer.

### Bottleneck Strength: **3.1/5.**

### Brakes / mechanical locks

Useful for static load holding, emergency stops and power saving, especially in vertical joints and hands. Minebea's hand demonstrates a mechanical lock to lower energy consumption.

Supplier base is broad and designs can be architecture-specific.

### Bottleneck Strength: **2.8/5.**

---

## 10. Thermal management — a system constraint, not yet a clean supplier bottleneck

Every kilogram carried by a mobile robot increases the load and energy demand on other joints. Continuous motor torque, gearbox friction and power electronics all create heat inside compact enclosures.

Thermal limitations therefore constrain:

- continuous torque versus peak torque;
- duty cycle;
- motor winding / magnet life;
- lubricant life;
- electronics reliability;
- battery endurance.

**INTERPRETATION:** thermal performance can decide which actuator architecture wins, but the economic capture is distributed across motor design, housing, bearings, lubricant, power electronics, fans / liquid cooling and control software. Treat thermal management as a **cross-cutting system constraint**, not a standalone company screen yet.

---

## 11. Manufacturing / calibration / test

High-volume humanoid production will require repeatable processes for:

- stator winding and magnet assembly;
- thin-wall flexspline / precision gear manufacturing;
- precision bearings and preload;
- torque / angle calibration;
- grease / sealing;
- electronics calibration;
- noise / vibration screening;
- shock / endurance testing;
- end-of-line joint characterization.

**FACT:** Schaeffler explicitly positions its automotive/industrial manufacturing capabilities — including automated coil winding and chipless forming — as a humanoid advantage. Its new formed strain-wave process is designed to reduce material and cost substantially before 2027 mass production.

### Bottleneck Strength: **4.0/5**, but much of the economic value may remain captive inside component / actuator suppliers rather than create a separate equipment-company opportunity.

---

## 12. Cross-layer bottleneck ranking

| Rank | Layer | Bottleneck Strength | Current conclusion |
|---:|---|---:|---|
| **1** | **Precision reducers / gearboxes** | **4.5/5** | Strongest current component bottleneck; architecture-specific and competition rising |
| **2** | **Integrated actuator industrialization / calibration / thermal integration** | **4.3/5** | Structural system capability; supplier capture vs OEM vertical integration unresolved |
| **3** | **Actuator manufacturing / end-of-line precision** | **4.0/5** | Hard to scale reliably; often captive inside suppliers |
| 4 | Frameless high-torque-density motors | 3.8/5 | critical but broad supplier base / custom OEM design |
| 5 | Ball screws / linear actuation | 3.8/5 today | architecture-dependent; upside if linear joints gain share |
| 6 | Encoders / torque / force sensing | 3.7/5 | important feedback layer; sensorless / alternate architectures reduce universality |
| 7 | Precision bearings | 3.4/5 | high content, but broad qualified supply |
| 8 | Drives / power electronics | 3.1/5 | important but relatively broad supply / vertical integration |
| 9 | Brakes / locks | 2.8/5 | useful but not scarce |

**CONCLUSION:** The first research wave should focus on **precision reducers and integrated actuator industrialization**, not generic motors or bearings.

---

## 13. Company candidate screen

This is **research prioritisation**, not investment recommendation.

| Company | Public line | Why it matters | Main concern | Proposed status |
|---|---|---|---|---|
| **Harmonic Drive Systems** | TSE: 6324 | Direct strain-wave / precision-reducer exposure; robot installed base and category know-how; orders recovering strongly | Sep-2026 valuation already extremely demanding; architecture competition and China localization | **Investigating** |
| **Schaeffler** | ETR: SHA0 | Only large public supplier reviewed with integrated humanoid actuator platform across strain-wave, planetary and cycloidal; direct supply partnerships; manufacturing-scale advantage | Humanoid revenue still tiny vs €23bn Group; execution and automotive dilution | **Investigating** |
| **MinebeaMitsumi** | TSE: 6479 | Architecture-agnostic content: bearings, ball screws, frameless/small motors, force sensors, semiconductors; North-American robot orders progressing | Robotics contribution currently small and highly diluted in Group | **Investigating** |
| **Nabtesco** | TSE: 6268 | ~60% share in medium/large industrial-robot joint reducers; 14m+ cumulative RV units; expanding compact range for humanoids/cobots | Traditional RV strength may not transfer to lightweight humanoids; mature company | **Investigating / benchmark** |
| **Leader Harmonious Drive** | SSE STAR: 688017 | Officially claims 60%+ Chinese domestic share and >300k strain-wave reducers sold in 2025; integrated actuator/motor expansion | Sep-2026 valuation extremely high; company claims require independent verification; China price competition | **Research queue** |
| **Regal Rexnord / Kollmorgen** | NYSE: RRX | Frameless motors, drives, linear motion, brakes/gears across group; substantial robotics installed experience | Humanoid / actuator economics diluted inside much larger parent | **Research queue** |
| **THK / NSK** | TSE: 6481 / 6471 | Ball screws, linear motion, precision bearings; potential beneficiaries of linear-actuator architectures | Humanoid sockets and revenue materiality not yet demonstrated | **Research queue** |

### Point-in-time valuation context — 4 September 2026

- HDS market cap ~**¥565bn**, published forward P/E ~**77x**.
- Nabtesco market cap ~**¥522bn**, trailing P/E ~**28x**.
- MinebeaMitsumi market cap ~**¥1.34tn**, trailing P/E ~**12x**.
- Schaeffler market cap ~**€7.0bn**, published forward P/E around **15x**; 2025 humanoid revenue was still <1% of Group sales.
- Leaderdrive market cap ~**CNY51bn**, trailing P/E >**300x** on the reviewed snapshot.

**INTERPRETATION:** The most obvious pure-play reducer equities are already priced aggressively. Schaeffler and Minebea deserve attention because they combine lower headline valuation with manufacturing / component optionality, but robotics must become large enough to move group earnings.

---

## 14. Evidence against the broad humanoid-component thesis

1. **Architecture is unsettled.** A win for QDD / planetary can reduce strain-wave content; linear actuation can shift value toward screws; OEMs can mix architectures by joint.
2. **Vertical integration is rational.** Actuators strongly affect robot mass, battery life, controls and safety, encouraging OEMs to design in-house.
3. **Chinese localization is accelerating.** Leaderdrive and other Chinese suppliers can compress reducer pricing and weaken incumbent margins.
4. **Automotive-scale entrants can attack cost.** Schaeffler's >25% claimed manufacturing-cost reduction for formed strain-wave gearboxes is direct evidence that incumbent cost structures are contestable.
5. **Component count does not equal pricing power.** Hundreds of bearings per robot can be valuable revenue without being a bottleneck.
6. **Humanoid deployment forecasts remain highly uncertain.** MinebeaMitsumi itself has expressed skepticism about aggressive unit forecasts and has used a lower 2030 assumption than some market studies.
7. **Robot economics can fail before the supply chain does.** If useful-task hours, reliability or battery economics disappoint, component demand can lag technical readiness by years.

---

## 15. Current working conclusion

The original actuator thesis survives, but it becomes more specific:

> **The strongest near-term dependency is not “actuators” generically. It is the ability to manufacture compact, precise, efficient and durable joint transmissions — and increasingly to integrate the complete joint — at repeatable mass-production cost.**

The highest-value company questions are therefore:

1. Can **Harmonic Drive Systems** defend strain-wave economics as Schaeffler / Leaderdrive / others industrialize alternatives?
2. Can **Schaeffler** turn cross-architecture actuator manufacturing and direct humanoid supply agreements into material high-margin revenue?
3. Can **MinebeaMitsumi** convert very high component content per humanoid into enough incremental earnings to matter?
4. Does **Nabtesco** successfully extend its industrial-robot reducer moat into compact humanoid/cobot joints?

No company is promoted to `High-conviction research candidate` from value-chain evidence alone.

## Sources

Primary / company:

- Schaeffler humanoid actuator platform / gearbox architecture: https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20260205_humanoids_at_schaeffler.pdf
- Schaeffler planetary actuator: https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88156672
- Schaeffler formed strain-wave gearbox: https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88210241
- Schaeffler / Hexagon partnership: https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88184987
- Schaeffler / Humanoid partnership: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88159810
- Schaeffler FY2025 results / growth areas: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88175106
- Nabtesco precision reducers / market share: https://www.nabtesco.com/en/products/robot/
- Nabtesco RVmini / Monocrank humanoid expansion: https://www.nabtesco.com/en/news/20251202-17329/
- Harmonic Drive Systems Q1 FY2027 filing: https://financialfilings.com/filings/harmonic-drive-systems-inc/interim-quarterly-report/2026/57070153/
- HDS FY2026–2030 strategy: https://www.hds.co.jp/english/ir/management_policy/strategy/
- HDS 2025 integrated report / China robot strategy: https://www.hds.co.jp/Portals/0/files/csr/HDSreport/2025/HDSREPORT2025_EN_s.pdf
- Leaderdrive company / production / share claims: https://www.leaderdrive.com/
- Leaderdrive product / actuator range: https://www.leaderdrive.com/product/
- MinebeaMitsumi FY2026 humanoid strategy / component counts: https://www.minebeamitsumi.com/english/corp/investors/disclosure/financial/p2026/__icsFiles/afieldfile/2026/05/21/e2026_slide_en.pdf
- MinebeaMitsumi humanoid product map: https://product.minebeamitsumi.com/en/pickup/humanoidrobot/index.html
- MinebeaMitsumi World Robot Conference 2026: https://www.minebeamitsumi.com/english/news/press/2026/1210917_20482.html
- Kollmorgen humanoid motion stack: https://www.kollmorgen.com/en-us/company/events/join-regal-rexnord-motion-brands-humanoid-robot-forum-automate-2026
- Kollmorgen frameless motors: https://www.kollmorgen.com/en-us/solutions/robotics/humanoid-robots
- NSK ball-screw technical review: https://www.nsk.com/tools-resources/research-and-development/technical-review/2026/mt-frix/

Technical / academic:

- Yu et al., IEEE/ASME, quasi-direct-drive actuation and backdrivability: https://pmc.ncbi.nlm.nih.gov/articles/PMC7971415/

High-quality current reporting:

- Reuters on Schaeffler humanoid orders / developer relationships: https://www.reuters.com/business/schaeffler-sees-humanoid-robotics-orders-three-digit-million-euros-by-2030-2026-05-05/
- Reuters on Humanoid / Schaeffler actuator supply agreement: https://www.reuters.com/business/humanoid-deploy-up-2000-robots-schaeffler-plants-2026-05-13/

Point-in-time market data:

- HDS: https://stockanalysis.com/quote/tyo/6324/market-cap/ and https://stockanalysis.com/quote/tyo/6324/financials/ratios/
- Nabtesco: https://stockanalysis.com/quote/tyo/6268/market-cap/
- MinebeaMitsumi: https://stockanalysis.com/quote/tyo/6479/market-cap/
- Schaeffler: https://stockanalysis.com/quote/etr/SHA0/market-cap/
- Leaderdrive: https://stockanalysis.com/quote/sha/688017/market-cap/

## Change history

2026-09-07 — First value-chain map. Precision reducers score 4.5/5 and integrated actuator industrialization 4.3/5 as the highest-priority bottleneck candidates. HDS, Schaeffler, MinebeaMitsumi and Nabtesco enter active company investigation; no company is promoted beyond `Investigating`.