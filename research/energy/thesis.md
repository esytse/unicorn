# AI Energy / Power Delivery — Working Thesis

**Status:** Structural bottleneck map, common-basis ranking, supplier underwriting and Gate C capital allocation complete; valuation / earnings monitoring  
**Confidence:** **High** on the coupled speed-to-power / speed-to-usable-compute thesis; **Medium-High** on leading supplier capture; **Medium** on normalized valuation scenarios  
**Last substantive update:** 2026-09-08

## Current thesis

**FACT:** The IEA's 2026 work projects global data-centre electricity consumption rising from about **485 TWh in 2025 to ~950 TWh in 2030**, while AI-focused facilities grow materially faster than the overall data-centre fleet.

**INTERPRETATION:** The research does not support framing AI energy as a simple electricity-volume shortage.

The stronger conclusion is:

> **AI infrastructure is constrained by speed-to-power and speed-to-usable-compute: the ability to secure, generate, transmit, transform, protect, distribute and thermally reject large blocks of power at the required location and timetable.**

This is a **serial constrained system**. Removing one constraint often shifts the bottleneck elsewhere rather than eliminating it.

## Canonical chain

> **site / power rights → primary energy / fuel → generation → generation equipment → transmission → substation / transformers / switchgear → site distribution → behind-the-meter power → data-centre electrical backbone → grid-to-rack conversion → compute**, with **cooling / heat rejection** and **energy management / load flexibility** as coupled constraints.

Nuclear adds an explicit upstream branch:

> **uranium → conversion → enrichment / HALEU where required → fuel fabrication → qualified forgings / components → nuclear EPC / QA → reactor / turbine-generator → the same transformer / transmission / electrical / cooling chain.**

The canonical map and bottleneck-migration logic are in `research/energy/value-chain.md`.

## Validated bottleneck frontier

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

Near-term nuclear power is primarily an **existing-fleet / life-extension / restart / uprate** story. Most new large and advanced reactors remain a 2030s pathway.

## Common-basis economic-capture ranking

The completed ranking deliberately separates structural scarcity from merchant economic capture.

Current supplier-underwriting order by bottleneck/function:

1. **large gas turbines / manufacturing slots / long-duration service**;
2. **transformers + MV/HV switchgear**;
3. **integrated thermal systems / qualified cooling capacity**;
4. **integrated data-centre electrical infrastructure + BTM orchestration**.

**Western LEU enrichment / UF6 conversion** remains a separate strategic nuclear lane.

**INTERPRETATION:** A supplier is most interesting when it owns a function that remains necessary after architectures change and can convert scarcity into backlog, pricing, qualification, service or lifecycle economics.

## Company capture — Gate B complete

The supplier underwriting validates meaningful capture at several companies:

- **GE Vernova — 4.4/5:** clearest gas-turbine scarcity → reservation/backlog → service-economics chain;
- **Vertiv — 4.4/5:** highest direct AI-infrastructure sensitivity across electrical, thermal and BTM architecture;
- **Eaton — 4.3/5:** high-quality diversified electrical platform with architecture-resilient content;
- **Siemens Energy — 4.3/5:** gas-turbine and grid scarcity plus service economics, offset by Gamesa risk;
- **HD Hyundai Electric — 4.2/5:** direct transformer sensitivity and strong current economics;
- **nVent — 4.2/5:** smaller electrical + thermal platform with higher total-company AI sensitivity.

Specialist / higher-risk investigations include **Hainan Jinpan, Centrus Energy and Modine**.

## Gate C capital allocation — current conclusion

The completed capital-allocation work reaches the same conclusion as the memory programme:

> **The bottlenecks are real and the companies are capturing them, but most obvious beneficiaries already price in a substantial portion of the buildout.**

**No energy company passes strict Gate C at the September 2026 reference prices.**

The current normalized capital-monitoring order is:

