# AI Memory Bottleneck Research Plan

**Status:** Active research plan  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Turn the memory value-chain map into a ranked, evidence-based view of structural bottlenecks and the companies most likely to capture disproportionate value from them.

## 1. Decision we want to reach

The research must answer two separate questions:

1. **Where are the real structural bottlenecks in the AI-memory value chain?**
2. **Which investable companies capture the economics of those bottlenecks strongly enough for AI-driven demand to materially change their earnings trajectory?**

A severe technical bottleneck can still be a poor investment if the economics accrue to a very large incumbent, are competed away, require excessive capital, or are already fully reflected in valuation.

## 2. Current validated state

Three workstreams have now passed Gate A:

| Bottleneck | Bottleneck Strength | Current conclusion |
|---|---:|---|
| Advanced packaging / interposers / process control | **4.7/5** | Structural and likely to persist through architecture transitions |
| HBM stacking / bonding / thermal / yield | **4.6/5** | Structural; the bottleneck is likely to migrate toward hybrid-bond surface preparation/alignment/metrology rather than disappear |
| Test / known-good-die / burn-in | **4.6/5** | Structural; expensive heterogeneous packages increase the value and number of test insertion points |

The research has therefore reached a transition point: **the highest-value next work is no longer broad bottleneck discovery. It is investment-capture underwriting plus one strategically different bottleneck test — memory interfaces / MRDIMM / CXL.**

## 3. Research principle

We are looking for **structural dependency plus economic capture**, not simply growth.

A bottleneck is stronger when:

- the physical problem gets harder with each generation;
- capacity is slow or expensive to add;
- there are few qualified suppliers;
- qualification and switching are difficult;
- failure at that step prevents the final system from shipping;
- the supplier can retain some economics through pricing, margins, share, service or content growth.

Every deep dive must actively search for evidence that the apparent bottleneck is temporary, easy to substitute, vertically integrated, or economically unattractive.

## 4. Two-score framework

### A. Bottleneck Strength Score — 1 to 5

Score:

- physical difficulty;
- supply elasticity;
- supplier concentration;
- qualification / switching;
- system criticality.

A bottleneck should normally reach approximately **4/5 or higher** before substantial company-level valuation work.

### B. Investment Capture Score — 1 to 5

For a company exposed to a validated bottleneck, score:

- revenue / earnings sensitivity;
- pricing and margin capture;
- competitive durability;
- market-share or content-per-system runway;
- size / asymmetry;
- valuation and execution risk.

A strong research candidate requires both a real bottleneck and credible economic capture.

## 5. Revised execution sequence

### Priority A — Memory interfaces / MRDIMM / CXL (#13)

**Priority:** Immediate

This workstream is deliberately different from the manufacturing-side bottlenecks already validated. It tests whether rising memory speed, bandwidth and capacity make specialist interface/controller silicon structurally mandatory.

Separate:

1. DDR5 register clock drivers / data buffers;
2. MRDIMM multiplexing and interface silicon;
3. PMIC / clocking support;
4. CXL memory-expander controllers;
5. CXL switches;
6. firmware / interoperability.

Key questions:

- Which chips are mandatory versus optional?
- How concentrated are qualified suppliers and market share?
- How long is platform/OEM qualification and what are the switching costs?
- Can CPU vendors or hyperscalers integrate these functions?
- Does each generation increase silicon content per DIMM/system?
- Is CXL creating a durable new profit pool or shifting value to larger incumbents?

**Montage Technology must be assessed as a candidate, not assumed to be the winner.**

Deliverable: `research/memory/deep-dives/interfaces-cxl.md`.

### Priority B — Company Investment Capture deep dives

Start company underwriting in parallel because three bottlenecks have already passed Gate A.

**First wave:**

