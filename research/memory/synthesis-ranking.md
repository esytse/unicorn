# AI Memory — Synthesis & Capital-Allocation Ranking

**Status:** Capital-allocation synthesis  
**Confidence:** Medium-High on structural/company evidence; Medium on valuation scenarios; Medium-Low on JEM HBM-specific evidence  
**Last substantive update:** 2026-09-07  
**Capital-allocation detail:** `research/memory/capital-allocation.md` and `research/memory/probe-card-capital-allocation.md`

## Purpose

Keep three different decisions separate:

1. Is the bottleneck structural?
2. Does the company capture the economics?
3. Does the current price leave enough risk-adjusted upside?

PR #30 added a new test of the third question: whether listed probe-card peers provide a better valuation expression of the already-validated HBM-test bottleneck than FormFactor.

---

## 1. Bottleneck ranking

| Rank | Bottleneck | Bottleneck Strength | Current conclusion |
|---:|---|---:|---|
| 1 | Advanced packaging / interposers / process control | **4.7/5** | Structural and architecture-resilient; larger area/interconnect density increase yield-control needs |
| 2 | HBM stacking / bonding / thermal / yield | **4.6/5** | Structural; difficulty migrates from TCB/MUF/warpage toward hybrid-bond surface prep/alignment/metrology |
| 3 | Test / known-good-die / burn-in | **4.6/5** | Structural; higher package value increases number and value of test insertions |
| 4 | DDR5 / MRDIMM interface silicon | **4.4/5** | Structural within registered/multiplexed server memory; qualified merchant supply is concentrated |
| — | CXL memory-expander controllers | **3.2/5** | Important optionality, but not yet mandatory and merchant competition is broad |

**INTERPRETATION:** The most durable opportunities remain functions that become more valuable as complexity rises regardless of exact architecture: inspection/metrology, known-good-die test, precision wafer handling and qualified memory-interface silicon.

---

## 2. Completed Investment Capture ranking

| Research rank | Company | Bottleneck | Investment Capture | Key attraction | Main constraint |
|---:|---|---|---:|---|---|
| **1** | **Onto Innovation** | AP inspection / metrology | **4.0/5** | HBM4 process-of-record win, >$240m HBM VPA, >$1bn backlog, strong margins | Rerated valuation; KLA/Camtek/Applied competition |
| **2** | **FormFactor** | HBM test / probe cards | **4.0/5** | Volume at all 3 HBM makers, share gains, direct earnings leverage | Valuation; absolute HBM profit not disclosed |
| **3** | **Camtek** | AP inspection / metrology | **3.9/5** | Very visible HBM/OSAT orders and rising AP mix | Premium valuation and possible capex pull-forward |
| **4** | **SUSS** | HBM thinning / TBDB | **3.7/5** | Small-cap asymmetry and direct HBM qualification | Customer competition and unproven HBM hybrid-bond position |
| **5** | **ASMPT** | HBM/AP bonding | **3.7/5** | Multi-customer, multi-architecture TCB/AOR/hybrid exposure | HBM earnings diluted by broader Group |
| **6** | **Montage Technology** | DDR5 / MRDIMM interfaces | **3.8/5** | Exceptional oligopoly franchise and high interface GM | Large market value and demanding valuation |
| **7** | **Hanmi Semiconductor** | HBM TCB | **3.6/5** | Exceptional current HBM sensitivity | Customer/TCB concentration, hybrid transition and extreme valuation |

JEM, Micronics and Technoprobe are **not inserted mechanically into this table yet** because PR #30 is a peer-value screen rather than a completed Investment Capture underwriting wave.

---

## 3. Initial capital allocation (#27)

At the 4 September 2026 references:

| Capital rank | Company | Bear CAGR | Base CAGR | Bull CAGR | Gate C? |
|---:|---|---:|---:|---:|---|
| **1** | **Onto Innovation** | **-7.9%** | **10.4%** | **24.7%** | **No — closest** |
| **2** | **SUSS** | **-17.1%** | **8.8%** | **27.8%** | **No** |
| **3** | **Camtek** | **-15.7%** | **3.8%** | **19.0%** | **No** |
| **4** | **FormFactor** | **-15.7%** | **1.5%** | **14.9%** | **No** |

The conclusion from #27 remains valid: **business quality and stock attractiveness have separated.**

---

## 4. Probe-card peer challenge (#31)

PR #30 surfaces a different way to express the 4.6/5 test/KGD bottleneck.

| Peer | 4 Sep reference | Base CAGR | Bear CAGR | ~12% base-return zone | Evidence status |
|---|---:|---:|---:|---:|---|
| **Japan Electronic Materials (JEM)** | **¥6,230** | **~9.4%** | **-9.8%** | **~¥5,640** | **Investigating — HBM customers/share not yet verified** |
| **Micronics Japan** | **¥11,940** | **~6.8%** | **-11.8%** | **~¥9,760** | Investigating — stronger memory leadership evidence |
| **Technoprobe** | **€27.46** | **~6.9%** | **-16.2%** | **~€22.55** | Watch — operating benchmark, premium valuation |
| **FormFactor** | **$103.90** | **~1.5%** | **-15.7%** | **~$68** | Watch — strongest direct HBM evidence |

