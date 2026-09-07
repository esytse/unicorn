# AI Energy / Power Delivery — Research Plan

**Status:** Active — structural discovery complete; canonical E2E synthesis next  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Validate which AI power-delivery constraints are structural, then underwrite only the suppliers that capture the economics.

## Decision framework

Keep three questions separate:

1. **Bottleneck:** Is the function genuinely scarce / difficult to substitute?
2. **Investment Capture:** Does a supplier capture enough pricing, share or content for AI power demand to materially change earnings?
3. **Capital Allocation:** Does valuation leave enough risk-adjusted upside after normalizing the cycle?

## Current hypothesis

The highest-value question is not "who generates more electricity?" but:

> **Which layers determine speed-to-power and speed-to-usable-compute for large AI loads, and which suppliers own those constraints?**

The initial end-to-end map in `research/energy/value-chain.md` is now intentionally stale. Issue #51 will replace preliminary scores with the full validated chain, including nuclear and cooling, and explicitly map bottleneck migration.

## Validated bottlenecks

| Workstream | Bottleneck Strength | State | Main caveat |
|---|---:|---|---|
| **HALEU enrichment / deconversion** | **4.7 / 5** | **Gate A passed** | narrow / policy-shaped market; demand depends on advanced-reactor execution |
| **Transformers / critical substation equipment** | **4.7 / 5** | **Gate A passed** | large global capacity additions should gradually reduce scarcity through 2027–2030 |
| **Physical transmission deliverability** | **4.7 / 5** | **Gate A passed** | flexible service, reconductoring and GETs can reduce required greenfield build |
| **Western LEU enrichment** | **4.6 / 5** | **Gate A passed** | major expansions are underway, but meaningful new capacity arrives gradually |
| **Large gas-turbine equipment / manufacturing slots** | **4.6 / 5** | **Gate A passed** | GE / Siemens / Mitsubishi capacity expansion and non-gas substitutes cap long-run scarcity |
| **Large nuclear forgings / long-lead heavy components** | **4.5 / 5** | **Gate A passed** | new-build demand is mostly a 2030s output story and designs differ |
| **Integrated thermal chain / qualified cooling capacity** | **4.4 / 5** | **Gate A passed** | open interfaces and aggressive capacity additions weaken generic component scarcity |
| **MV/HV switchgear** | **4.4 / 5** | **Gate A passed** | broader qualified supplier base and somewhat faster capacity expansion than LPTs |
| **Nuclear EPC / QA / qualified workforce** | **4.4 / 5** | **Gate A passed** | labor / delivery scarcity is real but hard to translate into attractive listed economics |
| **UF6 conversion** | **4.3 / 5** | **Gate A passed narrowly** | concentrated Western footprint, but less technically scarce than enrichment |
| **Integrated data-centre electrical backbone** | **4.3 / 5** | **Gate A passed** | broader multi-vendor supply; scarcity is integration / qualification / delivery rather than one uniquely scarce component |
| **DTC liquid-cooling function** | **4.2 / 5** | **Gate A passed as function** | generic cold-plate / CDU supplier scarcity is only ~3.8 because of standardisation / multi-sourcing |
| **Facility heat-rejection function** | **4.2 / 5** | **Gate A passed** | heat rejection persists, but chillers / dry coolers / towers / hybrid implementations can migrate |
| **Integrated behind-the-meter power / microgrid architecture** | **4.1 / 5** | **Gate A passed narrowly** | component supply is broad; value sits in site architecture, orchestration, protection, execution and time-to-power rather than generic generation/storage |

Canonical deep dives:

- `research/energy/deep-dives/transformers-grid-equipment.md`
- `research/energy/deep-dives/transmission-large-load.md`
- `research/energy/deep-dives/dispatchable-generation.md`
- `research/energy/deep-dives/electrical-backbone-800vdc.md`
- `research/energy/deep-dives/behind-the-meter-microgrids.md`
- `research/energy/deep-dives/cooling-heat-rejection.md`
- `research/energy/deep-dives/nuclear-supply-chain.md`

### Important distinctions

