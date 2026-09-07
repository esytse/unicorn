# AI Energy / Power Delivery — End-to-End Value Chain

**Status:** Initial evidence-backed map  
**Confidence:** Medium overall; higher on grid/transformer constraints, lower on emerging 800 VDC supplier capture  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #34

## Purpose

Map the full physical and control path from primary energy to AI compute, then distinguish:

- where demand is structurally increasing;
- where supply is slow or difficult to expand;
- where qualification / engineering / regulation creates switching costs;
- where the bottleneck may migrate as architecture changes;
- where attractive economics might accrue to suppliers.

This is a **value-chain / bottleneck map**, not a company recommendation list.

---

## 1. System map

```text
AI / data-centre demand signal
        ↓
Site selection + power rights + utility / PPA contracting
        ↓
Primary energy / fuels
(gas, uranium, wind, solar, hydro, coal where relevant)
        ↓
Utility-scale generation
(gas / nuclear / renewable / hydro / other)
        ↓
Generation equipment
(turbines, generators, inverters, balance of plant)
        ↓
Bulk transmission
(lines, substations, HV equipment, protection / control)
        ↓
Large-load interconnection / grid studies / permitting
        ↓
Substation transformation + switching
(LPTs, distribution transformers, switchgear, breakers, relays)
        ↓
Distribution to data-centre site
        ↓
Behind-the-meter power layer
(onsite generation + microgrid + BESS + UPS + controls)
        ↓
Data-centre electrical backbone
(MV/LV switchgear, transformers, UPS, PDUs, busway)
        ↓
Facility / row power conversion
(AC architecture → hybrid AC/DC → 800 VDC)
        ↓
Rack-level distribution / conversion
(busbars, power shelves, DC/DC, protection, power semiconductors)
        ↓
AI compute
```

Two cross-cutting loops sit around this chain:

- **thermal / cooling** determines how much electrical load can actually be converted into usable compute;
- **load flexibility / energy management** can reduce upstream grid and generation requirements by smoothing or shifting demand.

---

## 2. Demand signal: AI factories / high-density data centres

**FACT:** The IEA's 2026 update projects data-centre electricity use rising from about **485 TWh in 2025 to ~950 TWh in 2030**. AI-focused facilities grow much faster than the total.

**FACT:** The same IEA work says server-rack power density increased approximately **11x between 2020 and 2025** and could rise a further **4x by 2027**.

**INTERPRETATION:** The energy opportunity is driven by two separate quantities:

1. **more total MW / TWh**;
2. **more MW per site and kW per rack**.

The second is strategically important because it stresses equipment, voltage architecture, protection, copper, cooling and grid connection even if aggregate electricity supply is sufficient.

### Bottleneck strength: demand itself — not scored

Demand is the forcing function, not an investable bottleneck.

---

## 3. Site selection, power rights and commercial access

### What sits here

- land with proximity to transmission / substations;
- utility service agreements;
- interconnection deposits / studies;
- PPAs / generation contracts;
- water / cooling access where relevant;
- permitting and local planning.

**FACT:** IEA notes that data-centre demand is geographically concentrated and that around **20% of planned projects may face delays** if grid-integration risks are not addressed.

**INTERPRETATION:** A site with **credible near-term deliverable power** is economically different from land with an announced but uncertain utility allocation.

### Preliminary Bottleneck Strength: **4.5 / 5**

**Drivers:** location specificity, long planning cycles, transmission constraints, regulatory process.

**Counterpoint:** data centres can relocate more easily than many industrial plants, and flexible / co-located arrangements can reduce the constraint.

---

## 4. Primary energy / fuel supply

### Natural gas

Relevant for utility-scale CCGT / simple-cycle generation and onsite turbines / reciprocating generation.

### Nuclear fuel

Relevant to conventional nuclear and future SMR deployment.

### Renewables resource

Wind / solar / hydro supply low-marginal-cost energy but require grid, storage or complementary firm capacity for 24/7 power requirements.

