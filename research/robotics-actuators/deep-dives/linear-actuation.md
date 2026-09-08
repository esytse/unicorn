# Linear Actuation — Roller Screws, Ball Screws & Integrated Linear Joints

**Status:** Initial Gate-A comparison complete  
**Backlog:** #79  
**Confidence:** **Medium on manufacturing difficulty; Low-Medium on humanoid architecture share**  
**Last substantive update:** 2026-09-08

## Executive conclusion

**CONCLUSION:** **Precision planetary roller-screw manufacture passes Gate A at 4.4/5**, making it one of the strongest current actuator bottleneck candidates. The technical moat is credible: many threaded rollers must share large loads through extremely accurate geometry, controlled preload, heat treatment, surface finish and assembly, while small errors can produce uneven contact stress, accelerated wear and transmission error.

But the investment thesis is more nuanced than the engineering thesis:

- planetary roller screws are **not proven as a universal humanoid-joint architecture**;
- ball screws are credible lower-cost substitutes in some high-load robotic joints;
- lower-ratio rotary/QDD joints can eliminate the screw entirely;
- several established suppliers already possess roller/ball-screw capability;
- the cleanest specialist suppliers are often private or embedded in larger industrial groups.

Current Gate-A scores:

| Function | Bottleneck Strength | Conclusion |
|---|---:|---|
| Planetary roller screw / high-force precision linear conversion | **4.4 / 5** | **Gate A passed** |
| Inverted roller-screw precision thread manufacture | **4.4 / 5** | technically very hard; supplier concentration still to prove |
| Integrated high-force linear actuator | **4.2 / 5** | Gate A passed narrowly; architecture / integration dependent |
| Precision ball screw for robotic joints | **3.8 / 5** | important qualified alternative; broader supply reduces scarcity |

The most important conclusion is:

> **Roller screws may be a stronger manufacturing bottleneck than strain-wave reducers, but architecture uncertainty currently prevents a stronger investment conclusion.**

---

## 1. How linear actuation fits the humanoid

A typical electromechanical linear joint is:

```text
DC bus
→ inverter / servo drive
→ motor
→ roller screw / ball screw
→ nut / rollers / balls
→ thrust + radial support
→ force / position feedback
→ housing / linkage
→ joint motion
```

Instead of producing output torque directly at the joint axis, a screw creates linear force that acts through a linkage or lever arm.

Potential advantages:
- very high axial force in compact diameter;
- high stiffness;
- precise positioning;
- ability to package motor/screw along a limb rather than at the joint axis;
- potentially favorable lower-limb load paths.

Potential disadvantages:
- stroke and packaging constraints;
- side-load sensitivity;
- lubrication / contamination / wear;
- conversion efficiency and heat;
- force-sensor / linkage complexity;
- failure can jam rather than simply freewheel;
- architecture is less naturally backdrivable than some QDD rotary joints.

**FACT:** Schaeffler's humanoid portfolio includes inverted roller screws, planetary roller screws, ball-screw drives and integrated linear actuators. Its illustrative humanoid BOM model assigns roughly **30%** to linear-actuator integration versus roughly 25% to rotary-actuator integration. This is a supplier estimate, not an industry standard.

**INTERPRETATION:** The supplier is explicitly preparing for multiple linear architectures, which is evidence for meaningful demand but also against assuming planetary roller screws win every joint.

---

## 2. Why planetary roller screws are technically difficult

A planetary roller screw uses multiple threaded rollers arranged around a threaded screw, engaging a threaded nut. Compared with a ball screw, many line/contact interfaces share load simultaneously.

### Engineering advantages

- very high static and dynamic load capacity;
- high stiffness;
- high speed / acceleration capability;
- long potential life;
- small lead / high mechanical advantage without recirculating balls;
- ability to withstand repeated high-force duty cycles.

**FACT:** Ewellix describes planetary roller screws as suitable for very high loads, high speeds and high acceleration, with customized/preloaded configurations and diameters from 8 to 240 mm.

