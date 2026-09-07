# HBM Stacking, Bonding, Thermal and Yield — Deep Dive

**Status:** Evidence-backed deep dive  
**Confidence:** Medium-High on the bottleneck; Medium on supplier capture  
**Last substantive update:** 2026-09-07  
**Backlog:** closes issue #9 when merged

## Executive conclusion

**FACT:** HBM is moving from 8/12-high stacks toward 16-high products, while transfer rates and thermal density continue to rise. SK hynix, Samsung and Micron have all disclosed 16-high HBM4 products or samples in 2026. Samsung has also publicly positioned hybrid copper bonding for next-generation HBM with 16 or more layers.

**INTERPRETATION:** The structural bottleneck is not simply “stacking more DRAM dies.” The hard part is preserving **yield, flatness, alignment, interconnect quality and heat removal while the dies become thinner and the interconnect pitch becomes finer**. These constraints reinforce one another: thinner dies warp more easily; tighter gaps and finer pitch increase bonding sensitivity; more interfaces trap heat; and a defect late in the stack destroys more accumulated value.

**CONCLUSION:** HBM stacking / bonding / thermal / yield passes Gate A as a structural bottleneck with a **Bottleneck Strength Score of 4.6/5**. The highest-confidence sub-bottlenecks are:

1. **Die bonding / stacking process control** — current TCB/MR-MUF/TC-NCF and the transition toward hybrid bonding.
2. **Wafer thinning + temporary bonding/debonding** — required because higher stacks force thinner dies while breakage and warpage risk increase.
3. **Underfill / molding / warpage-control materials** — mechanically and thermally critical, but supplier-level economics are less transparent.
4. **Surface preparation, cleaning, alignment and metrology for hybrid bonding** — likely to become more important as the industry moves beyond micro-bump-based stacking.

The investment opportunity is therefore likely to sit in **process equipment and qualified materials**, but the technology transition creates a major trap: the supplier that wins TCB today is not automatically the supplier that wins hybrid bonding tomorrow.

## 1. Bottleneck Strength Score

| Dimension | Score | Evidence / rationale |
|---|---:|---|
| Physical difficulty | **5/5** | SK hynix disclosed that 12-layer HBM required DRAM dies around 40% thinner than its 8-layer product and that warpage became a major issue; Samsung identifies die warping, voids, temperature/pressure control and shrinking gaps as high-stack challenges; technical literature finds thermal resistance worsening beyond 12 layers. |
| Supply elasticity | **4/5** | HBM-specific bonding and temporary-bonding equipment requires qualification and customer process tuning. SK hynix has continued placing dedicated HBM4 TC-bonder orders; SUSS reports strong HBM-driven temporary-bonding/debonding orders. Capacity can be added, but not instantaneously. |
| Supplier concentration | **4/5** | Current TCB is concentrated among a small set of suppliers; Hanmi has a particularly strong SK hynix position. SUSS says it supplies temporary bonding/debonding to two of the three HBM IDMs. Hybrid bonding also has a relatively limited specialist equipment set (Besi, EVG, ASMPT, SUSS and others). |
| Qualification / switching | **5/5** | Bonding, thinning and materials directly affect yield and reliability. ASMPT disclosures describe HBM tools being installed and qualified for specific HBM generations/customers; HBM IDMs use materially different stacking architectures, making process qualification customer-specific. |
| System criticality | **5/5** | A stack cannot ship if bonding, warpage, thermal or interconnect yield fails. Failures later in assembly destroy the value of multiple otherwise-good dies. |
| **Average** | **4.6/5** | **Gate A passed.** |

## 2. Process map

The relevant process is simplified below. Exact flows differ by manufacturer and product generation.

```text
DRAM wafer / base-die fabrication
        ↓
TSV formation + backside process
        ↓
Temporary wafer-to-carrier bonding
        ↓
Wafer thinning / grinding / polishing
        ↓
Dicing / singulation + known-good-die screening
        ↓
High-precision die placement / stacking
        ↓
Electrical/mechanical bonding
  ├─ TCB + NCF (e.g. Samsung current high-stack approach)
  ├─ Mass reflow + molded underfill (SK hynix MR-MUF family)
  └─ Hybrid Cu/dielectric bonding (future / emerging HBM route)
        ↓
Underfill / molding / warpage stabilization
        ↓
Stack test / reliability
        ↓
Integration with accelerator package
```