### Preliminary Bottleneck Strength: **3.0 / 5 globally; highly regional**

**INTERPRETATION:** AI is unlikely to create a universal scarcity of fuel molecules or renewable resource. The stronger constraint is usually turning energy into **firm, permitted and connected electrical capacity at the right site**.

**Exception:** local pipeline capacity, gas interconnection, water availability or fuel logistics can become site-specific constraints.

---

## 5. Utility-scale generation

### Technologies

- natural-gas combined-cycle and simple-cycle plants;
- nuclear;
- solar / wind + storage;
- hydro;
- coal in grids where it remains part of the physical supply mix;
- geothermal / other emerging firm clean generation.

**FACT:** IEA projects renewables meeting nearly half of incremental global data-centre electricity demand through 2030, while natural gas and coal together remain material near-term contributors; nuclear becomes more important later in the decade and beyond.

### Preliminary Bottleneck Strength: **3.6 / 5**

**Why not higher:** electricity can be generated through multiple technologies and generation capacity can move across a regional grid.

**Why it still matters:** the constraint becomes stronger when the requirement is **new firm capacity on a short timetable** rather than annual energy volume.

**OPEN QUESTION:** does generation become the binding constraint in specific US power markets after existing spare capacity is exhausted, or do transmission/interconnection and equipment remain more restrictive?

---

## 6. Generation equipment: turbines, generators, inverters and balance of plant

### Gas turbines

**FACT:** GE Vernova reported **116 GW** of gas-power equipment backlog and slot reservations at Q2 2026 and expects at least 125 GW by year-end; it is expanding annual gas-turbine output from 20 GW in 2026 toward 30 GW by 2030.

**INTERPRETATION:** This is direct evidence that dispatchable-generation equipment is capacity constrained enough to require multi-year manufacturing expansion.

### Reciprocating / standby generation

Data-centre demand is also increasing sales of large generator sets and distributed power systems. Cummins reported higher 2026 power-generation demand particularly in North American data-centre applications.

### Renewable inverters

Critical to renewable / BESS integration but with a broader supplier base and faster capacity expansion than large turbines.

### Preliminary Bottleneck Strength: **4.4 / 5 for large gas-turbine slots; 3.5 / 5 for gensets; 3.1 / 5 for mainstream renewable inverters**

**Structural elements:** long-cycle manufacturing, hot-section metallurgy, qualification, installed-base service, limited large-turbine OEM base.

**Falsification:** manufacturing expansions by GE Vernova, Siemens Energy and others could materially reduce lead times by the end of the decade.

**Reference suppliers for later underwriting:** GE Vernova, Siemens Energy, Mitsubishi Heavy Industries; Caterpillar / Cummins for distributed and backup generation.

---

## 7. Bulk transmission

### What sits here

- high-voltage AC / DC lines;
- conductors / towers;
- substations;
- breakers / protection / control;
- FACTS / power-quality systems;
- grid engineering and construction.

### Preliminary Bottleneck Strength: **4.7 / 5**

**Drivers:** permitting, rights-of-way, regulatory approvals, long project cycles, transformer / switchgear dependencies and regional planning.

**INTERPRETATION:** Transmission is one reason **aggregate generation** and **deliverable power** are not the same asset.

**Counterpoint:** data centres can partially bypass network expansion through co-location, flexible load, onsite generation and siting closer to available capacity.

---

## 8. Large-load interconnection / grid studies / tariffs

This is partly a regulatory / process layer rather than a manufactured product, but it determines speed-to-power.

**FACT:** In June 2026 FERC ordered all six US RTOs / ISOs under its jurisdiction to justify or reform rules for connecting data centres and other large loads, explicitly focusing on transmission-service applications, co-location, flexible load and nearby generation.

**FACT:** FERC defines the policy problem broadly around large loads exceeding roughly **20 MW**.

### Preliminary Bottleneck Strength: **4.8 / 5 — highest current system bottleneck**

