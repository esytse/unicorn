# Advanced Packaging, Interposers and Substrates — Deep Dive

**Status:** Evidence-backed deep dive  
**Confidence:** High on the bottleneck; Medium on supplier capture  
**Last substantive update:** 2026-09-07  
**Backlog:** closes issue #10 when merged

## Executive conclusion

**FACT:** AI accelerators increasingly combine multiple compute dies, HBM stacks and I/O components in very large 2.5D/3D packages. TSMC states that CoWoS demand accelerated sharply after generative AI adoption and is scaling package size from current multi-reticle formats toward 14-reticle packages capable of integrating roughly 10 large compute dies and 20 HBM stacks by 2028.

**INTERPRETATION:** The advanced-packaging bottleneck is not just “CoWoS capacity.” It is a chain of yield-sensitive dependencies that becomes harder as package area, interconnect density, power and HBM count increase: interposer/RDL fabrication, high-performance substrates, bonding and copper deposition/CMP, warpage control, inspection/metrology, and final assembly/test.

**CONCLUSION:** Advanced AI packaging passes Gate A with a **Bottleneck Strength Score of 4.7/5**. The strongest sub-bottlenecks are:

1. **Large-area package/interposer manufacturing and yield** — scaling package area creates lithography, overlay, warpage and defect-density challenges.
2. **High-performance package substrates** — capacity requires multi-year capital expansion and increasingly demanding layer counts, dimensional stability and power delivery.
3. **Inspection/metrology/process control** — defect cost rises sharply as multiple high-value dies and HBM stacks are integrated; direct 2026 order evidence exists for HBM4 and CoWoS-like packaging.
4. **Bonding/CMP/plating and hybrid-bond process equipment** — tighter interconnect pitch increases the need for surface flatness, copper uniformity, alignment and contamination control.

The main strategic conclusion is that **advanced packaging remains structurally constrained even if architecture shifts away from silicon interposers**. CoWoS-S can migrate toward CoWoS-L/R, fan-out, silicon bridges, panel-level packaging or glass/organic interposers, but those transitions create new process-control and substrate requirements rather than eliminating advanced packaging.

## 1. Bottleneck Strength Score

| Dimension | Score | Evidence / rationale |
|---|---:|---|
| Physical difficulty | **5/5** | Larger packages, finer RDL/interconnect pitch, more HBM stacks, high power and CTE mismatch increase overlay, warpage, thermal and yield difficulty. TSMC is scaling CoWoS package size materially over the roadmap. |
| Supply elasticity | **4.5/5** | TSMC, ASE, Amkor and substrate suppliers are all adding capacity, but new fabs/lines require years and large capital commitments. Amkor's Arizona expansion and Ibiden's FY2026-28 substrate plan are explicit examples. |
| Supplier concentration | **4/5** | TSMC remains the benchmark for leading AI 2.5D integration, while ASE/Amkor/Samsung provide alternatives. Several critical sub-layers such as high-end substrates and advanced inspection remain concentrated among a small qualified supplier set. |
| Qualification / switching | **5/5** | Package design is co-optimized with substrate, memory, materials and assembly partners. Amkor's long-term agreements with TSMC and NVIDIA illustrate roadmap-level qualification rather than spot procurement. |
| System criticality | **5/5** | A leading AI accelerator cannot ship if the package cannot integrate compute and HBM at acceptable yield, signal integrity and thermal performance. |
| **Average** | **4.7/5** | **Gate A passed.** |

## 2. Process map

```text
Known-good compute / I/O dies + qualified HBM stacks
        ↓
Interposer / RDL / bridge fabrication
  ├─ silicon interposer (CoWoS-S-like)
  ├─ RDL + local silicon interconnect (CoWoS-L-like)
  ├─ RDL interposer (CoWoS-R / fan-out-like)
  └─ bridge / organic / glass alternatives
        ↓
Lithography + copper plating + CMP + redistribution layers
        ↓
Microbump / hybrid-bond / die attach
        ↓
Chip-on-wafer / fan-out assembly
        ↓
Inspection + 2D/3D metrology + electrical process control
        ↓
High-performance package substrate
        ↓
Underfill / molding / warpage control / thermal integration
        ↓
Substrate attach + final package assembly
        ↓
Final test / system-level validation
```