### Load sharing is not automatic

**FACT:** A 2026 iScience review states that PRSMs are used in humanoid robots and other high-precision systems, but their geometry creates **uneven load distribution among thread teeth**, stress concentration and accelerated wear. The paper reviews thread-profile modifications that can materially improve load uniformity and reduce contact stress.

**FACT:** A January 2026 Advanced Engineering Informatics paper notes that complex component geometry, actual contact positions and sliding/rolling kinematics create major challenges in achieving transmission accuracy in humanoid/high-precision applications.

**FACT:** A March 2026 Precision Engineering paper shows that multiple geometric machining errors materially affect accumulated PRSM wear.

**INTERPRETATION:** A roller screw is not simply a screw plus many rollers. Production quality is the coupled result of geometry across the screw, nut and every roller.

---

## 3. Manufacturing process is the likely moat

Key process steps include:

- screw/nut/roller thread generation;
- internal-thread machining;
- precision grinding / finishing;
- roller matching and pitch-diameter control;
- heat treatment / hardness / residual-stress control;
- surface finish and tribology;
- preload selection;
- assembly phase / alignment;
- inspection of lead, profile and pitch error;
- load / efficiency / transmission-error testing.

### Inverted roller screws are especially difficult

**FACT:** A 2025 International Journal of Advanced Manufacturing Technology review says humanoid robots are increasing practical requirements for **inverted PRSMs**, whose nuts can have a large length-to-diameter ratio that makes internal-thread machining particularly difficult.

**INTERPRETATION:** This is the strongest manufacturing evidence behind the 4.4 score. The bottleneck is less about raw material and more about generating/measuring very accurate internal and external threads economically at production yield.

### Micron-scale errors matter

The 2026 profile-modification review discusses micro-scale changes to pitch diameter, crest/root and thread geometry that alter stress distribution.

**HYPOTHESIS:** At humanoid scale, the industrial advantage may accrue to suppliers that can **grind, inspect, match and assemble at automotive-like takt/yield**, not merely those that can make a high-spec aerospace roller screw in low volume.

This must be tested later at Gate B.

---

## 4. Architecture durability — biggest uncertainty

The physical bottleneck is stronger than the architecture certainty.

### Why linear could win lower limbs

- high leg loads favor high force density;
- screw actuators can package away from the joint center;
- stiffness can be useful for load-bearing and lifting;
- electromechanical linear actuation removes hydraulic infrastructure.

### Why it may not

- QDD / low-ratio rotary actuators offer better backdrivability and dynamic torque control;
- rotary joints can reduce linkages / side loads;
- high-ratio screw mechanisms can increase reflected inertia/friction;
- falls and impacts may favor robust rotary architectures;
- different robot missions value payload, speed and energy differently.

**OPEN QUESTION:** What percentage of production humanoid hip/knee/ankle joints ultimately use roller-screw linear actuators versus QDD/planetary/cycloidal rotary actuators?

Until this is evidenced with named robot BOMs or supply contracts, architecture durability is capped below the precision-manufacturing score.

---

## 5. Ball screws are real falsification

A simplistic thesis would say roller screws are required whenever humanoid joints need high linear force. Evidence does not support that.

**FACT:** THK's June 2026 BionicM robotic prosthetic-leg case uses a **ball screw + linear guide** to move the knee under full human-body load.

The initial off-the-shelf ball-screw arrangement suffered ball jamming under real-world angled/high loads. THK and BionicM changed ball diameter/count and optimized groove clearance to avoid locking, reduce backlash and meet durability requirements. The resulting system passed BionicM's durability testing representing roughly three million steps per year.

**INTERPRETATION:** This is strong evidence for two things simultaneously:

1. **qualified screw design matters materially** — generic catalog components can fail badly in human-scale dynamic joints;
2. **ball screws can still be good enough** after application-specific engineering, so PRSM is not automatically required.

