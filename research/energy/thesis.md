# AI Energy / Power Delivery — Working Thesis

**Status:** Research stream opened  
**Confidence:** Medium on demand / grid-delivery constraint; Low-Medium on company-level value capture  
**Last substantive update:** 2026-09-07

## Current thesis

**FACT:** The IEA's 2026 update projects global data-centre electricity consumption rising from about **485 TWh in 2025 to ~950 TWh in 2030**, while AI-focused data-centre consumption grows much faster than the total. The IEA also says local energy-system bottlenecks are already limiting the most aggressive near-term buildout scenarios.

**HYPOTHESIS:** The most important AI-energy constraint is not simply aggregate electricity generation. It is the ability to deliver **reliable, connectable, controllable megawatts at the required location and timetable**.

**INTERPRETATION:** This shifts the investment search away from generic exposure to electricity demand and toward the layers that determine **speed-to-power**: large-load interconnection, transmission/substations, transformers, switchgear, dispatchable generation equipment, behind-the-meter systems and the data-centre power-delivery architecture itself.

## Why AI is different from ordinary load growth

- Large AI campuses concentrate hundreds of megawatts or more in one location rather than distributing demand broadly.
- AI rack power density is rising much faster than conventional data-centre density, forcing changes in facility and rack-level power architecture.
- AI workloads can create fast power swings, increasing the importance of storage, UPS, controls and grid/load flexibility.
- Data-centre shell / compute deployment can move faster than transmission, generation and grid-equipment build cycles.

## Initial thesis

The working chain is:

> **fuel / primary energy → generation → transmission → large-load interconnection → substations / transformers / switchgear → site distribution → onsite generation / storage / microgrid → data-centre power conversion and distribution → rack-level power delivery → compute**

Cooling / heat rejection is a coupled capacity constraint rather than a simple downstream step, and load flexibility / controls can feed back upstream by reducing required firm grid capacity.

## Initial bottleneck hypothesis

The highest-priority layers to test are:

1. **large-load interconnection / transmission deliverability**;
2. **large and distribution transformers / substation equipment**;
3. **dispatchable generation equipment and turbine slots**;
4. **medium-/low-voltage switchgear and data-centre electrical distribution**;
5. **grid-to-rack power conversion, including the 800 VDC transition**;
6. **behind-the-meter storage, UPS and microgrid orchestration**.

The thesis is **not** that every company exposed to data-centre power demand will earn excess returns. Company-level capture still requires evidence on backlog, pricing, qualification, capacity expansion, competition, capital intensity and valuation.

## What would strengthen the thesis?

- persistent multi-year lead times for critical power equipment despite capacity additions;
- large-load connection delays that remain binding even as generation grows;
- supplier backlog / pricing evidence showing economic capture rather than volume alone;
- standards or architecture transitions that increase content per MW or raise qualification barriers;
- customers paying premiums for speed-to-power, onsite generation or integrated power systems;
- evidence that higher rack density creates new power-electronics / distribution bottlenecks.

## What would weaken it?

- grid/interconnection reforms materially shorten connection timelines without shifting scarcity elsewhere;
- rapid transformer, turbine or switchgear capacity additions erase pricing / lead-time power;
- open standards create broad substitutability before suppliers establish durable differentiation;
- AI efficiency improvements materially reduce site-level power requirements;
- announced data-centre demand proves materially overstated or duplicative;
- hyperscalers vertically integrate enough power infrastructure to commoditise merchant suppliers.

## Open questions

1. Which constraint is currently most binding: generation, grid connection, transformers/substations, onsite power or facility distribution?
2. Which bottlenecks are global versus region-specific?
3. Where do long lead times reflect temporary capacity shortages versus durable qualification / engineering barriers?
4. Which layers gain content per MW as rack density moves toward 200 kW, 600 kW and eventually MW-scale racks?
5. Does 800 VDC create a concentrated new supplier layer or an open ecosystem with limited pricing power?
6. Which smaller listed or private suppliers have disproportionate earnings sensitivity without already-large valuations?
7. Where does cooling become the binding constraint even if electrical power is available?

## Core sources

- IEA — Key Questions on Energy and AI, 2026: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- IEA — Energy and AI / Energy demand from AI: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- IEA — Energy supply for AI: https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai
- FERC — large-load integration orders, 18 June 2026: https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration
- US DOE — Distribution Transformer webinar, 2026: https://www.energy.gov/oe/distribution-transformer-webinar-text-alternative
- NVIDIA — 800 VDC architecture, August 2026: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
