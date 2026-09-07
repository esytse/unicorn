# Nuclear Power Supply Chain — AI-Relevant Bottleneck Deep Dive

**Status:** Nuclear branch decomposed; several fuel-cycle / manufacturing bottlenecks validated, but most new-reactor pathways are 2030s rather than near-term AI power  
**Confidence:** **Medium-High** overall; **High** on current enrichment / HALEU scarcity and existing-fleet timing; **Medium** on long-run supplier capture for new-build / advanced-reactor components  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #50

## Executive conclusion

**CONCLUSION:** Nuclear matters materially to the AI-energy chain, but the near-term and long-term investment cases are different.

Before 2030, the most credible nuclear contribution to AI power is:

1. **preserving / contracting existing nuclear output**;
2. **restarting shuttered plants where the asset is recoverable**;
3. **uprating existing reactors**;
4. only then, beginning in the 2030s, **advanced reactors / SMRs and new large reactors**.

The most important supply-chain finding is that **uranium itself is not the tightest layer**. Scarcity strengthens as the fuel and equipment become more qualified and specialized:

```text
uranium ore / U3O8
    ↓
conversion to UF6
    ↓
LEU enrichment
    ↓
HALEU enrichment / deconversion where required
    ↓
fuel fabrication / advanced fuel
    ↓
reactor-grade forgings / vessels / steam generators / pumps / valves / I&C
    ↓
specialist EPC / QA / nuclear workforce
    ↓
reactor construction / restart / uprate
    ↓
turbine-generator + grid connection
    ↓
firm electricity
```

Four nuclear supply-chain functions pass the structural scarcity test most clearly today:

- **HALEU enrichment / associated advanced-fuel supply — 4.7/5**;
- **Western LEU enrichment capacity — 4.6/5**;
- **ultra-large nuclear forgings / long-lead heavy reactor components — 4.5/5**;
- **qualified nuclear EPC / manufacturing / QA workforce — 4.4/5**.

**Conversion / UF6 capacity passes narrowly at 4.3/5.**

But the strongest near-term AI nuclear pathway is not an advanced reactor. It is the **existing fleet / restart / uprate route**, where the underlying licensed site, grid connection and reactor asset already exist.

---

## 1. Nuclear branch in the AI-energy value chain

Nuclear can enter the E2E power chain through three distinct routes.

### Route A — existing fleet

```text
operating nuclear plant
→ life extension / commercial support
→ optional uprate
→ existing transmission
→ regional grid / data-centre load
```

### Route B — restart / brownfield nuclear

```text
shuttered but recoverable reactor
→ licensing restoration
→ component inspection / replacement
→ refuelling / workforce rebuild
→ restart
→ existing transmission
```

### Route C — new build / advanced nuclear

```text
uranium / fuel cycle
→ reactor design + licensing
→ long-lead forgings / qualified equipment
→ civil works + nuclear EPC
→ commissioning
→ transmission / substation
→ grid / data-centre load
```

**INTERPRETATION:** These routes should not be valued as one category. Existing-fleet support can affect AI power in **2026–2028**; restart projects can plausibly affect the **late 2020s**; most commercial advanced reactors and new large reactors are **2030s** power sources.

---

## 2. AI demand for nuclear is already commercial, not hypothetical

**FACT:** Constellation and Microsoft have a 20-year PPA supporting restart of the **835 MW Crane Clean Energy Center**, with Microsoft purchasing the renewed plant's energy to help match its PJM data-centre power use.

**FACT:** Constellation currently expects Crane to be ready for service in **2027**, subject to NRC and other approvals.

**FACT:** Meta's 2026 nuclear agreements cover operating Vistra plants, uprates and advanced-reactor development. Meta says the package supports up to **6.6 GW** of existing and new nuclear energy by 2035.

