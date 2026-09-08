# Physical AI — End-to-End Value Chain

**Status:** Initial canonical map  
**Parent issue:** #91  
**Last substantive update:** 2026-09-08

## Executive map

Physical AI is not a linear hardware supply chain. It is a **closed cyber-physical learning loop** with two coupled paths:

### Learning / software loop

`deployed fleet / humans / environment`
→ `multimodal state + action + outcome data`
→ `curation / teleoperation / failure mining / action labeling`
→ `real-to-sim / digital twin / world model`
→ `synthetic data + scenario generation`
→ `foundation / embodied model training`
→ `post-training / adaptation / skill learning`
→ `evaluation / critic / safety validation`
→ `optimized model + runtime package`
→ `on-device deployment`
→ `new field experience`
→ **back into data**

### Embodiment / action loop

`environment`
→ `sensors / perception`
→ `state estimation / localization`
→ `high-level reasoning / task planning`
→ `VLA / policy / motion planning`
→ `real-time controller / servo stack`
→ `power electronics`
→ `actuator / drivetrain / mechanism`
→ `physical interaction / mobility`
→ `proprioception / force / tactile feedback`
→ `safety monitor / evaluator`
→ **back into perception and data**

Power, thermal, communications, manufacturing, calibration and field service cut across both loops.

---

## 1. Embodiments / markets

Physical AI should be tested across several form factors because a bottleneck that exists only in one body type is weaker than a cross-embodiment dependency.

| Embodiment | Typical environment | Main action | Key constraints | Existing scale signal |
|---|---|---|---|---|
| Autonomous vehicles / robotaxis | Open roads | Mobility | safety, rare events, sensor fusion, compute, regulation | Waymo ~200m fully autonomous miles; Tesla millions of fleet vehicles |
| Industrial robots / cobots | Structured/semi-structured factories | manipulation/process | precision, commissioning, uptime, safety, workflow integration | mature installed base; ABB/FANUC/Yaskawa/UR etc. |
| AMRs / mobile manipulators | Warehouses/factories | navigation + manipulation | fleet orchestration, mapping, uptime, workflow integration | Amazon >1m robots across >300 sites |
| Humanoids | Human-built spaces | mobility + manipulation | data scarcity, whole-body control, dexterity, energy, actuation, reliability | early production / commercial pilots |
| Drones / autonomous aerial systems | Outdoor/remote | mobility + sensing | power density, onboard autonomy, comms, navigation, regulation | mature commercial/defense deployment |
| Surgical / medical robots | Controlled clinical spaces | manipulation | safety, precision, regulatory validation | high-value deployed systems but narrow workflows |

**INTERPRETATION:** Humanoids are an important test case because they stress many layers simultaneously, but they should not define the entire Physical AI thesis.

---

## 2. Data acquisition / grounding

### Inputs

- onboard video / depth / lidar / radar;
- proprioception / joint state;
- force / torque / tactile data;
- human demonstration video;
- teleoperation trajectories;
- operator interventions / remote assist;
- task outcome / success / failure labels;
- fleet telemetry / incidents;
- site / map / workflow context.

### Economic question

Is the scarce asset:

- raw data volume;
- state/action alignment;
- coverage of rare failures;
- embodiment diversity;
- deployment-specific data rights;
- or the infrastructure that continuously converts field experience into better training examples?

### Evidence

- Figure says general-purpose physical data is not available on the internet and is spending heavily to build Index.
- Tesla explicitly emphasizes fleet-derived embodied data.
- Waymo combines real driving with massive virtual mileage.
- Skild says no single data source dominates scalability, diversity and hardware proximity; it blends teleoperation, egocentric video and other sources.
- NVIDIA combines internet video, real teleoperation and synthetic robot data.

### Preliminary Bottleneck Strength

- proprietary state/action/outcome feedback loop: **4.7**
- rare failure / intervention data: **4.7**
- high-fidelity robot teleoperation data: **4.0 technical scarcity / 3.5 merchant capture**
- generic human video: **3.2**

**Key falsification:** scalable video/synthetic learning may reduce robot-native data requirements.

---

## 3. Data engine / curation

Functions:

- synchronizing multimodal streams;
- action labeling / trajectory construction;
- filtering low-quality / redundant data;
- identifying failures / uncertainty;
- balancing task and environment coverage;
- replay / retrieval;
- privacy / customer data governance;
- dataset versioning / lineage;
- continuous learning pipelines.

