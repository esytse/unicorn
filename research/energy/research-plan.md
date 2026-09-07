# AI Energy / Power Delivery — Research Plan

**Status:** Active — canonical E2E synthesis complete; cross-layer ranking next  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Identify which AI-energy bottlenecks create durable supplier economics, then allocate capital only where valuation leaves enough asymmetry.

## Decision framework

Keep three gates separate:

1. **Bottleneck / Gate A** — is the function genuinely scarce, difficult to substitute and slow to expand?
2. **Investment Capture / Gate B** — does a supplier convert the bottleneck into pricing, margin, share, content or recurring service economics?
3. **Capital Allocation / Gate C** — does current valuation leave attractive normalized risk-adjusted return and margin of safety?

## Canonical system thesis

The research now supports:

> **AI energy is a speed-to-power and speed-to-usable-compute problem. The chain is serial: site access → fuel → generation → generation equipment → transmission → transformers / switchgear → BTM / site power → data-centre electrical infrastructure → rack power → compute, with cooling / heat rejection as a coupled capacity path.**

Solving one constraint often **moves** the bottleneck rather than eliminating it.

Canonical E2E map: `research/energy/value-chain.md`.

## Validated frontier

| Workstream | Bottleneck Strength | Timing / caveat |
|---|---:|---|
| **HALEU enrichment / deconversion** | **4.7 / 5** | very scarce, but mostly 2030s advanced-reactor demand and policy-shaped |
| **Transformers / critical substation equipment** | **4.7 / 5** | immediate; capacity additions should gradually reduce scarcity |
| **Physical transmission deliverability** | **4.7 / 5** | immediate / long duration; merchant capture is dispersed |
| **Western LEU enrichment** | **4.6 / 5** | current fleet + future nuclear; concentrated supply |
| **Large gas-turbine equipment / slots** | **4.6 / 5** | immediate; unusually direct reservation / pricing / service evidence |
| **Large nuclear forgings / heavy components** | **4.5 / 5** | strong scarcity, mainly 2030s build cycle |
| **Integrated thermal chain / cooling capacity** | **4.4 / 5** | immediate; direct AI sensitivity, broader multi-vendor supply |
| **MV/HV switchgear** | **4.4 / 5** | immediate; highly architecture-resilient |
| **Nuclear EPC / QA / qualified workforce** | **4.4 / 5** | restart + 2030s; difficult to translate into listed margin capture |
| **UF6 conversion** | **4.3 / 5** | concentrated Western footprint |
| **Integrated data-centre electrical backbone** | **4.3 / 5** | very high AI sensitivity; broader supplier set |
| **DTC liquid cooling / facility heat rejection** | **4.2 / 5** | function-level scarcity; generic components weaker |
| **Integrated BTM / microgrid architecture** | **4.1 / 5** | integration / control / execution value, not generic hardware |

## Important non-bottleneck / narrowed conclusions

- Interconnection **process friction** is real but reformable; physical transmission and equipment are the durable constraints.
- Generic BESS hardware: **3.4/5**.
- Reciprocating gensets: **3.6/5**.
- Broad 800 VDC supplier scarcity: **~3.6/5** despite strong technical pressure.
- Generic cold-plate / CDU supplier scarcity: **~3.8/5** despite DTC becoming structurally important.
- Uranium mining: **3.5/5**, weaker than downstream nuclear fuel-cycle bottlenecks.
- Existing nuclear assets are strategically scarce but are an **asset-owner thesis**, not a supplier Gate-A score.
- New large / advanced nuclear should not be treated as a 2026–2029 power solution; most output is a 2030s pathway.

## Programme sequence

### 1. #52 — Cross-layer bottleneck ranking

Create `research/energy/synthesis-ranking.md` and rank the validated frontier on one basis:

- structural scarcity;
- direct AI demand sensitivity;
- supply elasticity / time to qualified capacity;
- supplier concentration;
- qualification / switching cost;
- architecture resilience;
- reservation / pricing / backlog / margin evidence;
- installed-base / service economics;
- capital intensity and overbuild risk;
- non-AI demand support / cyclicality;
- timing: 2026–2030 versus 2030s;
- availability of listed suppliers with material company-level sensitivity.

**Output:** small top tier for company research; monitoring / deprioritised layers for the rest.

### 2. #53 — Supplier Investment Capture

Underwrite only companies tied to the top-ranked functions. Do not default to obvious large caps; deliberately search for smaller specialists with greater earnings asymmetry.

Potential reference universe, not predetermined selections:

- gas turbines: GE Vernova, Siemens Energy, Mitsubishi Heavy Industries;
- transformers / electrical: Eaton, Schneider, ABB, Hitachi / Hitachi Energy, HD Hyundai Electric and smaller qualified specialists;
- transmission / grid enabling: Quanta and evidence-backed conductor / GET suppliers;
- cooling / integrated infrastructure: Vertiv, Modine, nVent, Schneider / Motivair, Eaton / Boyd and specialists;
- nuclear fuel / manufacturing: Centrus, Cameco, Doosan Enerbility, Japan Steel Works, BWX Technologies, Curtiss-Wright and relevant cross-architecture suppliers.

Score revenue sensitivity, pricing / margin capture, durability, service economics, capital intensity, customer concentration, architecture resilience, asymmetry and execution risk.

### 3. #54 — Capital allocation

Only after Gate B:

- refresh point-in-time valuation;
- normalize peak backlog / margins;
- bear / base / bull 3–5 year earnings or FCF;
- terminal multiples below / around normalized history;
- annualized return and downside;
- 10% / 12% / 15% reverse-return tests;
- monitoring / margin-of-safety price zones;
- explicit thesis breakers.

## Falsification discipline

At each remaining gate, penalise:

- project announcements without deposits / construction / equipment orders;
- temporary shortages already being aggressively overbuilt;
- open-standard volume growth without supplier concentration;
- commodity exposure masquerading as bottleneck exposure;
- customer vertical integration;
- capex / working-capital intensity that absorbs the apparent margin pool;
- premium valuation already discounting the AI-power cycle;
- 2030s optionality being valued as near-term certainty.

## Stop rule

Broad energy bottleneck discovery is complete. Open a new structural workstream only if new evidence reveals a materially different constraint or a narrow sub-layer with direct qualification / price / capacity-reservation evidence.

The default sequence is now **#52 → #53 → #54**.