**Why:** site-specific network studies, generation adequacy, transmission upgrades, tariff uncertainty and cost allocation can delay otherwise buildable projects.

**INTERPRETATION:** This layer can create value for equipment and onsite-power suppliers because the economic premium shifts toward solutions that shorten **time-to-energisation**.

**Falsification:** successful 2026–27 tariff reform plus load flexibility could materially reduce the bottleneck, potentially shifting scarcity downstream to equipment manufacturing.

---

## 9. Transformers, substations and high-/medium-voltage equipment

### Large power transformers (LPTs)

Step voltage up/down across generation, transmission and large substations.

### Distribution / medium-voltage transformers

Step power toward facility-level voltage.

### Switchgear, breakers, relays, protection

Safely isolate faults and route power at high / medium / low voltage.

**FACT:** US DOE reported distribution-transformer demand up **41% since 2019**; lead times increased from roughly 3–6 months in 2019 to **1–2 years or longer** by 2024, while large transformers could take **3–4 years**.

**FACT:** DOE also identifies product fragmentation — tens of thousands of utility transformer variants — as one reason production is difficult to standardise.

### Preliminary Bottleneck Strength

- **Large / distribution transformers: 4.8 / 5**
- **MV/HV switchgear and breakers: 4.5 / 5**
- **protection / control: 3.8 / 5**

**Structural elements:** custom engineering, electrical-steel / copper inputs, factory test, utility qualification, transport, safety / reliability requirements and installed manufacturing footprint.

**Architecture resilience:** very high. Even if data centres shift toward onsite generation or 800 VDC internally, medium-/high-voltage transformation and protection remain necessary somewhere in the system.

**Reference suppliers for later underwriting:** GE Vernova / Prolec GE, Hitachi Energy / Hitachi, Siemens Energy, HD Hyundai Electric, Eaton, Schneider Electric, ABB.

---

## 10. Distribution from substation to site

### Components

- feeders / cables;
- transformers;
- MV switchgear;
- breakers / protection;
- e-houses / modular substations;
- bus ducts / conductors.

### Preliminary Bottleneck Strength: **4.2 / 5**

**INTERPRETATION:** The hardware is less concentrated than LPTs, but hyperscale builds require large quantities of equipment at once and qualified electrical-system integration matters.

**Evidence:** Eaton reported a 42% increase in rolling Electrical Americas orders in Q1 2026 driven by data-centre momentum and 48% year-over-year Electrical backlog growth; ABB and Schneider also report strong / record data-centre-led electrification demand.

---

## 11. Behind-the-meter generation / microgrid

### Purpose

- accelerate energisation when utility supply is delayed;
- provide backup / resilience;
- reduce peak grid draw;
- combine onsite gas, fuel cells, renewable generation and storage;
- enable flexible grid service.

### Components

- gas turbines / reciprocating generators;
- fuel cells where economic;
- BESS;
- microgrid controllers;
- switchgear and protection;
- grid synchronisation / islanding controls.

### Preliminary Bottleneck Strength: **4.1 / 5**

**INTERPRETATION:** This is less a single scarce component than an **integration bottleneck**. The value proposition rises when the grid connection is the critical path.

**Counterpoint:** the control architecture and generation technology are multi-vendor; supplier concentration may be lower than in turbines or transformers.

**Potential structural value:** turnkey engineering, controls, qualification, service and pre-integrated modular power blocks.

---

## 12. Energy storage / UPS / dynamic-load buffering

AI workloads can produce rapid load changes that grid and generator assets are not designed to follow directly.

**FACT:** IEA's 2026 Energy-and-AI update explicitly notes that rapid AI load swings make energy storage important for reliable supply.

### Functions

- ride-through during disturbances;
- backup before generator start;
- smoothing sub-second / second-scale power excursions;
- peak shaving;
- grid-flexibility services;
- possible replacement of part of traditional UPS architecture.

### Preliminary Bottleneck Strength: **3.9 / 5**

