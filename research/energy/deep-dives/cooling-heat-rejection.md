# AI Data-Centre Cooling + Heat Rejection — Bottleneck Deep Dive

**Status:** Integrated thermal chain validated; direct-to-chip liquid cooling is becoming mandatory at high density, but generic cold-plate / CDU exposure is not a concentrated moat  
**Bottleneck Strength:** **4.4 / 5 integrated thermal chain / cooling capacity**; **4.2 / 5 direct-to-chip liquid-cooling function**; **4.2 / 5 facility heat rejection function**; **3.8 / 5 generic liquid-cooling component supplier scarcity**  
**Confidence:** **Medium-High** on structural thermal constraint and integrated-system demand; **Medium** on supplier-level scarcity; **High** that the exact implementation will continue changing  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #49

## Executive conclusion

**CONCLUSION:** Cooling is the final major coupled bottleneck in the AI power chain and the **integrated thermal chain passes Gate A at 4.4/5**.

The reason is simple but economically important:

> **An electrical megawatt that cannot be rejected as heat is not a usable compute megawatt.**

At high rack density, air cooling is reaching practical limits and direct-to-chip (DTC) liquid cooling is becoming the dominant architecture. That makes the thermal path from silicon to ambient a mission-critical system:

```text
chip / package
  ↓
cold plate / thermal interface
  ↓
rack manifold / quick disconnects
  ↓
CDU / pumps / controls / heat exchanger
  ↓
facility water loop
  ↓
chiller / dry cooler / cooling tower / hybrid heat rejection
  ↓
ambient environment
```

But the investment conclusion is **not** “buy any liquid-cooling supplier.”

OCP is actively standardising cold-plate and liquid-cooling interfaces, multiple large electrical / thermal vendors are expanding capacity, and hyperscalers / ODMs can multi-source many components. The stronger scarcity is in **qualified system capacity, integrated engineering, deployment, testing and heat rejection at scale**, not in every cold plate or pump.

The strongest direct scarcity evidence is Modine's 2026 long-term capacity agreement: a strategic data-centre customer committed to more than **$4bn** of Airedale cooling products through 2029 and paid **$165m upfront** to support capacity investment. That is unusually strong revealed preference for guaranteed cooling capacity. Modine's next quarter then showed **90% year-over-year Data Centers revenue growth** while supply-chain constraints temporarily reduced segment margins — direct evidence that thermal demand can outrun production execution.

Strategic acquisitions reinforce the same conclusion. Eaton paid about **$9.5bn** for Boyd Thermal, whose forecast 2026 revenue included roughly **$1.5bn of liquid-cooling sales**. Schneider Electric acquired Motivair capabilities across CDUs, cold plates, chillers and technology-cooling loops. Vertiv acquired Strategic Thermal Labs for chip-side design / validation and ThermoKey for heat rejection while expanding chiller manufacturing.

The key falsification is architecture migration. High-temperature DTC liquid cooling can enable **chiller-less dry cooling**, reducing water use and bypassing part of the conventional mechanical-chiller stack. OCP standardisation can also reduce proprietary component lock-in. Therefore the durable investment target should own the **thermal function across architectures**, not one current cooling implementation.

---

## 1. Cooling is a coupled capacity constraint, not an auxiliary load

Traditional data-centre analysis often treats cooling as facility overhead. AI density changes that framing.

**FACT:** The PNNL / ASHRAE / NEMA AI Data Center Energy Performance Framework states that air cooling has reached practical limits for high-density deployments and that liquid cooling, particularly DTC cold-plate systems, is becoming the dominant AI/HPC approach.

**FACT:** ASHRAE describes DTC as emerging as the **de-facto thermal-management standard** for high-performance infrastructure and notes architectures capable of supporting racks upward of roughly **3 MW**.

**INTERPRETATION:** Thermal capacity now determines:

- which accelerators can be installed;
- rack density;
- usable MW per building;
- compute performance before thermal throttling;
- facility power overhead / PUE;
- water requirements;
- site climate suitability;
- electrical / cooling co-design.

The thermal system is therefore part of the **capacity path**, not a downstream accessory.

---

## 2. End-to-end thermal chain

### Chip / package level

- thermal interface materials;
- cold plates;
- microchannels / advanced heat spreaders;
- package and board mechanical interfaces.

### Rack / row level

- manifolds;
- hoses / tubing;
- quick disconnects;
- leak detection;
- rear-door heat exchangers in hybrid architectures;
- rack-level flow and pressure control.

### Technology Cooling System (TCS)

- coolant distribution units (CDUs);
- pumps;
- filters;
- heat exchangers;
- valves;
- sensors / controls;
- water chemistry / fluid management.

### Facility loop

- piping;
- pumps;
- plate heat exchangers;
- controls;
- redundancy and isolation.

### Heat rejection

- chillers;
- dry coolers;
- cooling towers;
- adiabatic hybrid coolers;
- refrigerant systems;
- heat pumps / heat reuse.

**INTERPRETATION:** The important architecture boundary is not “air versus liquid.” It is **where heat changes medium and where it finally leaves the site**.

Even a perfectly cooled GPU still requires facility-scale heat rejection.

---

## 3. Direct-to-chip liquid cooling is moving from optional to structural

**FACT:** ASHRAE's AI framework says DTC liquid cooling is the most mature liquid option and is expected to be the most widely used approach for high-density HPC / AI for the foreseeable future.

**FACT:** Schneider / Motivair states that GPU-intensive AI systems are pushing well beyond 100 kW/rack and designed for future densities approaching 1 MW and above.

**FACT:** Motivair introduced a **2.5 MW CDU** in 2026 and says its CDU architecture can scale to **10 MW+** in centralized deployments.

**FACT:** Vertiv's 2026 liquid-cooling products include multi-MW CDUs and modular hybrid infrastructure intended for high-density AI clusters.

**INTERPRETATION:** DTC is increasingly a **technical requirement**, not merely an efficiency upgrade, for the highest-density accelerators.

**COUNTERPOINT:** The technical requirement for liquid cooling does not mean any particular CDU / cold-plate vendor has a moat. The function can be supplied by multiple system vendors and increasingly standardized interfaces.

---

## 4. Modine provides direct evidence of cooling-capacity scarcity

This is the strongest economic evidence in the deep dive.

**FACT:** On 26 May 2026 Modine announced a long-term capacity agreement with a strategic data-centre customer covering **more than $4bn** of Airedale cooling products for 2027–2029.

**FACT:** The customer paid Modine **$165m upfront** to support capacity investments and other expenditures needed to guarantee supply.

**INTERPRETATION:** A customer pre-funding supplier capacity is strong revealed preference: schedule certainty / cooling availability has enough economic value to justify transferring capital to the vendor before products are delivered.

**FACT:** In Modine's Q1 FY2027, Data Centers segment sales rose **90% year over year to $348.6m**.

**FACT:** The same quarter's Data Centers gross margin fell materially because of North American capacity-expansion costs, production inefficiencies, material costs and supply-chain constraints, even while segment operating income increased.

**INTERPRETATION:** This is exactly the pattern expected in a genuine capacity-constrained buildout: demand and revenue rise rapidly, but supplier execution / upstream inputs can temporarily become the binding constraint.

**COUNTERPOINT:** Modine is expanding aggressively. Customer prepayments and new plants can remove scarcity over time. Current capacity value should not be capitalised as permanent monopoly economics.

---

## 5. Eaton's Boyd Thermal acquisition validates strategic value at the chip side

**FACT:** Eaton agreed in November 2025 to acquire Boyd Thermal for **$9.5bn**, or approximately **22.5x estimated 2026 adjusted EBITDA**.

**FACT:** Boyd forecast roughly **$1.7bn of 2026 revenue**, including approximately **$1.5bn from liquid cooling**.