The important point is that package yield is multiplicative. A late-stage defect can scrap several known-good compute dies plus multiple HBM stacks, so process control and early detection become more valuable as package value rises.

---

## 3. Sub-bottleneck A — large-area interposers, RDL and package scaling

### Evidence the problem is structural

**FACT:** TSMC describes CoWoS as an essential foundation for AI/HPC integration and says generative AI caused substantially greater demand. CoWoS-S currently supports silicon interposers up to about 3.3 reticles, while CoWoS-L/R support larger formats.

**FACT:** At its 2026 North America Technology Symposium, TSMC disclosed a roadmap toward **14-reticle CoWoS in 2028**, capable of integrating about 10 large compute dies and 20 HBM stacks, followed by still larger formats.

**FACT:** ASE is developing a 310 mm × 310 mm automated panel-level packaging line for FOCoS/FOCoS-Bridge, explicitly because package sizes are increasing and wafer-level area utilization becomes less efficient. Production is targeted for 2027.

### Why scaling creates bottlenecks

- larger area increases cumulative defect probability;
- RDL overlay must remain controlled over a larger, distortable surface;
- warpage and CTE mismatch worsen with heterogeneous materials;
- power delivery becomes more difficult across very large packages;
- reticle-limited lithography forces stitching/bridge/RDL alternatives;
- inspection field size and throughput become more demanding;
- handling and test move from die-scale toward module/panel-scale.

### Evidence against the bottleneck thesis

- Packaging architecture is flexible: RDL, bridges, organic or glass substrates can substitute for a full silicon interposer in some designs.
- Panel-level packaging could improve throughput and area utilization materially.
- OSAT competition and foundry investment are increasing quickly.

### Current view

**Bottleneck Strength: 4.7/5.** The exact architecture may change, but the need for high-yield large-area heterogeneous integration strengthens with AI package size. The bottleneck is architectural rather than tied permanently to one interposer technology.

---

## 4. Sub-bottleneck B — advanced package substrates

### Why the substrate matters

The substrate is no longer a passive board. It must provide dense routing, mechanical stability and power delivery beneath a package that can exceed 100 mm in dimension and contain multiple high-current compute dies plus HBM.

**FACT:** ASE notes that high-density AI packages can require sophisticated multi-layer substrates, including configurations up to 11-2-11 wiring layers.

**FACT:** Ibiden announced approximately **¥500 billion** of electronics-business investment across FY2026-28, including additional high-performance IC package substrate capacity mainly for AI/high-performance servers, with new capacity coming online from FY2027.

**FACT:** Shinko is developing an ultra-high-density organic 2.3D substrate intended as an alternative to silicon-interposer 2.5D packaging, specifically supporting logic plus HBM/chiplet integration. Its 2026 glass-core work highlights dimensional stability and warpage as key next-generation substrate challenges.

**FACT:** Ajinomoto continues to develop ABF materials for advanced semiconductor packages and photonic-electronic co-packages. ABF is a foundational build-up dielectric used widely in high-end package substrates.

### Evidence against the bottleneck thesis

- Substrate capacity is expanding aggressively.
- The supplier base includes multiple Japanese, Taiwanese and Korean companies.
- Large capital requirements may dilute returns even when demand is strong.
- Alternative package architectures can change substrate content and design rules.

### Current view

**Bottleneck Strength: 4.4/5.** Capacity and technical complexity are real, but supplier economics require company-specific work. **Ibiden** is the clearest public benchmark because its capex is explicitly tied to high-performance server substrate demand; **Shinko** and ABF/material suppliers are important comparators.

---

