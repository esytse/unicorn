# Physical AI Deep Dive — Data Engines, Teleoperation and Fleet Learning

**Issue:** #92  
**Status:** Gate-A initial pass complete  
**Confidence:** Medium-High on structural scarcity; Medium-Low on merchant capture  
**Last substantive update:** 2026-09-08

## Executive conclusion

**Proprietary real-world state/action/outcome feedback passes Gate A at 4.7/5.**

The key bottleneck is **not simply owning lots of video**. It is operating a system that repeatedly captures informative physical experience, aligns observations with actions/outcomes, identifies rare failures, converts them into training/evaluation data and closes the loop through redeployment.

The strongest evidence is unusually consistent across otherwise different Physical AI operators:

- Figure says the data needed for general-purpose robotics does not already exist online and has built a Figure-exclusive global collection pipeline.
- Tesla describes fleet-derived data from millions of cars as its embodied-AI data advantage.
- Waymo has nearly 200m fully autonomous miles plus billions of simulated miles and treats closed-loop simulation / evaluation as part of continuous improvement.
- Amazon has >1m robots across >300 facilities and applies a foundation model to optimize fleet behavior.
- Skild explicitly describes deployment generating data that improves a cross-embodiment model, which then enables more deployment and more data.
- NVIDIA GR00T combines internet human video, real teleoperation and synthetic data rather than relying on one source.

### Gate-A scores

| Sublayer | Score | Conclusion |
|---|---:|---|
| **Real deployment feedback / state-action-outcome data** | **4.7** | Pass |
| **Rare failure / intervention / edge-case mining** | **4.7** | Pass |
| **Data engine: selection, curation, replay, lineage** | **4.6** | Pass |
| Cross-embodiment data normalization / representation | 4.4 | Pass narrowly / architecture risk |
| Robot-native teleoperation data | 4.0 | Technically valuable; scaling-limited |
| Human egocentric / demonstration video | 3.6 | High scale, weaker hardware proximity |
| Generic unlabeled internet video | 3.1 | Useful for world priors, weak action grounding |

**Key investment implication:** the strongest structural moat may be **captive inside vertically integrated operators**. A merchant supplier only becomes interesting if it can collect/learn across many customers or retain data/evaluation rights without being disintermediated by the robot OEM.

---

## 1. Why Physical AI data is different

LLMs can learn enormous amounts from static text and images. Physical agents must learn mappings closer to:

`state_t + goal + embodiment → action_t → next state / contact / success / failure`

A useful physical training example can require:

- synchronized video/depth/tactile/proprioception;
- embodiment geometry / kinematics;
- action commands / torques / target poses;
- task context;
- success / failure / intervention signal;
- timing / latency;
- environment state;
- safety outcome.

**INTERPRETATION:** This makes high-quality action-grounded data both more expensive and more path-dependent than ordinary video.

---

## 2. Figure — direct revealed preference for a data bottleneck

### FACT

Figure's August 25, 2026 Index announcement says:

- it is building a Figure-exclusive physical-data pipeline;
- >264,000 app downloads across 100+ countries;
- >44,000 weekly active users;
- >16m uploaded videos;
- roughly 30 minutes of new video processed every second at announcement;
- $15m paid to data creators;
- commitment to spend >$1bn over the following 12 months on data + compute.

Figure states that the broad physical data required for general-purpose robots does not already exist on the internet.

### FACT

On September 3, 2026 Figure announced an Nscale partnership for up to 100,000 NVIDIA Vera Rubin GPUs, an initial $3.5bn compute commitment with intent to scale beyond $6bn. Figure explicitly said it had become largely **data- and compute-bound**.

### INTERPRETATION

A company whose core product is humanoid hardware is allocating enormous capital to **data + compute rather than only actuators/factories**. This is strong revealed-preference evidence that the bottleneck has moved upstream into learning infrastructure.

### FALSIFICATION

Index's consumer human-video strategy also proves that robot-native teleoperation is not the only scalable route. Human demonstrations can broaden diversity at much lower hardware cost.

---

## 3. Tesla — deployed fleet as embodied data engine

### FACT

Tesla's 2026 CVPR materials say its self-driving work curates an embodied-AI dataset from **millions of cars in its fleet** and presents architecture, data, training, evaluation, safety and deployment as one end-to-end AI system.

### FACT