**FACT:** Eaton completed the acquisition in March 2026 and positions Boyd as extending its data-centre offering from electrical power into chip-level and system-level thermal management.

**INTERPRETATION:** The price and strategic rationale are strong evidence that liquid cooling has become a critical adjacent profit pool for grid-to-chip infrastructure vendors.

**COUNTERPOINT:** Paying a high multiple is not evidence that Boyd itself is undervalued or that cold plates are scarce. Eaton may be paying for customer relationships, engineering, manufacturing footprint and portfolio integration as much as proprietary cooling technology.

---

## 6. Schneider / Motivair validates the integrated thermal-system model

**FACT:** Schneider's Motivair portfolio spans:

- dynamic cold plates;
- CDUs;
- rear-door heat exchangers;
- heat-dissipation units;
- chillers;
- technology-cooling-system loops;
- software / controls / services.

**FACT:** Motivair's 2026 MCDU-70 is rated at up to **2.5 MW** and designed to operate in multi-unit configurations beyond **10 MW**.

**FACT:** Schneider announced more than **$290m** of phased AI infrastructure solutions, including Motivair technologies, for TeraWulf's Lake Mariner campus in 2026.

**INTERPRETATION:** Cooling is increasingly sold as a validated **end-to-end system** rather than independent cold plates and chillers. This raises the economic value of reference designs, controls, commissioning, service and interface responsibility.

---

## 7. Vertiv is assembling the full thermal chain

**FACT:** Vertiv acquired Strategic Thermal Labs in April 2026 to add cold-plate design, server-side liquid-cooling expertise and high-density thermal validation.

**FACT:** Vertiv completed its acquisition of ThermoKey in June 2026 to expand heat-rejection / heat-exchange technology and manufacturing capability.

**FACT:** In July 2026 Vertiv announced investments intended to **double chiller production capacity** at its Tognana, Italy campus by the end of 2026 and add a large-scale testing laboratory in 2027.

**FACT:** Vertiv's liquid-cooling portfolio spans direct-to-chip, immersion, rear-door, CDU, fluid-network, heat-rejection, controls and service layers.

**INTERPRETATION:** Vertiv's sequence of acquisitions indicates that the valuable object is the **thermal chain** and its interfaces, not one isolated cooling product.

**COUNTERPOINT:** Vertiv also explicitly supports an open ecosystem. System integration can be valuable without component exclusivity.

---

## 8. nVent capacity expansion is evidence both for demand and against permanent scarcity

**FACT:** nVent announced its **third liquid-cooling manufacturing expansion in three years** in July 2026, adding a new 160,000-square-foot site and taking new liquid-cooling manufacturing space added over that period above 400,000 square feet.

**INTERPRETATION:** This is direct evidence of sustained demand growth.

**COUNTERPOINT:** It is also direct evidence that the industry can add supply. A liquid-cooling shortage is less structurally rigid than large-transformer or advanced gas-turbine manufacturing.

---

## 9. OCP standardisation is the strongest evidence against generic component moats

**FACT:** The Open Compute Project has a dedicated Cold Plate sub-project whose explicit objective is to **drive standardisation and enable an open ecosystem** for DTC liquid cooling.

**FACT:** OCP work covers standardized interfaces, technical guidelines and requirements from cold plate through the CDU / TCS environment.

**INTERPRETATION:** Standardisation should accelerate liquid-cooling adoption and reduce integration friction.

But it also creates a negative investment implication:

> **A standardized interface can expand the market while reducing vendor lock-in.**

Cold plates, manifolds, connectors and CDUs should therefore not receive high bottleneck scores merely because liquid cooling is mandatory.

---

## 10. Rack-level liquid cooling: technical necessity is stronger than supplier scarcity

