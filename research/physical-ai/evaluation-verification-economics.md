# Simulation, Evaluation and Verification Economics

**Issue:** #172  
**Status:** bounded discovery complete  
**Confidence:** Medium  
**Last substantive update:** 2026-09-23

## Executive conclusion

**INTERPRETATION:** The scarce complement is not generic simulation. The stronger economic bottleneck is the **trusted release/qualification loop**: calibrated models + scenario/coverage assets + repeatable regression + traceable evidence that a changing autonomous or cyber-physical system is safe enough to deploy.

The evidence supports three different markets that should not be conflated:

1. **Generic simulation / world-model infrastructure** — strategically important, but exposed to platform/open-tool commoditisation.
2. **Domain-calibrated digital twins and virtual commissioning** — stronger capture where the model is tied to real controllers, plants, machines and operating data.
3. **Continuous V&V / release gating** — strongest scarcity hypothesis because every material model/software change can recreate the validation obligation.

No company is promoted to Gate-E or the live Top-10 from this discovery pass.

## Bottleneck / capture map

| Layer | Scarcity | Recurrence | Capture mechanism | Main risk | Current view |
|---|---|---|---|---|---|
| Generic physics / rendering | Low-Medium | Medium | licenses / compute | open/platform substitution | Do not promote |
| World-model / synthetic generation | Medium | High usage | compute + platform | frontier capability diffuses | Watch |
| Domain-calibrated digital twin | High in specific domains | Medium-High | software + integration + lifecycle reuse | customer-specific services burden | Strong |
| Scenario / coverage / failure corpus | High | High | proprietary data + workflow lock-in | captive OEM data | Strong |
| Continuous regression / release gating | High | Very high | recurring software / workflow | customers build internally | Strongest hypothesis |
| Independent certification / assurance | Potentially High | Event + recurring updates | qualification / audit / evidence | standards fragment; low software economics | Research gap |

## Evidence

### Foretellix — clean private release-gating archetype

**FACT:** Foretellix describes simulation trustworthiness as measurable, repeatable evidence linking simulated and real-world behaviour, including trajectory and statistical fidelity. It explicitly connects this evidence to determining whether enough of an operating domain has been explored to release a system safely.

**FACT:** Its 2026 material also describes regression-test “intent drift”: a test can continue to pass while no longer checking the behaviour it was designed to validate.

**INTERPRETATION:** This is stronger than selling a simulator. The economic object is a persistent validation workflow whose value can rise as autonomy models change faster. If embedded in release criteria, switching requires rebuilding scenario definitions, coverage evidence and confidence in the validation methodology.

**OPEN QUESTION:** Foretellix is private and does not disclose revenue, retention, software margins or customer concentration. Merchant economic capture is therefore plausible but not financially proven.

### Applied Intuition — broader private platform archetype

**FACT:** Applied Intuition says world foundation models require production tooling around data pipelines, simulation, evaluation, experiment tracking and orchestration.

**FACT:** In September 2026 it described Digital Proving Grounds that test multi-vendor autonomous systems virtually and continuously before hardware deployment. In July it launched Dana across build, test, deploy and operate workflows.

**INTERPRETATION:** Applied Intuition supports the migration from “simulation product” toward an integrated autonomy development and assurance platform. Multi-vendor integration is particularly relevant because system-level failures can sit between components rather than inside one model.

**OPEN QUESTION:** Private-company disclosure does not allow a clean decomposition of simulation revenue versus validation/release-gating economics.

### Siemens — listed industrial digital-twin capture

**FACT:** Siemens positions executable digital twins as models that can move from engineering into commissioning and operations, including connection to live operational data and virtual PLC verification.

**FACT:** Siemens customer evidence for HELLER describes a one-to-one CNC digital twin using the real NC kernel for virtual prove-out before physical execution. Siemens also markets digital-twin validation in regulated pharma automation and protection systems.

**INTERPRETATION:** Siemens demonstrates why industrial twins can be more defensible than generic simulators: the twin is coupled to the installed controller, machine/process model, commissioning workflow and lifecycle operations. This can create switching cost and reuse beyond a one-off design simulation.

**COUNTERPOINT:** Siemens is highly diversified. Even if the bottleneck thesis is correct, V&V/digital-twin upside may not be sufficiently material to group earnings for a focused investment thesis.

### Synopsys + Ansys — listed simulation/verification benchmark

**FACT:** Synopsys completed its acquisition of Ansys in July 2025, combining silicon design/IP with system simulation and analysis. The combined roadmap includes testing and virtualization of complex intelligent systems.

**INTERPRETATION:** This is a useful listed benchmark for the thesis that verification expands from silicon into full cyber-physical systems. Existing EDA economics show that verification can become mandatory workflow infrastructure when failure cost is high.