**FACT:** MinebeaMitsumi's linear-motion strategy explicitly includes ball screws for humanoid applications and says it is developing integrated products by combining precision mechanics with motors, semiconductors and sensors.

**CONCLUSION:** Precision robotic ball screws score **3.8/5**: meaningful engineering/qualification barriers but broader process maturity and supplier availability than roller screws.

---

## 6. Supplier landscape — evidence, not investment ranking

### Schaeffler / Ewellix

**FACT:** Schaeffler's humanoid portfolio spans planetary roller screws, inverted roller screws, ball screws and integrated linear actuators.

**FACT:** Ewellix, part of Schaeffler, has an established planetary-roller-screw portfolio for high-load/high-speed actuation.

**INTERPRETATION:** Schaeffler has perhaps the broadest architecture hedge. It can benefit whether the market chooses planetary screws, ball screws or integrated modules. The drawback for investment purity is its huge diversified group exposure.

### Rollvis

Rollvis is a long-standing specialist producer of satellite/planetary roller screws and inverted variants, including customized designs.

**INTERPRETATION:** Rollvis is a useful technical/scarcity benchmark but private, so it does not provide a direct listed investment vehicle.

### MinebeaMitsumi

**FACT:** MinebeaMitsumi formed Minebea Linear Motion in October 2025 around acquired ball-screw/ball-way capability and explicitly targets humanoid robots, while combining screws with motors, semiconductors, sensors and precision components.

**INTERPRETATION:** Minebea provides important falsification against a narrow roller-screw thesis and may be more interesting later as a high-content integrated-component supplier than as a pure screw supplier.

### THK

**FACT:** THK has deep ball-screw and linear-motion capabilities and direct evidence of application-specific high-load robotic-joint development through BionicM.

**OPEN QUESTION:** How much of THK's future humanoid opportunity is direct production content versus broad linear-motion exposure?

### China / emerging suppliers

A large number of Chinese companies are now marketing or developing roller screws for humanoid robotics. Public market claims are far ahead of named production qualification evidence.

**RESEARCH RULE:** Do not promote any listed Chinese screw/linear-motion supplier until a primary source establishes production volume, customer qualification and financial materiality.

---

## 7. Supply elasticity

PRSM scarcity is likely to be more durable than simple ball-screw scarcity, but capacity can still expand.

Supply elasticity improves through:
- CNC/thread-grinding capacity;
- localized heat treatment;
- automated inspection;
- bearing/precision-machining firms moving into screws;
- automotive suppliers applying high-volume process engineering;
- Chinese localization.

What limits elasticity:
- difficult internal threads for inverted architectures;
- micron-level error interactions;
- multi-component matching;
- wear/lifetime qualification cycles;
- low yield while new suppliers learn the process.

**INTERPRETATION:** This looks like a **learning-curve bottleneck**, not an immutable material bottleneck.

That distinction matters: early qualified suppliers may capture attractive economics, but margins can normalize if manufacturing know-how diffuses faster than humanoid volume scales.

---

## 8. Gate-A score

### Planetary roller screw precision manufacture

| Dimension | Score | Rationale |
|---|---:|---|
| physical / precision difficulty | **4.8** | complex multi-thread contacts, internal threads, matching and preload |
| supply elasticity | **4.2** | capable precision firms can enter, but learning/yield/qualification take time |
| supplier concentration | **4.0** | established specialists exist; many emerging entrants, true production quality uncertain |
| qualification / switching cost | **4.5** | screw affects linkage, force, friction, control, life and safety |
| system criticality | **4.7** | direct force conversion in any linear joint using it |
| architecture durability | **3.8** | rotary QDD/planetary and ball-screw alternatives remain credible |
| production evidence | **4.0** | mature aerospace/industrial technology; humanoid-specific mass-volume evidence still limited |

**Bottleneck Strength: 4.4 / 5 — Gate A passed.**

### Integrated linear actuator