### DTC liquid-cooling function score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **4.4** | high heat flux, flow balance, pressure drop, leak avoidance and chip / package interfaces |
| Supply elasticity | **4.0** | qualified manufacturing / testing matter, but many vendors are expanding |
| Supplier concentration | **3.4** | several global platforms, ODMs and specialists |
| Qualification / switching cost | **4.3** | server reference design, reliability and leak risk create meaningful qualification |
| System criticality | **4.9** | high-density accelerators cannot sustain performance without thermal control |
| Architecture resilience | **4.2** | liquid heat transport persists, but cold-plate / immersion / hybrid implementations can shift |
| Pricing / backlog evidence | **4.0** | strong demand and capacity investment; less isolated component-level pricing evidence |

**DTC function: 4.2 / 5 — Gate A PASSED as a technical function.**

### Generic component supplier scarcity

Because OCP standardisation and multi-vendor supply materially reduce concentration, **generic cold-plate / CDU / manifold supplier scarcity scores only ~3.8/5**.

**Decision:** do not treat generic liquid-cooling exposure as equivalent to a 4.2 bottleneck.

---

## 11. Facility heat rejection is architecture-resilient — but the equipment can migrate

After heat is captured at the rack it still must leave the site.

Possible architectures include:

- chilled-water plant;
- dry coolers;
- evaporative cooling towers;
- hybrid / adiabatic dry coolers;
- high-temperature refrigerant systems;
- heat-pump / reuse systems.

**FACT:** ASHRAE's AI framework describes warm-water liquid loops capable of enabling chiller-less designs with dry coolers in many climates.

**FACT:** The same framework notes that dry coolers require materially more physical footprint than wet cooling towers for a given large heat load and can require adiabatic assistance in extreme heat.

**INTERPRETATION:** **Heat rejection is unavoidable; chillers are not.**

This makes heat rejection highly architecture-resilient while creating implementation risk for vendors whose moat depends specifically on mechanical chillers.

### Facility heat-rejection score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **4.1** | tens/hundreds of MW thermal loads, climate, redundancy and fluid engineering |
| Supply elasticity | **4.1** | large equipment / factories / testing matter, but capacity can be expanded |
| Supplier concentration | **3.5** | several large HVAC / thermal OEMs |
| Qualification / switching | **4.2** | mission-critical reliability and facility-specific engineering |
| System criticality | **5.0** | every compute MW becomes heat that must ultimately leave the site |
| Architecture resilience | **4.8 function / 3.5 implementation** | heat rejection persists, exact chiller/dry/wet technology migrates |
| Pricing / capacity evidence | **4.3** | Modine capacity prepayment and industry expansions show schedule value |

**Heat-rejection function: 4.2 / 5 — Gate A PASSED.**

---

## 12. Water is a site constraint, but not a universal cooling bottleneck

**FACT:** High-temperature DTC liquid cooling can use closed-loop dry coolers and greatly reduce or eliminate evaporative cooling water in suitable climates.

**FACT:** ASHRAE notes that hotter climates may require adiabatic assist or mechanical cooling when ambient conditions exceed the dry-cooling envelope.

**INTERPRETATION:** Water constraints can influence site selection and architecture, but **water scarcity does not imply that AI cooling universally requires more water**.

The system can trade among:

- water consumption;
- electrical efficiency;
- cooling footprint;
- capital cost;
- climate exposure;
- chiller / dry-cooler capacity.

**HYPOTHESIS:** In water-constrained locations, the value pool may shift toward higher-temperature liquid loops, oversized dry coolers, hybrid heat rejection and controls rather than toward water rights themselves.

---

## 13. Warm-water / chiller-less architecture is both opportunity and disruption

**FACT:** ASHRAE describes high-temperature facility liquid operation up to roughly 45°C inlet as an enabler of direct dry-cooler heat rejection in many climates.

**FACT:** ASHRAE also records industry disagreement about how broadly this architecture can persist as chip heat flux and reliability requirements evolve.

**INTERPRETATION:** Warm-water cooling can:

