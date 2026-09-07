# Test, Known-Good-Die and Burn-In — Deep Dive

**Status:** Evidence-backed deep dive  
**Confidence:** High on rising test intensity; Medium-High on supplier capture  
**Last substantive update:** 2026-09-07  
**Backlog:** closes issue #11 when merged

## Executive conclusion

**FACT:** AI/HBM devices are becoming more expensive, more heterogeneous, hotter, faster and more interconnect-dense. Test vendors are responding with more test insertion points, higher pin counts, greater power/thermal capability and dedicated HBM platforms.

**INTERPRETATION:** The structural test bottleneck is not merely “more chips need testing.” The economic logic changes when a package combines several expensive known-good compute dies plus multiple HBM stacks. A defect that escapes early screening can destroy a package worth orders of magnitude more than an individual die. This pushes testing **left** into wafer/die/module stages and **right** into system-level reliability, increasing both test content and the number of insertion points.

**CONCLUSION:** Test / known-good-die / module-level validation passes Gate A with a **Bottleneck Strength Score of 4.6/5**. The strongest sub-bottlenecks are:

1. **HBM wafer/probe-card test** — extreme I/O count, fine pitch, high current, high temperature and rising interface speed.
2. **Dedicated HBM memory ATE** — higher channel density and speed plus logic-rich base dies make HBM less like conventional commodity DRAM test.
3. **Known-good-everything / module-level test** — interposer, CoW/CoP module and multi-die validation become necessary before expensive final assembly.
4. **Thermal handling and system-level test** — high-power AI accelerators create failure modes that conventional ATE alone may not expose.

The best asymmetric public candidate from this layer is currently **FormFactor**, because it has direct HBM probe-card exposure, volume shipments to all three major HBM manufacturers, record HBM-driven DRAM revenue and a product roadmap aligned with rising HBM pin/power/thermal requirements. Advantest and Teradyne are stronger large-cap benchmarks with very clear economic capture but less small-company asymmetry.

## 1. Bottleneck Strength Score

| Dimension | Score | Evidence / rationale |
|---|---:|---|
| Physical difficulty | **5/5** | Next-generation HBM raises I/O count, speed, current, temperature and fine-pitch contact density simultaneously; advanced packages add large-area module probing and thermal constraints. |
| Supply elasticity | **4/5** | Advantest says it has roughly tripled production capacity and continues expanding memory/SoC tester capacity; FormFactor is expanding manufacturing support. Capacity can expand, but specialist test hardware and qualification are not instantaneous. |
| Supplier concentration | **4.5/5** | Leading memory ATE is concentrated among Advantest and Teradyne; advanced probe cards are concentrated among a limited set including FormFactor, Technoprobe and specialist peers. HBM-specific high-volume qualification narrows the field further. |
| Qualification / switching | **4.5/5** | Probe cards and ATE are tightly matched to device pad layout, speed, thermal conditions and customer test programs. FormFactor notes probe cards are device-specific; production customers qualify hardware for each generation. |
| System criticality | **5/5** | Poor test coverage allows bad die/interconnects into very expensive packages; insufficient throughput can directly constrain production. Advanced packaging economics make early defect screening increasingly mandatory. |
| **Average** | **4.6/5** | **Gate A passed.** |

## 2. Test-flow map

```text
DRAM / logic-base wafer fabrication
        ↓
Wafer probe / parametric + functional test
        ↓
Known-good-die selection
        ↓
HBM stacking / bonding
        ↓
Pre-singulated / stack-level HBM test
        ↓
Post-singulated HBM test / speed validation
        ↓
Integration with accelerator / interposer
        ↓
Known-good-interposer / known-good-CoW or module test
        ↓
Final package test
        ↓
Burn-in / reliability / system-level test
        ↓
AI accelerator shipment
```

The key structural change is the expansion from **known-good-die** toward **known-good-everything**: die, HBM stack, interposer, partially assembled module and final package all become economically relevant test points.

---

## 3. Sub-bottleneck A — HBM wafer probe and probe cards

### Why HBM probe becomes harder

**FACT:** FormFactor's 2026 HBM technical material describes next-generation requirements including:

- interface frequencies above 5 GHz;
- chuck temperatures above 125°C;
- high current delivery;
- dense fine-pitch micro-bump arrays;
- more than 80,000 probes per device under test in some next-generation configurations.

**FACT:** FormFactor describes future HBM/Custom HBM I/O scaling from roughly 1,024 toward 4,096 I/Os, with 16-high/20-high stacks and more logic in the base die.

The probe card has to maintain electrical contact, planarity, force, thermal stability, signal integrity and current delivery simultaneously. As temperature changes, the probe card, wafer and mechanical structure expand differently; fine-pitch arrays leave less tolerance for alignment and planarity errors.

### Direct company evidence — FormFactor

**FACT:** FormFactor said in Q2 2025 that it was shipping probe cards in volume to **all three major HBM manufacturers**.

**FACT:** Q1 2026 revenue was $226.1m, up 32% year-on-year, with **record DRAM revenue and increased HBM demand**.

**FACT:** Q2 2026 revenue reached a record $258.2m, up 31.9% year-on-year, with HBM among the growth initiatives driving sequential Probe Cards revenue.

**FACT:** FormFactor expanded its Keystone Microtech partnership in July 2026 to increase advanced probe-card manufacturing scale and regional support.

### Evidence against the bottleneck thesis

- Probe cards are consumable/custom hardware, but customers can qualify multiple suppliers.
- Higher tester parallelism and improved design-for-test can reduce cost per tested bit.
- HBM makers may redesign pads/test access to simplify testing.
- FormFactor has non-HBM businesses; not all revenue growth is memory-related.

### Current view

**Bottleneck Strength: 4.8/5.** Probe cards look like one of the cleanest physical bottlenecks because every HBM generation pushes pitch, probe count, thermal range and signal integrity simultaneously.

**Company implication:** **FormFactor passes Gate B for `Investigating`**. The company-level work should quantify HBM share of Probe Cards revenue, market share versus Technoprobe/MJC, replacement cycles, gross-margin mix and valuation.

---

## 4. Sub-bottleneck B — HBM memory ATE

### Why HBM needs more capable testers

HBM combines many memory channels, a very wide interface and increasingly sophisticated base-die logic. Testing must cover memory-core integrity, speed, power, interface timing and sometimes logic functionality across multiple process stages.

### Advantest evidence

**FACT:** Advantest launched a new advanced-memory test cell combining the T5801 ultra-high-speed DRAM test system with the M5241 handler for high-power/high-density AI memory.

**FACT:** Advantest says device complexity and rising chip value are causing customers to increase **test time, processes and test content**. It has roughly tripled production capacity over recent years and is continuing to expand memory and SoC tester capacity.

**FACT:** In FY2026 Q1, Advantest sales rose 39.3% year-on-year and operating income 53.3%; the company subsequently raised its FY2026 sales forecast to ¥1.714tn and said the tester market is expected to reach a record size due to AI-semiconductor complexity and volume.

### Teradyne evidence

**FACT:** Teradyne's Magnum 7H is a dedicated HBM test platform supporting base-die wafer test, pre-singulated HBM test and post-singulated HBM test, including HBM3/3E and HBM4/4E speed validation.

**FACT:** Teradyne's Q2 2026 filing says Memory revenue exceeded **$200m for the third consecutive quarter**, driven by strong HBM and DRAM test demand.

**FACT:** Teradyne's 2025 annual filing said memory-test revenue was supported by share gains in HBM and DRAM final test applications.

### Evidence against the bottleneck thesis

- Advantest and Teradyne are large, well-funded suppliers able to expand capacity rapidly.
- Tester platforms are modular/reusable, so customer capex does not necessarily scale linearly with HBM bit shipments.
- Parallelism and smarter adaptive test can reduce test time per unit.
- Very strong margins can attract competitive responses or customer pressure.

### Current view

**Bottleneck Strength: 4.5/5.** Dedicated HBM ATE is clearly benefiting from rising complexity and insertion count. **Advantest and Teradyne are validated benchmark beneficiaries**, but their size reduces the “small supplier becomes indispensable” asymmetry we are hunting.

---