The process should not be viewed as independent steps. Thinning determines warpage; warpage affects placement and bonding; bonding material and interconnect geometry affect thermal resistance; thermal stress affects reliability and yield.

---

## 3. Sub-bottleneck A — wafer thinning and temporary bonding/debonding

### What becomes harder

**FACT:** SK hynix says the DRAM dies used in its 12-layer HBM3 had to be roughly **40% thinner** than the dies in its 8-layer HBM3 to preserve the overall package-height specification. It identifies warpage as a major problem that had to be addressed with Advanced MR-MUF and chip-control technology.

**FACT:** DISCO sells equipment designed to process ultra-thin wafers below 25 μm and, in newer systems, wafers at 15 μm or below. Its technical materials explicitly map thinning and singulation steps to HBM. DISCO also notes that as memory packages become denser, wafer thinning and thickness control become increasingly important.

**FACT:** SUSS describes temporary bonding/debonding as a key enabler for wafer thinning and explicitly cites HBM as a major application. At its 2025 Capital Markets Day it described itself as the market leader in temporary bonding/debonding, supplying **two of the three HBM IDMs**. In Q1 2026 it said order intake for bonding tools tied to HBM-customer capacity expansion was already significantly higher than in the entire first half of 2025.

### Why temporary bonding matters

An ultra-thin device wafer is mechanically fragile. It is temporarily attached to a carrier so it can survive grinding, polishing, backside processing and subsequent handling. The harder the industry pushes thickness down, the more valuable controlled bonding/debonding, low total-thickness variation, particle control and clean release become.

### Evidence against the bottleneck thesis

- Thinning itself is not new; memory and image-sensor supply chains have decades of experience with thin wafers.
- Multiple suppliers can provide grinding, dicing and temporary-bonding solutions.
- Higher HBM capacity can also be achieved through higher DRAM density, reducing pressure to increase layer count indefinitely.
- If HBM package-height specifications loosen or package architectures change, extreme thinning pressure could ease.

### Current view

**Bottleneck Strength: 4.2/5.** The physical problem is structural, and SUSS's disclosed HBM penetration is notable. However, this workstream must distinguish **process criticality** from **supplier pricing power**. DISCO and SUSS deserve company-level research; EV Group is an important private benchmark.

---

## 4. Sub-bottleneck B — TCB, die placement and current-generation stacking

### Current process diversity matters

The three major HBM manufacturers do not use one identical stacking flow.

**SK hynix:** Uses the MR-MUF family. Its process connects stacked chips using mass reflow and then fills the gaps using liquid epoxy molding compound. SK hynix says Advanced MR-MUF adds chip-control technology and improved protective materials to manage warpage and heat. It continues to use Advanced MR-MUF in HBM4E disclosed in 2026.

**Samsung:** Uses Advanced TC-NCF in its high-stack HBM products. Samsung says precise temperature/pressure control and improved NCF material reduce voids, contamination and defects. Its HBM3E 12H uses a 7 μm chip-to-chip gap and varied bump sizes to improve both signal connectivity and heat dissipation.

**Micron:** Public disclosures confirm 12-high HBM4 volume production and 16-high HBM4 samples, but Micron does not publicly specify a single current bonding architecture in the sources reviewed. Its packaging hiring materials explicitly reference TCB, wafer support/thinning and hybrid bonding as relevant advanced-packaging capabilities.

### Why TCB is difficult

TCB must simultaneously control:

- placement accuracy;
- force;
- temperature;
- oxide/contamination at the bonding surface;
- bump collapse and joint quality;
- inter-die spacing;
- wafer/die warpage;
- throughput.

These requirements become harder as the pitch shrinks and the number of interfaces rises.

### Supplier evidence

**Hanmi Semiconductor (042700.KS):**

- Regulatory-filing-based reporting shows SK hynix placed a KRW 44.2 billion HBM4 TC-bonder order with Hanmi in June 2026, approximately 7.7% of Hanmi's 2025 revenue.
- TechInsights data reported in Korean press put Hanmi at 71.2% of the global HBM TC-bonder market through Q3 2025.
- Hanmi has historically been tightly linked to SK hynix HBM production.

**ASMPT (0522.HK):**

