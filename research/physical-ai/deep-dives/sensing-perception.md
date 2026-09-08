# Physical AI Deep Dive — Sensing, Perception, Localization and State Estimation

**Issue:** #96  
**Status:** Gate-A initial pass complete  
**Confidence:** Medium-High on no broad sensor bottleneck; Medium on fusion/calibration  
**Last substantive update:** 2026-09-08

## Executive conclusion

**No generic sensor category passes cross-embodiment Gate A.**

Physical AI absolutely depends on sensing, but the leading deployed systems do not even agree on the same sensor architecture. Waymo says multimodal cameras + lidar + radar are indispensable for fully autonomous driving, while Tesla deploys camera-based Tesla Vision without radar on some current models/markets. Industrial robots, humanoids, AMRs and drones have still different stacks.

The stronger cross-embodiment bottleneck is **sensor fusion + calibration + trained-system dependence**, not the individual sensor hardware.

### Gate-A scores

| Sublayer | Score | Conclusion |
|---|---:|---|
| **Sensor fusion / calibration / health monitoring** | **4.2** | Pass narrowly |
| Safety-critical localization / mapping in mobile autonomy | 4.1 | Architecture/domain-specific pass |
| Force / torque sensing for contact-rich manipulation | 3.9 | Important; supplier breadth / software substitutes |
| Tactile sensing for dexterity | 3.8 | High technical value; architecture not converged |
| Lidar in autonomous mobility | ~3.9 | Critical in Waymo-style stacks, not universal |
| Imaging radar in autonomous mobility | ~3.8 | Complementary, architecture-specific |
| Depth cameras | 3.6 | Broad alternatives |
| IMUs / proprioception | 3.5 | Essential content, broad supply |
| Generic RGB cameras | 3.2 | Ubiquitous but elastic/multi-source |

**Core implication:** sensor replacement becomes expensive mainly because the **trained perception stack, calibration, safety case and failure history depend on it**, not because cameras/lidar/radar are intrinsically scarce merchant products.

---

## 1. Sensors are critical but not a single market

A Physical AI system can use some combination of:

- RGB / monochrome cameras;
- depth / stereo;
- lidar;
- radar;
- ultrasonic;
- IMU;
- GNSS;
- joint encoders;
- motor current sensing;
- force / torque sensors;
- tactile arrays;
- microphones;
- external/infrastructure-mounted sensors.

The optimal stack depends on:

- environment;
- speed;
- failure consequence;
- payload/contact;
- available power;
- weather;
- cost;
- whether infrastructure sensors are available.

**INTERPRETATION:** A sensor can be mission-critical within one embodiment without being a broad Physical AI bottleneck.

---

## 2. Waymo — multimodal sensing as safety architecture

### FACT

Waymo's August 26, 2026 '10 AI Lessons' says cameras alone are not enough and describes multimodal sensors as indispensable after more than 200m fully autonomous miles.

### FACT

Waymo's 6th-generation Driver uses cameras, radar and lidar as complementary, overlapping sensing modalities. Waymo says redundancy is essential for safe backup behavior and difficult weather/visibility conditions.

### FACT

The 6th-generation system entered fully autonomous operation in February 2026 with a streamlined/lower-cost sensor suite while preserving custom multimodal sensing.

### INTERPRETATION

Waymo demonstrates high switching cost at the **system level**:

- perception models are trained on a specific suite;
- sensor geometry and timing are calibrated;
- simulation reproduces those modalities;
- safety evidence accumulates against that configuration;
- vehicle integration is co-designed.

Changing lidar/camera/radar is not only a procurement event; it can trigger retraining and revalidation.

This supports fusion/calibration scarcity more strongly than raw sensor scarcity.

---

## 3. Tesla — direct falsification of sensor convergence

### FACT

Tesla support pages state that some Model 3/Y vehicles in Europe/Middle East use **camera-based Tesla Vision without radar** for Autopilot-related functions.

### FACT

Tesla's FSD (Supervised) remains a driver-supervised system and its current consumer materials emphasize onboard 360-degree cameras and neural-net processing.

### INTERPRETATION

Tesla is not evidence that lidar/radar are unnecessary for every autonomous system; it is evidence that **credible system architectures can make radically different sensor choices**.

This sharply weakens any cross-Physical-AI thesis such as:

> 'Every autonomous machine must buy lidar from a narrow supplier set.'

Architecture choice can substitute software/data/compute for hardware modalities.

---

## 4. Cross-embodiment sensor requirements

### Autonomous vehicles

High speeds, weather and safety consequences create the strongest case for redundant multimodal sensing.

### Drones

Common stack:
- cameras;
- IMU;
- GNSS;
- depth/lidar/radar in selected missions;
- onboard obstacle perception.

Weight/power can rule out sensors that are attractive in cars.

### AMRs

Typically use:
- cameras / lidar;
- odometry / IMU;
- mapped environment;
- infrastructure context.

Highly structured sites can reduce sensor complexity.

### Humanoids / manipulators

Vision is necessary but manipulation adds:
- force/torque;
- proprioception;
- tactile/contact feedback;
- joint/motor state.

### Industrial arms

Structured environments may rely on relatively little sensing until Physical AI adds vision/force adaptation.

**Conclusion:** no one sensing BOM survives all embodiments unchanged.

---

