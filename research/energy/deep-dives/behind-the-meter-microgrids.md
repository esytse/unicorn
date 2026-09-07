# Behind-the-Meter Power, Microgrids + Storage — Bottleneck Deep Dive

**Status:** Integrated behind-the-meter power architecture is a credible speed-to-power profit pool but only a moderate structural bottleneck; generic storage is not scarce  
**Bottleneck Strength:** **4.1 / 5 integrated behind-the-meter architecture / controls / electrical integration**; **3.4 / 5 generic BESS / battery hardware**; generation hardware inherits technology-specific scores (large gas turbines **4.6 / 5**, reciprocating gensets **3.6 / 5**)  
**Confidence:** **Medium-High** on strategic value of integrated behind-the-meter power; **Medium** on durable supplier concentration / economic capture; **High** that generic battery cells are not the scarce layer  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #47

## Executive conclusion

**CONCLUSION:** Behind-the-meter (BTM) power is real and strategically important, but it is not one monolithic equipment bottleneck.

The evidence now supports a more precise thesis:

> **The value is in shortening time-to-power by designing, permitting, financing and controlling a complete local power system — not simply in owning a generator or a battery.**

Integrated BTM architecture / microgrid controls / electrical-system integration scores **4.1/5** and passes a narrow Gate-A-style threshold at **Medium confidence**. The strength comes from system complexity, qualification, project execution, fault protection, real-time orchestration and the economic value of bringing an AI campus online before a conventional grid connection is available.

However, broad component scarcity is weaker:

- large advanced gas turbines remain genuinely scarce at **4.6/5** from the completed turbine deep dive;
- reciprocating gensets remain a **3.6/5** demand beneficiary with broader supply;
- generic battery cells / BESS hardware score only **3.4/5** because supply is broad and technology is substitutable;
- fuel cells have credible commercial momentum, but as a broad function they remain an **emerging alternative rather than a validated scarce layer**;
- microgrid controls / protection / integration are the most interesting BTM-specific layer, but supplier concentration is still not proven enough to treat them like transformers or gas turbines.

The strongest new evidence is strategic revealed preference: Vertiv agreed in September 2026 to acquire UtilityInnovation Group for about **$1.45bn upfront plus up to $1.15bn contingent consideration** specifically to extend from rack-level infrastructure upstream into microgrid controls, onsite-generation orchestration, microgrid switchgear and BTM architecture. The deal is evidence that **time-to-power architecture has become strategically valuable**, but it does not by itself prove a narrow moat.

The major falsification is equally important. IEA analysis shows onsite gas is not a frictionless bypass: reliable operation for variable critical data-centre load can require **30–70% generation overbuild**, turbine supply is itself constrained, and only a minority of announced onsite-gas projects have moved into physical construction. BTM therefore often **moves the bottleneck** from grid queue to turbines, gas supply, emissions permits, land, storage, protection and integration rather than eliminating it.

---

## 1. Where behind-the-meter power sits in the chain

A conventional path is:

```text
regional generation
        ↓
transmission network
        ↓
utility interconnection
        ↓
substation / feeder
        ↓
data centre
```

A BTM / bridge-to-grid architecture can become:

```text
grid connection delayed or insufficient
        ↓
onsite / nearby firm generation
        +
BESS / UPS / dynamic buffer
        +
microgrid controls + protection
        +
MV/LV switchgear / transformation
        ↓
data-centre electrical backbone
        ↓
AI load
```

or a hybrid path:

```text
partial / flexible grid service
        +
onsite generation
        +
storage
        +
load flexibility
        ↓
common microgrid controller
        ↓
AI load
```

**INTERPRETATION:** BTM is best understood as an **architecture and integration layer** that can combine multiple generation technologies. The scarce economic function is potentially not the power source itself but the ability to make several assets behave like one reliable utility-grade supply for a highly dynamic critical load.

---

## 2. The demand signal: developers are paying to escape grid timing

**FACT:** The IEA's 2026 analysis says slow grid connections are pushing U.S. data-centre developers toward onsite natural-gas power. Satellite tracking indicates roughly **one-fifth** of identified onsite-gas projects had begun land clearing or construction.

**FACT:** The IEA estimates **15–27 GW of onsite natural-gas capacity** could serve data centres globally by 2030, predominantly in the United States.

**FACT:** The same analysis estimates roughly **20–25 GW of battery storage** could be installed in data centres globally by 2030.

**INTERPRETATION:** The addressable BTM system is large enough to matter. It is no longer limited to emergency diesel backup or small campus microgrids.