- ASMPT reported TCB orders from multiple HBM players.
- It installed a bulk HBM3E 12H TCB order for a leading HBM customer and reported another HBM customer entering low-volume HBM4 12H manufacturing with ASMPT tools.
- Its AOR TCB technology is designed to remove oxide without flux, reducing contamination and supporting finer-pitch HBM bonding.
- Advanced-packaging demand has materially lifted orders and revenue.

### Evidence against the bottleneck thesis

- Hanmi's dependence on specific customer capex schedules can create sharp order volatility.
- Competition is increasing from Hanwha Semitech, ASMPT and other equipment makers.
- The largest risk is **technology substitution**: if high-volume HBM shifts from micro-bump/TCB toward hybrid bonding, the economics of today's TCB installed base may not carry forward automatically.
- Memory IDMs may internalize more assembly equipment/process know-how or dual-source aggressively to reduce supplier leverage.

### Current view

**Bottleneck Strength: 4.8/5 today.** Current HBM stacking has strong technical difficulty, customer-specific qualification and limited high-volume suppliers.

**Investment implication:** Hanmi has the strongest visible direct revenue sensitivity, while ASMPT appears better diversified across customers and bonding architectures. Hanmi is therefore potentially more asymmetric but also more exposed to generational and technology-transition risk.

---

## 5. Sub-bottleneck C — MR-MUF / TC-NCF / underfill, molding and warpage-control materials

### Why the material layer matters

**FACT:** SK hynix attributes a large part of its HBM stacking progress to new material development. It says the EMC used in Advanced MR-MUF improved heat-dissipation characteristics by **1.6×** versus the earlier MR-MUF material while helping address warpage in thinner dies.

**FACT:** Samsung says Advanced TC-NCF reduces voids and contamination and supports a 7 μm inter-chip gap in 12-layer HBM3E. It also uses an outer epoxy molding compound with high thermal conductivity.

The material must do several jobs simultaneously:

- electrically insulate;
- fill very small gaps without voids;
- mechanically stabilize a multi-die stack;
- tolerate repeated thermal cycling;
- manage coefficient-of-thermal-expansion mismatch;
- conduct enough heat to prevent the interfaces becoming thermal barriers;
- avoid inducing excessive warpage or stress.

### Supplier universe

**Sumitomo Bakelite (4203.T):** its 2026 investor materials explicitly list **HBM sealing materials (liquid, granular and MUF)** and high-thermal-conductivity TIM materials in its advanced-package portfolio.

**Kyocera:** markets mold-underfill EMC for flip-chip packaging, but the reviewed public source does not establish a named HBM customer.

**Shin-Etsu Chemical:** identifies temporary-bond/debond materials and thermal-interface materials as part of its AI-semiconductor materials portfolio, including HBM-related manufacturing support; direct HBM-stack customer penetration remains to be established.

### Evidence against the bottleneck thesis

- Public disclosure of actual HBM material share and customer qualification is sparse.
- The underlying chemistries may have several capable Japanese/Korean suppliers, limiting pricing power.
- IDMs co-develop materials and may capture much of the IP/process advantage internally.
- A shift to hybrid bonding changes the material stack and could reduce the role of some underfill approaches.

### Current view

**Bottleneck Strength: 4.1/5; Investment Capture confidence: Low.** The material problem is clearly structural, but we do not yet know which independent supplier owns the critical formulation or whether margins/revenue sensitivity are large enough to matter. This is a **supplier-discovery priority**, not yet a company thesis.

---

## 6. Sub-bottleneck D — thermal management inside the HBM stack

### Evidence the problem is worsening

**FACT:** SK hynix states that heat management has become a critical challenge as HBM stacking and speeds rise. Its 2026 iHBM concept embeds Integrated Cooling Elements inside the package and claims a **30% reduction in thermal resistance** while preserving compatibility with its MR-MUF process.

**FACT:** SK hynix's 12-layer HBM4E uses Advanced MR-MUF that the company says reduces heat resistance by **17%**.

**FACT:** Samsung says its hybrid copper bonding technology for next-generation HBM with 16 or more layers can reduce heat resistance by **more than 20%** compared with thermal compression bonding.

**TECHNICAL LITERATURE:** A 2025 review of thermal issues in 3D HBM reports that internal thermal resistance rises sharply beyond 12 layers and summarizes hybrid-bonding studies showing materially lower inter-layer thermal resistance and reduced stack height.

### Evidence against the bottleneck thesis