1. **Siemens Energy** — preferred current monitor; base return ~**11.2%**, ~12% zone **~€144** versus ~€148 reference;
2. **nVent** — second monitor; base ~**10.5%**, ~12% zone **~$147** versus ~$156;
3. **Vertiv** — exceptional business / AI sensitivity, but valuation-bound; base ~**8.5%**, ~12% zone **~$245** versus ~$281;
4. **Hainan Jinpan** — higher-risk specialist; base ~**8.4%**, ~12% zone **~CNY59**;
5. **Centrus Energy** — event-driven nuclear optionality, not conventional compounding; ~12% base-value zone **~$147**;
6. **Modine** — strong thermal demand but FCF / concentration risk; base ~**7.7%**, ~12% zone **~$165**;
7. **HD Hyundai Electric** — strong transformer capture, current valuation reduces asymmetry; ~12% zone **~KRW606k**;
8. **Eaton** — high-quality diversified platform, ~12% zone **~$325**;
9. **GE Vernova** — strongest Gate-B capture but the weakest current-price asymmetry in the normalized screen; ~12% zone **~$702**.

**INTERPRETATION:** **Best business ≠ best expected return.** Gate A scarcity, Gate B company capture and Gate C valuation must remain separate decisions.

No company is promoted to `High-conviction research candidate`.

## What the research has rejected or narrowed

The evidence does **not** support several broad thematic shortcuts:

- interconnection queue MW is not a credible demand forecast or durable merchant bottleneck by itself;
- generic BESS hardware is not structurally scarce (**3.4/5**);
- reciprocating gensets benefit from demand but remain relatively substitutable (**3.6/5**);
- 800 VDC is a major architecture transition, but broad supplier scarcity is only about **3.6/5** because the ecosystem is deliberately open;
- liquid cooling can be technically mandatory while generic cold plates / CDUs remain multi-source (~**3.8/5 supplier scarcity**);
- uranium mining is not the tightest nuclear layer (**3.5/5**); downstream conversion, enrichment and qualified manufacturing are scarcer;
- generic SMR exposure should not be promoted before actual licensed repeat deployment / fuel / manufacturing evidence.

## Bottleneck migration remains central

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

## What would strengthen the thesis further?

- customers continuing to reserve or prepay qualified capacity;
- scarcity translating into persistent price / margin / service economics after announced factory expansions;
- physical transmission and transformer demand remaining strong after speculative data-centre projects are screened out;
- BTM architectures continuing to move rather than remove scarcity;
- nuclear enrichment / component reservation extending beyond government-supported first-of-a-kind projects;
- multi-MW thermal qualification narrowing the practical supplier set despite open interfaces;
- architecture-resilient suppliers gaining content as 800 VDC and liquid cooling mature;
- normalized earnings / FCF rising enough to move Gate C return zones toward current prices.

## What would weaken it?

- AI campus construction falling far below funded / contracted pipelines;
- transformer, turbine, cooling or electrical capacity expansions removing schedule premiums without sustained service economics;
- transmission reform / reconductoring unlocking sufficient capacity with limited new equipment demand;
- rapid standardisation commoditising integrated systems faster than technical complexity rises;
- hyperscaler vertical integration materially reducing merchant supplier capture;
- advanced nuclear projects slipping well beyond current 2030–2035 windows;
- efficiency improvements reducing total site MW and rack heat density materially faster than compute demand grows;
- current operating winners failing to convert backlog into normalized earnings / FCF while valuations remain elevated.

## Current decision state

Broad bottleneck discovery is complete by default. The energy programme is now a **valuation / earnings / evidence monitoring system**.

Re-open capital work when:

- a monitored company crosses its ~12% return zone without deterioration in the operating thesis;
- earnings / FCF materially raise the normalized return zone;
- a specialist materially improves qualification, customer-diversification or cash-conversion evidence;
- new architecture or supply expansion changes the common-basis bottleneck ranking.

The next substantive cross-theme discovery stream is **robotics actuators (#3)**.

## Canonical supporting documents

- `research/energy/value-chain.md` — end-to-end chain and bottleneck-migration map
- `research/energy/synthesis-ranking.md` — common-basis bottleneck economic-capture ranking
- `research/energy/investment-capture.md` — Gate B supplier underwriting
- `research/energy/capital-allocation.md` — Gate C scenarios and monitoring zones
- `research/energy/deep-dives/` — source-backed bottleneck validation
- `watchlist.md` — cross-theme status and current monitoring questions

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
