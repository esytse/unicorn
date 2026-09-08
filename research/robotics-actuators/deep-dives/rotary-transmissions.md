# Rotary Actuator Transmissions — Gate A Deep Dive

**Status:** Initial Gate-A comparison complete  
**Backlog:** #78  
**Confidence:** **Medium**  
**Last substantive update:** 2026-09-08

## Executive conclusion

The original question — "are harmonic reducers the humanoid bottleneck?" — is too narrow.

**CONCLUSION:** **Qualified precision rotary transmission** is a strong actuator bottleneck, but **no single reducer architecture currently owns the whole humanoid body**.

Current preliminary Gate-A scores:

| Architecture / function | Bottleneck Strength | Conclusion |
|---|---:|---|
| Qualified precision rotary-reducer manufacture across architectures | **4.4 / 5** | **Gate A passed as a function** |
| Strain-wave reducer manufacture | **4.3 / 5** | Gate A passed, but supplier scarcity is weakening |
| Compact cycloidal / RV / Monocrank | **4.1 / 5** | Gate A passed narrowly; humanoid body-zone share still uncertain |
| Precision planetary / QDD transmission | **4.0 / 5** | Gate A passed narrowly at integrated-actuator level; standalone gearbox scarcity weaker |

The key investment implication is:

> **The durable moat appears to be process capability, lifetime consistency, qualification and actuator integration — not a patent-protected gear concept.**

Strain-wave reducers remain highly attractive because of compact high-ratio/low-backlash performance, but Chinese production evidence and Schaeffler's rapid entry with planetary and strain-wave actuator platforms are direct falsification against treating Harmonic Drive Systems as the only scalable path.

---

## 1. What a rotary joint must optimize

A humanoid/cobot rotary joint simultaneously trades:

- peak and continuous torque density;
- ratio and motor size;
- backlash / lost motion;
- torsional stiffness;
- reflected inertia;
- efficiency;
- backdrivability / force transparency;
- shock / fall load survival;
- bearing moment capacity;
- acoustic noise / vibration;
- thermal rise;
- lifetime and backlash growth;
- outer diameter / axial length / hollow shaft;
- mass-production yield and calibration.

No architecture dominates all dimensions.

---

## 2. Strain-wave gearing

### Why it wins

A strain-wave reducer uses a compliant flexspline, rigid circular spline and wave generator to create a large ratio from only a small tooth-count difference.

**FACT:** Harmonic Drive Systems describes HarmonicDrive®/strain-wave units as compact, lightweight, high-torque and high-accuracy. Lightweight robot products reduce mass by around 30% versus prior series and higher-torque families extend rated life versus standard models.

Key advantages:
- very high single-stage reduction;
- compact/light package;
- very low backlash / high positioning precision;
- hollow/flat geometries for robotic joints;
- mature use in industrial/collaborative robots.

### Manufacturing moat

**FACT:** Harmonic Drive Systems says its reducer R&D includes materials development, structural analysis and repeated endurance testing.

**INTERPRETATION:** The difficult part is not understanding the mechanism. It is repeatedly manufacturing a thin flexing spline, tooth geometry, wave generator, bearings and heat-treated materials that retain backlash, stiffness and fatigue life across production lots.

Likely process barriers:
- flexspline material / forming / heat treatment;
- tooth-profile generation and surface finish;
- circular-spline concentricity;
- wave-generator/bearing precision;
- assembly preload / lubrication;
- endurance validation and lot consistency.

### Direct humanoid evidence

**FACT:** Harmonic Drive Systems disclosed in a 2024 results presentation that it was providing prototype products to multiple humanoid startups and had **begun mass production for some customers**.

**FACT:** In June 2026 HDS identified **AI robots** as a focus development area in its new medium-term plan.

**FACT:** HDS and MinebeaMitsumi co-developed an ultra-compact high-torque micro actuator using a strain-wave reducer for a humanoid robot hand.

### Strongest falsification — Chinese production is real

**FACT:** Laifual's June 2026 Hong Kong listing document states that, as of end-2025, it was **one of two domestic Chinese manufacturers that had achieved deliveries and mass production of harmonic reducers used in humanoid robots**. According to the CIC report cited in its prospectus, Laifual ranked #2 by Chinese robotic harmonic-reducer shipment volume in 2025 at **21.4%**.

The same prospectus states that its 2025 products achieved ±15 arcsecond positioning precision and >10,000-hour service life; these are company/prospectus claims rather than independent comparative lifetime tests.

**INTERPRETATION:** This is strong evidence against a permanent Japan-only supply bottleneck. Strain-wave Gate A survives because qualification/lifetime/process control remain difficult, but **supplier concentration should be expected to decline**.

### Score

