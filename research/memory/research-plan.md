# AI Memory Research Plan

**Status:** Active — monitoring / architectural optionality phase  
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

## 2. Validated current bottlenecks

| Bottleneck | Strength | State |
|---|---:|---|
| Advanced packaging / interposers / process control | **4.7/5** | Gate A passed |
| HBM stacking / bonding / thermal / yield | **4.6/5** | Gate A passed |
| Test / known-good-die / burn-in | **4.6/5** | Gate A passed |
| DDR5 / MRDIMM interface silicon | **4.4/5** | Gate A passed |
| CXL memory-expander controllers | **3.2/5** | Gate A not passed; optionality only |

Broad bottleneck discovery is no longer the default priority.

---

## 3. Completed company underwriting

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

## 4. Capital allocation — completed current-bottleneck work

### Initial capital allocation (#27)

| Capital watch rank | Company | Bear CAGR | Base CAGR | Bull CAGR | Approx. 12% base-return zone |
|---:|---|---:|---:|---:|---:|
| **1** | **Onto Innovation** | -7.9% | **10.4%** | 24.7% | **~$252** |
| **2** | **SUSS** | -17.1% | **8.8%** | 27.8% | **~€64** |
| **3** | **Camtek** | -15.7% | **3.8%** | 19.0% | **~$106** |
| **4** | **FormFactor** | -15.7% | **1.5%** | 14.9% | **~$68** |

No company passed Gate C.

### Probe-card peer challenge (#31)

PR #30 identified JEM/Micronics/Technoprobe as alternative listed expressions of the validated HBM-test bottleneck. #31 normalized and falsified the apparent JEM valuation advantage.

| Peer | 4 Sep reference | Base CAGR | ~12% base-return zone | Current research view |
|---|---:|---:|---:|---|
| **JEM** | ¥6,230 | **~9.4%** | **~¥5,640** | Investigating — best new valuation lead, but FCF/dilution/HBM socket gaps remain |
| **Micronics Japan** | ¥11,940 | **~6.8%** | **~¥9,760** | Investigating — quality/value comparator |
| **Technoprobe** | €27.46 | **~6.9%** | **~€22.55** | Watch — operating benchmark / premium expectations |
| **FormFactor** | $103.90 | **~1.5%** | **~$68** | Watch — strongest direct HBM evidence, valuation demanding |

JEM remains `Investigating`; it does not outrank the fully underwritten Onto / SUSS capital watch because cash conversion, dilution, concentration and HBM-socket evidence remain weaker.

---

## 5. Weebit Nano (#5) — deep dive complete

Canonical file: `research/memory/companies/weebit-nano.md`.

**Previous state:** `Research queue`, Low confidence; the thesis still depended on proving that ReRAM technical promise was translating into commercial adoption.

**New conclusion:** commercial adoption is now **real but early**.

Evidence now includes:

- production-qualified ReRAM platforms at SkyWater and DB HiTek;
- Tier-1 IDM licences with onsemi and Texas Instruments;
- three product-customer tape-outs by June 2026, with at least one returned chip functional and running software;
- FY26 revenue of **A$15.3m**, up from A$4.4m, driven by licensing and NRE.

The unresolved step is also the most important one for valuation: **mass production and recurring royalties have not yet been demonstrated**. The company hopes its first customer reaches mass production in CY27.

### Status decision

**Weebit: `Research queue` → `Watch`; confidence Low → Medium.**

This is an **architectural-optionality** conclusion, not a Gate-A bottleneck conclusion. The base commercial thesis is embedded non-volatile-memory replacement; AI / compute-in-memory remains upside optionality rather than the current base case.

### Valuation discipline

At the 4 September 2026 reference, WBT was about **A$3.53**, market cap ~**A$849m** and EV ~**A$681m**, around **45x FY26 revenue**. FY26 also included a **A$54.9m net loss**, operating cash outflow, material stock-based compensation and roughly A$102m of equity funding during 2026.

A reverse commercialization screen suggests the business needs roughly **5–7x FY26 revenue by end-2030 plus a meaningful shift to royalty economics** to support an attractive return without relying on an even more aggressive terminal multiple.