**INTERPRETATION:** Raw fleet size is not enough. A weak data engine can drown a model in repetitive easy examples. The compounding moat may lie in **finding the next most informative physical experience cheaply and repeatedly**.

Preliminary score: **4.6/5**.

---

## 4. Simulation / digital twins / world models

Sub-layers:

1. geometry / CAD / scene reconstruction;
2. rigid/deformable-body physics;
3. contact / friction / materials;
4. sensor simulation;
5. generative world models;
6. digital twins / virtual commissioning;
7. synthetic trajectory generation;
8. rare-event / adversarial scenario generation;
9. closed-loop policy evaluation;
10. sim-to-real calibration.

### Evidence

- Waymo uses a generative world model built on Genie 3 for controllable multi-sensor driving simulation and calls closed-loop simulation critical.
- NVIDIA Isaac / Cosmos / GR00T creates synthetic motion data and supports closed-loop evaluation.
- ABB RobotStudio HyperReality integrates Omniverse and claims sim-to-real / virtual commissioning can reduce physical prototyping and improve deployment reliability.

### Preliminary scores

- generic physics engine: **3.6**
- generic world foundation model: **4.0**
- synthetic trajectory generation: **4.2**
- domain-calibrated digital twin / sim-to-real: **4.6**
- closed-loop safety / policy evaluation: **4.7**

**INTERPRETATION:** The moat likely sits in calibration + evaluation rather than rendering alone.

---

## 5. Training compute / data infrastructure

Requirements:

- multimodal training clusters;
- high-throughput storage and replay;
- video / sensor preprocessing;
- distributed training;
- simulation at scale;
- synthetic-data generation;
- reinforcement learning / policy evaluation.

### Evidence

Figure's September 2026 Nscale agreement targets up to 100,000 NVIDIA Vera Rubin GPUs with an initial $3.5bn commitment and intent to exceed $6bn; Figure explicitly says it is becoming data- and compute-bound.

### Interpretation

Physical AI can become a major incremental AI-compute workload, but much of the bottleneck may be the **same memory / energy / accelerator infrastructure already researched elsewhere**.

Preliminary Physical-AI-specific score:

- generic training compute availability: **4.3**, but cross-theme rather than unique;
- large-scale simulation compute: **4.3**;
- dataset storage/replay I/O: **3.8**.

Cross-links:

- `research/memory/`
- `research/energy/`

Do not double count general AI infrastructure as a new Physical AI bottleneck.

---

## 6. Embodied models / robot brains

Sub-layers:

- vision-language models with spatial reasoning;
- embodied reasoning / task planners;
- VLA models;
- navigation policies;
- manipulation policies;
- whole-body policies;
- low-level locomotion/control policies;
- skill libraries;
- multi-agent / multi-robot coordination;
- cross-embodiment representations.

### Evidence

- Google Gemini Robotics separates high-level embodied reasoning from VLA execution and demonstrates multiple embodiments.
- Gemini Robotics 2 extends to whole-body control and dexterous hands.
- Figure Helix 02 connects all onboard sensors to all actuators through a unified visuomotor system.
- NVIDIA GR00T is an open reference model/platform.
- Skild targets omni-bodied intelligence and an explicit fleet data flywheel.

### Preliminary scores

- general VLA capability: **4.1 technical / 3.6 scarcity**
- cross-embodiment transfer: **4.4 technical problem / 4.0 supplier scarcity**
- embodiment-specific post-training: **4.4**
- low-level real-time policy/control integration: **4.3**

**FALSIFICATION:** Open models and fast capability diffusion may make base model weights less defensible than proprietary deployment data and post-training.

---

## 7. On-device compute / runtime

Requirements:

- low latency;
- performance per watt;
- sensor ingest / bandwidth;
- deterministic control;
- model compression / quantization;
- local safety fallback;
- thermal limits;
- intermittent / zero-cloud connectivity.

### Evidence

- NVIDIA GR00T includes Jetson Thor for real-time inference/control.
- Google has Gemini Robotics On-Device.
- Tesla designs custom FSD inference hardware and emphasizes performance-per-watt; its 2026 filing says runtime changes cut inference latency and it is expanding semiconductor-manufacturing scope alongside Robotaxi/Optimus ramps.
- Skydio documents onboard routing/autonomy that continues through degraded connectivity.