## 5. Sub-bottleneck C — known-good-everything and module-level test

### Why KGD is no longer enough

**FACT:** Teradyne describes a shift from known-good-die to **known-good-everything** as chiplet-based packages integrate compute dies, HBM, interposers, substrates and other components.

**FACT:** In July 2026, Teradyne described new test insertions on partially assembled chip-on-wafer/chip-on-panel modules before substrate attach. These modules can require large-area probing, high current, thermal control and verification of interconnects across HBM, compute die and the interposer.

The economic driver is powerful: once multiple expensive good dies are assembled, a latent defect in an interposer or bonding interface causes a much larger scrap loss. Testing earlier in the assembly chain becomes rational even if it adds test cost.

### New constraints

- probing C4/microbump interfaces rather than conventional pads;
- very large module area;
- high probe force and mechanical stability;
- thousands of watts of power/thermal management at test;
- difficult physical access as bump pitch shrinks;
- test-content partitioning across die/interposer/package boundaries.

### Evidence against the bottleneck thesis

- Some module defects can be addressed using built-in self-test and design-for-test rather than more external test hardware.
- Better assembly yield can reduce the value of intermediate test insertions.
- Standards such as UCIe can make chiplet test more modular over time.

### Current view

**Bottleneck Strength: 4.7/5.** This is a structural consequence of heterogeneous integration. It may create opportunities not only for ATE but also probers, probe cards, interface hardware, sockets and test-cell automation.

---

## 6. Sub-bottleneck D — thermal handling, burn-in and system-level test

### Why final test is moving beyond simple pass/fail

AI accelerators run sustained, high-power workloads close to thermal and electrical limits. A device can pass conventional ATE yet fail under realistic workloads because of power delivery, thermal-induced degradation, package-interconnect weakness or firmware interactions.

**FACT:** Teradyne's 2026 system-level test material argues that ATE and SLT are complementary; advanced HBM/2.5D packages create thermal, interconnect and system-behavior failure modes that require realistic workload validation.

**FACT:** Advantest's M5241 handler emphasizes tighter temperature control and long-duration high-volume operation for advanced memory production.

### Evidence against the bottleneck thesis

- SLT can be expensive and slow; customers will optimize coverage aggressively.
- Better design-for-test and telemetry may reduce physical burn-in duration.
- Hyperscalers may perform additional system validation themselves rather than paying semiconductor suppliers for all coverage.

### Current view

**Bottleneck Strength: 4.2/5.** Thermal/system-level validation is increasingly important, but supplier economics are less cleanly mapped than wafer probe or HBM ATE.

---

## 7. Supplier map

| Test layer | Public / notable suppliers | Current view |
|---|---|---|
| HBM memory ATE | Advantest, Teradyne | Clear large-cap beneficiaries / benchmarks |
| HBM probe cards | **FormFactor**, Technoprobe, MJC and specialist peers | **Highest-priority smaller-company hunting ground** |
| Probers / module probing | TEL and other prober suppliers; FormFactor systems | Growing importance as test shifts to modules |
| Handlers / thermal test | Advantest, Cohu and peers | Important, but HBM-specific capture needs validation |
| Interface boards / sockets | Cohu, Yamaichi, specialist suppliers | Candidate discovery area; evidence not yet strong enough for watchlist promotion |
| System-level test | Teradyne, Advantest and specialist test-cell suppliers | Structural growth, but economics need separation from broader AI test |

## 8. Company candidates after Gate A

### Investigating — FormFactor (FORM)

Why:

- volume production exposure to all three major HBM manufacturers;
- record DRAM revenue with HBM-driven growth;
- device-specific probe cards with extreme next-generation electrical/mechanical requirements;
- smaller revenue base than Advantest/Teradyne, so HBM growth can be more financially material.

Key questions:

- What percentage of Probe Cards revenue is HBM?
- How much HBM share does FormFactor hold versus Technoprobe/MJC?
- What is replacement frequency / recurring content as HBM production grows?
- Does next-generation HBM increase probe-card ASP/content per wafer materially?
- Are gross margins improving as HBM mix rises?
- Is valuation already discounting the full AI/HBM ramp?

### Watch / benchmark — Advantest (6857.T)