**COUNTERPOINT:** The current investable exposure is broad and dominated by semiconductor design and engineering software; #172 does not establish that Physical-AI V&V is yet a material incremental earnings driver.

### dSPACE — specialist private comparator

**FACT:** dSPACE states that automated-driving safety arguments increasingly rely on simulation, but the simulation models themselves must be verified and validated before their outputs can be trusted.

**INTERPRETATION:** This creates a recursive assurance requirement: as simulation replaces physical testing, proving simulation fidelity becomes its own bottleneck.

## Candidate screen

| Candidate | Public? | Exposure | Capture quality | Earnings purity | #172 disposition |
|---|---|---|---|---|---|
| Foretellix | No | scenario generation, coverage, V&V, simulation trust | High potential | n/a | private archetype; monitor commercial proof |
| Applied Intuition | No | integrated autonomy development, simulation, evaluation | High potential | n/a | private archetype; monitor release-gating evidence |
| Siemens | Yes | industrial digital twins, controls, virtual commissioning | High in installed workflows | Low | benchmark / watch, not focused promotion |
| Synopsys (incl. Ansys) | Yes | simulation, analysis, verification | High established workflow economics | Medium-Low for Physical AI specifically | benchmark; require materiality proof |
| dSPACE | No | automotive simulation / V&V | High domain fit | n/a | specialist comparator |
| NVIDIA | Yes | Omniverse / Isaac / world models / compute | platform capture strong, V&V scarcity weaker | Low for V&V | commoditisation/enabler benchmark |

## Bottleneck migration indicators

### Evidence that strengthens the thesis
- validation becomes an explicit release gate for autonomous/agentic systems;
- customers maintain reusable scenario/coverage libraries across model versions;
- vendors disclose recurring subscriptions, retention or expansion tied to V&V;
- regulators/customers accept simulation-derived evidence in formal safety cases;
- digital twins remain connected to live assets after commissioning;
- multi-vendor system validation becomes harder than component validation.

### Evidence that weakens the thesis
- open simulation/evaluation stacks become sufficiently standardized that switching costs collapse;
- model vendors self-validate successfully enough to remove independent tooling;
- real-world testing remains the dominant acceptance mechanism;
- synthetic/virtual test results fail to correlate with field performance;
- V&V stays predominantly captive inside OEMs;
- commercial revenue remains project/services-heavy rather than recurring software.

## Investment implication

**HYPOTHESIS:** As model intelligence becomes cheaper and model iteration accelerates, the number of candidate releases can rise faster than the ability to prove them safe and effective. That makes **verification throughput and trusted evidence** a possible scarce complement to abundant intelligence.

The best economic exposure would therefore not simply own a simulator. It would own a **repeat release gate** with proprietary coverage/failure assets, workflow integration and accepted evidence.

Current listed proxies are too diluted to justify a portfolio change from this pass. The highest-purity examples are private.

## Next research trigger

Re-open/promote this lane when one of the following appears:
- a listed vendor discloses material recurring revenue/ARR specifically from autonomous-system V&V, digital-twin validation or release gating;
- Foretellix, Applied Intuition or another high-purity vendor becomes investable;
- a major regulatory/industry framework makes simulation/evaluation evidence a formal recurring release requirement;
- Siemens/Synopsys separately disclose enough segment economics to show Physical-AI validation is material.

## Sources

- Foretellix simulation trustworthiness (2026): https://www.foretellix.com/unified-approach-to-simulation-trustworthiness-in-av-development/
- Foretellix regression test intent drift (2026): https://www.foretellix.com/how-ai-helps-keeping-scenario-tests-aligned-with-their-true-purpose/
- Foretellix Physical AI toolchain: https://www.foretellix.com/
- Applied Intuition world foundation models (2026): https://www.appliedintuition.com/engineering-blog/world-foundation-models-from-research-to-reality
- Applied Intuition Digital Proving Grounds (2026): https://www.appliedintuition.com/blog/digital-proving-grounds
- Applied Intuition Dana (2026): https://www.appliedintuition.com/press-releases/applied-intuition-launches-dana
- Siemens executable digital twin: https://www.siemens.com/en-gb/products/simcenter/integration-solutions/executable-digital-twin/
- Siemens HELLER digital-twin reference (2026): https://references.siemens.com/en/reference/cnc-digital-twin-heller
- Siemens pharma DigiTwin: https://www.siemens.com/en-gb/products/masco-group-automation-digitwin/
- Synopsys completes Ansys acquisition: https://investors.ansys.com/news-releases/news-release-details/synopsys-completes-acquisition-ansys
- dSPACE simulation validation: https://www.dspace.com/en/pub/home/learning-center/recordings/learningconnections/how-to-validate-simulations.cfm