- Thermal problems can be attacked at several levels: memory package, interposer, cold plate, liquid cooling, package materials and system architecture. No single supplier necessarily owns the solution.
- HBM vendors are themselves innovating in package-internal cooling and material design.
- Better process nodes and lower-voltage operation may offset some heat-density growth.

### Current view

**Bottleneck Strength: 4.4/5; standalone supplier capture uncertain.** Thermal is a genuine physical limit, but the investment opportunity may be distributed across materials, package design and datacenter cooling. The most compelling thermal candidates are likely those whose materials/processes are *qualified inside the HBM stack*, not generic cooling vendors.

---

## 7. Sub-bottleneck E — hybrid bonding: the likely transition point

### Why hybrid bonding matters

Conventional HBM stacking relies on solder/micro-bump-style interconnects plus underfill/molding. As pitch shrinks and layer counts rise, bumps consume vertical space and add thermal/electrical resistance.

**FACT:** Samsung demonstrated hybrid copper bonding in 2026 specifically as a technology intended to enable **16 or more HBM layers** while reducing thermal resistance versus TCB.

**TECHNICAL LITERATURE:** IEEE work on die-to-wafer hybrid bonding identifies surface pretreatment, contamination, void-free bonding and high-precision placement as key challenges for HBM stacks above 16 layers. Imec has demonstrated wafer-to-wafer hybrid bonding at sub-micron pitch, showing the technology path exists but also emphasizing the precision required.

### What gets harder in hybrid bonding

Hybrid bonding removes some bump/underfill limitations but creates new bottlenecks:

- extremely flat and clean bonding surfaces;
- very tight overlay accuracy;
- copper/dielectric surface preparation;
- particle control — a small particle can create a void across the bonded interface;
- defect inspection after bonding;
- die-to-wafer handling of known-good die;
- throughput at production yield.

This means the bottleneck does not disappear; **it migrates from pressure/temperature/bump control toward surface preparation, alignment, contamination control and metrology.**

### Supplier universe

**Besi (BESI.AS):** a leading public hybrid-bonding equipment vendor. It reports strong growth in hybrid bonding and explicitly identifies new use cases in memory. HBM-specific mass-production penetration still requires validation.

**EV Group (private):** provides wafer-to-wafer and die-to-wafer hybrid-bonding process equipment, including cleaning, surface activation and overlay metrology, and explicitly positions these for HBM stacks.

**ASMPT:** has both current TCB exposure and hybrid-bonding solutions, potentially allowing it to bridge generations.

**SUSS (SMHN.DE):** current strength is temporary bonding/debonding; it describes hybrid bonding as an emerging growth area and itself as a follower today, with HBM as a target application.

**SCREEN (7735.T):** argues that hybrid bonding and increasing HBM stack counts increase cleaning opportunities because particles create bonding voids. It has also expanded wafer-bonding R&D capability.

### Evidence against the bottleneck thesis

- Hybrid bonding may take longer than expected to reach high-volume HBM production.
- Wafer-to-wafer hybrid bonding can suffer yield penalties when individual die yield is imperfect; die-to-wafer solves some issues but is slower/more complex.
- Incumbent HBM vendors may continue improving TCB/MR-MUF/TC-NCF enough to delay the transition.
- Equipment competition is broadening rapidly; no durable winner is proven yet.

### Current view

**Future Bottleneck Strength: 4.7/5; Current investability confidence: Medium-Low.** Hybrid bonding appears likely to *move* rather than remove the bottleneck. We should research companies that have exposure to both the current architecture and the transition, or that own surface-prep/metrology steps independent of which bonder wins.

---

## 8. Supplier map

