# AI Memory Research Plan

**Status:** Active — probe-card valuation challenge / selective optionality phase  
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

## 3. Company underwriting — first two waves complete

| Company | Investment Capture | Status | Main constraint |
|---|---:|---|---|
| Onto Innovation | **4.0/5** | Watch | valuation / competition |
| FormFactor | **4.0/5** | Watch | valuation / undisclosed absolute HBM profit |
| Camtek | **3.9/5** | Watch | premium valuation / capex pull-forward risk |
| Montage Technology | **3.8/5** | Watch | large size / premium valuation |
| SUSS | **3.7/5** | Watch | customer competition / unproven hybrid-bond capture |
| ASMPT | **3.7/5** | Watch | HBM exposure diluted by broader Group |
| Hanmi Semiconductor | **3.6/5** | Watch | customer + TCB concentration / extreme valuation |

DISCO remains a process benchmark `Watch` rather than a priority company deep dive.

---

## 4. Initial capital allocation (#27) — complete

Canonical analysis: `research/memory/capital-allocation.md`.

**Conclusion:** no company passed Gate C at the 4 September 2026 reference prices.

| Capital watch rank | Company | Bear CAGR | Base CAGR | Bull CAGR | Approx. 12% base-return zone |
|---:|---|---:|---:|---:|---:|
| **1** | **Onto Innovation** | -7.9% | **10.4%** | 24.7% | **~$252** |
| **2** | **SUSS** | -17.1% | **8.8%** | 27.8% | **~€64** |
| **3** | **Camtek** | -15.7% | **3.8%** | 19.0% | **~$106** |
| **4** | **FormFactor** | -15.7% | **1.5%** | 14.9% | **~$68** |

These are scenario outputs, not price targets or recommendations.

---

## 5. Probe-card peer challenge (#31) — active / immediate priority

PR #30 changed the research frontier by identifying listed memory-probe-card peers that may express the already-validated 4.6/5 HBM-test bottleneck at better valuations than FormFactor.

Canonical analyses:

- `research/memory/deep-dives/probe-card-peer-value.md`
- `research/memory/probe-card-capital-allocation.md`

### First normalization result

| Peer | 4 Sep reference | Base CAGR to end-2030 | ~12% base-return zone | Current research view |
|---|---:|---:|---:|---|
| **JEM** | ¥6,230 | **~9.4%** | **~¥5,640** | **Investigating — provisional capital challenger** |
| **Micronics Japan** | ¥11,940 | **~6.8%** | **~¥9,760** | Investigating — quality/value comparator |
| **Technoprobe** | €27.46 | **~6.9%** | **~€22.55** | Watch — operating benchmark / premium expectations |
| **FormFactor** | $103.90 | **~1.5%** | **~$68** | Watch — strongest direct HBM evidence, valuation demanding |

**Interpretation:** JEM is the only new probe-card peer whose initial base/bear distribution is competitive with the existing Onto/SUSS capital frontier. However, its HBM-specific customer/share evidence is materially weaker, so it remains `Investigating` and does not pass Gate C.

### #31 completion gate

Before JEM can move to `Watch` or alter Gate C conclusions, verify:

- which HBM manufacturers / production insertions use JEM;
- HBM-specific revenue/share versus conventional DRAM;
- normalized operating margin after current high utilization;
- capex and free-cash-flow conversion;
- fully diluted share count / capital actions;
- refreshed valuation after evidence changes.

A lower multiple alone is not enough.

---

## 6. Gate C remains deliberately rare

A `High-conviction research candidate` requires:

- Gate A and Gate B evidence;
- explicit bear/base/bull valuation;
- attractive base and risk-adjusted expected return;
- meaningful downside protection / margin of safety;
- manageable balance sheet, dilution and customer risk;
- explicit monitoring indicators and thesis breakers.

**No company qualifies today.** Do not promote a name merely because its share price falls or its headline multiple looks cheap; verify that the operating thesis remains intact.

---

## 7. Current capital / research frontier

### Fully underwritten capital watch

**Onto → SUSS → Camtek → FormFactor** remains the completed #27 order.

### New challenger lane

