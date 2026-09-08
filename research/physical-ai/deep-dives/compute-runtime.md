# Physical AI Deep Dive — Training Compute, Edge Inference and Runtime

**Issue:** #94  
**Status:** Gate-A initial pass complete  
**Confidence:** Medium-High on edge constraint; Medium on merchant scarcity  
**Last substantive update:** 2026-09-08

## Executive conclusion

Physical AI creates **two different compute questions**:

1. **training / simulation compute**, which can be enormous but largely inherits the generic AI infrastructure bottlenecks already covered by memory and energy research;
2. **on-device / edge inference and deterministic runtime**, which is genuinely Physical-AI-specific because autonomy must operate under latency, connectivity, power, thermal, sensor-I/O and safety constraints.

### Gate-A result

- **Edge performance-per-watt / low-latency compute as a system function: 4.5/5 — PASS.**
- **Deterministic mixed-criticality runtime / deployment stack: 4.3/5 — PASS narrowly.**
- **Merchant edge-accelerator supplier scarcity: ~3.9/5 — not yet a structural concentration bottleneck.**
- **Generic training compute: 4.3/5 technically, but not a distinct Physical AI bottleneck.**

The important distinction is:

> **Physical AI strongly needs edge compute, but NVIDIA, Qualcomm, Google/custom accelerators and OEM silicon strategies provide credible alternative supply paths.**

Do not turn a hard system requirement into an automatic single-vendor thesis.

---

## 1. Why the edge is structurally different from cloud AI

Physical agents often cannot wait for a cloud round trip.

Requirements include:

- millisecond-scale reaction;
- operation during network loss;
- bounded/jitter-controlled latency;
- continuous sensor ingest;
- real-time motor/control interfaces;
- safety fallback;
- low energy use;
- limited cooling/weight;
- privacy/data sovereignty;
- long field deployment lifetimes.

This is especially strong in:

- drones;
- autonomous vehicles;
- humanoids;
- AMRs;
- safety-critical industrial robots.

**INTERPRETATION:** The edge is not simply a smaller data center. Compute architecture is coupled to sensors, control and power.

---

## 2. NVIDIA — integrated Physical AI reference stack

### FACT

NVIDIA Isaac GR00T explicitly spans:

- data pipelines;
- foundation models;
- simulation;
- middleware/runtime libraries;
- Jetson Thor for real-time robot inference and control.

### INTERPRETATION

This is strong evidence that edge compute is part of the Physical AI critical path rather than an interchangeable afterthought.

NVIDIA's advantage is broader than silicon:

- CUDA ecosystem;
- model/runtime optimization;
- simulation integration;
- TensorRT / deployment tooling;
- robot developer ecosystem.

### FALSIFICATION

That integrated position must be tested against alternative robotics SoCs and custom silicon rather than assumed to be permanent.

---

## 3. Qualcomm — credible high-end merchant alternative

### FACT

Qualcomm introduced the Dragonwing IQ10 robotics platform in January 2026 for advanced AMRs and full-size humanoids and disclosed a collaboration with Figure on next-generation compute architecture.

### FACT

Qualcomm describes IQ10 as providing:

- up to ~700 TOPS;
- an 18-core Oryon CPU;
- heterogeneous CPU/GPU/NPU compute;
- support for up to 20 cameras plus lidar/radar;
- real-time safeguarding / motion-control capabilities;
- operation under tight power budgets.

### FACT

Qualcomm's Physical AI architecture explicitly combines edge compute, sensing/perception, planning/control, connectivity and a fleet learning/data flywheel.

### INTERPRETATION

Qualcomm materially weakens a thesis that robotics edge AI becomes NVIDIA-only. Its automotive/embedded heritage is directly relevant to deterministic, power-efficient, long-lifecycle autonomy.

---

## 4. Google — model efficiency reduces hardware dependence

### FACT

Gemini Robotics On-Device 2 is designed to run locally because many robots operate with network constraints and latency sensitivity.

### FACT

Google says the model can adapt to new embodiments with limited examples and is based on efficient on-device model families.

### INTERPRETATION

Model efficiency is itself a substitute for hardware scale. If smaller models deliver strong robotics capability, the edge-compute scarcity score should not simply extrapolate cloud-GPU demand.

---

## 5. Tesla — strongest vertical-integration falsification

### FACT

Tesla designs its own FSD inference hardware around performance-per-watt and applies the same broader AI strategy to vehicles and humanoid robotics.

### FACT

Tesla's 2026 filing says its AI runtime work reduced inference latency and that, alongside Robotaxi/Optimus ramps, it is expanding manufacturing scope toward semiconductor fabrication to improve supply resilience.

### INTERPRETATION

If large Physical AI OEMs reach sufficient volume, merchant edge silicon can be strategically insourced.

This does not make edge compute less critical; it makes **merchant supplier capture less certain**.

---

## 6. Connectivity is complement, not substitute

Cloud/edge coordination can support:

- fleet learning;
- large-model planning;
- model updates;
- simulation;
- global maps;
- remote assist.