### Preliminary score

- high-performance edge AI compute: **4.5**
- deterministic runtime / deployment optimization: **4.4**

**FALSIFICATION:** merchant capture is weakened by custom silicon, ARM/Qualcomm/other alternatives and OEM vertical integration.

---

## 8. Sensing / perception / state estimation

### Sensor categories

- RGB cameras;
- depth cameras;
- lidar;
- radar;
- ultrasonic;
- IMU;
- GNSS;
- force / torque;
- tactile;
- joint encoders;
- current / motor sensing.

### Higher-level functions

- object / scene understanding;
- 3D reconstruction;
- SLAM / mapping;
- localization;
- occupancy / freespace;
- pose estimation;
- contact state;
- sensor health / calibration.

### Preliminary view

There is unlikely to be one cross-Physical-AI sensor bottleneck.

- generic cameras: **3.2**
- lidar in autonomous driving: architecture-specific; scarcity TBD
- tactile for fine manipulation: **3.8 preliminary**
- force / torque sensing: **3.9** from actuator work
- sensor fusion / calibration: **4.1 preliminary**

**INTERPRETATION:** Calibration and training dependence may create more switching cost than the sensor hardware itself.

---

## 9. Planning / control / safety runtime

Layers:

- high-level mission planning;
- behavior planning;
- trajectory planning;
- whole-body control;
- model predictive control;
- collision avoidance;
- stability control;
- safety envelopes;
- watchdog / fallback controllers;
- human override.

Physical AI foundation models increasingly touch these layers, but safety-critical low-level control remains embodiment/domain-specific.

Preliminary score: **4.3/5**, with merchant capture uncertain.

---

## 10. Embodiment hardware

Includes:

- motors;
- reducers;
- linear screws;
- bearings;
- brakes;
- wheels / legs / propellers;
- arms / hands / grippers;
- structures / materials;
- joints / transmissions.

The detailed humanoid actuator work is already canonical in `research/robotics-actuators/`.

Current validated humanoid findings:

- precision rotary-transmission manufacture: **4.4**
- planetary roller-screw precision manufacture: **4.4**
- actuator industrialization / calibration: **4.4**
- common motors / encoders / bearings: mostly below Gate A.

**Physical AI implication:** these can be excellent embodiment-specific bottlenecks without being the highest cross-embodiment bottleneck.

---

## 11. Energy storage / power / thermal

### Functions

- batteries / cells / packs;
- BMS;
- DC power distribution;
- motor drives / inverters;
- charging;
- thermal management;
- power budgeting / mission planning.

### Embodiment dependence

- drones: extremely sensitive to specific energy / weight;
- humanoids: runtime and mass sensitive;
- AMRs: opportunity for scheduled charging / battery swaps;
- autonomous vehicles: large batteries, but power is less constrained relative to platform size;
- industrial arms: often grid-powered.

Preliminary cross-Physical-AI score:

- energy density as a system constraint: **4.2**
- merchant battery-cell scarcity specific to Physical AI: **3.2**
- pack/BMS/integration: **3.7**

**Lesson:** technical constraint ≠ scarce profit pool.

---

## 12. Manufacturing / calibration / reliability

Functions:

- precision assembly;
- sensor calibration;
- actuator calibration;
- end-of-line test;
- thermal / noise / vibration test;
- functional-safety validation;
- traceability;
- field failure analysis;
- refurbishment / service.

The actuator stream already showed industrialization can equal component manufacturing in scarcity.

Preliminary cross-embodiment score: **4.4/5**, especially where safety/reliability requirements are high.

---

## 13. Deployment / commissioning

Physical AI value is not realized until the agent performs useful work in a real workflow.

Tasks:

- site mapping / digital twin;
- workflow integration;
- task teaching / demonstration;
- no-code setup;
- safety zones;
- user permissions;
- integration with WMS/MES/ERP/fleet systems;
- acceptance testing;
- local network / cloud integration.

ABB's Physical AI strategy emphasizes virtual commissioning; Amazon's fleet economics show the importance of workflow/fleet optimization rather than one robot's intelligence.

Preliminary score: **4.4**.

---

## 14. Safety / evaluation / critics

### Functions