Why: strongest evidence that AI/HPC/high-end memory test complexity is translating into scale, margins and capacity expansion. The company is already very large and highly valued, so it is more useful as a benchmark for the size of the profit pool than as the default asymmetric candidate.

### Watch / benchmark — Teradyne (TER)

Why: HBM/DRAM memory test revenue has exceeded $200m for three consecutive quarters; Magnum 7H has dedicated HBM capability and the company is investing in module-level and system-level AI test. Still broader and larger than the ideal “unicorn” hunting target.

## 9. Evidence against the overall test-bottleneck thesis

1. Test vendors are expanding capacity aggressively; Advantest has roughly tripled production capacity.
2. Parallelism, adaptive test and design-for-test can reduce test time per unit.
3. Device makers can add self-test features and standardized chiplet interfaces.
4. ATE is cyclical capital equipment; strong demand can be followed by digestion periods.
5. Large customers can pressure hardware pricing even as test content rises.
6. Some test-value growth may accrue to software/data analytics rather than hardware suppliers.

## 10. Thesis breakers / monitoring indicators

- HBM tester/probe utilization or orders weaken despite continued HBM shipment growth.
- Test time/content per device falls materially as HBM generations advance.
- Probe-card competition commoditizes ASPs or reduces FormFactor share.
- HBM makers internalize more test hardware or adopt architectures that reduce physical probing.
- Module-level test insertion is bypassed by much higher assembly yields and built-in self-test.

## 11. Current conclusion

**Test is a validated structural bottleneck, and it is becoming more valuable rather than less as AI packages become more expensive and heterogeneous.**

The key mechanism is **multiplicative scrap economics**: each extra die, HBM stack and interconnect raises the cost of an escaped defect, so manufacturers add earlier and more sophisticated test rather than simply accepting yield loss.

The most interesting smaller public candidate is **FormFactor**, where HBM directly drives advanced probe-card demand and the technical requirements intensify across generations. Advantest and Teradyne confirm that the overall test profit pool is expanding and provide essential benchmarks for company-level underwriting.

## Sources

- Advantest 2026 CEO address / test-content and capacity: https://www.advantest.com/en/news/2026/20260105.html
- Advantest SEMICON Korea 2026 advanced-memory test cell: https://www.advantest.com/en/news/2026/20260203.html
- Advantest M5241 handler: https://www.advantest.com/en/products/component-test-system/test-handler/m5241/
- Advantest FY2026 Q1 financial review: https://www.advantest.com/en/investors/financial-highlights/review/
- Advantest FY2026 forecast: https://www.advantest.com/en/investors/financial-highlights/forecast/
- Teradyne Magnum 7H: https://www.teradyne.com/products/magnum-7h/
- Teradyne Q2 2026 10-Q: https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-327715/ter-20260628.htm
- Teradyne 2025 10-K: https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-059002/ter-20251231.htm
- Teradyne AI chiplet test insertions: https://www.teradyne.com/2026/07/27/ai-chiplet-architectures-redefining-test-insertions/
- Teradyne system-level test in AI era: https://www.teradyne.com/2026/08/24/slt-in-the-ai-era-validating-reliability-at-scale/
- FormFactor HBM test technical roadmap: https://www.formfactor.com/blog/2026/genai-hbm-architecture-semiconductor-test/
- FormFactor wafer-test/HBM probe discussion: https://www.formfactor.com/blog/2026/from-commodity-to-enabler-wafer-test-at-the-heart-of-the-ai-era/
- FormFactor HFTAP HBM probe-card family: https://www.formfactor.com/product/probe-cards/dram/hftap-series/
- FormFactor Q1 2026 results: https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-first-quarter-results/
- FormFactor Q2 2026 results: https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2026-second-quarter-results
- FormFactor Q2 2025 / all-three-HBM-manufacturers statement: https://investors.formfactor.com/news-releases/news-release-details/formfactor-inc-reports-2025-second-quarter-results/
- FormFactor/Keystone partnership: https://www.formfactor.com/press-release/formfactor-and-keystone-microtech-announce-strategic-partnership-supporting-next-generation-semiconductor-technologies/