**FACT:** Vistra disclosed 20-year Meta PPAs covering **2,609 MW**, including **2,176 MW of existing operating output** and **433 MW of future uprate capacity**. Existing-energy delivery begins in late 2026 and is expected to reach full delivery by end-2027; the uprate portion begins later, in the 2030s.

**FACT:** Google / Kairos target a first **50 MW** advanced-reactor delivery in 2030 and up to **500 MW by 2035**.

**FACT:** TerraPower / Meta target two Natrium units totaling **690 MW as early as 2032**, with rights for up to six additional units by 2035.

**FACT:** X-energy says the first Amazon / Energy Northwest Xe-100 deployment is expected in the **early 2030s**, with four reactors / 320 MW initially and potential expansion to 960 MW at the site.

**INTERPRETATION:** Nuclear demand from hyperscalers is real, but near-term capacity is overwhelmingly tied to **existing or brownfield assets**. Advanced nuclear is strategically important but should be treated as 2030s optionality rather than a solution to the 2026–2029 power shortage.

---

## 3. Existing operating nuclear capacity is a scarce asset

Existing reactors combine several things that are extremely hard to recreate quickly:

- licensed nuclear site;
- trained operating organisation;
- grid interconnection;
- transmission rights;
- operating history;
- fuel-supply chain;
- security / emergency infrastructure;
- community / regulatory framework.

**FACT:** Constellation's Meta agreement supports the **1,121 MW Clinton** plant beginning in June 2027 and includes a 30 MW uprate.

**FACT:** Vistra / Meta agreements preserve and contract more than 2.1 GW of operating nuclear output at Perry and Davis-Besse, with separate future uprates at Perry, Davis-Besse and Beaver Valley.

**INTERPRETATION:** The scarcity is largely in the **asset**, not a merchant component. A functioning licensed nuclear plant near constrained load has greater strategic value than an equivalent amount of hypothetical future nuclear capacity.

### Existing-fleet / contractable firm capacity score: **4.6 / 5 as an asset scarcity**

This is **not** a Gate-A supplier score. It is a reminder that nuclear asset owners may capture economics even when no particular component supplier is scarce.

---

## 4. Restarts are the fastest route to material new nuclear MW — but rare

**FACT:** Crane was shut in 2019 and is being restored under a Microsoft-backed 20-year PPA. DOE closed a **$1bn loan** in November 2025 to support the restart.

**FACT:** NRC states that restarting Crane requires restoring the plant's licensing basis, returning components to safe operational status and making necessary upgrades; NRC created a dedicated Restart Panel.

**FACT:** Palisades is undergoing a separate first-of-a-kind NRC restart process after shutting in 2022.

**INTERPRETATION:** Restart economics benefit from already-existing civil structures, grid connection and a known reactor design, but they still require extensive inspection, component replacement, licensing, refuelling and workforce rebuilding.

**LIMIT:** The number of suitable shuttered reactors is small. Restart is therefore a **high-value but non-scalable pathway**.

### Restart pathway score: **4.4 / 5 current scarcity / complexity**

**Decision:** treat restart capability as a strategically valuable brownfield pathway, not a repeatable large market comparable to turbine or transformer manufacturing.

---

## 5. Uprates add real capacity but do not solve the whole AI power gap

**FACT:** NRC's August 2026 expected-application schedule lists **31 anticipated power uprates totaling about 2.42 GW electric through 2032**.

**FACT:** Expected 2026–2030 applications sum to roughly **2.29 GW electric**.

**FACT:** Meta-backed Vistra uprates total **433 MW**, expected to enter service in the early 2030s.

**INTERPRETATION:** Uprates are attractive because they leverage existing reactors, sites and grid infrastructure. However, the total MW opportunity is measured in low single-digit GW nationally rather than tens of GW.

### Uprate pathway score: **4.2 / 5 strategic value; limited total volume**

Likely value pools include:

- turbine-generator upgrades;
- steam-path / thermal systems;
- reactor instrumentation / control;
- pumps / valves / electrical systems;
- engineering / licensing;
- outage execution.

---