## 5. Sub-bottleneck C — inspection, metrology and process control

### Why this layer is especially attractive

Inspection and metrology become more valuable when the cost of missing a defect rises faster than the cost of testing for it. Advanced AI packages combine expensive known-good dies, HBM and interposers; therefore the economic value of finding defects before final assembly increases.

### Direct supplier evidence

**Onto Innovation (ONTO):**

- In March 2026, Onto said a leading HBM manufacturer completed evaluation and selected its Dragonfly G5 2D inspection platform for an **HBM4 ramp**.
- It received commitments for double-digit orders of Dragonfly G5 and 3Di systems, with shipments beginning Q2 2026.
- Onto expects advanced packaging to grow more than 30% in 2026 and offers inspection/metrology for wafer, substrate and panel-level packaging.

**Camtek (CAMT):**

- In February 2026, Camtek disclosed **$45 million** of Hawk inspection/metrology orders from a tier-1 IDM for AI applications. Hawk targets HBM, chiplets, hybrid bonding and wafers with very high micro-bump counts.
- In March 2026, Camtek disclosed more than **$90 million** of Q1 orders from leading OSATs, the majority for CoWoS-like AI packaging, including a single $31 million order.

**Applied Materials (AMAT):**

- Applied launched advanced-packaging CMP, electrochemical deposition and e-beam metrology systems in 2026 targeting HBM TSV, fine-pitch interconnect, hybrid bonding and package process control.
- Applied's scale makes it a benchmark rather than the most asymmetric candidate, but its product launches validate the process-control intensity of the bottleneck.

### Evidence against the bottleneck thesis

- Several strong process-control suppliers compete in advanced packaging, including KLA, Applied, Onto and Camtek.
- Tool share can shift by inspection modality and customer architecture.
- High order growth could be partly cyclical capex rather than durable content expansion.

### Current view

**Bottleneck Strength: 4.8/5.** This is one of the strongest investable sub-layers because there is both technical necessity and direct order evidence. **Camtek and Onto Innovation pass the threshold for company-level investigation.**

---

## 6. Sub-bottleneck D — bonding, CMP, copper deposition and hybrid-bond preparation

### Why it matters

As interconnect pitch shrinks, small variations in copper fill, surface topography, oxide, particles and alignment can reduce bond yield. Hybrid bonding makes the surface specification even tighter.

**FACT:** Applied Materials' 2026 advanced-packaging portfolio includes:

- Nokota VMax 2 ECD for high-uniformity copper plating and TSV/microbump applications;
- Opta Quad CMP for tighter total-thickness variation and hybrid-bond surface control;
- e-beam systems optimized for advanced-packaging defect review;
- Kinex die-to-wafer hybrid bonding.

**FACT:** Besi reported Q2 2026 revenue up 69% year-on-year and orders up 129%, driven particularly by hybrid bonding, photonics and datacenter applications.

### Evidence against the bottleneck thesis

- Hybrid bonding adoption timing remains uncertain.
- TCB/microbump approaches can continue improving for multiple generations.
- Large equipment companies may absorb much of the opportunity without creating extreme revenue sensitivity.

### Current view

**Bottleneck Strength: 4.6/5.** This overlaps with the HBM stacking workstream. Besi and Applied are useful cross-checks; company selection should focus on revenue sensitivity and HBM/AI qualification rather than generic advanced-packaging exposure.

---

## 7. Sub-bottleneck E — OSAT / foundry advanced packaging capacity

### Evidence

**TSMC:** continues to expand CoWoS and 3DFabric capacity and is the benchmark for leading AI accelerator packaging.

**Amkor (AMKR):**

- announced a 10-year advanced-packaging and test partnership with TSMC in June 2026;
- announced a **$1.5 billion multi-year agreement with NVIDIA** in July 2026 to expand advanced packaging capacity and co-develop next-generation packaging/test;
- is expanding a large Arizona advanced-packaging/test campus and reported record Q2 2026 revenue with AI/HPC programs growing.