## 5. Force / torque sensing — closest manipulation-specific candidate

The actuator Gate-A work scored joint force/torque sensing at ~3.9/5.

### Why it matters

Contact-rich tasks require estimates of:

- insertion force;
- grasp force;
- collisions;
- balance/contact;
- slip;
- external disturbance.

### Why it does not pass broadly

Force can be estimated from:

- dedicated strain/torque sensors;
- motor current;
- joint deflection;
- series-elastic elements;
- tactile arrays;
- learned observers.

Different robot architectures trade hardware precision against model/control complexity.

**Conclusion:** important, but no current evidence of broad supplier concentration.

---

## 6. Tactile sensing — technically hard, architecture unsettled

Dexterous manipulation benefits from:

- contact location;
- normal/shear force;
- slip;
- texture;
- pressure distribution.

But current hands vary across:

- fingertip-only sensors;
- palm/finger arrays;
- camera-based tactile sensing;
- force estimation from actuators;
- underactuated/simple grippers that avoid dense tactile stacks.

### Score: **3.8/5**

High technical difficulty does not yet equal standardized high-volume supplier lock-in.

---

## 7. Localization / mapping

Mobile Physical AI systems require a stable estimate of:

- position;
- orientation;
- free space;
- map context;
- dynamic obstacles.

Approaches include:

- HD maps;
- visual-inertial odometry;
- lidar SLAM;
- radar localization;
- GNSS/RTK;
- infrastructure beacons;
- learned end-to-end navigation.

### Waymo evidence

Waymo's 2026 lessons describe maps as a powerful prior rather than a substitute for perception.

### Score: **4.1/5** in safety-critical mobile autonomy, lower cross-embodiment universality.

The likely moat is **map/update/data integration + localization validation**, not commodity GNSS/IMU hardware.

---

## 8. Sensor fusion / calibration — stronger than components

A production system must solve:

- extrinsic calibration between sensors;
- intrinsic calibration;
- time synchronization;
- temperature/drift correction;
- vibration / mechanical movement;
- degraded-sensor detection;
- uncertainty weighting;
- sensor replacement calibration;
- online health monitoring.

In high-safety systems, a change in sensor can cascade into:

- perception retraining;
- simulation updates;
- safety regression;
- certification evidence;
- field validation.

### Gate-A score: **4.2/5**

**INTERPRETATION:** This creates a system/software/validation moat rather than a guaranteed sensor-vendor moat.

---

## 9. Infrastructure sensing can move the bottleneck

NVIDIA Halos Outside-In Safety uses external cameras to extend robot safety perception beyond onboard sensors.

Qualcomm describes robot-to-infrastructure architectures where overhead sensors can update shared world models and fleet behavior.

### Implication

Physical AI can shift sensing from:

`every robot carries everything`

toward:

`robot + site infrastructure + shared world model`

This is additional falsification against rigid per-unit sensor-content forecasts.

---

## 10. Economic capture

### Sensor manufacturers

Can benefit from volume, but moat requires:

- unique modality/performance;
- qualification / safety certification;
- embedded software/calibration;
- sticky design-ins;
- difficult substitutes.

### Perception/fusion platform

Potentially more durable if it owns:

- multimodal fusion;
- calibration;
- health monitoring;
- safety evidence;
- cross-sensor data layer.

But model vendors/OEMs may keep this captive.

### Mapping/localization platforms

Can create recurring data/service economics in mobility, but less relevant to fixed manipulators.

---

## 11. Thesis breakers

Raise individual sensor scarcity if:

- multiple leading embodiments converge on the same modality/supplier technology;
- safety regulations mandate redundant modalities;
- production design-in/certification creates multi-year lock-in;
- one supplier has materially superior reliability/performance at scale.

Lower it if:

- vision-only systems reach equivalent safety across domains;
- learned perception substitutes for expensive modalities;
- sensor ASPs fall quickly / supplier base broadens;
- infrastructure sensing shifts content off the robot;
- OEMs vertically integrate optics/sensor modules.

---

## 12. Gate-A decision

**NO broad sensor category passes cross-Physical-AI Gate A.**

**PASS narrowly — 4.2/5 for sensor fusion / calibration / health monitoring.**  
**PASS narrowly in mobile autonomy — 4.1/5 for safety-critical localization / mapping.**  
**WATCH — 3.9/5 force/torque sensing and architecture-specific lidar.**

This is a valuable negative result: **sensing is essential without currently being a single concentrated cross-embodiment merchant bottleneck.**

No company is promoted to `Watch` from Gate A alone.

## Primary sources

- Waymo — 10 AI Lessons from 200m+ autonomous miles: https://waymo.com/blog/2026/08/10ailessons/
- Waymo — 6th-generation Driver: https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/
- Waymo — 6th-generation fully autonomous operations: https://waymo.com/intl/zh-cn/blog/2026/02/ro-on-6th-gen-waymo-driver/
- Tesla UK Autopilot / Tesla Vision: https://www.tesla.com/en_gb/support/autopilot
- Tesla FSD (Supervised): https://www.tesla.com/en_ie/fsd
- NVIDIA Halos Robotics: https://www.nvidia.com/en-us/ai-trust-center/halos/robotics/
- Qualcomm Physical AI architecture: https://www.qualcomm.com/news/onq/2026/02/physical-ai-6g-robotics
