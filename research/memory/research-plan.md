# AI Memory Research Plan

**Status:** Active — capital-allocation phase  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Identify structural AI-memory bottlenecks, determine which companies capture their economics, then test whether current valuation leaves attractive risk-adjusted returns.

## 1. Decision framework

Keep three questions separate:

1. **Bottleneck:** Is the technical / manufacturing dependency structural?
2. **Investment Capture:** Does a company capture enough of the economics for the theme to materially change earnings?
3. **Capital Allocation:** Is enough upside left at today's price after normalising the cycle and downside risk?

A severe bottleneck is not automatically a good investment. A great company is not automatically a good buy at any price.

---

## 2. Validated bottlenecks

| Bottleneck | Strength | State |
|---|---:|---|
| Advanced packaging / interposers / process control | **4.7/5** | Gate A passed |
| HBM stacking / bonding / thermal / yield | **4.6/5** | Gate A passed |
| Test / known-good-die / burn-in | **4.6/5** | Gate A passed |
| DDR5 / MRDIMM interface silicon | **4.4/5** | Gate A passed |
| CXL memory-expander controllers | **3.2/5** | Gate A not passed; optionality only |

The programme should no longer prioritise broad bottleneck discovery unless new evidence materially changes this map.

---

## 3. Company underwriting — two waves complete

