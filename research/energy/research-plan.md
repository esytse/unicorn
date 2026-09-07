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
| **Transformers / critical substation equipment** | **4.7 / 5** | **Gate A passed** | very large global capacity additions should gradually reduce scarcity through 2027–2030 |
| **MV/HV switchgear** | **4.4 / 5** | **Gate A passed** | broader qualified supplier base and somewhat faster capacity expansion than LPTs |

Canonical deep dive: `research/energy/deep-dives/transformers-grid-equipment.md`.

The conclusion is deliberately narrower than "electrical equipment wins": qualified transformer capacity is structurally scarce today, while supplier-level economics still need later underwriting.

## Current validation priority

| Priority | Workstream | Initial score / status | Why next |
|---:|---|---|---|
| 1 | **Large-load interconnection / transmission** | **4.8 / 4.7 preliminary** | likely highest system-level speed-to-power constraint; need to separate policy scarcity from investable hardware |
| 2 | **Dispatchable generation equipment** | **4.4 preliminary** | direct backlog / manufacturing-capacity evidence; need concentration and service-economics test |
| 3 | **Data-centre electrical backbone** | **4.4 preliminary** | high content per MW / rack and strong order evidence |
| 4 | **800 VDC / grid-to-rack power architecture** | **4.2 technical preliminary** | major architecture transition; supplier capture not yet established |
| 5 | **Behind-the-meter / microgrid + storage** | **4.1 / 3.9 preliminary** | grid bypass / flexibility value; integration economics need testing |
| 6 | **Cooling / heat rejection** | **4.1 provisional** | coupled constraint on usable compute; separate deep dive warranted |

## Transformer validation result (#36)

The first full Gate-A-style pass finds that the transformer shortage is **structural through the late 2020s rather than permanent**.

Evidence supporting persistence:

- DOE still reports 1–2+ year distribution-transformer and 3–4 year large-transformer lead times;
- specialized factory / test equipment itself can take years to add;
- >80,000 U.S. distribution-transformer variants reduce fungibility and factory efficiency;
- large transformers remain heavily customized, difficult to transport and qualification-sensitive;
- raw-material / component dependence, including GOES, reduces supply elasticity;
- customers are paying extreme logistics costs for urgent hyperscale transformer delivery;
- GE Vernova / Prolec, Hitachi Energy, Eaton and others show strong backlog / order and capacity-expansion evidence.

Evidence against permanence:

- Hitachi Energy is deploying >$9bn globally across manufacturing / engineering;
- GE Vernova is investing about $1bn in Prolec GE through 2028 plus other grid capacity;
- Eaton and other vendors are expanding transformer / switchgear production;
- DOE is explicitly trying to standardise transformer specifications and reduce SKU fragmentation.

**Decision:** treat transformers as validated, but monitor lead-time normalization, capacity additions and backlog/margin changes before company underwriting.

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

1. **Large-load interconnection / transmission** — separate regulatory / queue scarcity from equipment and service profit pools.
2. **Dispatchable generation equipment** — compare GE Vernova, Siemens Energy, Mitsubishi Heavy and distributed-generation alternatives at the function level.
3. **Data-centre electrical backbone** — determine whether integrated grid-to-chip portfolios capture structurally higher content / margins or merely volume.
4. **AC → hybrid → 800 VDC** — identify scarce conversion, protection, busway and power-semiconductor sub-layers versus a broad open ecosystem.
5. **Behind-the-meter / microgrid + storage** — test durable integration economics versus temporary grid-queue workaround.
6. **Cooling / heat rejection** — separate coupled bottleneck map after core electrical validation.
7. Only after the major functions are validated, open company-level Investment Capture work on a common basis.

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

Reference suppliers in `value-chain.md` and the transformer deep dive are **starting points only**. Do not move a company to `Watch` or `High-conviction research candidate` from theme exposure alone.

Company underwriting should begin only when enough of the power-delivery functions are validated to compare supplier capture across the energy frontier rather than promoting the first bottleneck we studied.