**Why not higher:** battery cells and mainstream power electronics have broad supply bases.

**Where scarcity may emerge:** high-power BMS / PCS, safety qualification, integrated UPS-BESS controls, very-high-reliability systems and DC-native storage integration.

---

## 13. Data-centre electrical backbone

### Typical current AC path

```text
utility MV AC
→ transformers
→ MV/LV switchgear
→ UPS
→ PDU / busway
→ rack PSU
→ 54 VDC / 12 VDC
→ point-of-load conversion
→ GPU / CPU
```

### Components

- MV/LV switchgear;
- transformers;
- UPS;
- PDU / RPP;
- busway;
- breakers / fuses;
- monitoring / controls;
- backup generation interface.

### Preliminary Bottleneck Strength: **4.4 / 5**

**Evidence:** Eaton, Schneider Electric, ABB, GE Vernova and Vertiv all report strong data-centre-driven electrical demand / architecture investment in 2026.

**INTERPRETATION:** The opportunity is not simply volume. Rack density increases the **power content per rack and per square metre**, and electrical rooms / copper / conversion losses become physical design constraints.

**Reference suppliers:** Vertiv, Eaton, Schneider Electric, ABB, Delta Electronics, Legrand / nVent in selected distribution layers.

---

## 14. 800 VDC / grid-to-rack power architecture transition

### Why the architecture is changing

**FACT:** NVIDIA says traditional 54 VDC in-rack distribution is approaching physical limits as racks exceed ~200 kW and future systems move toward MW-class racks.

**FACT:** NVIDIA, Google and Microsoft have developed an 800 VDC architecture through OCP; more than **80 ecosystem companies** are building to the specification as of August 2026.

### Architectural progression

1. **today:** multiple AC/DC conversions, rack-level PSUs and 54 VDC distribution;
2. **near term:** AC facility + 800 VDC sidecar / power rack;
3. **next:** row-level 800 VDC power centres / busways;
4. **future:** direct medium-voltage AC → 800 VDC facility-scale power blocks / possibly solid-state transformers.

### Preliminary Bottleneck Strength: **4.2 / 5 and rising technically; 3.5 / 5 on supplier concentration today**

**INTERPRETATION:** This may become one of the most important **architecture transitions** in the chain, but it is not yet clear that it produces durable supplier scarcity. An open ecosystem with 80+ participants can create rapid innovation while also limiting pricing power.

**Potential scarce sub-layers:**

- high-power AC/DC rectification;
- DC protection / solid-state breakers;
- high-voltage DC busway / connectors;
- very-high-power DC/DC conversion;
- power semiconductors with efficiency / thermal advantages;
- DC-native UPS / BESS integration;
- solid-state transformers if they become production viable.

---

## 15. Rack-level power delivery and power semiconductors

### Components

- DC/DC converters;
- power modules / shelves;
- busbars;
- connectors;
- fuses / breakers;
- Si / SiC / GaN power semiconductors;
- magnetics / capacitors.

### Preliminary Bottleneck Strength: **3.8 / 5**

**Why important:** content and technical requirements rise sharply with rack density.

**Why not yet a Gate-A equivalent:** NVIDIA's 800 VDC ecosystem already includes a broad set of semiconductor and power-system vendors, suggesting substitution may remain relatively high.

**Reference suppliers / ecosystem participants:** Infineon, STMicroelectronics, onsemi, Texas Instruments, Monolithic Power Systems, ROHM, Navitas, Delta, Lite-On and others.

**OPEN QUESTION:** which component becomes the new hard-to-substitute failure / efficiency bottleneck at 800 VDC and MW-rack scale?

---

## 16. Cooling / heat rejection — coupled constraint

Cooling is not merely a downstream auxiliary system. At high rack density it directly determines how much electrical power can be turned into usable compute.

### Layers

- direct-to-chip liquid cooling;
- coolant distribution units (CDUs);
- pumps / heat exchangers;
- chillers / dry coolers / cooling towers;
- facility water / refrigerant systems;
- controls.