**COUNTERPOINT:** The majority of data centres still prefer grid connection. BTM is therefore best framed as a **bridge, supplement or site-specific alternative**, not the default global architecture.

---

## 3. Vertiv / UtilityInnovation Group — strongest strategic revealed-preference evidence

**FACT:** On 2 September 2026 Vertiv announced an agreement to acquire UtilityInnovation Group (UIG) for approximately **$1.45bn cash at closing**, plus up to **$1.15bn** in contingent cash consideration based on EBITDA targets.

**FACT:** At the base purchase price Vertiv said the transaction represented approximately **13x expected 2027 EBITDA**.

**FACT:** UIG adds:

- microgrid controls;
- onsite-generation and storage orchestration;
- microgrid-specific switchgear;
- BTM architecture design;
- real-time load / frequency balancing;
- pre-validated reference designs for grid-connected, bridge-to-grid and islanded sites.

**FACT:** Vertiv explicitly describes the strategic objective as accelerating **time to power** for AI data centres and extending its portfolio from grid interconnect through rack-level infrastructure.

**INTERPRETATION:** This is strong evidence that the BTM integration layer has become economically strategic enough for a major critical-infrastructure vendor to pay a material acquisition price for capabilities it did not previously own.

**INTERPRETATION:** The acquisition also supports the architecture-resilience thesis: UIG is generation-agnostic. It can coordinate whatever a site can permit, fuel and finance rather than depending on one generation technology.

**COUNTERPOINT:** An acquisition price is not evidence of enduring scarcity. Strategic urgency, expected cross-selling and current AI valuations can all inflate transaction economics. UIG's customer concentration, standalone margins and sustainable competitive advantage are not disclosed in enough detail for company-level conclusions.

---

## 4. Integrated BTM power can materially compress development timelines

**FACT:** Eaton and Siemens Energy offer a standardized onsite data-centre power architecture based on a **500 MW** modular plant using SGT-800 gas turbines, N+2 redundancy and integrated battery storage.

**FACT:** The partners state that simultaneous construction of the power plant and data-centre facility can reduce deployment timelines by **up to about two years**, with some materials describing a two-to-four-year reduction depending on location.

**FACT:** The architecture combines Siemens Energy generation with Eaton MV/LV switchgear, UPS, busway, modular electrical systems, engineering and software.

**FACT:** Eaton explicitly states that suitable sites still require access to **gas, water and fibre**.

**INTERPRETATION:** Time-to-power is monetisable because a completed AI facility has very high opportunity cost while idle. A two-year schedule advantage can justify significant infrastructure premium even if the BTM system is not the lowest-cost long-run source of electricity.

**COUNTERPOINT:** The same evidence reveals bottleneck migration: a site that escapes utility interconnection may become dependent on pipeline capacity, turbine slots, air permitting, water and land.

---

## 5. Gigawatt-scale onsite power is moving from concept to real projects

**FACT:** Mitsubishi Power announced the Cheyenne Power Hub in May 2026 with two M501JAC turbines planned for phase one and roughly **1,150 MW of site-ready power** for a large-scale data-centre development.

**FACT:** The project is designed around an existing major natural-gas pipeline and retains future grid-interconnection / renewable-integration options.

**INTERPRETATION:** BTM is no longer synonymous with small gensets. It can be utility-scale generation physically dedicated to a data-centre campus.

**INTERPRETATION:** This reinforces the earlier turbine conclusion: where BTM relies on large turbines, the scarce hardware remains the advanced turbine manufacturing slot rather than a new independent onsite-power bottleneck.

---

## 6. Bloom Energy shows a second architecture with real financing momentum

**FACT:** Bloom Energy and Brookfield expanded their AI-infrastructure financing framework from **$5bn to $25bn** in June 2026 to support fuel-cell power projects.

**FACT:** Bloom describes demand from hyperscalers / AI developers for islanded and rapidly deployable onsite power, and it has continued announcing data-centre deployments and partnerships during 2026.

**FACT:** Bloom's August 2026 materials describe factory-integrated / standardized designs intended to reduce onsite installation time materially.

**INTERPRETATION:** Fuel cells matter because they demonstrate that BTM is **technology-substitutable**. A site can choose among turbines, reciprocating engines, fuel cells, batteries plus grid supply, or hybrids depending on emissions, gas pressure, project scale and timetable.

**COUNTERPOINT:** Bloom-specific financing and customer announcements are evidence of commercial adoption, not proof that fuel cells are the scarce function. The economics depend on equipment cost, gas supply, stack replacement / service, financing and competition with turbines / grid / batteries.

