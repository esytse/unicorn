# Common Actuator Components — Motors, Encoders, Force/Torque Sensors & Bearings

**Status:** Gate-A screen complete  
**Backlog:** #81  
**Confidence:** **Medium**  
**Last substantive update:** 2026-09-08

## Executive conclusion

**CONCLUSION:** None of the common component classes tested here independently passes the primary 4.0/5 structural-bottleneck threshold today.

They can still be enormous beneficiaries of humanoid volume. The difference is **supply elasticity**: capable suppliers already exist across motors, bearings and position/force sensing, while robot OEMs and integrated actuator vendors can often redesign or internalize these layers more easily than a reducer or precision screw.

Current scores:

| Layer | Bottleneck Strength | Research conclusion |
|---|---:|---|
| Joint force / torque sensing | **3.9 / 5** | strongest common-component watch; calibration / overload / drift matter, but alternative estimation and sensor architectures exist |
| Cross-roller / thin-section / specialized joint bearings | **3.8 / 5** | precision and content are high; supplier base is broad enough to cap scarcity |
| Frameless torque motors | **3.7 / 5** | torque density / thermal design matter; many qualified motor companies and vertical integration |
| Absolute encoders / resolvers / joint position feedback | **3.7 / 5** | essential feedback, but optical/magnetic/inductive/resolver alternatives reduce concentration |
| Miniature bearings | **3.6 / 5** | extremely high unit content, broad global supply |
| Generic small motors / hand motors | **3.6 / 5** | high content, multiple architectures and suppliers |

The key conclusion is:

> **Humanoid scale may create a component-volume supercycle without creating a component-scarcity moat.**

---

## 1. Frameless torque motors

A rotary actuator often uses a frameless stator/rotor integrated directly into the joint housing.

Performance variables include:
- continuous/peak torque density;
- copper fill and winding quality;
- magnet grade / topology;
- cogging and torque ripple;
- rotor inertia;
- air-gap control;
- thermal path;
- insulation life;
- sensorless / FOC control compatibility.

**FACT:** Schaeffler's humanoid BOM explicitly includes frameless torque motors in both rotary and linear actuator integrations.

**FACT:** MinebeaMitsumi markets frameless motors for humanoid joints and says customization can target output torque, outer diameter and weight.

**INTERPRETATION:** Motors are performance-critical, but the manufacturing technologies — winding, magnets, laminations, rotor/stator assembly — exist across automotive, industrial servo and drone/aerospace supply chains. Integrated packaging can be difficult without the motor itself becoming scarce.

### Falsification

- Schaeffler can build motors inside its integrated platform.
- MinebeaMitsumi can supply/customize them.
- many established servo / BLDC / frameless motor companies have adjacent capability.
- lower-ratio QDD increases motor content but does not necessarily concentrate suppliers.

**Bottleneck Strength: 3.7 / 5.**

Re-open if production robot OEMs repeatedly qualify a very narrow set of high-torque-density motor suppliers or if magnet/winding capacity becomes a demonstrated delivery constraint.

---

## 2. Position feedback — encoders and resolvers

Actuators need rotor and/or output position feedback for commutation and joint control.

Possible technologies:
- optical encoders;
- magnetic Hall/AMR/TMR angle sensing;
- inductive encoders;
- resolvers;
- dual motor/output feedback systems.

Important specifications:
- absolute vs incremental position;
- resolution / repeatability;
- latency / update rate;
- hollow-shaft packaging;
- thermal drift;
- magnetic/electrical interference;
- shock / contamination tolerance.

**FACT:** Schaeffler's planetary humanoid actuator integrates an encoder and controller rather than treating position feedback as a standardized external module.

**FACT:** MinebeaMitsumi already sells magnetic encoder options across motor products and integrates sensor/electronics capabilities across its robotics portfolio.

**INTERPRETATION:** Position feedback is indispensable, but there are multiple viable physical principles and many established industrial suppliers. That lowers supplier concentration and makes joint-level integration more interesting than encoder scarcity.

**Bottleneck Strength: 3.7 / 5.**

---

## 3. Force / torque sensing — strongest common-component watch

Force control is important for:
- collision safety;
- compliant manipulation;
- ground contact;
- load estimation;
- grasp control;
- calibration / diagnostics.

Possible implementations:
- strain-gauge torque sensor in the joint;
- MEMS force sensor;
- multi-axis F/T sensor;
- tendon tension sensor;
- motor-current + transmission-model torque estimation;
- observer / model-based estimates from joint dynamics.

### Why direct sensors are attractive

They can measure output-side load after gearbox friction/backlash and can improve low-force contact control.

**FACT:** Schaeffler includes torque sensors in rotary actuator BOMs and force sensors in linear actuators, and promotes automotive-derived MEMS technology.

**FACT:** MinebeaMitsumi's 2026 humanoid portfolio includes joint torque/force sensors, single-axis force sensors and compact multi-axis fingertip sensors.

### Why scarcity is capped

Motor current provides an alternative torque estimate. It is imperfect because torque constant, temperature, gearing, friction and dynamics introduce error, but it can reduce or eliminate dedicated load sensing in some joints.