## 6. Uranium mining is important, but not the strongest bottleneck

The fuel cycle starts with uranium mining and milling.

**INTERPRETATION:** Mining has long permitting and development cycles and geopolitical concentration, but uranium concentrate is relatively storable and the fuel cost is a small share of nuclear generation economics.

**COUNTERPOINT:** Western energy security is increasingly important as Russia expands its role across uranium and enrichment supply chains and as nuclear demand rises.

### Uranium mining / U3O8 score: **3.5 / 5 globally**

**Decision:** do not equate a nuclear buildout automatically with the strongest economics accruing to uranium miners. The more specialized downstream fuel-cycle steps currently show stronger structural scarcity.

---

## 7. UF6 conversion is a concentrated Western bottleneck

Natural uranium concentrate must be converted into uranium hexafluoride before enrichment for light-water-reactor fuel.

**FACT:** Cameco says its Port Hope Conversion Facility is one of **three Western suppliers of UF6** and has annual licensed production capacity of about **14 million kgU**.

**FACT:** Cameco produced **11.2 million kgU of UF6 in 2025**, a record for Port Hope, and plans total fuel-services production of 13–14 million kgU in 2026.

**INTERPRETATION:** Conversion is less technically exotic than enrichment, but the actual qualified industrial footprint is small and difficult to add quickly because of chemical, nuclear and environmental licensing.

### Conversion / UF6 score: **4.3 / 5 — Gate A passed narrowly**

**Falsification:** conversion economics weaken if Western plants add meaningful capacity faster than reactor / enrichment demand grows or if inventory / contracting buffers absorb near-term shortages.

---

## 8. Western LEU enrichment is one of the strongest nuclear bottlenecks

Enrichment is strategically sensitive, capital intensive and highly concentrated.

**FACT:** World Nuclear Association identifies three major global commercial producers — **Rosatom, Urenco and Orano** — with CNNC also a major supplier. Its current table shows 2025 capacity of about **29.1m SWU Rosatom**, **17.3m Urenco**, **7.5m Orano** and **13.8m CNNC**.

**FACT:** Urenco USA's existing annual capacity is **4.3m SWU**, about one-third of current U.S. demand. Its current expansion adds **700,000 SWU** by early 2027.

**FACT:** Urenco announced a further **2.1m SWU** U.S. expansion in June 2026, but initial production is not expected until **2032**.

**FACT:** Orano's Georges Besse II expansion adds four modules, with first new capacity from **2028** and full commissioning by 2030.

**FACT:** DOE awarded **$2.7bn** in January 2026 to expand U.S. LEU / HALEU enrichment services.

**INTERPRETATION:** This is strong bottleneck evidence:

- very few qualified suppliers;
- sanctions / geopolitical substitution pressure;
- multi-year centrifuge-factory expansion;
- strategic government funding;
- demand from both existing fleet and advanced reactors.

### Western LEU enrichment score: **4.6 / 5 — Gate A passed**

**Architecture resilience:** High. Existing LWRs, uprates, restarts and many future reactors all require enriched uranium even if the precise assay changes.

---

## 9. HALEU is even scarcer — but narrower and more policy-dependent

HALEU is uranium enriched above 5% and below 20% U-235. Many advanced-reactor designs use it to enable smaller cores, longer cycles or different fuel geometries.

**FACT:** DOE states that the United States currently has **limited commercial HALEU enrichment services** and that supply gaps can delay advanced-reactor deployment.

**FACT:** DOE awarded **$900m task orders each** to American Centrifuge Operating / Centrus and General Matter in January 2026 for HALEU enrichment capacity.

**FACT:** Centrus's July 2026 DOE contract calls for expansion of its Piketon facility to commercial-scale HALEU production.

**FACT:** X-energy and Centrus signed a long-term LEU / HALEU agreement in August 2026 intended to secure a portion of initial fuel for X-energy's 11.5 GW commercial pipeline.