**Conclusion:** Weebit is now credible enough to monitor, but the current price already capitalizes substantial future success. It does not enter the primary capital-allocation ranking.

### Monitoring triggers

Move the thesis materially higher only if several occur:

- first meaningful recurring royalty revenue;
- a customer reaches sustained mass production;
- onsemi and/or TI reach commercial availability / product milestones;
- another Tier-1 foundry/IDM licence converts to production;
- royalties scale faster than R&D / SBC;
- dilution falls materially;
- a named commercial AI / compute-in-memory customer appears;
- valuation resets enough to absorb execution risk.

---

## 6. Gate C remains deliberately rare

A `High-conviction research candidate` requires Gate A/B evidence where applicable, explicit valuation, attractive risk-adjusted return, downside protection, manageable balance-sheet/dilution/customer risk and explicit monitoring indicators / thesis breakers.

**No company qualifies today.**

---

## 7. Current research / capital frontier

### Current-bottleneck capital watch

**Onto → SUSS → Camtek → FormFactor.**

### Probe-card challenger lane

**JEM → Micronics → Technoprobe.**

### Architectural optionality

**Weebit Nano — Watch / Medium.** Commercial adoption is credible; royalty-scale economics are unproven.

Do not mix Weebit's speculative architecture path mechanically into the Bottleneck × Investment Capture ranking used for the current HBM ecosystem.

---

## 8. Monitoring triggers

Re-run capital allocation when material price, earnings, customer/share, qualification, margin/FCF, dilution or architecture evidence changes.

Existing price-monitoring references remain approximately:

- Onto **~$250** or below;
- SUSS **~€64** or below;
- JEM **~¥5,600** or below only if HBM/cash evidence remains intact;
- Micronics **~¥9,800** or below;
- Technoprobe **~€22.5** or below;
- Camtek **~$105** or below;
- FormFactor **~$68** or below.

For Weebit, price alone is not a promotion trigger. Commercial royalty evidence must improve first.

---

## 9. Research-effort allocation from here

The current AI-memory programme has now tested:

- the main structural bottlenecks;
- multiple supplier capture cases;
- capital allocation;
- a new valuation expression of HBM test;
- an architectural-discontinuity option through Weebit.

The marginal value of opening another broad AI-memory supplier screen is now low.

### Current sequence

1. **Maintain the AI-memory watch** using the evidence and valuation triggers above.
2. **#3 robotics actuators — next substantive research stream.** Build the end-to-end actuator stack, identify structural bottlenecks and only then identify investable suppliers.
3. Reopen AI-memory deep research only when a material monitoring trigger or genuinely new architecture/economic opportunity appears.

---

## 10. Evidence standard and falsification

Prefer regulatory/audited disclosures, technical standards/papers, customer/supplier primary disclosure, earnings calls/investor presentations, reputable industry research, then specialist journalism. Community discussion is question generation only.

Every analysis must actively search for second sourcing/share loss, architecture substitution, customer bargaining power, falling content intensity, margin normalization, capex pull-forward, dilution and valuation that already assumes the upside.

Point-in-time valuation must carry a date and be refreshed before a capital-allocation conclusion. Contradictory evidence stays in the canonical file.

---

## 11. Working outputs

Maintain canonical living files only: `value-chain.md`, `research-plan.md`, `deep-dives/*.md`, `companies/*.md`, `synthesis-ranking.md`, capital-allocation analyses, `watchlist.md`, `sources/source-register.md` and `CHANGELOG.md`.

Git history is the version record; do not create versioned copies.

---

## 12. Agent + collaborator workflow

For each substantive workstream: read governance/current research, work on a branch, build the primary evidence case, perform falsification, update canonical documentation and sources, update `CHANGELOG.md`, open a PR, wait for `Research governance`, merge only after required checks pass, then comment/close completed backlog issues.

---

## 13. Immediate question

> **Within robotics actuators, which component or enabling layer becomes structurally hard to substitute as advanced robotics scales — and which supplier captures that dependency without the valuation already assuming success?**