- closed-loop scenario evaluation;
- failure prediction;
- uncertainty estimation;
- stress / adversarial scenarios;
- policy regression testing;
- regulatory evidence;
- incident reconstruction;
- safe fallback / remote assist.

Waymo's Driver + Simulator + Critic framework is direct evidence that evaluation is not a final QA step but part of the learning loop.

Preliminary score: **4.7/5** for domain-calibrated closed-loop evaluation in safety-critical autonomy.

---

## 15. Fleet operations / continuous improvement

Functions:

- orchestration / dispatch;
- route/task allocation;
- remote assist;
- telemetry;
- OTA updates;
- predictive maintenance;
- uptime optimization;
- anomaly detection;
- fleet-wide learning.

### Evidence

- Amazon DeepFleet is designed to improve travel efficiency across a >1m-robot fleet.
- NEURA/AWS explicitly targets shared intelligence / real-time processing across robot fleets.
- autonomous vehicle operators run centralized fleet/safety/remote-assist infrastructure.

Preliminary score: **4.5** where scale and workflow integration create switching costs.

---

# Preliminary common-basis frontier

| Rank | Layer | Preliminary Bottleneck Strength | Cross-embodiment durability | Merchant-capture uncertainty |
|---:|---|---:|---:|---:|
| 1 | Proprietary real-world feedback / rare failure data | **4.7** | High | High — often captive |
| 1 | Domain-calibrated closed-loop evaluation / safety critic | **4.7** | High | High |
| 3 | Domain-calibrated sim-to-real / digital twin | **4.6** | High | Medium |
| 3 | Data engine / curation / replay | **4.6** | High | High |
| 5 | Edge inference / deterministic runtime | **4.5** | High | Medium |
| 5 | Fleet operations / continuous learning | **4.5** | High | High |
| 7 | Manufacturing / calibration / reliability | **4.4** | Medium-High | Medium |
| 7 | Embodiment-specific precision actuation | **4.4** | Medium | Medium |
| 7 | Embodiment-specific post-training/control integration | **4.4** | Medium-High | High |
| 10 | Generic training compute | 4.3 | High | Lower Physical-AI specificity |
| 10 | Physical energy density constraint | 4.2 | Medium | Low merchant scarcity |
| 12 | Base VLA / foundation model weights | ~4.1 technical / lower scarcity | High | open-model risk |
| 13 | Generic sensors / motors / bearings | mostly <4.0 | Medium | broad supply |

These scores are **prioritization hypotheses**, not completed Gate-A conclusions except where explicitly inherited from the actuator research.

---

# Bottleneck-migration hypotheses

Physical AI is likely to behave like the energy research: solving one bottleneck moves the constraint.

### Better foundation models

`model capability improves`
→ data/evaluation becomes limiting
→ deployment exposes long-tail failures
→ fleet feedback / safety validation becomes more valuable.

### More synthetic data

`synthetic generation scales`
→ generic data shortage falls
→ real calibration / reality-gap measurement becomes more valuable.

### Cheaper/better hardware

`actuators/sensors commoditize`
→ deployment economics improve
→ more fleet data accumulates
→ differentiation migrates toward learning/deployment loops.

### Better cross-embodiment transfer

`one policy adapts across bodies`
→ model weights become more general
→ embodiment-specific post-training/calibration may shrink
→ platform data and runtime integration become more important.

### Edge compute improves

`more intelligence runs locally`
→ latency/connectivity constraints ease
→ power/thermal and safety validation may become the binding deployment limits.

---

# Investment-research implications

Do not automatically target:

- every humanoid component supplier;
- generic camera suppliers;
- battery makers purely on robot volume;
- VLA startups purely because models are capable;
- simulation companies without evidence of calibration / workflow lock-in.

Prefer hunting for:

1. **merchantizable feedback loops** — companies that improve from many customer deployments;
2. **domain-calibrated simulation / evaluation platforms** with high switching cost;
3. **edge compute/runtime platforms** that survive OEM custom-silicon pressure;
4. **deployment/fleet software** with recurring revenue and data network effects;
5. **architecture-resilient precision / industrialization suppliers** where physical qualification remains hard;
6. **enabling infrastructure already captured by memory/energy research**, without double counting.

The synthesis issue #99 will replace this preliminary frontier with evidence-backed common-basis scores after #92–#98 complete.