- **FormFactor (#21)** — HBM probe-card leverage and moat;
- **Camtek (#22)** — advanced-packaging inspection/metrology leverage;
- **SUSS (#15)** — temporary bonding/debonding and hybrid-bond transition.

**Second wave:**

- **Onto Innovation (#23)** — HBM4 / advanced-packaging process control;
- **Hanmi Semiconductor (#16)** — current TCB leadership versus hybrid-bond transition risk;
- **ASMPT (#18)** — multi-customer, multi-architecture bonding exposure.

The first wave should be completed before opening many more company deep dives unless new evidence materially changes priorities.

### Priority C — Narrowed wafer-processing follow-up (#12)

Do **not** rerun a broad wafer-thinning / TSV study. The HBM stacking work already established thinning plus temporary bonding/debonding as a real sub-bottleneck.

Issue #12 should now answer only the unresolved economic-capture questions:

- Is ultra-thin grinding/polishing/dicing sufficiently hard to create durable supplier power?
- Does DISCO or another precision-processing supplier gain disproportionate HBM content?
- Which temporary-carrier, debond, metrology or dicing steps remain under-researched after the SUSS work?
- How does hybrid bonding alter demand for these tools?

Treat #12 as a **targeted validation / gap-closing workstream**, not another broad value-chain exercise.

### Priority D — Interim synthesis

Do not wait for every possible backlog item to finish.

After #13 and at least three company Investment Capture deep dives, create an interim ranking comparing:

- Bottleneck Strength Score;
- Investment Capture Score;
- market cap / asymmetry;
- durability across architecture transitions;
- valuation;
- thesis breakers;
- strongest evidence against the thesis.

Use that synthesis to decide which remaining backlog items deserve more research.

## 6. Benchmark workstream — large incumbents

SK hynix, Micron, Samsung, TSMC, Advantest and Teradyne should primarily remain **benchmarks** unless new evidence shows they are the best way to capture the thesis.

Track them for:

- HBM / advanced-packaging mix;
- capacity and capex;
- pricing / contracts;
- yields and qualification where disclosed;
- customer concentration;
- margin and return-on-capital effects.

Their disclosures help determine whether economic value is flowing into smaller equipment/material/interface suppliers.

## 7. Supplier discovery and economic-capture process

For each validated bottleneck:

### Pass 1 — Exposure

Identify equipment, materials, test/metrology, interface silicon/IP and assembly suppliers.

### Pass 2 — Qualification evidence

Look for:

- named customers or credible customer-class evidence;
- design wins / qualified-vendor status;
- installed-base share;
- repeat orders;
- multi-year agreements;
- customer capex linked to supplier orders.

Treat vague references to "AI demand" as weak evidence.

### Pass 3 — Financial sensitivity

Estimate:

- percentage of revenue exposed to the relevant bottleneck;
- growth of that revenue;
- margins / incremental margins;
- capital needs;
- backlog / book-to-bill where meaningful;
- customer concentration;
- content per HBM stack/package/server.

### Pass 4 — Asymmetry

Ask:

> If the bottleneck doubles in economic value over 3–5 years, how much can this company's revenue, earnings and valuation plausibly change?

## 8. Evidence standard

Prefer, roughly:

1. regulatory filings and audited disclosures;
2. technical standards / peer-reviewed papers;
3. customer and supplier primary disclosures;
4. earnings calls and investor presentations;
5. reputable industry research;
6. specialist journalism;
7. community discussion only for question generation.

For a material bottleneck claim, try to establish multiple independent indicators: customer constraint, supplier capacity expansion, backlog/lead time, technical difficulty, limited substitution and/or economic capture.

## 9. Falsification requirement

Every deep dive must include **Evidence against the thesis** and explicitly search for:

- rapid capacity additions;
- second sourcing;
- process simplification;
- vertical integration;
- alternative architectures;
- falling equipment intensity;
- customer bargaining power;
- commoditisation;
- margin compression despite strong demand.

## 10. Completion gates

### Gate A — Bottleneck validated

Advance to company work only if the bottleneck is approximately **4/5 or higher**, supported by multiple source classes, structural across generations, and not obviously displaced by a rapid substitute.

### Gate B — Company candidate validated

A company should be `Investigating` only if it has meaningful exposure, qualification/adoption evidence, potentially material financial sensitivity and a non-obviously commoditised position.

### Gate C — High-conviction research candidate

Require strong bottleneck evidence, strong competitive evidence, clear economic capture, manageable execution/balance-sheet risk, valuation headroom and explicit thesis breakers.

## 11. Working outputs

Maintain canonical living files only:

1. `value-chain.md` — end-to-end map;
2. `research-plan.md` — this execution plan;
3. `deep-dives/*.md` — bottleneck work;
4. company files — Investment Capture underwriting;
5. `watchlist.md` — prioritisation;
6. synthesis/ranking file once enough company work exists.

Git history is the version record; do not create `final-v2` style copies.

## 12. Agent + collaborator workflow

For each workstream:

1. read `AGENTS.md` and relevant canonical files;
2. work on a branch;
3. build the evidence case;
4. actively challenge/falsify it;
5. update canonical files and sources;
6. update `CHANGELOG.md` for material changes;
7. open a PR;
8. wait for `Research governance` to pass;
9. merge after required checks pass unless manual review was explicitly requested.

Parallelise by distinct bottleneck/company files rather than having multiple agents edit the same file simultaneously.

## 13. Current recommended order

**Run now, in parallel:**

1. #13 — Interfaces / MRDIMM / CXL, including Montage;
2. #21 — FormFactor;
3. #22 — Camtek;
4. #15 — SUSS.

**Then:**

5. #23 — Onto Innovation;
6. #16 — Hanmi Semiconductor;
7. #18 — ASMPT;
8. narrowed #12 — wafer-processing gap analysis.

**Then:** interim cross-bottleneck/company synthesis before opening many additional deep dives.

## 14. Immediate research question

The next system-level question is:

> **Does the memory-interface layer create a fourth structural bottleneck with better small/mid-cap investment asymmetry than the already validated manufacturing-side bottlenecks?**

In parallel, the next company-level question is:

> **Among FormFactor, Camtek and SUSS, which has the strongest combination of validated bottleneck exposure, revenue sensitivity, competitive durability and valuation headroom?**