**Large-load interconnection-process friction is not itself treated as a durable investable bottleneck.** It is a real current constraint, but FERC/RTO reforms, flexible service, co-location and stronger project screening can reduce it materially. The durable layer is the **physical network / equipment / engineering required by credible loads that remain after screening**.

**Reciprocating gensets / distributed generation are demand beneficiaries rather than validated structural scarcity.** They score **3.6/5** because modularity, broader supplier choice and substitution make supply more elastic than advanced large turbines.

**800 VDC is a validated architecture transition, not yet a validated broad supplier bottleneck.** Technical pressure scores roughly **4.3/5**, but supplier scarcity is only about **3.6/5** today because Google / Microsoft / NVIDIA are deliberately creating an open interoperable OCP ecosystem with 80+ participants. Future scarcity may emerge in specific MVAC-to-DC conversion, DC protection, busway/connectors or high-power DC/DC layers.

**Generic battery / BESS hardware is a growth layer, not a structural scarcity layer.** #47 scores it **3.4/5**. Storage becomes strategically important for dynamic AI loads and resilience, but broad cell/system supply and technology substitution weaken durable pricing power.

**Cooling is now validated as part of the capacity path, not an auxiliary load.** The integrated thermal chain scores **4.4/5**, but the investment target should be architecture-resilient thermal capacity / engineering rather than generic cold plates, CDUs or one particular chiller topology.

**Nuclear must be split by time horizon.** Existing nuclear output, restarts and selected uprates can affect power availability before 2030. Most new large reactors and commercial advanced-reactor fleets are 2030s supply. The strongest nuclear supply-chain scarcity sits downstream of uranium in **enrichment, HALEU, conversion, qualified forgings/components and specialist delivery capacity**.

## Current synthesis / underwriting priority