Tesla also applies related vision/planning/inference capabilities across autonomous vehicles and Optimus, although the degree of direct dataset transfer is not publicly quantified.

### INTERPRETATION

The important moat is not a camera stream by itself. It is the ability to:

- observe a huge distribution of real environments;
- identify interesting/failed cases;
- retrieve similar events;
- retrain;
- deploy updated models back into a fleet;
- observe the next generation of failures.

This is a closed data flywheel unavailable to a model vendor with no field deployment.

### OPEN QUESTION

How much driving data genuinely transfers to humanoid manipulation versus providing only general visual/world priors?

---

## 4. Waymo — real data + virtual miles + evaluation

### FACT

Waymo said in February 2026 that the Waymo Driver had traveled nearly **200m fully autonomous miles** and navigates **billions of miles in virtual worlds**.

### FACT

Its world model is adapted to driving and generates camera + lidar outputs, including controllable rare events.

### FACT

Waymo later emphasized that large-scale **closed-loop** simulation is critical because open-loop replay does not capture the way surrounding agents react to the autonomous vehicle's actions.

### INTERPRETATION

Waymo demonstrates that the strongest dataset is not purely real or purely synthetic. The moat is a **hybrid real-data → scenario/evaluation → simulation → policy → fleet loop**.

### Investment implication

The data asset is strongly proprietary but economically captive to Waymo/Alphabet rather than available as a standalone merchant data business.

---

## 5. Amazon — scale changes the data problem

### FACT

Amazon said in June 2025 it had deployed its **one millionth robot**, with the fleet spanning >300 facilities.

### FACT

Amazon's DeepFleet generative-AI foundation model is designed to coordinate robot movement across that fleet and improve travel efficiency by ~10%.

### INTERPRETATION

Amazon illustrates a second type of Physical AI data moat: **workflow and fleet-operation data**, not only manipulation trajectories.

At very large scale, optimization opportunities appear in:

- congestion;
- routing;
- task allocation;
- storage placement;
- maintenance;
- facility-specific dynamics.

This strengthens the thesis that fleet operations and data learning can compound after hardware is commoditized.

---

## 6. Skild — data-source trade-offs are explicit

### FACT

Skild's August 2026 S1 post says no single robotics data source wins simultaneously on:

- hardware proximity;
- diversity;
- scalability.

Its characterization:

- robot teleoperation — high hardware proximity, low diversity/scale;
- intermediate capture approaches — moderate across dimensions;
- egocentric human video — high diversity/scale, low hardware proximity.

### FACT

Skild says new tasks traditionally require tens to hundreds of hours of deployment-condition post-training data, motivating in-context learning and broader pretraining.

### FACT

Skild separately describes its deployed cross-embodiment model as a flywheel: existing robots generate data, which improves the model, which enables more deployments.

### INTERPRETATION

This is important falsification against a simplistic 'teleoperation data is the moat' thesis.

The durable advantage may be the **ability to combine heterogeneous data sources and learn which data is worth collecting next**.

---

## 7. NVIDIA — synthetic amplification weakens raw-data scarcity

### FACT

NVIDIA GR00T uses a mixture of:

- internet-scale human video;
- real-world teleoperation;
- synthetic data.

### FACT

NVIDIA's synthetic-motion pipeline reported generating ~780k synthetic trajectories / ~6.5k hours equivalent from limited demonstrations in ~11 hours and reported better model performance when synthetic and real data were combined.

### FACT

GR00T N1.5 research showed synthetic DreamGen trajectories could add new behaviors without task-specific teleoperation, while post-training on ~1,000 real Unitree demonstrations materially improved object-manipulation performance.

### INTERPRETATION

Synthetic data is a strong **falsification of raw real-data volume scarcity**.

But it does not eliminate the need for reality:

- real demonstrations seed / ground the process;
- simulation must model contact/dynamics correctly;
- deployment exposes distribution shifts and failures;
- real evaluation is required to detect simulation blind spots.

**Conclusion:** synthetic data shifts value from 'collect everything physically' toward **real-data quality, calibration, failure mining and data-engine intelligence**.

---

## 8. The hierarchy of data value

### Highest-value data

1. **rare safety / intervention / failure data**
2. successful and failed state-action-outcome trajectories in actual deployment
3. customer/workflow-specific edge cases
4. force/tactile/proprioception aligned to vision and action
5. diverse human demonstrations with useful task semantics
6. synthetic variants grounded in real examples
7. generic internet video/world priors

