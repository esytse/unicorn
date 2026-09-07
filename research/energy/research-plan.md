# AI Energy / Power Delivery — Research Plan

**Status:** Active — final structural-bottleneck validation before synthesis  
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

> **Which layers determine speed-to-power for large AI loads, and which suppliers own those constraints?**

Initial end-to-end map: `research/energy/value-chain.md`.

## Validated bottlenecks

| Workstream | Bottleneck Strength | State | Main caveat |
|---|---:|---|---|
| **Transformers / critical substation equipment** | **4.7 / 5** | **Gate A passed** | large global capacity additions should gradually reduce scarcity through 2027–2030 |
| **Physical transmission deliverability** | **4.7 / 5** | **Gate A passed** | flexible service, reconductoring and GETs can reduce required greenfield build |
| **Large gas-turbine equipment / manufacturing slots** | **4.6 / 5** | **Gate A passed** | GE / Siemens / Mitsubishi capacity expansion and non-gas substitutes cap long-run scarcity |
| **MV/HV switchgear** | **4.4 / 5** | **Gate A passed** | broader qualified supplier base and somewhat faster capacity expansion than LPTs |
| **Integrated data-centre electrical backbone** | **4.3 / 5** | **Gate A passed** | broader multi-vendor supply; scarcity is integration / qualification / delivery rather than one uniquely scarce component |
| **Integrated behind-the-meter power / microgrid architecture** | **4.1 / 5** | **Gate A passed narrowly** | component supply is broad; value sits in site architecture, orchestration, protection, execution and time-to-power rather than generic generation/storage |

Canonical deep dives:

- `research/energy/deep-dives/transformers-grid-equipment.md`
- `research/energy/deep-dives/transmission-large-load.md`
- `research/energy/deep-dives/dispatchable-generation.md`
- `research/energy/deep-dives/electrical-backbone-800vdc.md`
- `research/energy/deep-dives/behind-the-meter-microgrids.md`

### Important distinctions

**Large-load interconnection-process friction is not itself treated as a durable investable bottleneck.** It is a real current constraint, but FERC/RTO reforms, flexible service, co-location and stronger project screening can reduce it materially. The durable layer is the **physical network / equipment / engineering required by credible loads that remain after screening**.

**Reciprocating gensets / distributed generation are demand beneficiaries rather than validated structural scarcity.** They score **3.6/5** because modularity, broader supplier choice and substitution make supply more elastic than advanced large turbines.

**800 VDC is a validated architecture transition, not yet a validated broad supplier bottleneck.** Technical pressure scores roughly **4.3/5**, but supplier scarcity is only about **3.6/5** today because Google / Microsoft / NVIDIA are deliberately creating an open interoperable OCP ecosystem with 80+ participants. Future scarcity may emerge in specific MVAC-to-DC conversion, DC protection, busway/connectors or high-power DC/DC layers.

**Generic battery / BESS hardware is a growth layer, not a structural scarcity layer.** #47 scores it **3.4/5**. Storage becomes strategically important for dynamic AI loads and resilience, but broad cell/system supply and technology substitution weaken durable pricing power.

## Current validation priority

| Priority | Workstream | Initial score / status | Why next |
|---:|---|---|---|
| 1 | **Cooling / heat rejection** | **4.1 provisional** | final major coupled constraint on converting electrical MW into usable compute |
| 2 | **800 VDC narrow sub-layers** | **3.6 supplier scarcity today** | investigate only if direct qualification / margin evidence identifies a concentrated new bottleneck |

After cooling, **stop broad bottleneck discovery and synthesize the energy frontier** unless new evidence reveals a materially different function.

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

1. **Cooling / heat rejection** — map direct-to-chip liquid cooling, CDUs, heat exchangers, pumps, chillers / dry coolers, facility water and controls as the final major coupled constraint on usable electrical capacity.
2. Run an **interim energy synthesis** after cooling. Rank validated functions by structural scarcity, architecture resilience and likely merchant economic capture.
3. Compare supplier Investment Capture across **transformers / switchgear, transmission EPC / GETs, large turbines, integrated data-centre electrical infrastructure and BTM integration** on one common basis.
4. Only then move to capital-allocation / valuation work.

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

Company underwriting should begin only when enough of the power-delivery functions are validated to compare supplier capture across the energy frontier rather than promoting the first bottleneck studied.
