# AI Energy / Power Delivery — Research Plan

**Status:** Active — structural-bottleneck validation phase  
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

Canonical deep dives:

- `research/energy/deep-dives/transformers-grid-equipment.md`
- `research/energy/deep-dives/transmission-large-load.md`
- `research/energy/deep-dives/dispatchable-generation.md`

### Important distinctions

**Large-load interconnection-process friction is not itself treated as a durable investable bottleneck.** It is a real current constraint, but FERC/RTO reforms, flexible service, co-location and stronger project screening can reduce it materially. The durable layer is the **physical network / equipment / engineering required by credible loads that remain after screening**.

**Reciprocating gensets / distributed generation are demand beneficiaries rather than validated structural scarcity.** They score **3.6/5** because modularity, broader supplier choice and substitution make supply more elastic than advanced large turbines.

## Current validation priority

| Priority | Workstream | Initial score / status | Why next |
|---:|---|---|---|
| 1 | **Data-centre electrical backbone** | **4.4 preliminary** | high content per MW / rack and strong order evidence; closest layer to physical AI buildout |
| 2 | **800 VDC / grid-to-rack power architecture** | **4.2 technical preliminary** | major architecture transition; supplier capture not yet established |
| 3 | **Behind-the-meter / microgrid + storage** | **4.1 / 3.9 preliminary** | grid bypass / flexibility value; integration economics need testing |
| 4 | **Cooling / heat rejection** | **4.1 provisional** | coupled constraint on usable compute; separate deep dive warranted |

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

1. **Data-centre electrical backbone** — determine whether integrated MV/LV power portfolios capture structurally higher content / margins or merely more volume.
2. **AC → hybrid → 800 VDC** — identify scarce conversion, protection, busway and power-semiconductor sub-layers versus a broad open ecosystem.
3. **Behind-the-meter / microgrid + storage** — test durable integration economics versus temporary grid-queue workaround.
4. **Cooling / heat rejection** — separate coupled bottleneck map after core electrical validation.
5. After these core functions, compare supplier Investment Capture across **transformers / switchgear, transmission EPC / GETs, large turbines and data-centre electrical infrastructure** on one basis.
6. Only then move to capital-allocation / valuation work.

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