| Company | Investment Capture | Status | Main constraint |
|---|---:|---|---|
| Onto Innovation (#23) | **4.0/5** | Watch | market-cap rerating / competition |
| FormFactor (#21) | **4.0/5** | Watch | valuation / undisclosed absolute HBM profit |
| Camtek (#22) | **3.9/5** | Watch | premium valuation / capex pull-forward risk |
| Montage Technology (#25) | **3.8/5** | Watch | large size / ~52x point-in-time forward P/E |
| SUSS (#15) | **3.7/5** | Watch | customer competition / unproven hybrid-bond capture |
| ASMPT (#18) | **3.7/5** | Watch | HBM exposure diluted by broader Group |
| Hanmi Semiconductor (#16) | **3.6/5** | Watch | customer + TCB concentration / extreme valuation |

The targeted wafer-processing follow-up (#12) is also complete. Precision thinning/singulation remains structurally important, but the evidence does not justify a dedicated DISCO company deep dive today. DISCO remains a benchmark `Watch`.

No company is a `High-conviction research candidate` yet.

---

## 4. Immediate priority — Capital allocation (#27)

The next research question is:

> **Which of Onto Innovation, FormFactor, Camtek and SUSS offers the best risk-adjusted expected return after current valuation and a normal semiconductor-capex cycle are explicitly modelled?**

ASMPT may be included if refreshed valuation shows its architecture durability offsets lower HBM earnings sensitivity.

### Required work

For each candidate:

1. refresh share price, market cap, enterprise value and valuation;
2. reconstruct / normalise current earnings and free cash flow;
3. estimate how much earnings are tied to HBM/AP versus other businesses;
4. build **bear / base / bull** 3–5 year revenue, margin and earnings scenarios;
5. use plausible terminal valuation multiples, not today's multiple by default;
6. calculate downside, upside and annualised return in each scenario;
7. calculate probability-weighted expected return where defensible;
8. identify what growth/margins the current share price appears to imply;
9. assess balance sheet, capital needs, dilution and customer concentration;
10. specify monitoring indicators and thesis breakers.

### Required output

Create/update a canonical capital-allocation file under `research/memory/`. Update `synthesis-ranking.md`, `watchlist.md`, source register and changelog only when the new valuation work changes conclusions.

**The Bottleneck Strength × Investment Capture screen is not a valuation model and must not determine the winner automatically.**

---

## 5. Two-score framework retained for research triage

### A. Bottleneck Strength — 1 to 5

Score:

- physical difficulty;
- supply elasticity;
- supplier concentration;
- qualification / switching;
- system criticality.

A bottleneck normally needs around **4/5** to pass Gate A.

### B. Investment Capture — 1 to 5

Score:

- revenue / earnings sensitivity;
- pricing / margin capture;
- competitive durability;
- market-share / content runway;
- size / asymmetry;
- valuation / execution.

These scores identify where deeper valuation work is worth the effort. They do not replace capital-allocation analysis.

---

## 6. Evidence standard

Prefer:

1. regulatory filings / audited disclosures;
2. technical standards / peer-reviewed papers;
3. customer / supplier primary disclosures;
4. earnings calls and investor presentations;
5. reputable industry research;
6. specialist journalism;
7. community discussion only for question generation.

Material claims should be triangulated across source classes when possible. Point-in-time valuation must always carry a date and be refreshed before a capital-allocation conclusion.

---

## 7. Falsification requirement

Every analysis must actively search for evidence against the thesis, including:

- second sourcing / share loss;
- rapid capacity additions;
- architecture substitution;
- process simplification;
- customer bargaining power;
- falling equipment/content intensity;
- margin normalisation;
- cyclicality / capex pull-forward;
- valuation that already assumes the upside.

Contradictory evidence stays in the canonical file.

---

## 8. Completion gates

### Gate A — Bottleneck validated

Approximately 4/5+, multiple evidence classes, persistence across generations, no obvious rapid substitute.

### Gate B — Company capture validated

Meaningful exposure, qualification/adoption evidence, potentially material financial sensitivity and a non-obviously commoditised position.

### Gate C — High-conviction research candidate

Require:

- Gate A and Gate B evidence;
- explicit valuation / scenario analysis;
- attractive risk-adjusted expected return;
- meaningful margin of safety;
- manageable balance-sheet / execution risk;
- explicit thesis breakers / monitoring indicators.

Gate C remains intentionally rare.

---

## 9. Benchmark / monitoring set

Use large incumbents and lower-priority candidates to test assumptions rather than deep-dive automatically:

- SK hynix / Micron / Samsung — HBM economics and capacity;
- TSMC — advanced-packaging capacity / architecture;
- Advantest / Teradyne — test intensity;
- DISCO — wafer-thinning/singulation economics;
- Montage / Hanmi / ASMPT — monitor valuation and architecture transitions after completed underwriting.

---

## 10. Working outputs

Maintain canonical living files only:

1. `value-chain.md` — end-to-end bottleneck map;
2. `research-plan.md` — active execution plan;
3. `deep-dives/*.md` — bottleneck/process work;
4. `companies/*.md` — Investment Capture underwriting;
5. `synthesis-ranking.md` — cross-company prioritisation;
6. capital-allocation file — scenario / expected-return comparison;
7. `watchlist.md` — research status;
8. `sources/source-register.md` — important cross-file sources;
9. `CHANGELOG.md` — material conclusion/status/priority changes.

Git history is the version record; do not create `final-v2` copies.

---

## 11. Agent + collaborator workflow

For each substantive workstream:

1. read `AGENTS.md` and canonical files;
2. work on a branch;
3. build the primary evidence case;
4. perform an explicit falsification pass;
5. update canonical documentation and source register where relevant;
6. update `CHANGELOG.md` for material changes;
7. open a PR;
8. wait for `Research governance` to pass;
9. merge only after required checks pass;
10. comment/close completed backlog issues.

Parallelise distinct files/workstreams rather than editing the same canonical file simultaneously.

---

## 12. Current order

**Now:**

1. **#27 — capital allocation: Onto vs FormFactor vs Camtek vs SUSS** (ASMPT optional comparator).

**After #27:**

2. decide whether any candidate passes Gate C;
3. update monitoring thresholds / buy-zone or re-entry conditions if appropriate;
4. only then decide whether further AI-memory supplier work is worth opening.

**Separate backlog:**

- **#5 Weebit Nano** — speculative emerging-memory / architectural-discontinuity thesis;
- **#3 robotics actuators** — separate value-chain research stream.

## 13. Immediate question

> **We have found strong businesses. Which one, if any, is mispriced enough today to deserve capital?**