### Preliminary Bottleneck Strength: **4.1 / 5**, to be researched separately

**INTERPRETATION:** Electrical power availability without thermal capacity does not create usable AI capacity. Power and cooling should therefore be modelled as a **joint capacity constraint**.

This initial energy map does not yet underwrite cooling suppliers; a separate thermal deep dive may be warranted after the electrical bottlenecks are validated.

---

## 17. Load flexibility / orchestration / demand response

### Capabilities

- workload shifting across time / geography;
- power capping;
- battery dispatch;
- generator / grid coordination;
- flexible transmission service;
- peak shaving;
- predictive controls.

**FACT:** FERC's June 2026 large-load actions specifically contemplate flexible transmission services and co-located / nearby generation as ways to speed connection and reduce network upgrades.

### Preliminary Bottleneck Strength: **3.3 / 5 as a supplier layer; high strategic leverage**

Software itself may be broadly supplied, but flexibility can **change the economics of every upstream layer** by lowering the amount of firm generation and network capacity required for a given compute site.

---

## 18. Preliminary bottleneck ranking

| Rank | Layer | Bottleneck Strength | Confidence | Core reason |
|---:|---|---:|---|---|
| **1** | Large-load interconnection / transmission deliverability | **4.8** | Medium-High | site-specific studies, upgrades, tariffs, generation adequacy, long planning cycles |
| **2** | Transformers / critical substation equipment | **4.8** | High | 1–4 year lead times, custom/qualified hardware, difficult manufacturing expansion |
| **3** | Bulk transmission infrastructure | **4.7** | High | permitting, rights-of-way, multi-year build cycles, equipment dependencies |
| **4** | MV/HV switchgear / electrical distribution | **4.5** | Medium-High | high simultaneous demand, qualification and manufacturing capacity |
| **5** | Large gas-turbine capacity / slots | **4.4** | Medium-High | concentrated OEM base, large backlog, multi-year output expansion |
| **6** | Data-centre electrical backbone | **4.4** | Medium-High | more power content per rack/site, high reliability, integrated system design |
| **7** | 800 VDC power architecture | **4.2 technical** | Medium | physical need is rising; supplier concentration / moat not yet proven |
| **8** | Site distribution / modular substations | **4.2** | Medium | equipment + engineering + delivery sequencing |
| **9** | Behind-the-meter / microgrid integration | **4.1** | Medium | speed-to-power value, system integration complexity |
| **10** | Cooling / heat rejection | **4.1** | Medium-Low | coupled limit on usable MW; separate deep dive needed |
| **11** | UPS / BESS / dynamic-load buffering | **3.9** | Medium | essential reliability / smoothing, but broader hardware supply |
| **12** | Rack power semiconductors / DC conversion | **3.8** | Medium-Low | high technical intensity, but broad ecosystem today |
| **13** | Utility generation capacity | **3.6** | Medium | firm MW important, but technology / regional substitution exists |
| **14** | Load-flexibility software / controls | **3.3** | Medium-Low | high system leverage but less obvious supplier scarcity |
| **15** | Primary fuel / energy resource | **3.0** | Medium | usually not AI-specific; strongest only in local constraints |

These scores are **initial research prioritisation**, not final Gate-A conclusions.

---

## 19. Where value may accrue

### Strongest initial hypothesis

> **The highest-value layers are likely to be those that sell speed-to-power rather than energy volume.**

This includes:

- transformer / substation capacity;
- grid connection and high-voltage equipment;
- dispatchable-generation slots;
- integrated MV/LV data-centre power systems;
- onsite generation + storage + microgrid packages;
- architecture-enabling conversion / protection equipment as 800 VDC scales.

### Lower-confidence / potentially commoditised layers

- generic renewable-generation hardware;
- standard battery cells;
- ordinary cabling / passive components without qualification barriers;
- software layers without proprietary system integration or installed-base advantage.

---

## 20. Architecture migration risk