**DECISION:** Fuel cells remain a later company-underwriting candidate, not a separately validated Gate-A function at this stage.

---

## 7. Reciprocating gensets confirm demand but also substitution

**FACT:** Cummins has announced natural-gas generator deployments for BTM AI-data-centre microgrids, including multi-year delivery programmes paired with microgrid controls.

**FACT:** Caterpillar and partners are also pursuing integrated data-centre prime-power systems combining natural-gas generation, batteries and other technologies.

**INTERPRETATION:** These examples strengthen the demand case while weakening a concentration thesis. Multiple engine OEMs and modular designs make reciprocating generation more elastic than large advanced gas turbines.

**DECISION:** Retain the existing **3.6/5** score for reciprocating gensets; do not pass Gate A.

---

## 8. Storage is necessary, but generic battery cells are not the moat

AI loads can change rapidly. A gas turbine or reciprocating engine does not necessarily respond efficiently to every millisecond- or second-scale load swing.

Storage can provide:

- ride-through;
- sub-second / second-scale balancing;
- generator ramp support;
- black-start / islanding support;
- peak shaving;
- flexible grid service;
- integration with UPS;
- potential direct DC coupling under 800 VDC architectures.

**FACT:** IEA analysis identifies approximately **20–25 GW** of potential data-centre battery storage by 2030 and notes the potential for those assets to support the grid if incentives align.

**INTERPRETATION:** Storage content per AI campus can grow rapidly even without cell scarcity.

**COUNTERPOINT:** lithium-ion cells, mainstream battery racks and many PCS/BMS functions have broad global supply. Chemistry alternatives and multiple system integrators provide substitution.

### Generic BESS / battery hardware score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | 3.4 | system safety matters, but cells/modules are widely manufactured |
| Supply elasticity | 3.5 | large global battery supply chain can add capacity faster than turbines/transformers |
| Supplier concentration | 2.8 | many cell and system suppliers |
| Qualification / switching | 3.5 | safety / UPS integration matter, but multiple qualified designs exist |
| System criticality | 4.0 | buffering / resilience increasingly useful but architecture-dependent |
| Architecture resilience | 4.0 | storage function persists and may strengthen in DC architectures |
| Pricing / backlog scarcity | 2.8 | broad demand, but little evidence of durable cell-level scarcity premiums |

**Bottleneck Strength: 3.4 / 5 — Gate A NOT passed.**

---

## 9. Microgrid controls and protection are more differentiated than battery cells

An AI microgrid must coordinate:

- generators with different ramp rates;
- BESS / UPS;
- utility import/export;
- islanding and reconnection;
- frequency and voltage control;
- fault isolation;
- protection coordination;
- dynamic AI load swings;
- maintenance / redundancy;
- fuel constraints;
- emissions / operating limits.

**INTERPRETATION:** At hundreds of MW or GW scale this is closer to a small private power system than a building-energy-management application.

**FACT:** Vertiv's acquisition rationale specifically highlights UIG's proprietary controls, real-time load / frequency balancing and custom / pre-engineered microgrid switchgear.

**INTERPRETATION:** The moat candidate is therefore **system-level control + protection + validated architecture + execution**, not generic monitoring software.

**OPEN QUESTION:** Is the credible supplier set narrow enough to support sustained pricing power, or can Eaton, Schneider, Siemens, ABB, GE Vernova, Vertiv/UIG and specialist integrators compete effectively?

---

## 10. The largest falsification: onsite gas is not automatically faster or simpler

**FACT:** The IEA estimates that reliably serving a critical, variable data-centre load using onsite gas may require **30–70% more installed generation capacity than nominal demand** to cover redundancy, maintenance and operating requirements.

**FACT:** IEA also notes that the same gas-turbine supply crunch affecting utility projects can constrain onsite projects.

**FACT:** Only a fraction of announced onsite-gas projects have entered visible physical construction, indicating substantial permitting, financing, equipment and site-development attrition.

**INTERPRETATION:** This materially weakens a naive thesis that BTM automatically bypasses all grid delays.

Instead:

```text
grid interconnection bottleneck
        ↓
onsite power decision
        ↓
new constraints emerge:
- turbine / generator slot
- natural-gas pipeline / pressure
- air permit / emissions
- land / noise / water
- electrical equipment
- storage / redundancy
- protection / controls
- financing
- operations / service
```

**CONCLUSION:** BTM is best understood as **bottleneck migration and schedule optimisation**, not bottleneck elimination.

---

## 11. Why integrated BTM still passes a narrow Gate-A threshold

Even though component substitution is broad, complete systems have several barriers:

### 11.1 Project architecture is site-specific

A credible design must reconcile:

- available grid service;
- pipeline / fuel availability;
- local emissions rules;
- power quality;
- compute phasing;
- redundancy standard;
- storage duration;
- land / water;
- construction sequencing;
- future grid connection.

### 11.2 Reliability is economically extreme

The system supports very expensive compute. Outages can destroy far more economic value than the cost of the microgrid controller or switchgear.

### 11.3 Controls + protection need real-world qualification

Real-time balancing, fault clearing, islanding and restart are difficult to validate purely in software.

### 11.4 One accountable integrator has schedule value

The ability to coordinate generation, switchgear, BESS, controls and downstream critical infrastructure can reduce interface risk and project-management delay.

### 11.5 Lifecycle service matters

The system creates recurring service, monitoring, maintenance, firmware/control updates and equipment replacement opportunities.

**INTERPRETATION:** This creates an integration moat even where individual hardware categories remain competitive.

---

## 12. Integrated BTM architecture score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **4.2** | multi-asset power system, protection, redundancy and dynamic load |
| Supply elasticity | **3.8** | integration teams / qualified gear can scale, but not instantly; hardware bottlenecks can migrate into project |
| Supplier concentration | **3.5** | several global platforms plus specialist integrators |
| Qualification / switching cost | **4.4** | critical-load reliability, protection, utility interface and site validation |
| System criticality | **4.8** | failure strands the entire AI load |
| Architecture resilience | **4.4** | generation-agnostic orchestration remains useful across turbine / genset / fuel cell / grid / BESS mixes |
| Pricing / strategic-value evidence | **4.0** | Vertiv/UIG acquisition and integrated offerings validate value; direct standalone margin evidence remains limited |

**Bottleneck Strength: 4.1 / 5 — Gate A PASSED narrowly.**

**Confidence: Medium.**

This is weaker than transformers, transmission or gas turbines because supplier concentration and physical scarcity are lower. It passes because the combined function — reliable, site-specific, multi-source power orchestration under schedule pressure — is difficult to substitute with a single commodity component.

---

## 13. 800 VDC changes storage and microgrid topology, not the core function

The completed 800 VDC deep dive found that the broad open ecosystem does not yet support a supplier-scarcity thesis.

BTM adds one new implication:

**HYPOTHESIS:** DC-native storage may become more valuable if future facilities distribute 800 VDC deeper into the data hall, because battery storage can connect more directly to the DC bus and potentially reduce repeated AC/DC conversion.

Potential value shifts toward:

- bidirectional DC/DC conversion;
- DC protection;
- energy-buffer controls;
- BESS/UPS convergence;
- DC bus management.

**COUNTERPOINT:** Open OCP standards and a broad power-electronics supplier base could commoditise these functions rapidly.

**DECISION:** Do not create a separate DC-storage bottleneck issue until direct commercial / qualification evidence shows a concentrated supplier set.

---

## 14. Supplier archetypes for later Investment Capture

This deep dive produces **candidate archetypes**, not company promotions.

### Integrated grid-to-rack / BTM platforms

- Vertiv / UIG
- Eaton
- Schneider Electric
- ABB
- Siemens / Siemens Energy combinations
- GE Vernova in selected upstream / microgrid layers

**Question:** Does portfolio breadth + controls + service create higher returns than specialist hardware exposure?

### Scarce generation OEMs

- GE Vernova
- Siemens Energy
- Mitsubishi Heavy Industries / Mitsubishi Power

Already covered by the 4.6/5 turbine Gate A conclusion.

### Distributed-generation / fuel-cell specialists

- Bloom Energy
- Cummins
- Caterpillar

**Question:** Does direct AI sensitivity outweigh broader substitution and normalized-cycle / valuation risk?

### Storage / power-conversion integrators

Broad set; do not promote from volume growth alone.

**Question:** Is there a narrow high-power, safety-critical control / conversion layer with demonstrably limited qualified supply?

---

## 15. Falsification / thesis breakers

The integrated BTM thesis weakens materially if:

- grid reforms and transmission expansion shorten utility connection enough that bridge-to-grid economics collapse;
- developers consistently prefer relocating to power-rich regions rather than building onsite systems;
- turbine / generator queues become as long as grid queues, eliminating schedule advantage;
- gas pipeline / air-permit constraints block large onsite deployments;
- BTM systems require so much redundancy / overbuild that economics become unattractive;
- standard microgrid controllers and protection packages become highly interchangeable;
- hyperscalers internalise architecture / controls and multi-source hardware directly;
- a large share of announced AI campuses never reach financing / construction;
- distributed generation faces regulatory restrictions because of emissions / grid-cost shifting;
- integrated providers win revenue but fail to capture margins after turnkey execution risk.

