# AI Energy / Power Delivery — Research Plan

**Status:** Active — value-chain validation phase  
**Created:** 2026-09-07  
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

## Preliminary priority order

| Priority | Workstream | Initial score / status | Why next |
|---:|---|---|---|
| 1 | Transformers + substations / switchgear | **4.8 / 4.5** | Longest physical lead times; high architecture resilience |
| 2 | Large-load interconnection / transmission | **4.8 / 4.7** | Highest system-level constraint; determines speed-to-power |
| 3 | Dispatchable generation equipment | **4.4** | Direct backlog / manufacturing-capacity evidence |
| 4 | Data-centre electrical backbone | **4.4** | High content per MW / rack and strong order evidence |
| 5 | 800 VDC / grid-to-rack power architecture | **4.2 technical** | Major architecture transition; supplier capture not yet established |
| 6 | Behind-the-meter / microgrid + storage | **4.1 / 3.9** | Grid bypass / flexibility value; integration economics need testing |
| 7 | Cooling / heat rejection | **4.1 provisional** | Coupled constraint on usable compute; separate deep dive warranted |

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

1. Deep dive transformers / critical grid equipment.
2. Separate policy/process scarcity from investable hardware in interconnection/transmission.
3. Compare turbine / generator OEM supply capacity and service economics.
4. Map the AC → hybrid → 800 VDC component stack and identify genuinely scarce sub-layers.
5. Test microgrid / onsite power as a durable profit pool versus a temporary response to grid queues.
6. Only then open company-level Investment Capture work.

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

Reference suppliers in `value-chain.md` are **starting points only**. Do not move a company to `Watch` or `High-conviction research candidate` from theme exposure alone.

Company underwriting should begin only after the relevant function passes structural bottleneck validation.