| Priority | Workstream | Status | Why next |
|---:|---|---|---|
| 1 | **Canonical E2E refresh (#51)** | Open | reconcile all preliminary scores, integrate nuclear + cooling, separate 2026–2030 from 2030s pathways, and map bottleneck migration across the full chain |
| 2 | **Cross-layer bottleneck ranking (#52)** | Open | rank structural scarcity, AI sensitivity, architecture resilience, economic capture and capital intensity before proliferating company work |
| 3 | **Supplier Investment Capture (#53)** | Open | underwrite only the top-ranked layers on one common company basis |
| 4 | **Capital allocation (#54)** | Open | valuation / scenario / margin-of-safety gate after company capture is validated |

Broad bottleneck discovery is now complete. Do not reopen it unless evidence identifies a materially different physical function or a narrow 800 VDC / nuclear sub-layer with direct qualification / pricing evidence.

## Transformer validation result (#36)

Transformers are **structurally scarce through the late 2020s rather than permanently scarce**. DOE lead times, custom engineering, factory/test capacity, qualification, transport and component dependence support Gate A; Hitachi / Prolec / Eaton capacity additions and DOE standardisation are the main evidence against permanence.

## Transmission validation result (#38)

**Physical transmission deliverability passes Gate A at 4.7/5.** DOE's 2026 Needs Study identifies pressing transmission needs driven partly by data centres and other large loads, while major regions are approving record transmission portfolios.

The work also separates physical scarcity from queue/process friction:

- FERC's June 2026 reforms can shorten connection by enabling flexible service, co-location and integrated load/generation studies;
- SPP / ERCOT are redesigning large-load processes;
- raw queue MW materially overstates credible demand because of duplicate / speculative "ghost demand";
- advanced reconductoring, dynamic line rating and power-flow control can unlock existing corridors faster than greenfield lines.

**Decision:** treat physical transmission as validated, but seek investment capture in **EPC / engineering, grid equipment, advanced conductors / GETs, substations and related physical solutions**, not in the queue process itself.

## Dispatchable-generation validation result (#41)

**Large gas-turbine equipment / manufacturing slots pass Gate A at 4.6/5.** GE Vernova had 116 GW of backlog / slot reservations at Q2 2026 versus roughly 20 GW of 2026 annual output; Siemens Energy is sold out through FY2028 with FY2029 filling rapidly and identifies blades / vanes as the principal production bottleneck; Mitsubishi Power provides a third qualified advanced-class supplier and has direct dedicated data-centre deployment evidence.

The strongest economic-capture evidence is unusually direct:

- multi-year customer reservations;
- favorable new-unit pricing / margin quality;
- concentrated advanced-class OEM supply;
- gradual rather than immediate factory expansion;
- long-lived aftermarket / service economics.

**Decision:** validate the function, but do not promote GE Vernova, Siemens Energy or Mitsubishi Heavy Industries before common-basis Investment Capture and valuation work. AI is an important marginal accelerator, not the only driver of the turbine cycle.

## Electrical-backbone / 800 VDC validation result (#45)

**The integrated data-centre electrical backbone passes Gate A at 4.3/5.** Eaton, Schneider and Vertiv provide direct 2026 evidence of strong order / backlog growth with attractive or expanding margins, while ABB confirms broad source-to-rack architecture investment. The bottleneck is less concentrated than transformers or turbines, but qualification, system integration, delivery sequencing and very high system criticality make it structural.

The architecture work changes the conclusion for 800 VDC:

- Google, Microsoft and NVIDIA are standardising 800 VDC through OCP;
- the technical transition is now credible and increasingly necessary at very high rack power;
- more than 80 suppliers are already building compatible infrastructure;
- open interfaces are explicitly intended to reduce fragmentation and enable interoperability;
- therefore **800 VDC as a broad category does not pass supplier-scarcity Gate A**.

**Decision:** focus later underwriting on architecture-resilient functions and only investigate narrow 800 VDC sub-layers if direct evidence of qualification scarcity / pricing power emerges. Do not treat generic 800 VDC exposure as a moat.

## Behind-the-meter validation result (#47)

**Integrated behind-the-meter power / microgrid architecture passes Gate A narrowly at 4.1/5, Medium confidence.** The economic function is not generic onsite generation. It is the ability to design, permit, protect and orchestrate a site-specific mix of grid service, firm generation, BESS/UPS and dynamic AI load so a campus can energise sooner and operate reliably.

Key evidence and caveats:

- Vertiv's September 2026 agreement to acquire UtilityInnovation Group for ~$1.45bn upfront plus up to $1.15bn contingent consideration is strong strategic revealed preference for microgrid controls, BTM architecture and time-to-power capability;
- Siemens Energy + Eaton have a standardized 500 MW onsite architecture and market schedule compression of up to roughly two years;
- Mitsubishi Power's Cheyenne Power Hub demonstrates >1 GW dedicated onsite power is moving into real projects;
- Bloom/Brookfield's expanded $25bn financing framework confirms alternative onsite fuel-cell architecture has meaningful commercial momentum;
- IEA analysis is important falsification: reliable onsite gas can require **30–70% overbuild**, turbine queues remain a constraint and onsite power often shifts bottlenecks into gas pipelines, permits, land, equipment, storage and controls;
- generic BESS / battery hardware scores only **3.4/5** and does not pass Gate A;
- fuel cells remain an emerging alternative, not a broadly scarce function;
- gensets remain **3.6/5**, not Gate A.

**Decision:** treat integrated BTM architecture / controls / protection / execution as a moderate structural profit pool, while avoiding a broad “onsite power” scarcity thesis. Later Investment Capture should compare generation-agnostic integrators with the already validated scarce turbine OEMs and electrical-platform suppliers.

## Cooling / heat-rejection validation result (#49)

**Integrated thermal chain / qualified cooling capacity passes Gate A at 4.4/5, Medium-High confidence.** Cooling is a coupled capacity constraint because essentially every compute MW becomes heat that must be captured, transported and rejected before it becomes usable compute capacity.

Key evidence and caveats:

- ASHRAE / PNNL / NEMA guidance treats direct-to-chip liquid cooling as the dominant high-density AI/HPC path as air cooling reaches practical limits;
- Modine secured a >$4bn 2027–2029 capacity agreement with a strategic data-centre customer, including a $165m upfront payment to support supply expansion — unusually strong revealed preference for guaranteed cooling capacity;
- Modine's subsequent data-centre revenue rose 90% y/y while capacity-expansion / supply-chain effects compressed margins, showing both real demand and real execution constraints;
- Eaton's ~$9.5bn Boyd Thermal acquisition and Schneider / Vertiv thermal-platform expansion validate strategic value across the chip-to-ambient chain;
- OCP standardisation and rapid capacity additions by multiple vendors are strong evidence against generic cold-plate / CDU scarcity;
- facility heat rejection is unavoidable, but the implementation can migrate from chillers to dry / wet / hybrid systems as coolant temperatures and climate permit.

**Decision:** treat the integrated thermal chain as validated, with DTC and facility heat rejection at **4.2/5 function-level**. Generic liquid-cooling component scarcity is only about **3.8/5**. Later company underwriting should favor suppliers with architecture-resilient thermal-system capacity, qualification, testing, integration and service rather than generic liquid-cooling exposure.

## Nuclear supply-chain validation result (#50)

Nuclear changes the timing and location of the energy bottleneck rather than replacing the grid / electrical / cooling chain.

**Near-term pathway:** existing operating nuclear output → life extension / contracted output → selected restarts → uprates. Microsoft-backed Crane targets 835 MW from a brownfield restart, while Meta-backed agreements preserve / contract operating nuclear output and support uprates. NRC's expected uprate schedule totals about **2.42 GW electric through 2032**.

**Longer-duration pathway:** new large reactors / advanced reactors → fuel / enrichment → qualified heavy components → specialist EPC / commissioning → turbine / grid / cooling. Hyperscaler demand is credible, but most new commercial output is targeted for **2030–2035+**.

Validated nuclear scarcity:

- **HALEU enrichment / deconversion: 4.7/5** — limited commercial supply, DOE-backed capacity buildout, Centrus / advanced-reactor contracts;
- **Western LEU enrichment: 4.6/5** — concentrated major supplier base, geopolitical substitution pressure, new capacity arriving only gradually;
- **large nuclear forgings / long-lead heavy components: 4.5/5** — no U.S. capacity for the largest nuclear forgings in DOE's supply-chain work; X-energy has already reserved Doosan forging capacity;
- **nuclear EPC / QA / qualified workforce: 4.4/5** — persistent hiring / experience constraints after a generation with limited U.S. new build;
- **UF6 conversion: 4.3/5** — concentrated Western footprint; Cameco describes Port Hope as one of only three Western UF6 suppliers.

**Decision:** uranium mining itself is a weaker 3.5/5 bottleneck than downstream fuel-cycle / qualification layers. Do not treat generic SMR exposure as a validated investment thesis. The E2E synthesis must separate **2026–2030 power availability** from the **2030s nuclear industrial buildout**.

## Gate A-style validation criteria

Score each workstream 1–5 on:

- physical / engineering difficulty;
- supply elasticity / capacity expansion time;
- supplier concentration;
- qualification / switching cost;
- system criticality;
- architecture resilience;
- pricing / backlog evidence.

A preliminary score is **not** a validated bottleneck until contradictory evidence is tested.

## Immediate work

1. **E2E synthesis #51** — rebuild `research/energy/value-chain.md` using all validated evidence. Include explicit nuclear branches, cooling as a cross-cutting capacity path, two timing horizons and bottleneck migration.
2. **Cross-layer ranking #52** — rank the entire frontier on structural scarcity, AI sensitivity, architecture resilience, evidence quality, capital intensity and likely merchant capture; identify a small top tier.
3. **Investment Capture #53** — compare suppliers only after the structural ranking is fixed, including smaller specialists rather than defaulting to the obvious large-cap platforms.
4. **Capital allocation #54** — move to normalized return / valuation / margin-of-safety analysis only after company capture is validated.

## Falsification requirements

Every workstream must test:

- announced demand versus funded / credible projects;
- capacity additions already under construction;
- standardisation reducing product complexity;
- customer vertical integration;
- regional substitution / data-centre relocation;
- architecture changes that bypass the incumbent component;
- commodity input rather than supplier-specific economics;
- valuation already discounting the AI-power boom.

## Company discipline

Reference suppliers in the energy value-chain and deep dives are **starting points only**. Do not move a company to `Watch` or `High-conviction research candidate` from theme exposure alone.

Company underwriting should begin only after the E2E refresh and common-basis bottleneck ranking identify which generation / grid / fuel / thermal functions deserve concentrated Investment Capture work.