- reduce chiller electricity;
- reduce or eliminate cooling-tower water;
- raise usable IT MW within a fixed site-power envelope;
- simplify portions of the mechanical plant.

But it can also:

- increase outdoor heat-rejection footprint;
- create extreme-weather limits;
- require different cold-plate / flow conditions;
- reduce content for conventional chiller vendors.

**Decision:** favour suppliers that own **heat-transfer / heat-rejection capability across chiller, dry, liquid and hybrid architectures** rather than relying on one plant topology.

---

## 14. Immersion remains a real but secondary architecture

**FACT:** Industry guidance continues to recognize immersion as technically viable for very high density.

**COUNTERPOINT:** ASHRAE notes operational / maintenance complexity and ecosystem resistance relative to DTC.

**INTERPRETATION:** Immersion is important as a substitute / thesis breaker for cold-plate suppliers, but it does not currently appear likely to displace DTC as the dominant near-term architecture.

**Decision:** do not open a separate immersion research stream absent evidence of materially faster commercial adoption.

---

## 15. Why integrated thermal systems pass Gate A

### 15.1 The function is physically mandatory

Nearly all electrical input to compute ultimately becomes heat.

### 15.2 Rack density raises difficulty faster than ordinary data-centre floor area

Higher heat flux, pressure / flow requirements, redundancy and leak risk make thermal design more complex.

### 15.3 Capacity is already being reserved / pre-funded

The Modine LTA is unusually direct evidence that customers value guaranteed supply.

### 15.4 System interfaces are difficult

Cold plate, rack manifold, CDU, facility loop and heat rejection must work together under changing load.

### 15.5 Testing / commissioning matters

High-density systems need factory and site validation to avoid catastrophic leak, flow, contamination or control failures.

### 15.6 Thermal capacity creates operating leverage for the customer

Efficient cooling reduces non-IT power and can increase compute capacity within a fixed electrical allocation.

### Integrated thermal-chain score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **4.5** | high heat flux + fluid systems + facility-scale heat rejection |
| Supply elasticity | **4.2** | plants/testing/engineering are expanding but current capacity is valuable |
| Supplier concentration | **3.7** | several global suppliers; not turbine-like concentration |
| Qualification / switching | **4.5** | reliability, leak risk, reference designs and commissioning |
| System criticality | **5.0** | no heat rejection = no usable compute capacity |
| Architecture resilience | **4.7** | thermal function persists while implementation migrates |
| Pricing / backlog evidence | **4.4** | capacity prepayment, acquisitions, rapid segment growth and expansions |

**Integrated thermal chain: 4.4 / 5 — Gate A PASSED.**

**Confidence: Medium-High.**

---

## 16. Evidence against a simplistic cooling-unicorn thesis

The cooling thesis can be right while most cooling stocks are unattractive.

Important counter-evidence:

- OCP standardisation can commoditise interfaces;
- nVent, Vertiv, Schneider, Eaton / Boyd, Modine and others are rapidly adding capacity;
- Asian ODM / thermal specialists can expand into standardized cold plates / manifolds;
- warm-water dry cooling can bypass mechanical chillers;
- immersion can bypass some cold-plate / manifold content;
- hyperscalers increasingly define reference architectures and can multi-source suppliers;
- customer concentration can become extreme when one hyperscaler reserves large supplier capacity;
- rapid production expansion can depress margins even during strong demand, as Modine's Q1 FY2027 demonstrates;
- liquid-cooling acquisitions have occurred at demanding strategic valuations.

**INTERPRETATION:** Cooling looks structurally attractive at the **function level**, but supplier Investment Capture must test margins, concentration, capex and valuation with the same discipline used in memory.

---

## 17. Supplier archetypes for Investment Capture

No status promotion is made in this deep dive.

### Integrated power + thermal platforms