**ASE (ASX / 3711.TW):**

- is expanding VIPack 2.5D/3D, fan-out and bridge platforms for HBM/AI;
- is building new advanced AI packaging capacity and a panel-level packaging line.

### Evidence against the bottleneck thesis

- OSAT/foundry packaging is capital intensive.
- Large customers have substantial bargaining power and may use prepayments to secure capacity while limiting supplier economics.
- TSMC, ASE, Amkor and Samsung are all expanding, so capacity scarcity can ease.

### Current view

**Bottleneck Strength: 4.5/5; Investment Capture confidence: Medium.** The service layer is critical, but the more asymmetric research candidates may sit in equipment/process control rather than capacity ownership. Amkor is still worth monitoring because direct NVIDIA and TSMC commitments provide unusually strong demand visibility.

---

## 8. Architecture transition — what could remove today's bottleneck?

The critical falsification question is whether alternatives to silicon-interposer CoWoS meaningfully reduce the bottleneck.

### Potential transitions

- CoWoS-S → CoWoS-L/R
- full silicon interposer → silicon bridge
- wafer-level → panel-level fan-out
- organic/glass interposer or advanced substrate
- 2.5D → more 3D/hybrid-bonded integration

### Interpretation

These transitions **reduce particular constraints but create others**. For example, panel-level packaging can improve area utilization but raises panel lithography, distortion and metrology challenges. Organic/glass alternatives reduce silicon-interposer cost but increase substrate/RDL process-control demands. Hybrid bonding reduces bump pitch/stack-height limitations but tightens surface preparation and alignment requirements.

Therefore the most durable supplier thesis is not “owns silicon interposers”; it is “owns a process that remains mandatory as advanced-package area and interconnect density rise.”

---

## 9. Supplier map and research priority

| Layer | Public / notable suppliers | Current view |
|---|---|---|
| Foundry / 2.5D integration | TSMC | Benchmark; strongest ecosystem, but very large company |
| OSAT advanced packaging | ASE, Amkor | Capacity owners; strong demand evidence, capital intensive |
| High-end substrates | Ibiden, Shinko, Unimicron; ABF via Ajinomoto | Structurally important; company economics need validation |
| Inspection / metrology | **Camtek, Onto Innovation**, KLA, Applied Materials | **Highest-priority company hunting ground** |
| CMP / plating / deposition | Applied Materials and peers | Process-critical; large-cap benchmark |
| Hybrid bonding | Besi, Applied, ASMPT, EVG (private) | Strong transition exposure; adoption timing risk |
| Panel-level lithography / metrology | Onto and other specialists | Emerging as package sizes grow |

## 10. Company candidates after Gate A

### Investigating — Camtek

Why: unusually direct 2026 order evidence tied to CoWoS-like AI packaging and HBM/hybrid-bond inspection. The next question is whether this order intensity is sustainable, differentiated and financially material enough to justify valuation.

### Investigating — Onto Innovation

Why: direct HBM4 selection, double-digit tool commitments, and broad exposure to inspection/metrology/lithography across wafer, advanced substrate and panel packaging. Need to quantify advanced-packaging revenue sensitivity, share and competition versus Camtek/KLA/Applied.

### Research queue — Ibiden

Why: high-performance AI/server substrate capacity expansion is explicit and very large. Need to test customer concentration, incremental returns on the ¥500bn investment plan, pricing power and architecture risk.

### Research queue / benchmark — Amkor

Why: $1.5bn NVIDIA agreement plus 10-year TSMC partnership provide strong evidence of capacity demand. Need to determine whether economics justify the capital intensity and whether AI packaging can materially change long-run margins/ROIC.

## 11. Evidence against the overall bottleneck thesis