**FACT:** Oklo disclosed a Centrus letter of intent for HALEU deliveries beginning in **2029** for up to five Aurora powerhouses.

**FACT:** TerraPower's Natrium uses HALEU; its first Wyoming unit is targeted around **2031**.

### HALEU enrichment / deconversion score: **4.7 / 5 — Gate A passed**

**Important caveats:**

- not every advanced reactor requires HALEU;
- demand timing depends on reactor licensing / construction actually occurring;
- DOE procurement / allocations can shape economics heavily;
- new domestic suppliers are being deliberately subsidized into existence.

**INTERPRETATION:** HALEU is one of the strongest technical bottlenecks, but it is closer to a **venture / policy-enabled market** than a mature industrial shortage. Do not capitalize announced reactor pipelines as certain fuel demand.

---

## 10. Fuel fabrication is fragmented by reactor architecture

After enrichment, uranium must be fabricated into a qualified fuel form.

Conventional LWR fuel is mature but highly regulated. Advanced reactors introduce new forms such as:

- TRISO particles / compacts;
- metallic fuels;
- sodium fast-reactor fuel;
- molten-salt-related fuel forms;
- higher-assay LWR / LEU+ products.

**INTERPRETATION:** Advanced-reactor diversity creates two opposing effects:

1. high qualification barriers and scarce specialized lines;
2. fragmented demand that can prevent one supplier from achieving large scale.

### Conventional fuel fabrication: **4.0 / 5**
### Advanced / HALEU fuel fabrication: **4.4 / 5**

**Decision:** advanced fuel is strategically important, but later Investment Capture should prefer suppliers with signed fuel agreements / qualified lines rather than exposure to generic “advanced nuclear.”

---

## 11. Ultra-large forgings and nuclear heavy components are a real physical bottleneck

Large reactors require highly specialized reactor vessels, vessel shells, steam generators, pressurizers and other components with exacting material and QA requirements.

**FACT:** DOE's 2024 near-net-shape manufacturing report states that there is **no U.S. domestic capacity** to produce the largest nuclear forged / cast components; these large components are produced overseas.

**FACT:** Japan Steel Works states that it operates two **14,000-ton presses** and supplies monoblock nuclear-reactor pressure-vessel forgings from ultra-large high-quality steel ingots.

**FACT:** X-energy signed a **reservation agreement** with Doosan Enerbility to pre-secure forgings for **16 Xe-100 reactors**.

**FACT:** Doosan signed a 2026 contract to manufacture major Natrium reactor structures for TerraPower's first Wyoming project.

**FACT:** Doosan also secured 2026 strategic-manufacturing work for Rolls-Royce SMR and continues supplying ultra-large steam-generator forgings for conventional reactors.

**INTERPRETATION:** Reservation agreements are particularly important evidence. Developers are securing manufacturing slots / materials before full fleet deployment, indicating concern about future qualified capacity.

### Large nuclear forgings / long-lead heavy components: **4.5 / 5 — Gate A passed**

**Architecture resilience:** Medium-High. Exact components differ by reactor design, but heavy nuclear-qualified structures persist across many large-reactor and SMR architectures.

---

## 12. Nuclear-grade pumps, valves, I&C and electrical equipment form a qualified supplier layer

Nuclear equipment must meet safety-class requirements, documentation, traceability and long operating-life expectations.

Relevant layers include:

- reactor coolant / feedwater pumps;
- safety and isolation valves;
- control-rod / drive equipment;
- heat exchangers / steam generators;
- instrumentation and control;
- nuclear-qualified electrical systems;
- seals, fasteners, specialty materials and inspection.

### Nuclear-qualified component layer: **4.2 / 5**

**INTERPRETATION:** This is more fragmented than enrichment or large forgings, but qualification creates switching costs and a smaller supplier universe than general industrial equipment.

**OPEN QUESTION:** Which public component suppliers have enough nuclear-specific revenue sensitivity for a buildout to change total-company earnings?