- **Vertiv** — broad thermal chain plus electrical infrastructure; strong AI sensitivity; valuation must be normalized.
- **Schneider Electric / Motivair** — chip-to-chiller + electrical controls; diversified economics.
- **Eaton / Boyd Thermal** — grid-to-chip integration; Boyd adds a large direct liquid-cooling business but acquisition price raises return-on-capital questions.

### Thermal / heat-rejection specialists

- **Modine / Airedale** — strongest direct cooling-capacity scarcity evidence via $4bn LTA / customer prepayment; supply-chain / margin and customer-concentration risks are material.
- **nVent** — liquid-cooling manufacturing expansion plus electrical connection/protection exposure; needs company-level sensitivity / valuation work.

### Additional comparators

- Johnson Controls;
- Trane Technologies;
- Carrier;
- Delta Electronics;
- private / specialist DTC vendors and ODMs.

**OPEN QUESTION:** Which listed supplier combines direct AI thermal sensitivity, architecture resilience, capacity scarcity and a valuation that has not already capitalized the buildout?

---

## 18. Thesis breakers / monitoring

The integrated thermal thesis weakens if:

- accelerator efficiency / packaging materially slows rack heat-density growth;
- liquid-cooling interfaces standardize faster than complexity rises;
- supplier expansions eliminate delivery bottlenecks without margin persistence;
- hyperscalers move significant thermal design / manufacturing in-house;
- warm-water reference designs simplify facility thermal systems enough to reduce total equipment content per MW;
- AI campus construction falls far below announced / contracted pipelines;
- thermal suppliers win revenue but fail to convert it to FCF because capex, warranty, material and project-execution costs rise just as quickly;
- chip vendors broaden allowable cooling envelopes enough that commodity dry cooling dominates.

The thesis strengthens if:

- more customers prepay / sign LTAs for cooling capacity;
- DTC becomes mandatory across a larger share of AI racks;
- multi-MW CDU / heat-rejection qualification narrows the supplier set;
- high-temperature liquid loops increase total integrated thermal content while improving customer PUE;
- recurring controls / service / lifecycle revenue grows with installed thermal systems;
- supplier margins remain attractive after 2026–2028 capacity additions.

---

## 19. Decision

### Integrated thermal chain / qualified cooling capacity

**Gate A PASSED — 4.4 / 5, Medium-High confidence.**

### Direct-to-chip liquid-cooling function

**Gate A PASSED as a technical function — 4.2 / 5.**

But **generic component supplier scarcity is only ~3.8 / 5** because open standards and multi-vendor capacity reduce lock-in.

### Facility heat-rejection function

**Gate A PASSED — 4.2 / 5.**

Heat rejection is unavoidable, but exact equipment migrates between chillers, dry coolers, towers and hybrid systems.

### Water

**Important regional site constraint, not a universal AI cooling bottleneck.** High-temperature closed-loop dry cooling can materially reduce water dependence.

---

## 20. Energy-program implication

With cooling complete, broad energy bottleneck discovery should stop.

The validated frontier is now:

1. transformers / critical substation equipment — **4.7**;
2. physical transmission deliverability — **4.7**;
3. large gas-turbine equipment / manufacturing slots — **4.6**;
4. integrated thermal chain / cooling capacity — **4.4**;
5. MV/HV switchgear — **4.4**;
6. integrated data-centre electrical backbone — **4.3**;
7. facility heat rejection / DTC cooling functions — **4.2**;
8. integrated BTM power / microgrid orchestration — **4.1**.

The next step is **synthesis and Investment Capture**, not another wide discovery stream.

The cross-chain thesis is now stronger:

> **AI energy is a speed-to-power and speed-to-usable-compute problem. Power availability, electrical delivery and thermal rejection form one coupled capacity system.**

The best investment candidates should therefore be identified by asking which suppliers own architecture-resilient functions across that coupled system and capture enough economics for AI demand to change normalized earnings.

---

## Sources

### Neutral / standards evidence

