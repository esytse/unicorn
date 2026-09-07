# AI Energy / Power Delivery — Working Thesis

**Status:** Structural bottleneck map validated; moving to cross-layer ranking and company underwriting  
**Confidence:** **High** on the coupled speed-to-power / speed-to-usable-compute thesis; **Medium** on supplier-level value capture before common-basis underwriting  
**Last substantive update:** 2026-09-07

## Current thesis

**FACT:** The IEA's 2026 work projects global data-centre electricity consumption rising from about **485 TWh in 2025 to ~950 TWh in 2030**, while AI-focused facilities grow materially faster than the overall data-centre fleet.

**INTERPRETATION:** The research no longer supports framing AI energy as a simple electricity-volume shortage.

The stronger conclusion is:

> **AI infrastructure is constrained by speed-to-power and speed-to-usable-compute: the ability to secure, generate, transmit, transform, protect, distribute and thermally reject large blocks of power at the required location and timetable.**

This is a **serial constrained system**. Removing one constraint often shifts the bottleneck elsewhere rather than eliminating it.

## Canonical chain

> **site / power rights → primary energy / fuel → generation → generation equipment → transmission → substation / transformers / switchgear → site distribution → behind-the-meter power → data-centre electrical backbone → grid-to-rack conversion → compute**, with **cooling / heat rejection** and **energy management / load flexibility** as coupled constraints.

Nuclear adds an explicit upstream branch:

> **uranium → conversion → enrichment / HALEU where required → fuel fabrication → qualified forgings / components → nuclear EPC / QA → reactor / turbine-generator → the same transformer / transmission / electrical / cooling chain.**

The canonical map and bottleneck-migration logic are in `research/energy/value-chain.md`.

## What has been validated

### Immediate 2026–2030 physical bottlenecks

- **transformers / critical substation equipment — 4.7/5**;
- **physical transmission deliverability — 4.7/5**;
- **large gas-turbine equipment / manufacturing slots — 4.6/5**;
- **integrated thermal chain / qualified cooling capacity — 4.4/5**;
- **MV/HV switchgear — 4.4/5**;
- **integrated data-centre electrical backbone — 4.3/5**;
- **DTC liquid-cooling and facility heat-rejection functions — 4.2/5**;
- **integrated behind-the-meter / microgrid architecture — 4.1/5**.

### Nuclear supply-chain bottlenecks

- **HALEU enrichment / deconversion — 4.7/5**, mainly tied to 2030s advanced-reactor demand;
- **Western LEU enrichment — 4.6/5**;
- **large nuclear forgings / long-lead heavy components — 4.5/5**;
- **nuclear EPC / QA / qualified workforce — 4.4/5**;
- **UF6 conversion — 4.3/5**.

Near-term nuclear power is primarily an **existing-fleet / life-extension / restart / uprate** story. Most new large and advanced reactors are a 2030s pathway.

## What the research has rejected or narrowed

The evidence does **not** support several broad thematic shortcuts:

- interconnection queue MW is not a credible demand forecast or durable merchant bottleneck by itself;
- generic BESS hardware is not structurally scarce (**3.4/5**);
- reciprocating gensets benefit from demand but remain relatively substitutable (**3.6/5**);
- 800 VDC is a major architecture transition, but broad supplier scarcity is only about **3.6/5** because the ecosystem is deliberately open;
- liquid cooling can be technically mandatory while generic cold plates / CDUs remain multi-source (~**3.8/5 supplier scarcity**);
- uranium mining is not the tightest nuclear layer (**3.5/5**); downstream conversion, enrichment and qualified manufacturing are scarcer;
- generic SMR exposure should not be promoted before actual licensed repeat deployment / fuel / manufacturing evidence.

## Bottleneck migration is central to the thesis

Examples:

```text
grid queue reform
→ physical transmission / substation work remains
```

```text
grid delay
→ onsite power
→ turbine / gas / permit / electrical constraints
→ cooling constraint
```

```text
new nuclear demand
→ enrichment / HALEU
→ forgings / qualified components
→ EPC / workforce
→ transformer / transmission / cooling constraints downstream
```

```text
54 VDC architecture reaches limits
→ 800 VDC
→ value shifts toward conversion / protection / busway
→ open standards reduce broad supplier lock-in
```

**INTERPRETATION:** A supplier is more interesting when it owns the **function that remains necessary after the architecture changes**, not merely the current implementation.

## Investment hypothesis

The programme should now stop broad bottleneck discovery and test which companies satisfy four conditions simultaneously:

1. **validated structural bottleneck exposure**;
2. **direct enough revenue / margin sensitivity for AI demand to change normalized earnings**;
3. **architecture resilience plus qualification / service economics**;
4. **valuation / company size that leaves meaningful asymmetry**.

Bottleneck strength and stock attractiveness remain separate gates.

## What would strengthen the thesis further?

- customers continuing to reserve or prepay qualified capacity;
- scarcity translating into persistent price / margin / service economics after announced factory expansions;
- physical transmission and transformer demand remaining strong after speculative data-centre projects are screened out;
- more evidence that BTM architectures move rather than remove bottlenecks;
- nuclear enrichment / component reservation extending beyond government-supported first-of-a-kind projects;
- multi-MW thermal qualification narrowing the practical supplier set despite open interfaces;
- evidence that architecture-resilient suppliers gain content as 800 VDC / liquid cooling mature.

## What would weaken it?

- AI campus construction falling far below funded / contracted pipelines;
- transformer, turbine, cooling or electrical capacity expansions removing schedule premiums without sustained service economics;
- transmission reform / reconductoring unlocking sufficient capacity with limited new equipment demand;
- rapid standardisation commoditising integrated systems faster than technical complexity rises;
- hyperscaler vertical integration materially reducing merchant supplier capture;
- advanced nuclear projects slipping well beyond current 2030–2035 windows, reducing enrichment / manufacturing demand;
- efficiency improvements reducing total site MW and rack heat density materially faster than compute demand grows.

## Next decision gate

Issue #52 ranks the validated bottlenecks on a common basis including:

- structural scarcity;
- AI-specific sensitivity;
- supplier concentration;
- supply elasticity;
- qualification / switching cost;
- architecture resilience;
- pricing / backlog / margin evidence;
- service economics;
- capital intensity / overbuild risk;
- timing;
- investable supplier availability.

Only a small top tier should proceed to company Investment Capture #53, followed by capital allocation #54.

## Core sources

The canonical value-chain and deep dives contain the recoverable source set. Key starting points include:

- IEA — Key Questions on Energy and AI, 2026: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- IEA — Energy and AI / Energy demand from AI: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- FERC — large-load integration action, 18 June 2026: https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration
- US DOE — Distribution Transformer webinar: https://www.energy.gov/oe/distribution-transformer-webinar-text-alternative
- NVIDIA — 800 VDC architecture: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
- ASHRAE / PNNL / NEMA — AI Data Center Energy Performance Framework: https://www.ashrae.org/technical-resources/ai-data-center-framework
- US DOE — uranium enrichment awards: https://www.energy.gov/articles/us-department-energy-awards-27-billion-restore-american-uranium-enrichment
- US DOE — American Nuclear Supply Chain Loans: https://www.energy.gov/articles/department-energy-announces-american-nuclear-supply-chain-loans