**JEM → Micronics → Technoprobe** now challenges that order.

On the first common-basis normalization, the provisional combined research order is:

**Onto → JEM (provisional) → SUSS → Micronics / Technoprobe → Camtek → FormFactor.**

This is not a recommendation ranking. JEM's position is explicitly provisional because evidence quality is lower than Onto, SUSS and FormFactor.

---

## 8. AI-memory monitoring triggers

Re-run capital allocation when any of the following occurs:

### Price triggers, absent thesis deterioration

- Onto approaches **~$250** or below;
- JEM approaches **~¥5,600** or below, or normalized earnings rise enough to move the hurdle;
- SUSS approaches **~€64** or below;
- Micronics approaches **~¥9,800** or below;
- Technoprobe approaches **~€22.5** or below;
- Camtek approaches **~$105** or below;
- FormFactor approaches **~$68** or below.

### Evidence triggers

- material earnings-estimate revisions;
- new HBM4/HBM4E/HBM5 process-of-record or customer/share evidence;
- probe-card customer concentration / second-sourcing changes;
- backlog cancellation / capex pull-forward evidence;
- hybrid-bond production qualification;
- margin deterioration or operating leverage materially different from the model;
- architecture substitution changes.

A material change should update the company file, capital-allocation analysis, synthesis, watchlist and changelog as appropriate.

---

## 9. Research-effort allocation from here

The marginal value of finding another conventional HBM equipment supplier remains low. PR #30 is an exception because it found a potentially better **valuation expression of an already-validated bottleneck**.

### Current sequence

1. **#31 probe-card capital allocation / JEM evidence gap — immediate.** Complete the HBM customer/share, normalized-margin, cash-conversion and dilution work before deciding whether JEM enters `Watch` or the primary capital allocation set.
2. **#5 Weebit Nano** — test the speculative emerging-memory / architectural-discontinuity thesis. Treat it as high-risk optionality, not as a current Gate-A beneficiary.
3. **#3 robotics actuators** — build the separate end-to-end actuator bottleneck map.

Do not open additional AI-memory supplier deep dives unless new evidence suggests a materially better combination of bottleneck strength, company capture and valuation than the existing frontier.

---

## 10. Evidence standard and falsification

Prefer:

1. regulatory filings / audited disclosures;
2. technical standards / peer-reviewed papers;
3. customer / supplier primary disclosures;
4. earnings calls and investor presentations;
5. reputable industry research;
6. specialist journalism;
7. community discussion only for question generation.

Every analysis must actively search for second sourcing/share loss, rapid capacity additions, architecture substitution, customer bargaining power, falling content intensity, margin normalization, capex pull-forward and valuation that already assumes the upside.

Point-in-time valuation must carry a date and be refreshed before a capital-allocation conclusion. Contradictory evidence stays in the canonical file.

---

## 11. Working outputs

Maintain canonical living files only:

1. `value-chain.md` — bottleneck map;
2. `research-plan.md` — active execution plan;
3. `deep-dives/*.md` — bottleneck/process research;
4. `companies/*.md` — company underwriting;
5. `synthesis-ranking.md` — cross-company synthesis;
6. `capital-allocation.md` and focused peer capital-allocation files — scenario / margin-of-safety comparisons;
7. `watchlist.md` — research status and monitoring;
8. `sources/source-register.md` — important sources;
9. `CHANGELOG.md` — material changes.

Git history is the version record; do not create versioned copies.

---

## 12. Agent + collaborator workflow

For each substantive workstream:

1. read `AGENTS.md` and canonical files;
2. work on a branch;
3. build the primary evidence case;
4. perform an explicit falsification pass;
5. update canonical documentation and sources where relevant;
6. update `CHANGELOG.md` for material changes;
7. open a PR;
8. wait for `Research governance` to pass;
9. merge only after required checks pass;
10. comment/close completed backlog issues.

---

## 13. Immediate question

> **Can JEM's apparent low-teens earnings valuation survive verification of HBM customer/share, normalized margins, cash conversion and dilution strongly enough to challenge Onto — or is the discount simply compensation for lower evidence quality and memory-cycle risk?**