| Dimension | Score | Rationale |
|---|---:|---|
| precision / manufacturing difficulty | 4.7 | flexspline fatigue, profile, heat treatment, bearings, assembly |
| supply elasticity | 4.0 | more Chinese production/capacity is coming online |
| supplier concentration | 4.1 | HDS remains major benchmark but credible challengers now mass-produce |
| qualification / switching cost | 4.5 | reducer changes alter stiffness, control, mounting and life validation |
| system criticality | 4.7 | direct joint torque/position/reliability function |
| architecture durability | 3.8 | planetary/QDD/cycloidal/linear substitutes exist by body zone |
| production evidence | 4.5 | mature industrial use + humanoid mass-production disclosures |

**Bottleneck Strength: 4.3 / 5.**

---

## 3. Cycloidal / RV / Monocrank

Cycloidal/RV architectures use eccentric motion and multiple engaged lobes/pins or gears to achieve high reduction with high stiffness and shock tolerance.

### Strengths

- high rigidity;
- strong moment/load capacity;
- many simultaneous load-bearing contacts;
- high shock/fall tolerance;
- extensive heavy industrial-robot history.

### Weaknesses

- more mass/diameter/inertia than a comparable distal strain-wave joint in many designs;
- more complex multi-part mechanics;
- less proven current humanoid share.

### Direct evidence

**FACT:** Nabtesco's 2026 FY2025 results materials introduced **Monocrank®** specifically for humanoid robots. The product targets high rigidity + high torque density, compact/light construction and a multi-engagement structure designed to avoid skipped/ratcheted motion under high torque.

**FACT:** Nabtesco's 2026 corporate material specifically describes Monocrank as suitable for **shoulder and hip joints** of humanoid robots.

**FACT:** Nabtesco is not betting on cycloidal alone; it also owns/markets strain-wave products through Ovalo, whose 2026 short-gear technology claims substantially improved power density and service life.

**INTERPRETATION:** Nabtesco's multi-architecture portfolio itself is evidence that humanoids may use different transmissions by joint rather than converge on one reducer.

### Gate-A tension

The function is technically difficult and qualified, but we do not yet have enough named humanoid production programmes to prove Monocrank/RV becomes a high-volume humanoid chokepoint.

**Bottleneck Strength: 4.1 / 5 — passed narrowly, Medium-Low confidence on humanoid-specific share.**

---

## 4. Precision planetary and QDD

Planetary gearing distributes torque through multiple planet gears around a sun/ring arrangement. QDD generally pairs a high-torque motor with relatively low reduction to reduce reflected inertia/friction and improve backdrivability.

### Strengths

- high mechanical efficiency;
- conventional gear geometry and scalable machining;
- low-ratio versions improve backdrivability / torque transparency;
- robust multi-gear load sharing;
- potentially attractive for dynamic legged motion.

### Weaknesses

- lower ratio means larger / higher-current motor;
- thermal burden shifts into motor/inverter;
- multiple stages can reintroduce backlash, noise and tolerance accumulation;
- conventional gear manufacturing means a broader potential supplier base.

### Direct commercial evidence — Schaeffler

**FACT:** Schaeffler's CES 2026 humanoid actuator integrates a **two-stage planetary gearbox, electric motor, encoder and controller** in one unit, with a 60–250 Nm torque range and thermal design for continuous duty.

**FACT:** In 2026 Schaeffler signed:
- a preferred actuator relationship with Humanoid for wheeled systems;
- a five-year agreement that Humanoid says covers >50% of its wheeled joint-actuator demand through 2031 and is expected to total **seven-digit actuator volume**;
- a separate partnership with Hexagon Robotics covering high-precision strain-wave and planetary actuators.

**INTERPRETATION:** This is unusually strong revealed-preference evidence for an integrated actuator supplier. It also shows that automotive/industrial motion companies can enter humanoid joints using planetary architecture rather than needing decades of harmonic-drive specialization.

### QDD evidence

A 2026 review of humanoid joint modules highlights the high bandwidth/backdrivability potential of QDD for dynamic lower-limb locomotion. This is technical evidence, not proof that QDD will dominate production humanoids.

### Score

Standalone precision planetary gearing is **not** as concentrated as strain-wave manufacture. The stronger bottleneck is the **integrated planetary/QDD actuator**, where motor, gear, encoder, controller, bearing, thermal and calibration have to work as a unit.

**Precision planetary/QDD transmission: 4.0 / 5 at integrated-actuator level; standalone gearbox scarcity ~3.6–3.8 / 5.**

---

## 5. Body-zone architecture — current working map

| Zone | Strong candidates | Current interpretation |
|---|---|---|
| wrist / distal arm | strain-wave | compactness/low backlash favors high-ratio lightweight gear |
| elbow / shoulder | strain-wave, planetary, compact cycloidal | no convergence; torque/mass/backdrive trade differs by robot |
| torso | strain-wave / planetary / cycloidal | packaging and stiffness dominate |
| hip | planetary/QDD or compact cycloidal; some designs may use linear | shock, torque and backdrive matter more than maximum ratio |
| knee / ankle | QDD/planetary **or linear screw** | architecture contest remains open; #79 critical |
| hand | micro strain-wave/geared/tendon | separate economy; #80 |

This table is a research map, not a statement that every robot uses these architectures.

