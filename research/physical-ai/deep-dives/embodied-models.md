# Physical AI Deep Dive — Embodied Models, VLA, Planning and Control Transfer

**Issue:** #95  
**Status:** Gate-A initial pass complete  
**Confidence:** Medium  
**Last substantive update:** 2026-09-08

## Executive conclusion

The model layer is central to Physical AI capability, but **base model weights do not currently look like the strongest structural scarcity layer**.

The harder and more defensible problems appear to be:

- cross-embodiment transfer;
- embodiment-specific post-training;
- control integration;
- safety validation;
- access to proprietary deployment data.

### Gate-A scores

| Sublayer | Score | Conclusion |
|---|---:|---|
| Embodiment-specific post-training / adaptation | **4.4** | Pass |
| Cross-embodiment transfer / action representation | **4.4** | Pass technically; merchant moat unproven |
| Low-level policy / real-time control integration | **4.3** | Pass narrowly |
| High-level embodied reasoning / planning | 4.2 | Important; capability diffusing quickly |
| General VLA foundation-model weights | **3.8 supplier scarcity** | Do not treat as concentrated moat |
| Generic VLM world understanding | 3.4 | increasingly general/open |

**Core finding:** Physical AI likely resembles enterprise AI in one important way: **model capability can diffuse faster than the proprietary data, workflow integration and validation loops around it.**

---

## 1. The model stack is becoming layered

Current leading systems increasingly separate or combine several functions:

1. world / semantic understanding;
2. embodied spatial reasoning;
3. task planning;
4. VLA policy generation;
5. whole-body / navigation / manipulation policy;
6. low-level control;
7. embodiment adapter;
8. safety/fallback control.

Different vendors draw the boundaries differently.

**INTERPRETATION:** This architectural fluidity itself reduces confidence that one model class or interface becomes a durable monopoly layer.

---

## 2. Google — high-level reasoning + VLA separation

### FACT

Gemini Robotics uses:

- an embodied reasoning model for world understanding / planning;
- a VLA model for translating perception/instruction into robot actions.

### FACT

Gemini Robotics 2 demonstrates whole-body control, advanced dexterity and multi-robot coordination.

### FACT

Gemini Robotics On-Device 2 is designed for local operation and Google says it can adapt to new robot embodiments with relatively small example sets.

### INTERPRETATION

This architecture suggests that high-level intelligence may become increasingly reusable across embodiments while lower-level action/control remains adapted to hardware.

If true, value migrates away from a monolithic robot model toward:

- embodiment adapters;
- post-training data;
- action representations;
- runtime/control integration;
- evaluation.

---

## 3. Figure — end-to-end unification is also credible

### FACT

Figure's Helix 02 connects onboard vision, touch and proprioception directly to the robot's actuators through a unified visuomotor network and demonstrates long-horizon whole-body autonomy.

### INTERPRETATION

This is a counterexample to the idea that Physical AI must permanently separate high-level reasoning, planning and control into independent stacks.

Neural systems can absorb more of the control hierarchy over time.

### Falsification for middleware/control moats

If end-to-end learned control becomes robust enough, some classical planning/control software layers may shrink.

But the system still depends on:

- embodiment data;
- real-time execution;
- safety envelopes;
- calibration;
- evaluation.

---

## 4. NVIDIA — open models weaken base-weight scarcity

### FACT

NVIDIA GR00T is explicitly an open reference platform, and GR00T 1.7 is described as an open commercially usable VLA model.

### FACT

The stack includes open data/pipelines, simulation, middleware/runtime and deployment hardware rather than monetizing only model weights.

### INTERPRETATION

NVIDIA's strategy is direct falsification of a thesis that the foundation model itself must remain scarce.

A capable open model can become the base layer on which vendors compete through:

- data;
- tools;
- compute;
- deployment;
- optimization;
- hardware integration.

This looks closer to an ecosystem/platform strategy than a closed-model scarcity strategy.

---

## 5. Skild — cross-embodiment transfer is the strategic prize

### FACT

Skild explicitly targets 'omni-bodied' intelligence: one model that can work across quadrupeds, humanoids, tabletop arms and mobile manipulators.

### FACT

Its architecture is hierarchical, with a low-frequency high-level policy feeding a higher-frequency low-level action policy.

### FACT

Skild says using multiple morphologies expands the training set and improves robustness to hardware changes/failures.

### INTERPRETATION

If cross-embodiment transfer works, it creates a potentially powerful data-network effect:

`more embodiments → more diverse data → better shared representation → faster new embodiment deployment → more data`