| Supplier | Public? / ticker | Relevant step | Evidence today | Transition positioning | Current research view |
|---|---|---|---|---|---|
| **Hanmi Semiconductor** | Yes — 042700.KS | HBM TC bonding | Direct HBM4 orders from SK hynix; reported dominant HBM TCB share | Developing hybrid bonders; transition is the core risk | **Deep dive now** — highest direct current HBM leverage, highest transition risk |
| **SUSS** | Yes — SMHN.DE | Temporary bonding/debonding, surface prep; emerging hybrid | Says it supplies 2 of 3 HBM IDMs; HBM-driven bonding orders rose sharply in 2026 | Has hybrid-bonding roadmap but calls itself a follower | **Deep dive now** — unusually interesting bridge across thinning + future hybrid |
| **ASMPT** | Yes — 0522.HK | TCB, mass reflow, hybrid bonding | Multiple HBM customers; HBM3E/HBM4 production evidence | Strongest cross-architecture portfolio among current public suppliers | **Investigate** — diversified, less pure-play but technically well positioned |
| **DISCO** | Yes — 6146.T | Grinding, thinning, polishing, dicing | Explicit HBM process use; ultra-thin wafer tools and consumables | Likely remains relevant under both TCB and hybrid | **Benchmark / investigate after wafer-processing workstream** |
| **Besi** | Yes — BESI.AS | Hybrid bonding | Strong hybrid-bonding commercial momentum; memory use cases | Strong future architecture exposure | **Research queue** — HBM production adoption not yet proven |
| **SCREEN Holdings** | Yes — 7735.T | Cleaning, surface prep, bonding R&D | Identifies rising HBM/hybrid-bond cleaning opportunity | Likely benefits as surface cleanliness becomes more critical | **Research queue** |
| **Sumitomo Bakelite** | Yes — 4203.T | MUF/encapsulation/TIM materials | Explicit HBM sealing and thermal material portfolio | Material demand persists but formulations may shift | **Research queue** — qualification/share opaque |
| **EV Group** | Private | Temporary/hybrid bonding, activation, metrology | Explicit HBM die-to-wafer/wafer-to-wafer solutions | Strong future hybrid position | **Private benchmark** |
| **Shin-Etsu Chemical** | Yes — 4063.T | TBDB and TIM materials | Broad AI/HBM-related materials exposure | Likely process-agnostic materials exposure | **Low-priority candidate until HBM revenue sensitivity is quantified** |

## 9. The most important investment distinction

There are three different ways to be exposed to this bottleneck:

### A. Current-generation pure leverage

**Example: Hanmi Semiconductor.**

Advantage: HBM capex flows directly into bonder orders, and current customer qualification/installed base can create strong economics.

Risk: if the process architecture moves, the same installed base can become less valuable. A high current market share is not automatically a durable moat across hybrid bonding.

### B. Process-agnostic enabling layer

**Example: DISCO; potentially SUSS temporary bonding/debonding.**

Advantage: thinning, handling and some surface-prep steps remain necessary even if the exact final bond changes.

Risk: the process may be critical but highly competitive, limiting pricing power.

### C. Transition option

**Examples: Besi, EVG, ASMPT, SUSS hybrid bonding.**

Advantage: if HBM moves to hybrid bonding, tool intensity and qualification could create a new high-value market.

Risk: timing and winner are uncertain; current revenue may be small and expectations may already be high.

**INTERPRETATION:** The best asymmetric opportunity may be a supplier that combines **current HBM revenue with credible hybrid-bonding transition exposure**, rather than the company with the single highest current TCB share.

This is why SUSS and ASMPT are strategically interesting even though Hanmi has stronger pure HBM TCB exposure today.

---

## 10. Evidence against the overall bottleneck thesis

The following could materially weaken this thesis:

1. **16-high does not become mainstream.** Higher-density DRAM could deliver capacity without continuously increasing stack count.
2. **HBM package-height rules relax.** That would reduce wafer-thinning pressure.
3. **TCB improves faster than expected.** Advanced MR-MUF/TC-NCF could defer hybrid bonding for several generations.
4. **Hybrid bonding commoditizes.** Multiple tool vendors may qualify quickly, eroding supplier margins.
5. **IDMs vertically integrate.** SK hynix, Samsung or Micron may internalize more of the critical process/tool know-how and dual-source aggressively.
6. **Thermal bottlenecks move outside the memory stack.** Better package/system cooling could reduce the value of specialized HBM-internal materials.
7. **HBM demand growth slows.** Even a structural process bottleneck can lose investment relevance if accelerator/HBM capacity overshoots demand.

None of these currently eliminates the bottleneck, but they matter for supplier-level underwriting.

---

## 11. Technology trajectory