1. TSMC, ASE, Amkor, Samsung and substrate vendors are investing aggressively; capacity scarcity can normalize.
2. Panel-level packaging and alternative interposers may improve throughput/cost faster than expected.
3. Hyperscalers and accelerator vendors have purchasing power and can fund supplier capacity directly.
4. Process-control tool demand can be cyclical and concentrated around capex ramps.
5. Some suppliers have broad semiconductor exposure, reducing AI-specific earnings asymmetry.

## 12. Thesis breakers / monitoring indicators

- CoWoS/advanced packaging lead times normalize while margins and equipment orders weaken.
- Package architecture shifts reduce inspection/metrology or substrate content per accelerator.
- Camtek/Onto lose HBM/AP qualifications or customers dual-source aggressively.
- Substrate capacity ramps ahead of demand and pricing weakens.
- Large-area panel solutions reach high yield with materially lower equipment intensity.

## 13. Current conclusion

**Advanced packaging is a validated structural bottleneck, but the investment opportunity is more specific than owning packaging capacity.**

The strongest hunting ground is currently **inspection/metrology and process-control equipment**, because package value, area and interconnect density all increase the cost of defects and create more demanding measurement requirements. Camtek and Onto Innovation have the clearest direct 2026 evidence and should be underwritten next.

High-performance substrates are the second priority. Ibiden's very large AI/server substrate investment confirms the demand signal, but we still need to establish economic capture rather than simply capital intensity.

## Sources

- TSMC CoWoS overview: https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm
- TSMC 2026 North America Technology Symposium: https://pr.tsmc.com/english/news/3302
- TSMC advanced packaging services: https://www.tsmc.com/english/dedicatedFoundry/services/advanced-packaging
- ASE VIPack: https://ase.aseglobal.com/VIPack/
- ASE 310 mm × 310 mm panel-level packaging: https://ase.aseglobal.com/press-room/310x310/
- ASE/WUS AI packaging hub: https://www.aseglobal.com/press-room/ase-and-wus-announce-strategic-expansion
- ASE advanced-package substrate discussion: https://ase.aseglobal.com/blog/technology/advanced-packaging-design-for-heterogeneous-integration/
- Amkor Q2 2026 results: https://ir.amkor.com/news-releases/news-release-details/amkor-technology-reports-financial-results-second-quarter-2026
- Amkor/NVIDIA partnership: https://ir.amkor.com/news-releases/news-release-details/amkor-technology-announces-strategic-partnership-nvidia-expand
- TSMC/Amkor partnership: https://ir.amkor.com/news-releases/news-release-details/tsmc-and-amkor-technology-announce-long-term-partnership
- Ibiden FY2026-28 package-substrate investment: https://www.ibiden.com/company/2026/02/notice-regarding-capital-investment-plan-for-high-performance-ic-package-substrates.html
- Shinko i-THOP substrate: https://www.shinko.co.jp/english/product/package/substrate/i-thop.php
- Shinko glass-core substrate: https://www.shinko.co.jp/english/news/2026/07/b2e0e1c9fadd06989a3ba3940788615cdb6ddaf4.php
- Ajinomoto 2026 CEO message / ABF roadmap: https://www.ajinomoto.com/sustainability/ir/ceo_2026.php
- Camtek Hawk AI/HBM order: https://www.camtek.com/news-and-events/camtek-receives-multiple-hawk-systems-order-of-approximately-25-million-from-an-idm-for-ai-applications/
- Camtek CoWoS-like OSAT orders: https://www.camtek.com/news-and-events/camtek-receives-31-million-multi-system-order-from-a-leading-osat/
- Onto Dragonfly G5 HBM4 selection: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System/default.aspx
- Onto panel inspection / Firefly G5: https://ontoinnovation.com/products/firefly-g5/
- Applied 2026 DRAM/advanced packaging systems: https://investors.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and
- Applied advanced-packaging bottlenecks: https://www.appliedmaterials.com/us/en/newsroom/blogs/tackling-key-hbm-and-advanced-packaging-bottlenecks-for-ai-era.html
- Besi Q2/H1 2026 results: https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q2-26-and-h1-26-results/
