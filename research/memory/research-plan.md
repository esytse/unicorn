# AI Memory Research Plan

**Status:** Active — valuation monitoring / selective optionality phase  
**Created:** 2026-09-07  
**Last reprioritised:** 2026-09-07  
**Purpose:** Identify structural AI-memory bottlenecks, determine which companies capture their economics, then allocate research effort only where valuation or new evidence creates genuine asymmetry.

## 1. Decision framework

Keep three questions separate:

1. **Bottleneck:** Is the dependency structural?
2. **Investment Capture:** Does a company capture enough economics for the theme to materially change earnings?
3. **Capital Allocation:** Does the current price leave enough risk-adjusted upside after normalising the cycle?

A severe bottleneck is not automatically a good investment. A great company is not automatically attractive at any price.

---

## 2. Validated bottlenecks

| Bottleneck | Strength | State |
|---|---:|---|
| Advanced packaging / interposers / process control | **4.7/5** | Gate A passed |
| HBM stacking / bonding / thermal / yield | **4.6/5** | Gate A passed |
| Test / known-good-die / burn-in | **4.6/5** | Gate A passed |
| DDR5 / MRDIMM interface silicon | **4.4/5** | Gate A passed |
| CXL memory-expander controllers | **3.2/5** | Gate A not passed; optionality only |

Broad bottleneck discovery is no longer the default priority.

---

## 3. Company underwriting — complete

| Company | Investment Capture | Status | Main constraint |
|---|---:|---|---|
| Onto Innovation | **4.0/5** | Watch | valuation / competition |
| FormFactor | **4.0/5** | Watch | valuation / undisclosed absolute HBM profit |
| Camtek | **3.9/5** | Watch | premium valuation / capex pull-forward risk |
| Montage Technology | **3.8/5** | Watch | large size / premium valuation |
| SUSS | **3.7/5** | Watch | customer competition / unproven hybrid-bond capture |
| ASMPT | **3.7/5** | Watch | HBM exposure diluted by broader Group |
| Hanmi Semiconductor | **3.6/5** | Watch | customer + TCB concentration / extreme valuation |

The targeted wafer-processing follow-up is complete; DISCO remains a benchmark `Watch` rather than a priority deep dive.

---

## 4. Capital allocation (#27) — complete

Canonical analysis: `research/memory/capital-allocation.md`.

**Conclusion:** no company passes Gate C at the 4 September 2026 reference prices.

| Capital watch rank | Company | Bear CAGR | Base CAGR | Bull CAGR | Approx. 12% base-return zone |
|---:|---|---:|---:|---:|---:|
| **1** | **Onto Innovation** | -7.9% | **10.4%** | 24.7% | **~$252** |
| **2** | **SUSS** | -17.1% | **8.8%** | 27.8% | **~€64** |
| **3** | **Camtek** | -15.7% | **3.8%** | 19.0% | **~$106** |
| **4** | **FormFactor** | -15.7% | **1.5%** | 14.9% | **~$68** |

These are scenario outputs, not price targets or recommendations.

### Key interpretation

- **Onto** is closest to Gate C because it combines strong HBM/AP evidence, margins and the least demanding valuation hurdle among the high-quality US names.
- **SUSS** has the highest small-cap asymmetry but much wider execution/customer downside.
- **Camtek** and **FormFactor** remain excellent businesses; current valuations are the binding constraint.
- **ASMPT** was screened but does not improve the current allocation frontier at its current multiple and broader-company earnings dilution.

---

## 5. Gate C remains deliberately rare

A `High-conviction research candidate` now requires:

- Gate A and Gate B evidence;
- explicit bear/base/bull valuation;
- attractive base and risk-adjusted expected return;
- meaningful downside protection / margin of safety;
- manageable balance sheet, dilution and customer risk;
- explicit monitoring indicators and thesis breakers.

**No company qualifies today.** Do not promote a name merely because its share price falls; verify that the operating thesis remains intact at the new price.

---

## 6. AI-memory monitoring triggers

Re-run `capital-allocation.md` when any of the following occurs:

### Price triggers, absent thesis deterioration

- Onto approaches **~$250** or below;
- SUSS approaches **~€64** or below;
- Camtek approaches **~$105** or below;
- FormFactor approaches **~$68** or below.

### Evidence triggers

- material earnings-estimate revisions;
- new HBM4/HBM4E/HBM5 process-of-record or share evidence;
- backlog cancellation / capex pull-forward evidence;
- hybrid-bond production qualification;
- margin deterioration or operating leverage materially different from the model;
- customer concentration, second sourcing or architecture substitution changes.

A material change should update the company file, capital-allocation model, synthesis, watchlist and changelog as appropriate.

---

## 7. Research-effort allocation from here

The marginal value of finding another conventional HBM equipment supplier is now lower than it was at the start of the programme.

### Current priority

1. **Maintain the AI-memory capital watch** using the triggers above.
2. **#5 Weebit Nano** — test the speculative emerging-memory / architectural-discontinuity thesis. This is deliberately different from the validated current bottlenecks and should be treated as a high-risk optionality study, not grouped with the current Gate-A beneficiaries.
3. **#3 robotics actuators** — build the separate end-to-end actuator bottleneck map.

Do not open additional AI-memory supplier deep dives unless new evidence suggests a materially better combination of bottleneck strength, company capture and valuation than the existing set.

---

## 8. Evidence standard

Prefer:

1. regulatory filings / audited disclosures;
2. technical standards / peer-reviewed papers;
3. customer / supplier primary disclosures;
4. earnings calls and investor presentations;
5. reputable industry research;
6. specialist journalism;
7. community discussion only for question generation.

Point-in-time valuation must carry a date and be refreshed before a capital-allocation conclusion.

---

## 9. Falsification requirement

Every analysis must actively search for:

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

## 10. Working outputs

Maintain canonical living files only:

1. `value-chain.md` — bottleneck map;
2. `research-plan.md` — active execution plan;
3. `deep-dives/*.md` — bottleneck/process research;
4. `companies/*.md` — company underwriting;
5. `synthesis-ranking.md` — cross-company synthesis;
6. `capital-allocation.md` — scenario / margin-of-safety comparison;
7. `watchlist.md` — research status and monitoring;
8. `sources/source-register.md` — important sources;
9. `CHANGELOG.md` — material changes.

Git history is the version record; do not create versioned copies.

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

---

## 12. Immediate question

> **Can a price reset or stronger normalized earnings evidence turn Onto or SUSS into a genuine Gate-C candidate — while Weebit offers a separate, much more speculative architecture-discontinuity path?**