The complete motor+screw+bearing+sensing+housing module has larger switching/recalibration burden, but many robot OEMs may integrate it themselves.

**Bottleneck Strength: 4.2 / 5 — passed narrowly, vertical-integration risk high.**

### Precision ball screw

**Bottleneck Strength: 3.8 / 5 — below primary Gate-A frontier.**

---

## 9. Investment implication

The linear-actuation work changes the cross-actuator ranking:

1. **Planetary roller screw precision manufacture — 4.4**
2. **Qualified precision rotary-reducer manufacture — 4.4**
3. **Actuator industrialization/calibration — 4.3 preliminary**
4. **Integrated linear actuator — 4.2**

This creates a tie at the top rather than a harmonic-drive-led hierarchy.

But there is a major difference in investability:
- rotary reducers have identifiable listed specialists (HDS, Nabtesco, Chinese challengers);
- premium roller-screw specialists are often private or diluted inside Schaeffler;
- public ball-screw suppliers are easier to access but the bottleneck is weaker.

**INTERPRETATION:** PRSM may ultimately be the stronger *engineering* bottleneck while rotary reducers produce the cleaner public-market *Investment Capture* candidates.

That question belongs in #83 after the remaining Gate-A streams.

---

## 10. Thesis breakers / reopen triggers

The PRSM thesis weakens if:
- production humanoids converge on rotary/QDD lower limbs;
- ball screws achieve sufficient life/load at much lower cost;
- Chinese precision suppliers demonstrate comparable lifetime/yield at scale;
- humanoid unit volumes remain too low to make screw exposure financially material;
- robot OEMs vertically integrate screw manufacture or secure multiple interchangeable sources.

The thesis strengthens if:
- named leading robot OEMs disclose roller-screw production BOMs;
- multi-year supply agreements expose unit volumes;
- supplier filings show margin/backlog uplift specifically from humanoid roller screws;
- comparative lifetime/yield data show a persistent gap between established and new suppliers.

---

## 11. Next work

- #80: test whether dexterous-hand microactuation creates a higher-count but lower-margin bottleneck.
- #81: determine whether motors/sensors/bearings are true bottlenecks or mainly content-growth layers.
- #82: test whether integrated actuator production/calibration outranks both roller screws and reducers.
- #83: common-basis synthesis and first Gate-B company shortlist.

No company is promoted from #79 alone.

---

## Sources

Primary / company:
- Schaeffler humanoid portfolio / BOM: https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20251202_humanoids_at_schaeffler.pdf
- Ewellix planetary roller screws: https://www.ewellix.com/en/products/ball-and-roller-screws/roller-screws/planetary-roller-screws
- MinebeaMitsumi Q2 FY3/2026 presentation / Minebea Linear Motion: https://www.minebeamitsumi.com/english/corp/investors/disclosure/financial/p2026/__icsFiles/afieldfile/2025/11/06/e2026_q2_presentation_en.pdf
- MinebeaMitsumi humanoid technology: https://tech.minebeamitsumi.com/en/pickup/humanoidrobot/index.html
- THK BionicM robotic leg ball-screw case, Jun 2026: https://www.thk.com/jp/en/journal/products/article-26062026-1.html
- Rollvis satellite roller screws: https://www.rollvis.com/roller-screws/

Technical / independent:
- iScience 2026 PRSM thread-profile review: https://doi.org/10.1016/j.isci.2026.116249
- Advanced Engineering Informatics 2026 transmission-accuracy study: https://doi.org/10.1016/j.aei.2025.103884
- International Journal of Advanced Manufacturing Technology 2025 thread-machining review: https://doi.org/10.1007/s00170-025-16486-8
- Precision Engineering 2026 accumulated-wear / machining-error study: https://doi.org/10.1016/j.precisioneng.2025.12.014
- Proceedings of the IMechE 2025 PRSM complex-condition review: https://doi.org/10.1177/09544062251318929