But the robot still needs local autonomy for:

- immediate obstacle avoidance;
- balance/control;
- manipulation/contact;
- degraded connectivity;
- safe stopping.

Qualcomm's 2026 Physical AI architecture explicitly frames robots as nodes in an edge/cloud learning network rather than cloud-controlled terminals.

### Conclusion

Connectivity can redistribute workloads but does not eliminate local inference/control.

---

## 7. The runtime may be more defensible than raw TOPS

A production robotics compute platform must integrate:

- AI inference;
- classical real-time control;
- safety-critical threads;
- sensor drivers;
- motor / CAN / EtherCAT interfaces;
- memory / I/O scheduling;
- model lifecycle;
- OTA updates;
- fault containment.

Qualcomm/NEURA's 2026 collaboration explicitly calls for standardized runtime/deployment interfaces for validated, reliable, deterministic robotic workloads.

**INTERPRETATION:** The harder long-term platform moat may be **mixed-criticality runtime + developer ecosystem + validation**, not benchmark accelerator throughput.

But standardization can cut both ways: it may create ecosystem lock-in for a platform winner or reduce switching costs among silicon providers.

---

## 8. Training compute — enormous demand, weaker thematic novelty

### FACT

Figure's September 2026 Nscale agreement targets up to 100,000 Vera Rubin GPUs, initially ~$3.5bn and potentially >$6bn, and Figure says it is data- and compute-bound.

### INTERPRETATION

Physical AI can become a meaningful source of frontier training demand.

However, this demand principally reinforces already-known dependencies:

- accelerators;
- HBM / memory bandwidth;
- advanced packaging;
- data-center power / cooling.

Those are already canonical in:

- `research/memory/`
- `research/energy/`

### Decision

Do **not** create a duplicate 'Physical AI GPU' investment thesis unless evidence shows a distinct supplier/content mix.

---

## 9. Cross-embodiment view

| Embodiment | Edge requirement | Main reason |
|---|---|---|
| Autonomous vehicles | Very High | safety/latency, multi-sensor fusion, no cloud dependence |
| Drones | Very High | connectivity loss, power/weight, fast control |
| Humanoids | High | whole-body control, perception/manipulation, power limits |
| AMRs | High | navigation/safety, intermittent network |
| Industrial arms | Medium-High | deterministic control; AI inference can be local cell/controller |
| Surgical systems | High | safety/latency, controlled environment |

**Conclusion:** edge inference is highly cross-embodiment and architecture-resilient.

---

## 10. Where value could accrue

### Merchant silicon + platform

Strongest if supplier controls:

- accelerator;
- runtime;
- sensor interfaces;
- model optimization;
- developer ecosystem;
- safety libraries.

### OEM custom silicon

Captures value internally at high scale; major threat to merchant silicon margins.

### Runtime / middleware independent of silicon

Potentially attractive if it becomes a cross-chip deployment standard, but open-source robotics middleware and OEM stacks are strong competition.

### Cloud/edge fleet infrastructure

Potential recurring value, but belongs more naturally in #98 fleet/deployment work.

---

## 11. Thesis breakers

Lower merchant edge-silicon scarcity if:

- Qualcomm/NVIDIA/others become readily substitutable;
- common runtimes make hardware swaps easy;
- small efficient models reduce compute requirements rapidly;
- robot OEMs increasingly build custom silicon;
- cloud offload becomes reliable enough for most high-level inference.

Raise it if:

- one platform wins dominant production designs across multiple embodiments;
- safety certification ties software/runtime tightly to hardware;
- memory/sensor-I/O requirements create specialized architectures competitors cannot match;
- developers standardize on one integrated simulation→training→edge stack.

---

## 12. Gate-A decision

**PASS — 4.5/5 for edge performance-per-watt / latency as a Physical AI system constraint.**  
**PASS narrowly — 4.3/5 for deterministic runtime / mixed-criticality deployment.**  
**NO concentration pass yet — ~3.9/5 for merchant accelerator supplier scarcity.**

This is an important negative distinction: **edge compute is essential without yet being a concentrated supplier bottleneck.**

No company is promoted to `Watch` from Gate A alone.

## Primary sources

- NVIDIA Isaac GR00T: https://developer.nvidia.com/isaac/gr00t
- Google Gemini Robotics On-Device 2: https://deepmind.google/models/gemini-robotics/on-device/
- Qualcomm — Physical AI / Dragonwing architecture: https://www.qualcomm.com/news/onq/2026/02/physical-ai-6g-robotics
- Qualcomm IQ10 launch: https://www.qualcomm.com/news/releases/2026/01/qualcomm-introduces-a-full-suite-of-robotics-technologies-power
- Qualcomm / NEURA runtime collaboration: https://www.qualcomm.com/news/releases/2026/03/neura-robotics-and-qualcomm--enter-strategic-collaboration-to-ad
- Figure / Nscale compute: https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership
- Tesla AI & Robotics: https://www.tesla.com/en_gb/AI
- Tesla 2026 filing AI & Software: Tesla investor / SEC Q1 2026 filing