A key lesson from the memory work applies here: **the bottleneck can migrate rather than disappear.**

Examples:

- grid delays → co-location / onsite generation → turbine / switchgear / fuel constraints;
- AC distribution limits → 800 VDC → new rectification / DC protection / busway constraints;
- power availability → higher rack density → cooling / thermal constraints;
- transformer scarcity → solid-state transformer adoption → semiconductor / high-frequency magnetics / control constraints.

Supplier underwriting must therefore ask whether a company owns the **function** or only the current implementation.

---

## 21. Falsification / evidence against the thesis

The current map can be wrong if:

- AI/data-centre demand is materially overbooked and project pipelines contain large amounts of duplicate / speculative load;
- FERC / RTO reforms make large-load connection substantially faster than current evidence implies;
- transformer / switchgear / turbine capacity additions arrive faster than demand;
- 800 VDC becomes highly standardised with many interchangeable suppliers and low margins;
- AI efficiency gains materially reduce absolute MW requirements;
- hyperscalers increasingly build or vertically integrate their own power equipment;
- grid-scale renewables + batteries scale fast enough that firm-generation equipment loses scarcity;
- data centres migrate to regions with abundant existing power rather than paying for constrained-site infrastructure.

---

## 22. Priority follow-up workstreams

Do **not** begin broad company picking yet. First validate the highest-scoring functions:

1. **Transformers + substation / switchgear economics** — capacity, lead times, supplier concentration, qualification, pricing and expansion.
2. **Large-load interconnection / transmission** — determine whether this is investable directly or mainly a demand driver for equipment / onsite solutions.
3. **Dispatchable generation equipment** — turbine / genset capacity, services economics and data-centre-specific demand.
4. **Grid-to-rack / 800 VDC architecture** — identify genuinely scarce subcomponents versus broad ecosystem exposure.
5. **Behind-the-meter power / microgrids / storage** — test whether integration / controls create durable supplier economics.
6. **Cooling / heat rejection** — separate coupled bottleneck map after core electrical chain.

Only after these should the theme move to company-level Investment Capture and valuation work.

---

## Sources

### System demand / supply

- IEA — Key Questions on Energy and AI, 2026: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- IEA — Energy demand from AI: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- IEA — Energy supply for AI: https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai
- IEA — Electricity 2026 demand: https://www.iea.org/reports/electricity-2026/demand

### Grid / interconnection / transformers

- FERC — Large-load integration action, 18 June 2026: https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration
- FERC — RM26-4 large-load interconnection docket: https://ferc.gov/rm26-4
- US DOE — Distribution Transformer Webinar transcript, 2026: https://www.energy.gov/oe/distribution-transformer-webinar-text-alternative
- US DOE — Transformer supply-chain work: https://www.energy.gov/oe/supply-chain-and-market-analysis

### Generation / electrification demand evidence

- GE Vernova Q2 2026 results: https://www.gevernova.com/news/press-releases/ge-vernova-reports-second-quarter-2026-financial-results-raises-2026-financial
- Eaton Q1 2026 results: https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-reports-record-first-quarter-2026-results.html
- Schneider Electric 2026 financial results: https://www.se.com/ww/en/about-us/investor-relations/financial-results/
- ABB Q2 2026 results: https://new.abb.com/news/detail/137496/q2-2026-results
- Cummins Q2 2026 filing: https://investor.cummins.com/sec-filings/all-sec-filings/content/0000026172-26-000029/cmi-20260630.htm

### Data-centre power architecture

- NVIDIA — Why Scaling AI Compute Performance Requires a New Power Architecture, 11 Aug 2026: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
- NVIDIA — 800 VDC architecture overview: https://www.nvidia.com/en-eu/data-center/technologies/800-vdc-architecture/
- NVIDIA technical architecture: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- Vertiv — practical path to 800 VDC, July 2026: https://www.vertiv.com/en-us/insights/articles/blog-posts/from-rack-to-data-hall-the-practical-path-to-800-vdc/
