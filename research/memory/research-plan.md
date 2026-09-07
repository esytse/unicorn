# AI Memory Bottleneck Research Plan

**Status:** Active research plan  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Turn the memory value-chain map into a ranked, evidence-based view of structural bottlenecks and the companies most likely to capture disproportionate value from them.

## 1. Decision we want to reach

The research must keep two questions separate:

1. **Where are the real structural bottlenecks in the AI-memory value chain?**
2. **Which investable companies capture the economics strongly enough, and at a valuation that still leaves attractive asymmetry?**

A severe technical bottleneck can still be a poor investment if economics accrue to a giant incumbent, are competed away, require excessive capital, or are already priced in.

---

## 2. Current validated state

Four workstreams now pass Gate A:

| Bottleneck | Bottleneck Strength | Current conclusion |
|---|---:|---|
| Advanced packaging / interposers / process control | **4.7/5** | Structural and likely to persist through architecture transitions |
| HBM stacking / bonding / thermal / yield | **4.6/5** | Structural; bottleneck migrates toward hybrid-bond surface preparation/alignment/metrology rather than disappearing |
| Test / known-good-die / burn-in | **4.6/5** | Structural; expensive heterogeneous packages increase the number and value of test insertion points |
| DDR5 / MRDIMM interface silicon | **4.4/5** | Structural within registered/multiplexed server memory; concentrated qualified supplier base |

**CXL memory-expander controllers currently score 3.2/5 and do not pass Gate A.** Keep CXL as emerging optionality until adoption and merchant economic capture strengthen.

The programme has now moved decisively from broad bottleneck discovery toward **Investment Capture underwriting**.

---

## 3. First company wave — complete

The first planned underwriting wave is complete:

| Company | Bottleneck | Investment Capture | Status | Main unresolved issue |
|---|---|---:|---|---|
| FormFactor (#21) | HBM test / probe cards | **4.0/5** | Watch | Valuation and undisclosed absolute HBM profit share |
| Camtek (#22) | AP inspection / metrology | **3.9/5** | Watch | Premium valuation and whether 2026 orders contain pull-forward |
| SUSS (#15) | HBM thinning / temporary bonding | **3.7/5** | Watch | Customer/process-of-record competition and unproven HBM hybrid-bond capture |

The interim synthesis is maintained in `research/memory/synthesis-ranking.md`.

**No company is a High-conviction research candidate yet.** For FormFactor and Camtek, valuation is increasingly the binding constraint. For SUSS, technology/customer transition risk is the binding constraint.

---

## 4. Revised execution sequence

### Priority A — Montage Technology company underwriting (#25)

The DDR5/MRDIMM interface layer has passed Gate A at 4.4/5, so Montage now requires a company-level test rather than more generic interface research.

Focus on:

- DDR5 RCD revenue/share and gross-margin durability;
- MRDIMM MRCD/MDB content and adoption across Intel/AMD/OEM platforms;
- newer product revenue from CKD, retimers and CXL MXC;
- competition versus Renesas and Rambus in the core interface franchise;
- platform qualification / standards participation / switching costs;
- customer and geopolitical/foundry risk;
- market-cap asymmetry and valuation expectations.

**Important:** The technical thesis is now much stronger, but Montage is already large and highly valued. The company must not be promoted merely because the bottleneck passed Gate A.

### Priority B — second company wave

Run next, preferably as distinct files/branches:

1. **Onto Innovation (#23)** — compare directly with Camtek in HBM4/AP inspection and process control.
2. **Hanmi Semiconductor (#16)** — determine whether current TCB dominance is a moat or a technology-transition trap.
3. **ASMPT (#18)** — test whether multi-customer/multi-architecture bonding exposure is more durable than Hanmi's concentration.

### Priority C — targeted wafer-processing follow-up (#12)

Do **not** repeat a broad HBM/TSV value-chain study. The HBM stacking work already validated thinning and temporary bonding/debonding.

Close only the remaining economic-capture gaps:

- DISCO / ultra-thin grinding and polishing;
- precision dicing / singulation;
- carrier/debond steps not already covered by SUSS;
- metrology specific to ultra-thin HBM wafers;
- how hybrid bonding changes tool/content intensity.

Only open new company work if the incremental process evidence justifies it.

### Priority D — refresh synthesis

After #25, #23, #16 and #18 (or earlier if a thesis breaks materially), update the ranking rather than automatically adding more companies.

Compare:

- Bottleneck Strength;
- Investment Capture;
- market-cap asymmetry;
- valuation;
- architecture-transition durability;
- strongest evidence against the thesis;
- catalysts and thesis breakers.

---

## 5. Two-score framework

### A. Bottleneck Strength Score — 1 to 5

Score:

- physical difficulty;
- supply elasticity;
- supplier concentration;
- qualification / switching;
- system criticality.

A bottleneck normally needs approximately **4/5 or higher** before substantial company valuation work.

### B. Investment Capture Score — 1 to 5

For a company exposed to a validated bottleneck, score:

- revenue / earnings sensitivity;
- pricing and margin capture;
- competitive durability;
- market-share or content-per-system runway;
- size / asymmetry;
- valuation and execution risk.

A strong research candidate requires both a real bottleneck and credible economic capture.

---

## 6. Supplier-discovery / underwriting process

### Pass 1 — Exposure

Identify equipment, materials, test/metrology, interface silicon/IP and assembly suppliers.

### Pass 2 — Qualification evidence

Prefer named or strongly triangulated evidence of:

- design wins / qualified-vendor status;
- installed-base share;
- repeat orders;
- multi-year agreements;
- customer capex linked to supplier orders.

Treat generic "AI demand" references as weak evidence.

### Pass 3 — Financial sensitivity

Estimate:

- percentage of revenue/profit exposed to the bottleneck;
- growth of that revenue;
- margins and incremental margins;
- capital requirements;
- backlog / book-to-bill where meaningful;
- customer concentration;
- content per HBM stack/package/server/module.

### Pass 4 — Asymmetry

Ask:

> If the bottleneck doubles in economic value over 3–5 years, how much can this company's revenue, earnings and valuation plausibly change from today's starting point?

This must explicitly include the current market capitalization and valuation. A technically perfect supplier can fail the investment test if the market has already capitalised the opportunity.

---

## 7. Evidence standard

Prefer, roughly:

1. regulatory filings and audited disclosures;
2. technical standards / peer-reviewed papers;
3. customer and supplier primary disclosures;
4. earnings calls and investor presentations;
5. reputable industry research;
6. specialist journalism;
7. community discussion only for question generation.

For a material bottleneck or moat claim, triangulate across multiple source classes when possible.

Point-in-time valuation data must be labelled with its date and refreshed before a capital-allocation conclusion.

---

## 8. Falsification requirement

Every bottleneck/company deep dive must contain **Evidence against the thesis** and actively search for:

- rapid capacity additions;
- second sourcing;
- process simplification;
- vertical integration;
- alternative architectures;
- falling equipment/content intensity;
- customer bargaining power;
- commoditisation;
- margin compression despite strong demand;
- valuation that already assumes the upside.

Contradictory evidence must remain in the canonical file.

---

## 9. Completion gates

### Gate A — Bottleneck validated

Require approximately **4/5 or higher**, multiple evidence classes, persistence across generations and no obvious rapid substitute.

### Gate B — Company candidate validated

A company should be `Investigating` only if it has meaningful exposure, qualification/adoption evidence, potentially material financial sensitivity and a non-obviously commoditised position.

### Gate C — High-conviction research candidate

Require all of:

- strong bottleneck evidence;
- strong competitive/qualification evidence;
- clear financial capture;
- manageable balance-sheet/execution risk;
- valuation headroom;
- explicit thesis breakers and monitoring indicators.

This status should remain rare.

---

## 10. Benchmark workstream

Use SK hynix, Micron, Samsung, TSMC, Advantest and Teradyne primarily as benchmarks unless new evidence shows they are the cleanest investment vehicles.

Track:

- HBM/AP mix and capacity;
- capex and pricing/contracts;
- yield/qualification disclosures;
- customer concentration;
- margin / ROIC effects.

These disclosures help determine whether economic value is flowing into smaller suppliers.

---

## 11. Working outputs

Maintain canonical living files only:

1. `value-chain.md` — end-to-end map and validated bottleneck state;
2. `research-plan.md` — active execution sequence;
3. `deep-dives/*.md` — bottleneck work;
4. `companies/*.md` — Investment Capture underwriting;
5. `synthesis-ranking.md` — cross-company comparison;
6. `watchlist.md` — research prioritisation;
7. `sources/source-register.md` — important cross-file sources;
8. `CHANGELOG.md` — material conclusion/status/priority changes.

Git history is the version record; do not create `final-v2` copies.

---

## 12. Agent + collaborator workflow

For each workstream:

1. read `AGENTS.md` and relevant canonical files;
2. work on a branch;
3. build the evidence case;
4. actively challenge/falsify it;
5. update canonical files and source register where relevant;
6. update `CHANGELOG.md` for material changes;
7. open a PR;
8. wait for `Research governance` to pass;
9. merge after required checks pass unless manual review was explicitly requested;
10. close/comment the completed backlog issue so GitHub remains the operational research queue.

Parallelise by distinct company/bottleneck files rather than having multiple agents edit the same file simultaneously.

---

## 13. Current recommended order

**Next:**

1. #25 — Montage Technology company underwriting;
2. #23 — Onto Innovation;
3. #16 — Hanmi Semiconductor;
4. #18 — ASMPT;
5. narrowed #12 — wafer-processing economic-capture gap analysis.

**Then:** refresh `synthesis-ranking.md` and decide whether further company or bottleneck work is justified.

## 14. Immediate research question

> **After FormFactor, Camtek and SUSS, does Montage's validated memory-interface franchise produce enough incremental earnings and valuation headroom to outrank them — or has the market already priced the structural advantage?**