Robot manufacturers can also choose different strain structures, sensor ICs or in-house calibration architectures.

**INTERPRETATION:** The possible moat is not the strain gauge itself; it is a **compact overload-tolerant sensor + repeatable calibration process integrated into the joint**.

**Bottleneck Strength: 3.9 / 5.**

This is the only common-component layer close enough to Gate A to retain as a synthesis watch.

---

## 4. Bearings — exceptionally high content, weaker scarcity

Robotic joints can use:
- cross-roller bearings;
- thin-section ball bearings;
- angular-contact pairs;
- deep-groove miniature bearings;
- reducer-specific support bearings;
- thrust/radial bearings around screw drives.

Performance variables:
- stiffness / moment capacity;
- preload;
- runout;
- friction;
- grease / life;
- noise;
- compact cross section;
- shock / contamination.

**FACT:** MinebeaMitsumi's FY3/2026 materials estimate **120–200 bearings in a high-performance humanoid body excluding hands and 30–100 per hand**, while emphasizing cross-roller, thin-section and miniature bearings.

**FACT:** THK and IKO market cross-roller bearings specifically for compact high-rigidity robot-joint applications.

**INTERPRETATION:** This is perhaps the clearest example of a potential **content winner rather than bottleneck winner**.

Multiple Japanese/European/Chinese/global bearing suppliers can make precision rolling bearings, and architecture changes can materially alter counts.

### Specialized joint bearings

Cross-roller / very thin-section bearings deserve a higher score than generic bearings because joint stiffness and packaging are sensitive to geometry/preload.

But supply is still not narrow enough for Gate A today.

- specialized cross-roller/thin-section: **3.8 / 5**;
- generic/miniature bearings: **3.6 / 5**.

---

## 5. Why high unit count can mislead investors

A simple humanoid BOM screen might conclude:

```text
150 bearings × 1m robots = huge bearing opportunity
40 motors × 1m robots = huge motor opportunity
40 encoders × 1m robots = huge encoder opportunity
```

That arithmetic can be directionally right on revenue demand and still wrong on economics.

The missing variables are:
- supplier count;
- component ASP normalization;
- robot architecture changes;
- OEM dual sourcing;
- internal manufacturing;
- price erosion at volume;
- total-company exposure.

**CONCLUSION:** #83 should only promote a common-component supplier if direct production evidence shows that humanoid content materially changes margins / backlog / total-company earnings, not simply unit opportunity.

---

## 6. MinebeaMitsumi as the best common-component benchmark

Minebea is useful precisely because it spans nearly every tested layer.

**FACT:** FY3/2026 investor materials show humanoid offerings across:
- body and hand bearings;
- cross-roller / thin-section bearings;
- frameless motors;
- small motors;
- ball screws;
- torque / force / fingertip sensors;
- analog sensor-processing ICs;
- connectors;
- cooling fan motors.

**FACT:** Minebea says it is expanding sales to major North American and Chinese humanoid companies and that progress in winning North American orders is underway. It presents a long-term humanoid-products revenue ambition with >10% operating-margin target.

**INTERPRETATION:** Minebea may become an attractive **high-content platform company** even though none of its individual component layers qualifies as a structural bottleneck.

That distinction makes it a legitimate later Gate-B candidate, not because bearings are scarce, but because portfolio breadth + manufacturing scale could make humanoid growth financially material.

---

## 7. Implications for #82 industrialization

The common-component screen strengthens the integration thesis.

If:
- motors are multi-source;
- encoders are multi-technology;
- bearings are broadly available;
- torque sensors have substitute estimation paths;

then the higher switching burden may sit in **combining them into one joint and reproducing that joint at stable thermal, noise, backlash and calibration performance**.

That is the direct test for #82.

---

## 8. Gate-A decision

No standalone common component passes Gate A today.

**Strongest watch: joint force/torque sensing 3.9/5.**

This is a meaningful negative result. It prevents the research programme from equating rising component count with durable supplier scarcity.

No company is promoted from #81 alone.

---

## Sources

- Schaeffler humanoid BOM / actuator architecture: https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20251202_humanoids_at_schaeffler.pdf
- Schaeffler planetary actuator: https://www.schaeffler.de/en/news_media/press_releases/press_releases_detail.jsp?id=88158464
- MinebeaMitsumi FY3/2026 results / humanoid product map: https://www.minebeamitsumi.com/english/corp/investors/disclosure/financial/p2026/__icsFiles/afieldfile/2026/05/21/e2026_slide_en.pdf
- MinebeaMitsumi humanoid product platform: https://tech.minebeamitsumi.com/en/pickup/humanoidrobot/index.html
- MinebeaMitsumi magnetic encoders: https://www.minebeamitsumi.com/english/news/newproducts/2026/1210772_20485.html
- THK cross-roller rings: https://www.thk.com/jp/en/products/cross_roller_ring/cross_roller_ring/
- IKO crossed roller bearings: https://www.ikont.co.jp/eg/product/needle/ndl0803.html