---

## 13. Specialist EPC, QA and workforce may be as scarce as hardware

Nuclear plants require licensed engineering, nuclear-quality construction, documentation, welding / inspection, commissioning and operational training.

**FACT:** DOE's 2025 workforce analysis says **63% of nuclear power manufacturing employers** reported that finding qualified workers was “very difficult,” the highest of any single electric-power generation sector in that survey.

**FACT:** More than 80% of employers across nuclear construction, manufacturing, professional services and utilities reported at least some hiring difficulty.

**FACT:** DOE's Vogtle retrospective notes that the domestic nuclear supply chain and skilled workforce had been reduced substantially after a generation without new U.S. reactor construction, contributing to delays and cost increases.

**INTERPRETATION:** Workforce is not merely a labor-cost issue. Nuclear QA, procedures, certifications and accumulated project experience create a slow-learning constraint.

### Nuclear EPC / qualified workforce / QA score: **4.4 / 5 — Gate A passed**

**Investment implication:** The best capture may be in specialist engineering / components / services with recurring installed-base work, not construction labor itself.

---

## 14. New large reactors: strong supply-chain demand, weak near-term speed-to-power

**FACT:** DOE announced a **$17.5bn conditional nuclear supply-chain financing program** in June 2026 aimed at long-lead items for up to **10 AP1000 reactors**.

**FACT:** DOE says advance procurement of long-lead equipment can shorten project timelines by up to three years and explicitly intends the program to rebuild U.S. manufacturing capacity.

**INTERPRETATION:** This is excellent evidence that long-lead supply-chain capacity is a real constraint.

But even under an accelerated program, the objective is to have 10 large reactors **under construction by 2030**, not operating before 2030.

### Conventional new-build supply-chain scarcity: **4.4 / 5**
### Near-term AI speed-to-power relevance through 2030: **2.5 / 5**
### 2030s relevance: **High**

**Decision:** treat large-reactor supply-chain names as a long-duration industrial buildout, not the immediate answer to current data-centre power shortages.

---

## 15. SMRs / advanced reactors: real commercial demand, but deployment risk dominates today

Hyperscaler commitments are substantial:

- Google / Kairos: 50 MW in 2030, up to 500 MW by 2035;
- Meta / TerraPower: 690 MW as early as 2032, up to 2.8 GW by 2035;
- Meta / Oklo: up to 1.2 GW, targeted as early as 2030;
- Amazon / X-energy: 320 MW initial Energy Northwest deployment in early 2030s, potential 960 MW at that site and >5 GW U.S. option set through 2039.

**INTERPRETATION:** The customer demand signal is credible. The unresolved question is conversion from agreements / funding into repeatable licensed plants at predictable cost and schedule.

Common cross-architecture bottlenecks include:

- fuel / enrichment;
- forgings / qualified structures;
- nuclear-grade pumps / valves / I&C;
- licensing / QA;
- specialist EPC / commissioning;
- grid / transformer availability.

### Advanced-reactor / SMR industrialization: **4.3 / 5 technical / supply-chain difficulty**
### Commercial confidence before first repeat units: **Medium-Low**

**Decision:** avoid treating every SMR developer as equivalent. Prefer cross-architecture supply bottlenecks until repeat-unit economics are demonstrated.

---

## 16. Licensing / regulation is a major constraint but not a merchant profit pool by itself

Restart, uprate and new-reactor projects all depend on regulatory approval.

**FACT:** NRC's Crane restart process requires restoration of the operating licensing basis, component readiness and dedicated inspection / oversight.

**INTERPRETATION:** Regulatory process can be a 4+ severity bottleneck in schedule terms, but like large-load grid queue friction it is **not automatically an investable supplier layer**.

### Regulatory / licensing friction: **4.5 / 5 schedule constraint; not a standalone merchant Gate-A layer**

Potential economic capture sits in:

- experienced nuclear engineering;
- safety analysis / licensing support;
- qualified testing / inspection;
- proven reference designs;
- suppliers whose components already have regulatory pedigree.

---

## 17. Turbine-generator and grid layers reconnect nuclear to the existing energy map

A nuclear reactor still requires:

- steam turbine / generator;
- transformers;
- switchgear / protection;
- transmission;
- grid interconnection;
- cooling / heat rejection.

**INTERPRETATION:** Nuclear does not replace the previously validated energy bottlenecks. It **feeds into them**.

A new nuclear plant can therefore shift the constraint from fuel / reactor construction to:

```text
nuclear project
→ long-lead components / EPC
→ turbine-generator
→ transformers / switchgear
→ transmission
→ data-centre electrical backbone
→ cooling
```

The final E2E synthesis should avoid double counting common equipment layers.

---

## 18. Common-basis scorecard

| Nuclear layer / pathway | Bottleneck / scarcity score | AI timing | Gate A interpretation |
|---|---:|---|---|
| Existing operating nuclear asset | **4.6 asset scarcity** | **Now** | scarce asset, not supplier Gate A |
| Restart pathway | **4.4** | 2027+ | rare brownfield pathway, not scalable market |
| Uprates | **4.2** | 2026–2032 | valuable but limited total MW |
| Uranium mining | **3.5** | all periods | important commodity, not strongest bottleneck |
| UF6 conversion | **4.3** | all periods | **Gate A passed narrowly** |
| Western LEU enrichment | **4.6** | all periods | **Gate A passed** |
| HALEU enrichment / deconversion | **4.7** | advanced reactors | **Gate A passed**, narrow / policy-dependent |
| Conventional fuel fabrication | **4.0** | all periods | qualified but more mature |
| Advanced fuel fabrication | **4.4** | 2030s | likely structural; fragmented by design |
| Large forgings / heavy reactor components | **4.5** | 2030s build cycle | **Gate A passed** |
| Nuclear-grade pumps / valves / I&C | **4.2** | restart + new build | qualified supplier layer |
| Nuclear EPC / QA / workforce | **4.4** | restart + new build | **Gate A passed** |
| New large reactor pathway | **4.4 supply-chain** | mostly 2030s output | structural build constraint, poor near-term timing |
| SMR / advanced industrialization | **4.3** | 2030s | real demand; repeat economics unproven |
| Licensing / regulation | **4.5 schedule friction** | all pathways | not standalone merchant layer |

---

## 19. What this changes in the broader energy thesis

The prior energy thesis was:

> AI energy is primarily a speed-to-power and speed-to-usable-compute problem.

Nuclear refines it:

> **Nuclear can add highly valuable firm power, but nuclear itself is a chain of time-dependent bottlenecks. Near-term value sits in existing licensed assets, restarts and selected uprates; long-duration value shifts into enrichment, qualified fuel, forgings, nuclear-grade components and specialist delivery capacity.**

This means nuclear should not be treated as one line item called “generation.”

The investment frontier now needs two time horizons:

### 2026–2030

- existing fleet / life extension;
- contracted nuclear output;
- restarts;
- selected uprates;
- enrichment / conversion support for the existing fleet;
- outage / nuclear-qualified service capacity.

### 2030s

- HALEU / advanced fuel;
- advanced reactor fleets;
- large-reactor long-lead items;
- forgings / vessels / steam generators;
- nuclear EPC / skilled workforce;
- repeat-build economics and installed-base service.

---

## 20. Supplier archetypes for later Investment Capture

No company is promoted in this deep dive.

### Fuel cycle

- **Cameco** — uranium + Western conversion + Westinghouse exposure; diversified nuclear chain, but company size / valuation and commodity sensitivity matter.
- **Urenco** — major Western enrichment supplier; not conventionally listed.
- **Orano** — conversion / enrichment / fuel-cycle platform; largely state-controlled / not a simple listed equity.
- **Centrus Energy** — direct HALEU / enrichment optionality and DOE contracts; high policy / execution / valuation risk.