- PNNL / ASHRAE / NEMA — AI Data Center Energy Performance Framework: https://www.ashrae.org/technical-resources/ai-data-center-framework
- ASHRAE — Integrated Design Principles: https://www.ashrae.org/technical-resources/ai-data-center-framework/integrated-design-principles
- ASHRAE — Energy and Thermal Efficiency: https://www.ashrae.org/technical-resources/ai-data-center-framework/energy-and-thermal-efficiency
- ASHRAE — Retrofit & Modernization Strategies: https://www.ashrae.org/technical-resources/ai-data-center-framework/retrofit-modernization-strategies
- Open Compute Project — Cold Plate sub-project: https://www.opencompute.org/community/cold-plate
- OCP — ACS Liquid Cooling Cold Plate Requirements: https://www.opencompute.org/documents/ocp-acs-liquid-cooling-cold-plate-requirements-pdf

### Supplier / commercial evidence

- Modine — $4bn cooling capacity agreement, 26 May 2026: https://investors.modine.com/news/news-details/2026/Modine-Announces-Landmark-4-Billion-Long-Term-Capacity-Agreement-through-2029-with-Strategic-Data-Center-Customer-for-Airedale-by-Modine-Cooling-Solutions/default.aspx
- Modine — Q1 FY2027 results, 29 Jul 2026: https://investors.modine.com/news/news-details/2026/Modine-Reports-First-Quarter-Fiscal-2027-Results/default.aspx
- Eaton — Boyd Thermal acquisition agreement / economics: https://www.eaton.com/us/en-us/company/news-insights/news-releases/2025/eaton-signs-agreement-to-acquire-boyd-thermal--expanding-solutio.html
- Eaton — completed Boyd Thermal acquisition, 12 Mar 2026: https://www.eaton.com/sg/en-us/company/news-insights/news-releases/2026/eaton-completes-acquisition-of-leading-liquid-cooling-solutions-provider-boyd-thermal.html
- Schneider Electric / Motivair — 2.5 MW CDU / 10 MW+ architecture, Jan 2026: https://www.se.com/ww/en/about-us/newsroom/news/press-releases/motivair-by-schneider-electric-announces-new-cdu-with-capability-to-scale-to-10mw-and-beyond-for-next-gen-ai-factories-6970111e5238242c6201a203/
- Schneider Electric / Motivair — end-to-end liquid cooling portfolio: https://www.se.com/ww/en/about-us/newsroom/news/press-releases/Schneider-Electric-Unveils-Liquid-Cooling-Portfolio-with-Motivair-Featuring-Dedicated-Solutions-and-Services-for-HPC-and-AI-Workloads-68d69e595c9dbb622505caf3/
- Schneider Electric — TeraWulf Lake Mariner >$290m infrastructure delivery, 26 May 2026: https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-progresses-phaseddelivery-of-over-290M-in-AI-Infrastructure-Solutions-including-Motivair-technologies-at-TeraWulf%E2%80%99s-GoogleBacked-Lake-Mariner-Campus-6a1514cee67b3015570e068a/
- Vertiv — Strategic Thermal Labs acquisition, 27 Apr 2026: https://investors.vertiv.com/news/news-details/2026/Vertiv-Strengthens-Liquid-Cooling-System-Capability-with-Acquisition-of-Strategic-Thermal-Labs/
- Vertiv — ThermoKey heat-rejection acquisition, Jun 2026: https://investors.vertiv.com/news/news-details/2026/Vertiv-Completes-Acquisition-of-ThermoKey-Expanding-Heat-Rejection-Portfolio-for-AI-Data-Centers/default.aspx
- Vertiv — thermal manufacturing expansion, Jul 2026: https://www.vertiv.com/en-in/about/news-and-events/news-releases/2026/vertiv-expands-global-manufacturing-capacity-for-ai-ready-data-center-cooling-solutions/
- nVent — third liquid-cooling capacity expansion in three years, 31 Jul 2026: https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Expands-Data-Center-Liquid-Cooling-Capacity/default.aspx