---

## 6. Supplier concentration versus architecture concentration

A critical distinction:

### Supplier concentration
Historically, precision reducers were highly concentrated in specialists such as HDS (strain-wave) and Nabtesco (RV).

### Architecture concentration
Humanoids are broadening the architecture set:
- Schaeffler: planetary + strain-wave + QDD + linear;
- Nabtesco: RV/Monocrank + strain-wave;
- HDS: strain-wave + planetary product families + mechatronics;
- Chinese suppliers: growing strain-wave and integrated-module capability.

**CONCLUSION:** Supplier competition is rising faster than the underlying precision-manufacturing difficulty is falling.

That creates a nuanced thesis:

> **precision-reducer manufacturing remains scarce relative to generic gearing, but economic capture may migrate from a few historical reducer specialists toward multi-architecture integrated actuator suppliers.**

---

## 7. Dual-source difficulty

Reducer substitution is not equivalent to replacing a catalog bearing.

Changing transmission can alter:
- housing and mounting geometry;
- output bearing/preload;
- motor torque/speed requirement;
- joint inertia/friction model;
- torque-control tuning;
- encoder positioning;
- thermal envelope;
- safety/impact behavior;
- lifetime test qualification.

**INTERPRETATION:** Even if multiple vendors meet a torque/rating sheet, real dual sourcing can require significant mechanical/control revalidation. This supports the 4+ qualification score.

**OPEN QUESTION:** At high robot volumes, will joint interfaces standardize enough to turn reducers/modules into interchangeable second sources?

---

## 8. Thesis breakers

The rotary reducer thesis weakens if:

- Chinese mass producers demonstrate comparable multi-year field life/yield and sharply reduce price;
- robot OEMs standardize mechanical/electrical joint interfaces around multiple interchangeable modules;
- QDD reduces transmission ratio enough that generic planetary gear production becomes sufficient;
- linear actuators take a larger share of the highest-value lower-limb joints;
- robot OEMs vertically integrate reducers/module assembly;
- Schaeffler-like industrial suppliers expand faster than humanoid demand.

The HDS-specific thesis weakens even if strain-wave gearing remains important if its unit share erodes faster than the total market grows.

---

## 9. Gate-A conclusion and next work

**Gate A passes for the function `qualified precision rotary-reducer manufacture` at 4.4/5.**

Within it:
- strain-wave: **4.3**;
- compact cycloidal/RV: **4.1**;
- integrated precision planetary/QDD: **4.0**.

No company moves to `Watch` from this result alone.

### Next

1. **#79 linear / roller screws** now has equal or greater priority because lower-limb architecture could move value away from rotary reducers.
2. #80 hands should test whether micro strain-wave/motor/bearing scale creates a distinct bottleneck.
3. #82 industrialization must compare specialist component moats with Schaeffler-style integrated actuator production.
4. #83 should decide whether Gate-B company work starts with HDS, Nabtesco, Schaeffler, a Chinese strain-wave specialist, or a linear-actuation supplier.

---

## Sources

- Harmonic Drive Systems — collaborative robot products: https://www.hds.co.jp/english/products/applications/robots/
- Harmonic Drive Systems — R&D / endurance / mechatronics: https://www.hds.co.jp/english/development/structure/diagram/
- Harmonic Drive Systems — humanoid prototype/mass-production disclosure: https://www.hds.co.jp/Portals/0/files/english/ir/data/investor_event/pdf/E-setsumeikai_20241119%20V2.pdf
- Harmonic Drive Systems — 2026 AI robot strategy: https://www.hds.co.jp/english/ir/management_policy/top_message/
- MinebeaMitsumi — HDS micro-actuator collaboration: https://www.minebeamitsumi.com/english/news/press/2025/1210639_20344.html
- Nabtesco — FY2025 results / Monocrank humanoid product: https://www.nabtesco.com/cms/wp-content/uploads/Results_Briefing_Material_for_FY2025_e.pdf
- Nabtesco Precision Europe — 2026 multi-architecture portfolio: https://www.nabtesco.de/en/the-company/presse-detail/nabtesco-2026-technology-and-service-expertise-from-a-single-source
- Schaeffler — planetary humanoid actuator: https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88156672
- Schaeffler — Humanoid partnership: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88159810
- Humanoid — May 2026 actuator supply agreement: https://thehumanoid.ai/humanoid-secures-landmark-deal-with-schaeffler-to-deploy-thousands-of-humanoid-robots/
- Schaeffler — Hexagon Robotics partnership: https://www.schaeffler.com/en/investor-relations/events-publications/ir-releases/ir_releases_detail.jsp?id=88184988
- Laifual — HK listing document: https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0622/2026062200047.pdf
- Mechatronics 2026 — harmonic vs planetary actuator comparison: https://www.sciencedirect.com/science/article/pii/S095741582600019X
- Intelligent and Sustainable Manufacturing 2026 — humanoid joint module review/QDD: https://doi.org/10.70322/ism.2026.10019