**CONCLUSION:** JEM is the only new probe-card peer whose first normalized return screen is competitive with the existing Onto / SUSS capital frontier.

**But:** JEM's evidence quality is lower. Public evidence reviewed so far says memory-probe-card demand is driving growth, but does not establish the same HBM-customer specificity as FormFactor or the same claimed memory leadership as Micronics.

Therefore JEM becomes a **provisional capital challenger**, not a Gate-C candidate.

---

## 5. Combined frontier after PR #30

### Fully underwritten capital order

**Onto → SUSS → Camtek → FormFactor.**

### New challenger lane

**JEM → Micronics → Technoprobe.**

### Provisional combined research order

**Onto → JEM (provisional) → SUSS → Micronics / Technoprobe → Camtek → FormFactor.**

This ordering deliberately penalizes JEM for lower evidence quality. A clean HBM-customer/share verification plus durable normalized FCF could move JEM into the primary capital set; failure to verify would push it back below SUSS/Micronics regardless of its headline P/E.

No company is a `High-conviction research candidate`.

---

## 6. Why JEM matters

**FACT:** JEM's FY Mar-2027 guidance is ¥36.4bn revenue, ¥9.45bn operating profit and ¥6.7bn net income. At the 4 September ¥6,230 reference and ~14.65m shares, the equity value is ~¥91bn and the price is roughly **13.6x management-guided EPS**.

**FACT:** Management says rapidly expanding memory-probe-card demand and prior capacity investments are supporting higher production and high factory utilization.

**INTERPRETATION:** This is much closer to the repository's original asymmetric-upside objective than paying ~30x forward earnings for a large already-rerated US supplier.

**Evidence against:** the public record reviewed does not yet prove HBM4/HBM4E sockets, which HBM manufacturers are customers, what share of revenue/profit is HBM, or what operating margin survives utilization normalization.

**Current decision:** keep JEM `Investigating`; make closing those evidence gaps the immediate AI-memory priority.

---

## 7. Micronics and Technoprobe

### Micronics

MJC provides the strongest **quality/value comparator**. It explicitly says HBM drove DRAM probe-card demand and claims a commanding / world-leading memory-probe-card position. The trade-off is valuation and capital intensity: on the 4 September reference it is around ¥463bn equity value and roughly 19x a 2026 consensus earnings anchor, while its growth plan includes heavy capex and R&D.

### Technoprobe

Technoprobe is the **operating benchmark**. H1 2026 EBITDA margin reached 44.4% and management raised 2026 guidance to 46–48%. That validates the attractiveness of advanced probe-card economics, but a ~€17.6bn equity value and premium forward valuation mean the operating excellence is already heavily capitalized.

---

## 8. Monitoring / valuation zones

Research thresholds, not recommendations:

| Company | Reference | Approx. ~12% base-return zone |
|---|---:|---:|
| **Onto Innovation** | $268 | **~$252** |
| **JEM** | ¥6,230 | **~¥5,640** |
| **SUSS** | €72 | **~€64** |
| **Micronics** | ¥11,940 | **~¥9,760** |
| **Technoprobe** | €27.46 | **~€22.55** |
| **Camtek** | $146 | **~$106** |
| **FormFactor** | $104 | **~$68** |

JEM closed at ¥6,650 on 7 September, so the gap to the unchanged ~¥5,640 research zone had widened to roughly 15%. Do not chase the rerating without better HBM evidence.

---

## 9. What changes the ranking

### JEM moves toward Gate C if

- HBM production customers / sockets are verified;
- HBM-specific revenue/share is material rather than generic DRAM-cycle exposure;
- normalized operating margin and FCF remain strong after capex;
- dilution / share-count reconciliation is benign;
- refreshed valuation still provides ~12%+ base-case return.

### JEM falls back if

- HBM4 qualification is materially weaker than MJC / FORM;
- current growth is conventional DRAM utilization rather than HBM content/share;
- margins collapse with utilization;
- capex or dilution absorbs most incremental economics.

Existing Onto, SUSS, Camtek and FormFactor triggers remain as recorded in `capital-allocation.md`.

---

## 10. Current working conclusion

The core thesis remains intact: **AI-memory complexity creates durable value in process control, test and qualified interfaces.**

The new contribution improves the investment search because it distinguishes the **bottleneck** from the **listed vehicle used to capture it**. FormFactor can be an excellent HBM-test business and still be the wrong stock at its current valuation; JEM may be a better vehicle, but only if its apparent discount survives a much stricter evidence test.

**Immediate research question:**

> **Can JEM's low-teens guided earnings multiple survive HBM-customer/share verification and normalized cash-flow analysis strongly enough to challenge Onto — or is the discount simply compensation for lower evidence quality and memory-cycle risk?**