| Generation / architecture | Dominant problem | Likely supplier value pool |
|---|---|---|
| 8-high HBM3/HBM3E | basic stack yield, bandwidth, package thermal | TCB/mass reflow, TSV, test |
| 12-high HBM3E/HBM4 | much thinner dies, warpage, voids, tighter gaps, thermal resistance | temporary bonding, precision thinning, high-end TCB/MR-MUF/TC-NCF, EMC/NCF, test |
| 16-high HBM4/HBM4E | further height/yield/thermal pressure | same as above with higher process intensity; stronger case for hybrid bonding |
| 16+ / future custom HBM | finer pitch, lower interconnect resistance, greater logic-memory integration | hybrid bonding, cleaning/surface activation, overlay metrology, advanced inspection, known-good-die handling |

**Key insight:** The constraint is likely to migrate, not disappear. The durable research question is therefore: **which supplier owns a critical step across architectures, or can successfully cross the transition?**

---

## 12. Recommended company work

### Immediate company deep dives

1. **SUSS** — because it has disclosed current HBM penetration in temporary bonding/debonding and a hybrid-bonding roadmap. This may provide exposure on both sides of the technology transition.
2. **Hanmi Semiconductor** — because it has the highest visible current HBM TCB sensitivity and strong customer evidence, but also the clearest hybrid-transition risk.
3. **ASMPT** — because it has production evidence with multiple HBM customers and capabilities spanning TCB, mass reflow and hybrid bonding.

### Follow after adjacent workstreams

4. **DISCO** — after issue #12 validates whether thinning/dicing is economically concentrated enough.
5. **Besi** — when HBM hybrid-bonding production adoption can be demonstrated rather than inferred from general hybrid-bonding growth.
6. **Sumitomo Bakelite / other advanced materials suppliers** — after named HBM qualification/share can be triangulated.

---

## 13. Open questions

1. Which two HBM IDMs are SUSS's current temporary-bonding/debonding customers, and how much of SUSS Bonding revenue is HBM-related?
2. How long does it take a memory IDM to qualify a new TC bonder, temporary-bonding flow or molding material?
3. What percentage of Hanmi revenue is now HBM TCB, and how concentrated is revenue in SK hynix?
4. Which hybrid-bonding tool vendors are already in HBM pilot lines versus logic-only pilot lines?
5. Does die-to-wafer hybrid bonding or wafer-to-wafer hybrid bonding win for HBM, and how does that choice change the equipment list?
6. Which EMC/NCF/MUF material suppliers are qualified at SK hynix, Samsung and Micron?
7. How much does equipment content per HBM stack increase moving from 12-high to 16-high?
8. Can the memory IDMs expand bonding capacity faster than HBM demand, turning today's constraint into ordinary capex exposure?

---

## 14. Thesis breakers / monitoring indicators

Monitor:

- 16-high HBM shipment adoption versus 12-high;
- customer qualification announcements for hybrid-bond HBM;
- HBM TCB order growth and supplier diversification;
- SUSS HBM bonding order intake and customer expansion;
- Hanmi hybrid-bonder qualification / customer wins;
- Besi/ASMPT/EVG HBM-specific hybrid-bonding orders;
- material supplier HBM qualification disclosures;
- evidence that package-height constraints are changing;
- HBM yield commentary from SK hynix, Samsung and Micron.

The thesis should be downgraded if 16-high adoption stalls, hybrid bonding is delayed without increasing current-process intensity, or supplier concentration falls materially without offsetting growth in tool/material content.

---

## 15. Source register for this deep dive

### Memory-vendor primary sources

- **SRC-HBM-001 — SK hynix, MR-MUF development / heat control (2024):** https://news.skhynix.com/en/rulebreaker-revolutions-mr-muf-unlocks-hbm-heat-control/
- **SRC-HBM-002 — SK hynix, HBM4 production readiness / Advanced MR-MUF (2025):** https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/
- **SRC-HBM-003 — SK hynix, iHBM thermal solution (2026):** https://news.skhynix.com/en/ihbm-solution/
- **SRC-HBM-004 — SK hynix, HBM4E / Advanced MR-MUF (2026):** https://news.skhynix.com/en/sk-hynix-ships-samples-of-12-layer-next-gen-hbm4e-2/
- **SRC-HBM-005 — SK hynix, 16-layer HBM4 at CES 2026:** https://news.skhynix.com/en/sk-hynix-showcases-next-generation-ai-memory-innovations-at-ces-2026/
- **SRC-HBM-006 — Samsung, HBM3E 12H Advanced TC-NCF (2024):** https://news.samsung.com/global/samsung-develops-industry-first-36gb-hbm3e-12h-dram
- **SRC-HBM-007 — Samsung, HBM4 / HBM4E and hybrid copper bonding (2026):** https://news.samsung.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026
- **SRC-HBM-008 — Micron, HBM4 12H volume + 16H samples (2026):** https://stage-investors.micron.com/news/press-release/2026/Micron-in-High-Volume-Production-of-HBM4-Designed-for-NVIDIA-Vera-Rubin-PCIe-Gen6-SSD-and-SOCAMM2-03-16-2026/default.aspx