That could be a genuine platform moat.

### OPEN QUESTION

Can the platform retain data rights and customer dependence, or do OEMs use the shared model only as a starting point and then own the post-training/deployment stack themselves?

---

## 6. In-context learning reduces post-training burden — but does not eliminate it yet

### FACT

Skild S1 argues that traditional robotics post-training can require tens to hundreds of hours in deployment conditions and is designed to learn new tasks from demonstration context rather than task-by-task fine tuning.

### FACT

Google also emphasizes rapid adaptation to new embodiments for its on-device robotics model.

### INTERPRETATION

This is important falsification against a permanent high-cost fine-tuning moat.

If few-shot / in-context adaptation keeps improving, then the value of bespoke engineering and large task-specific data sets can fall.

But this may increase the value of:

- a broad pretrained data engine;
- high-quality demonstrations;
- deployment feedback;
- evaluation.

Again, scarcity migrates rather than disappears.

---

## 7. Action representation may be a hidden interface bottleneck

Cross-embodiment Physical AI needs to translate intent across bodies with different:

- joint counts;
- kinematics;
- torque limits;
- sensors;
- grippers/hands;
- coordinate frames;
- timing/control rates.

Possible abstractions include:

- end-effector poses;
- relative joint actions;
- motor torques;
- trajectory chunks;
- latent action tokens;
- high-level skills.

NVIDIA GR00T uses state-relative action chunks for many embodiments.

**HYPOTHESIS:** A robust cross-embodiment action representation could be strategically important, but it is too early to treat one representation/vendor as scarce.

Score: **4.4 technical problem / lower current supplier concentration.**

---

## 8. Why low-level integration still matters

A robot policy must ultimately connect to:

- servo rates;
- motor torque limits;
- collision handling;
- balance/stability;
- braking;
- thermal constraints;
- safety monitors.

A foundation model can generate actions, but the cost of an unstable or unsafe output is physical.

This keeps embodiment-specific control integration at **4.3/5** even if higher-level model weights commoditize.

---

## 9. What may become merchantizable

### Cross-OEM robot-brain platform

Potentially high value if it can prove:

- production deployments across several OEMs;
- model performance improves from shared fleet learning;
- customers allow cross-customer learning;
- switching costs rise with deployed skills/data;
- revenue is recurring rather than one-time engineering.

### Foundation-model API / licensing

Easier to scale but weaker moat if open alternatives become good enough.

### Post-training / adaptation platform

Potentially sticky if it owns:

- data tooling;
- embodiment adapters;
- evaluation;
- runtime deployment.

### Low-level control middleware

Can be valuable in fragmented hardware ecosystems, but vertical integration and open robotics middleware are threats.

---

## 10. Model-layer thesis breakers

Raise base-model scarcity if:

- one model family becomes meaningfully superior across many embodiments for a sustained period;
- switching requires large retraining costs and customer data cannot be ported;
- action/token representations become proprietary standards;
- production OEMs converge on one third-party brain.

Lower it if:

- open GR00T/Gemini-class alternatives converge rapidly;
- few-shot embodiment adaptation becomes routine;
- robot OEMs train their own policies from shared/open bases;
- model architecture matters less than deployment data/evaluation.

---

## 11. Gate-A decision

**PASS — 4.4/5 for embodiment-specific post-training / adaptation.**  
**PASS — 4.4/5 for cross-embodiment transfer as a technical platform problem, but merchant capture remains unproven.**  
**PASS narrowly — 4.3/5 for low-level policy/control integration.**  
**DO NOT treat general VLA foundation-model weights as a scarce supplier layer yet — ~3.8/5 supplier scarcity.**

### Physical AI implication

The model layer is likely to be hugely important while **economic defensibility sits around the model rather than only in the weights**.

This strengthens the current umbrella thesis:

`data + post-training + evaluation + deployment loop` > `model weights alone`

No company is promoted to `Watch` from Gate A alone.

## Primary sources

- Google Gemini Robotics: https://deepmind.google/models/gemini-robotics/
- Google Gemini Robotics 2: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Google Gemini Robotics On-Device 2: https://deepmind.google/models/gemini-robotics/on-device/
- Figure Helix 02: https://www.figure.ai/news/helix-02
- Figure Helix: https://www.figure.ai/helix
- NVIDIA Isaac GR00T: https://developer.nvidia.com/isaac/gr00t
- NVIDIA GR00T development platform: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/
- Skild — general-purpose robotic brain: https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- Skild — S1: https://www.skild.ai/blogs/s1