### Heavy components / manufacturing

- **Doosan Enerbility** — strong evidence across conventional reactor forgings, X-energy reservation agreements, TerraPower major equipment and Rolls-Royce SMR.
- **Japan Steel Works** — ultra-large forging capability; nuclear is only part of the business.
- **BWX Technologies** — nuclear-qualified components / services; commercial / naval mix must be separated.
- **Curtiss-Wright** — qualified nuclear components / aftermarket; AI sensitivity may be diluted by broader industrial exposure.

### Reactor / asset platforms

- **Constellation** / **Vistra** — existing-fleet economics / data-centre PPAs rather than supply-chain scarcity.
- **Westinghouse / Cameco-Brookfield** — AP1000 / fuel / service platform; indirect public exposure through Cameco / Brookfield structures.
- **GE Hitachi, TerraPower, X-energy, Oklo, Kairos, Rolls-Royce SMR** — architecture / developer exposure; commercial maturity varies materially.

**OPEN QUESTION:** Which listed company offers the best combination of direct exposure to a validated nuclear bottleneck, repeatable service economics, architecture resilience and a valuation that does not assume full nuclear-renaissance success?

---

## 21. Falsification / thesis breakers

The nuclear bottleneck thesis weakens if:

- Western enrichment expansions eliminate scarcity faster than reactor demand grows;
- U.S. / European policy reverses support or relaxes Russian-fuel restrictions materially;
- advanced-reactor projects slip well beyond current 2030–2035 targets;
- HALEU-requiring designs lose share to LEU / LEU+ alternatives;
- standardized reactor designs allow a much broader manufacturing base to qualify rapidly;
- DOE long-lead-item programs overbuild nuclear manufacturing capacity before projects reach final investment decision;
- existing-fleet PPAs prove to be mostly financial reshuffling without life-extension / incremental MW value;
- restart projects reveal materially worse component / licensing economics than current estimates;
- nuclear construction cost / schedule performance prevents repeat orders after first units.

The thesis strengthens if:

- more hyperscalers prepay for fuel / capacity / equipment;
- enrichment and conversion remain sold forward despite announced expansions;
- reactor developers sign additional reservation agreements for forgings / qualified components;
- restart / uprate projects achieve schedule and budget targets;
- multiple advanced-reactor designs reach commercial operation around 2030–2032;
- service / fuel contracts create long-duration recurring economics around installed reactors.

---

## 22. Decision

### Near-term nuclear AI power

**Best pathway:** existing fleet → life extension / contracted output → restart → uprate.

Do not rely on new nuclear construction to solve the 2026–2029 AI-power gap.

### Nuclear supply-chain Gate A

- **HALEU enrichment / deconversion: 4.7 — PASSED**
- **Western LEU enrichment: 4.6 — PASSED**
- **Large forgings / heavy nuclear-qualified components: 4.5 — PASSED**
- **Nuclear EPC / qualified workforce / QA: 4.4 — PASSED**
- **UF6 conversion: 4.3 — PASSED narrowly**

### Monitoring / secondary

- uranium mining: 3.5;
- conventional fuel fabrication: 4.0;
- generic “SMR exposure”: do not promote without project / fuel / manufacturing evidence;
- licensing friction: severe schedule constraint but not standalone investment layer.

### Programme implication

Issue #51 should now rebuild the canonical E2E energy map with nuclear as an explicit branch and with **two timing horizons**: near-term speed-to-power versus 2030s industrial buildout.

---

## Sources

### Existing fleet / restart / uprates