### Equipment/material primary sources

- **SRC-HBM-009 — SUSS CMD 2025, temporary/hybrid bonding:** https://www.suss.com/en/content/download/3012/42416?version=4
- **SRC-HBM-010 — SUSS Q1 2026 interim statement:** https://www.suss.com/en/content/download/3330/53284?version=3
- **SRC-HBM-011 — SUSS H1 2026 results / record order book:** https://www.suss.com/tw/news/corporate-news/2026/order-book-reaches-record-of-473.7-million-providing-strong-visibility-for-2027
- **SRC-HBM-012 — ASMPT H1 2025 HBM/TCB production evidence:** https://www.asmpt.com/site/assets/files/81364/e0522_results_announcement_2025_q2.pdf
- **SRC-HBM-013 — ASMPT AOR TCB HBM technology (2026):** https://semi.asmpt.com/en/news-center/press-releases/thermocompression-bonding-with-active-oxide-removal/
- **SRC-HBM-014 — DISCO 2025 technology briefing, HBM process map:** https://www.disco.co.jp/jp/ir/movie/doc/E_Tech_Briefing_2025.pdf
- **SRC-HBM-015 — DISCO ultra-thin wafer processing:** https://www-hq.disco.co.jp/eg/products/mounter/dmm9200.html
- **SRC-HBM-016 — EV Group HBM hybrid bonding / metrology (2026):** https://www.evgroup.com/fileadmin/media/company/news/2026/2026_02_04_SEMICON_KOREA/2026_02_04_SEMICON_Korea_2026_Round-up_EN.pdf
- **SRC-HBM-017 — Besi hybrid bonding:** https://www.besi.com/products-technology/productgroup/hybrid-bonding/
- **SRC-HBM-018 — Sumitomo Bakelite FY2025 presentation, HBM encapsulation / TIM:** https://www.sumibe.co.jp/ir/library/presentation/files/2026/0511_04.pdf
- **SRC-HBM-019 — SCREEN IR Day, HBM hybrid-bond cleaning opportunity:** https://hdjp-corporateweb-files.screen.co.jp/1617/2734/5775/20240919_Mtg_E.pdf

### Technical / independent sources

- **SRC-HBM-020 — IEEE ECTC, die-to-wafer hybrid-bonding challenges for >16-layer HBM:** https://ieeexplore.ieee.org/document/10565165/
- **SRC-HBM-021 — Imec 2025, wafer-to-wafer hybrid bonding at 300 nm pitch:** https://imec-publications.be/entities/publication/6228fcc8-685e-4e72-83ba-3cb478415500
- **SRC-HBM-022 — 2025 thermal review of hybrid-bonded 3D HBM:** https://www.mdpi.com/2079-9292/14/13/2682
- **SRC-HBM-023 — Yonhap, Hanmi HBM4 TC-bonder order based on regulatory filing (2026):** https://en.yna.co.kr/view/AEN20260608012500320
- **SRC-HBM-024 — Chosun / TechInsights, HBM TC-bonder market share (2025):** https://www.chosun.com/english/industry-en/2025/12/22/CI5ZPGQ2JJFQHHJPM2DTXWNKRY/

## Bottom line

The HBM stacking bottleneck is **validated**. The core physics gets harder with more layers, and the industry is already responding with thinner dies, more sophisticated bonding/molding, new thermal paths and a likely transition toward hybrid copper bonding.

The first supplier-level takeaway is not “buy the largest current bonder vendor.” It is:

> **Find the supplier whose critical process remains necessary as HBM moves from thin-die TCB/MR-MUF/TC-NCF toward hybrid bonding, or whose installed qualification is valuable enough to survive the transition.**

On the evidence available today, **SUSS and Hanmi Semiconductor deserve immediate company deep dives**, with **ASMPT** as the best diversified cross-architecture benchmark and **Besi/EVG** as key hybrid-bonding transition references.