**INTERPRETATION:** The marginal value of the next hour of data is extremely uneven. This increases the importance of selection / active learning rather than raw dataset size.

---

## 9. What could become a merchant profit pool?

### A. Vertically integrated fleet operators

Strongest data moat, but data economics are captive.

Examples / archetypes:

- autonomous vehicle operator;
- warehouse/factory fleet owner;
- vertically integrated robot OEM with installed fleet.

### B. Cross-OEM robot-brain platforms

Potentially powerful if one model is deployed across many manufacturers and contracts preserve learning rights.

Required evidence:

- production deployments across different embodiments;
- right to reuse learning/data;
- performance improves with cumulative fleet scale;
- customers do not fork/insource the model.

### C. Teleoperation / data-service providers

Easier to merchantize but weaker moat if collection labor is substitutable.

Best opportunities would own:

- specialized capture hardware;
- high-quality action labeling;
- difficult environments;
- data rights;
- active-learning / failure-mining workflow.

### D. Data infrastructure / replay / observability platforms

Potential recurring software economics, but incumbents/cloud platforms may commoditize generic tooling.

The investable layer needs domain-specific workflow and switching cost.

---

## 10. Gate-A scoring rationale

### Real deployment feedback — 4.7/5

Strengths:

- difficult to synthesize perfectly;
- tied to actual product usage;
- compounds with installed fleet;
- captures failures and environment distribution;
- can improve both training and evaluation;
- high switching cost if tightly integrated.

Limits:

- often captive rather than merchant;
- data may not transfer across embodiments;
- privacy/customer rights can restrict reuse.

### Rare failure/intervention data — 4.7/5

Rare events are precisely the cases hardest to collect intentionally and most valuable for safe autonomy.

Synthetic generation can expand variants but requires real anchors and validation.

### Data engine / curation / replay — 4.6/5

A large fleet creates value only if the operator can identify informative experiences, retrieve/replay them, maintain lineage and feed them into evaluation/training quickly.

### Cross-embodiment normalization — 4.4/5

Potentially very valuable but technically uncertain. If robustly solved, it converts fragmented robot fleets into one learning network.

### Teleoperation — 4.0/5 technical, lower merchant capture

High-fidelity but labor/hardware constrained and increasingly amplified or partially bypassed by synthetic data and human video.

---

## 11. Thesis breakers

Lower the data-engine score if:

- zero/few-shot robot learning removes the need for substantial deployment-specific data;
- world models become accurate enough that real data is needed only for small calibration sets;
- cross-embodiment policies generalize with little post-training;
- data rights prevent platform vendors from learning across customers;
- model improvements saturate quickly with fleet scale;
- synthetic/consumer video provides equivalent failure coverage to deployed fleets.

Raise the score if:

- operators show clear learning curves with fleet hours;
- intervention rates fall through targeted failure-data collection;
- cross-customer data rights create a genuine multi-OEM network effect;
- real-data access becomes a gating factor for foundation-model performance.

---

## 12. Gate-A decision

**PASS — 4.7/5 for proprietary real-world feedback / failure data.**  
**PASS — 4.6/5 for the data-engine / curation / replay function.**

**But:** do **not** open broad company underwriting from this alone.

The next step is #99 synthesis after testing whether simulation/evaluation can partially substitute for real data and whether data loops are merchantizable.

## Primary sources

- Figure — Index: https://www.figure.ai/news/introducing-index
- Figure / Nscale: https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership
- Tesla x CVPR 2026: https://www.tesla.com/event/tesla-x-cvpr-2026
- Waymo World Model: https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/
- Waymo — 10 AI Lessons: https://waymo.com/blog/2026/08/10ailessons/
- Amazon — one million robots / DeepFleet: https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model
- Skild — S1 / Data Engine: https://www.skild.ai/blogs/s1
- Skild — Reindustrial Revolution / data flywheel: https://www.skild.ai/blogs/reindustrial-revolution
- Skild — learning by watching: https://www.skild.ai/blogs/learning-by-watching
- NVIDIA GR00T: https://developer.nvidia.com/isaac/gr00t
- NVIDIA synthetic motion generation: https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/
- NVIDIA GR00T N1.5: https://research.nvidia.com/labs/gear/gr00t-n1_5/