The thesis strengthens if:

- more hyperscalers sign funded multi-hundred-MW / GW BTM projects;
- bridge-to-grid designs repeatedly compress energisation by 1–3 years;
- microgrid controls / protection qualify across multiple large campuses with recurring software / service revenue;
- BTM architecture becomes standard even after eventual grid connection because it provides resilience / flexibility;
- DC-native storage / load orchestration becomes mandatory at MW-rack scale;
- suppliers disclose sustained premium margins, backlog or pricing tied specifically to integrated power architectures.

---

## 16. Decision

### Integrated BTM power / microgrid architecture

**Gate A PASSED narrowly — 4.1 / 5, Medium confidence.**

The economic function is **time-to-power + reliable multi-source orchestration**, not generic onsite generation.

### Generic BESS / battery hardware

**Gate A NOT passed — 3.4 / 5.**

Storage deployment should grow strongly, but broad supply and substitution make the cell / generic hardware layer a volume beneficiary rather than a structural scarcity play.

### Fuel cells

**Emerging commercial alternative; no broad Gate-A conclusion.**

Bloom's financing / customer momentum is meaningful enough to revisit during supplier Investment Capture, but technology-level scarcity is unproven because gas turbines, engines, grid power and hybrid systems are substitutes.

### Gensets

**Remain 3.6 / 5 — Gate A NOT passed.**

### Large gas turbines

**Remain 4.6 / 5 — Gate A PASSED** from the prior deep dive and represent the strongest physically scarce hardware inside many BTM architectures.

---

## 17. Energy-program implication

The energy frontier now contains six validated functions:

1. transformers / critical substation equipment — **4.7**;
2. physical transmission deliverability — **4.7**;
3. large gas-turbine equipment / manufacturing slots — **4.6**;
4. MV/HV switchgear — **4.4**;
5. integrated data-centre electrical backbone — **4.3**;
6. integrated BTM power architecture / microgrid orchestration — **4.1**.

The programme should now validate **cooling / heat rejection** as the final major coupled constraint, then stop broad bottleneck discovery and run a common-basis Investment Capture synthesis.

A key cross-theme lesson is now visible:

> **AI power scarcity repeatedly migrates. The best businesses may be the ones that own the hard-to-substitute function across migrations rather than the current workaround.**

---

## Sources

### Neutral / system evidence

- IEA — Key Questions on Energy and AI, Executive Summary, 2026: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- IEA — Energy and AI / energy supply and grid-integration analysis: https://www.iea.org/reports/energy-and-ai

### Integrated BTM / microgrid evidence

- Vertiv — agreement to acquire UtilityInnovation Group, 2 Sep 2026: https://investors.vertiv.com/news/news-details/2026/Vertiv-Announces-Agreement-to-Acquire-UtilityInnovation-Group-to-Accelerate-Time-to-Power-for-AI-Data-Centers/default.aspx
- Eaton + Siemens Energy — integrated onsite data-centre power, 3 Jun 2025: https://www.eaton.com/gb/en-gb/company/news-insights/news-releases/2025/eaton-and-siemens-energy-join-forces-to-provide-power-and-technology.html
- Eaton — current integrated onsite data-centre solution: https://www.eaton.com/gb/en-gb/markets/data-centers/eaton-and-siemens-energy.html
- Siemens Energy — modular onsite generation for data centres: https://www.siemens-energy.com/us/en/home/products-services/product/modular-onsite-power-generation-data-center.html

### Technology / project alternatives

- Bloom Energy + Brookfield — $25bn AI infrastructure financing framework, 30 Jun 2026: https://investor.bloomenergy.com/press-releases/press-release-details/2026/Brookfield-and-Bloom-Energy-Expand-AI-Infrastructure-Partnership-to-25-Billion-Fivefold-Increase-to-Build-and-Finance-Rapid-Power-for-AI-Infrastructure/default.aspx
- Bloom Energy newsroom / 2026 onsite-power commercial updates: https://www.bloomenergy.com/newsroom/
- Mitsubishi Power — Cheyenne Power Hub / dedicated onsite data-centre power, 15 May 2026: https://power.mhi.com/regions/amer/news/20260515.html
- Cummins — data-centre / prime-power and microgrid materials: https://www.cummins.com/generators/data-centers
- Caterpillar — data-centre power solutions: https://www.cat.com/en_US/by-industry/electric-power/industries/data-centers.html