- Constellation — Crane / Microsoft PPA: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Constellation — Crane current restart path: https://www.constellationenergy.com/about/locations/crane-clean-energy-center.html
- NRC — Crane restart oversight: https://www.nrc.gov/info-finder/reactors/ccec
- DOE — Crane restart financing: https://www.energy.gov/edf/crane-restart
- NRC — Palisades restart: https://www.nrc.gov/info-finder/reactors/pali
- NRC — expected power uprates: https://www.nrc.gov/reactors/operating/licensing/power-uprates/status-power-apps/expected-applications
- Constellation — Meta / Clinton: https://www.constellationenergy.com/news/2025/constellation-meta-sign-20-year-deal-for-clean-reliable-nuclear-energy-in-illinois.html
- Meta — 2026 nuclear agreements: https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/
- Vistra 2025 10-K / Meta PPAs: https://www.sec.gov/Archives/edgar/data/1692819/000169281926000006/vistra-20251231.htm

### Fuel cycle

- Cameco — Port Hope conversion: https://www.cameco.com/businesses/fuel-services/conversion-port-hope
- Cameco 2025 annual filing: https://www.cameco.com/sites/default/files/documents/Cameco%202025%20Form%2040-F.pdf
- World Nuclear Association — uranium enrichment: https://world-nuclear.org/information-library/Nuclear-Fuel-Cycle/Conversion-Enrichment-and-Fabrication/Uranium-Enrichment
- Urenco USA — June 2026 current expansion: https://www.urenco.com/news/uusa/2026/urenco-usa-continues-successful-installation-of-us-uranium-enrichment-capacity
- Urenco USA — 2.1m SWU future expansion: https://www.urenco.com/news/uusa/2026/urenco-usa-plans-significant-expansion-of-u.s.-capacity
- Orano — Georges Besse II expansion: https://www.orano.group/en/news/news-group/2025/november/progress-on-orano-s-uranium-enrichment-plant-expansion-project-visit-by-the-european-investment-bank
- DOE — $2.7bn enrichment awards: https://www.energy.gov/articles/us-department-energy-awards-27-billion-restore-american-uranium-enrichment
- DOE — HALEU enrichment services: https://www.energy.gov/ne/haleu-enrichment-services
- Centrus Q2 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1065059/000162828026053863/leu-20260630.htm
- X-energy / Centrus HALEU agreement: https://x-energy.com/news/x-energy-centrus-sign-haleu-supplyagreement-for-xe-100-advanced-small-modular-reactor-development/
- Oklo Q2 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1849056/000162828026054571/oklo-20260630.htm

### Components / manufacturing / workforce

- DOE — near-net-shape / nuclear forgings report: https://www.energy.gov/sites/default/files/2024-02/near-net-shape-workshop-report-2024.pdf
- Japan Steel Works — reactor pressure-vessel forgings: https://www.jsw.co.jp/en/product/business/material_engineering/me_0600/
- Doosan — X-energy forging reservation: https://www.doosanenerbility.com/en/about/news_board_view?id=21000788
- Doosan — TerraPower Natrium equipment: https://www.doosanenerbility.com/en/about/news_board_view?id=21000823
- Doosan — Rolls-Royce SMR manufacturing: https://www.doosan.com/en/media-center/press-release_view?id=20172793
- DOE — 2025 nuclear workforce trends: https://www.energy.gov/ne/articles/3-workforce-trends-nuclear-energy-2025
- DOE — AP1000 nuclear supply-chain loans: https://www.energy.gov/articles/department-energy-announces-american-nuclear-supply-chain-loans

### Advanced-reactor AI demand

- Google / Kairos first 50 MW project: https://blog.google/company-news/outreach-and-initiatives/sustainability/google-first-advanced-nuclear-reactor-project-with-kairos-power-and-tennessee-valley-authority/
- Kairos / Google fleet: https://www.kairospower.com/google
- X-energy Q2 2026 10-Q / Amazon: https://www.sec.gov/Archives/edgar/data/2088896/000119312526347752/xe-20260630.htm
- Meta / TerraPower / Oklo / Vistra: https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/
- Reuters — TerraPower timing / HALEU / Meta: https://www.reuters.com/business/energy/gates-backed-terrapower-targets-british-nuclear-power-plant-start-by-2034-2026-09-07/
