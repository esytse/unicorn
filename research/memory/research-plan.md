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

## 4. Initial capital allocation (#27) — complete

Canonical analysis: `research/memory/capital-allocation.md`.

| Capital watch rank | Company | Bear CAGR | Base CAGR | Bull CAGR | Approx. 12% base-return zone |
|---:|---|---:|---:|---:|---:|
| **1** | **Onto Innovation** | -7.9% | **10.4%** | 24.7% | **~$252** |
| **2** | **SUSS** | -17.1% | **8.8%** | 27.8% | **~€64** |
| **3** | **Camtek** | -15.7% | **3.8%** | 19.0% | **~$106** |
| **4** | **FormFactor** | -15.7% | **1.5%** | 14.9% | **~$68** |

No company passed Gate C.

---

## 5. Probe-card peer challenge (#31) — immediate priority

PR #30 identified listed memory-probe-card peers that may express the already-validated 4.6/5 HBM-test bottleneck at better valuations than FormFactor.

Canonical analyses:

- `research/memory/deep-dives/probe-card-peer-value.md`
- `research/memory/probe-card-capital-allocation.md`
- `research/memory/companies/japan-electronic-materials.md`

### First normalization / falsification result

| Peer | 4 Sep reference | Base CAGR | ~12% base-return zone | Current research view |
|---|---:|---:|---:|---|
| **JEM** | ¥6,230 | **~9.4%** | **~¥5,640** | **Investigating — best new valuation lead, but FCF/dilution/evidence gaps remain** |
| **Micronics Japan** | ¥11,940 | **~6.8%** | **~¥9,760** | Investigating — quality/value comparator |
| **Technoprobe** | €27.46 | **~6.9%** | **~€22.55** | Watch — operating benchmark / premium expectations |
| **FormFactor** | $103.90 | **~1.5%** | **~$68** | Watch — strongest direct HBM evidence, valuation demanding |

JEM's HBM link is more credible after the evidence pass: a company-controlled page says DRAM share is rising around HBM, and FY2026 major-customer disclosures show Micron Memory Japan + Taiwan represented ~31% of sales. But the same pass found weak current FCF conversion, material 2026 equity issuance, high customer concentration and contradictory competitor evidence.

**Conclusion:** JEM is the immediate research priority, but **does not rank above Onto / SUSS for capital allocation yet**.

### #31 completion gate

Before JEM can move to `Watch` or alter Gate C conclusions, verify or explicitly exhaust public evidence on:

- HBM production sockets / share by customer;
- HBM-specific revenue versus conventional DRAM/NAND;
- normalized margin and FCF after current capacity investment;
- future capex / dilution requirements;
- refreshed valuation.

A lower P/E alone is not enough.

---

## 6. Gate C remains deliberately rare

A `High-conviction research candidate` requires Gate A/B evidence, explicit bear/base/bull valuation, attractive risk-adjusted return, downside protection, manageable balance-sheet/dilution/customer risk and explicit monitoring indicators / thesis breakers.

**No company qualifies today.**

---

## 7. Current research / capital frontier

### Fully underwritten capital watch

**Onto → SUSS → Camtek → FormFactor.**

### New probe-card challenger lane

**JEM → Micronics → Technoprobe.**

### Provisional combined order after JEM falsification

**Onto → SUSS → JEM (provisional investigation) → Micronics / Technoprobe → Camtek → FormFactor.**

This is a research-priority view, not a recommendation ranking. JEM's EPS-based scenario looks competitive, but cash conversion and evidence quality prevent a capital-ranking promotion.

---

## 8. Monitoring triggers

Re-run capital allocation when any of the following occurs:

### Price triggers, absent thesis deterioration

- Onto approaches **~$250** or below;
- SUSS approaches **~€64** or below;
- JEM approaches **~¥5,600** or below **and** cash-conversion / HBM evidence remains intact;
- Micronics approaches **~¥9,800** or below;
- Technoprobe approaches **~€22.5** or below;
- Camtek approaches **~$105** or below;
- FormFactor approaches **~$68** or below.

### Evidence triggers

- material earnings-estimate revisions;
- new HBM4/HBM4E/HBM5 customer/share evidence;
- probe-card second sourcing / customer concentration changes;
- backlog cancellation / capex pull-forward evidence;
- margin / FCF conversion materially different from the model;
- new equity issuance or other dilution;
- architecture substitution changes.

---

## 9. Research-effort allocation from here

PR #30 is an exception to the move away from broad supplier discovery because it found a potentially better **valuation expression of an already-validated bottleneck**.

### Current sequence

1. **#31 probe-card capital allocation / JEM evidence gap — immediate.** Finish the public-evidence exhaustion and decide whether JEM remains `Investigating`, moves to `Watch`, or is deprioritized.
2. **#5 Weebit Nano** — speculative emerging-memory / architectural-discontinuity thesis.
3. **#3 robotics actuators** — separate end-to-end actuator bottleneck map.

Do not open additional AI-memory supplier deep dives unless new evidence suggests a materially better combination of bottleneck strength, company capture and valuation than the existing frontier.

---

## 10. Evidence standard and falsification

Prefer regulatory/audited disclosures, technical standards/papers, customer/supplier primary disclosure, earnings calls/investor presentations, reputable industry research, then specialist journalism. Community discussion is question generation only.

Every analysis must actively search for second sourcing/share loss, rapid capacity additions, architecture substitution, customer bargaining power, falling content intensity, margin normalization, capex pull-forward, dilution and valuation that already assumes the upside.

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

> **Can JEM's low-teens guided earnings multiple survive a cash-flow, dilution and HBM-share evidence test strongly enough to enter the primary capital watch — or is the discount compensation for concentration, capital intensity and lower disclosure quality?**
