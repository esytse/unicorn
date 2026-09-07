# AI Memory — Synthesis & Capital-Allocation Ranking

**Status:** Capital-allocation synthesis  
**Confidence:** Medium-High on structural/company evidence; Medium on valuation scenarios  
**Last substantive update:** 2026-09-07  
**Capital-allocation detail:** `research/memory/capital-allocation.md`

## Purpose

Keep three different decisions separate:

1. Is the bottleneck structural?
2. Does the company capture the economics?
3. Does the current price leave enough risk-adjusted upside?

The first two company-underwriting waves are complete and issue #27 has now tested the third question for the leading candidates.

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

## 2. Investment Capture ranking

| Research rank | Company | Bottleneck | Investment Capture | Key attraction | Main constraint |
|---:|---|---|---:|---|---|
| **1** | **Onto Innovation** | AP inspection / metrology | **4.0/5** | HBM4 process-of-record win, >$240m HBM VPA, >$1bn backlog, strong margins | Rerated market cap; KLA/Camtek/Applied competition |
| **2** | **FormFactor** | HBM test / probe cards | **4.0/5** | Volume at all 3 HBM makers, share gains, direct earnings leverage | Post-rerating valuation; absolute HBM profit not disclosed |
| **3** | **Camtek** | AP inspection / metrology | **3.9/5** | Very visible HBM/OSAT orders and rising AP mix | Premium valuation and possible capex pull-forward |
| **4** | **SUSS** | HBM thinning / TBDB | **3.7/5** | Smallest-cap asymmetry and direct HBM qualification | Customer competition and unproven HBM hybrid-bond position |
| **5** | **ASMPT** | HBM/AP bonding | **3.7/5** | Multi-customer, multi-architecture TCB/AOR/hybrid exposure | HBM earnings diluted by broader Group; lower Group margins |
| **6** | **Montage Technology** | DDR5 / MRDIMM interfaces | **3.8/5** | Exceptional oligopoly franchise, ~36.8% reported share, high interface GM | Large market value and demanding valuation |
| **7** | **Hanmi Semiconductor** | HBM TCB | **3.6/5** | Exceptional current HBM sensitivity and ~52% Q2 operating margin | Customer/TCB concentration, hybrid transition and extreme valuation |

The ordering is a research-priority judgment, not a mechanical score ranking.

---

## 3. Bottleneck × capture screen

This remains useful for deciding what deserved valuation work, but it is **not** a valuation model.

| Company | Bottleneck Strength | Investment Capture | Screen /25 |
|---|---:|---:|---:|
| Onto Innovation | 4.7 | 4.0 | **18.8** |
| FormFactor | 4.6 | 4.0 | **18.4** |
| Camtek | 4.7 | 3.9 | **18.3** |
| SUSS | 4.6 | 3.7 | **17.0** |
| ASMPT | 4.6 | 3.7 | **17.0** |
| Montage | 4.4 | 3.8 | **16.7** |
| Hanmi | 4.6 | 3.6 | **16.6** |

Issue #27 demonstrates why the screen cannot select the investment: FormFactor and Camtek remain near the top technically, but their starting valuations materially reduce expected returns in a normalized scenario.

---

## 4. Capital-allocation result

**Reference date:** 4 September 2026 for Onto, FormFactor, Camtek and SUSS.  
**Detailed assumptions:** `capital-allocation.md`.

| Capital rank | Company | Reference price | 2027 EPS anchor multiple | Bear CAGR | Base CAGR | Bull CAGR | Gate C? |
|---:|---|---:|---:|---:|---:|---:|---|
| **1** | **Onto Innovation** | $268.01 | ~23x | **-7.9%** | **10.4%** | **24.7%** | **No — closest** |
| **2** | **SUSS** | €72.40 | ~21x | **-17.1%** | **8.8%** | **27.8%** | **No** |
| **3** | **Camtek** | $145.72 | ~30x | **-15.7%** | **3.8%** | **19.0%** | **No** |
| **4** | **FormFactor** | $103.90 | ~30x | **-15.7%** | **1.5%** | **14.9%** | **No** |

The scenario model uses 2027 consensus EPS as a visible-cycle anchor, haircuts it in the bear case, assumes slower 2027–2030 growth than the current AI ramp, and normalizes terminal P/E rather than preserving today's multiples.

### Current capital conclusion

**CONCLUSION:** **No candidate passes Gate C at current reference prices.**

- **Onto** is the preferred valuation/quality watch and is closest to a sufficient margin of safety.
- **SUSS** remains the higher-risk asymmetric alternative: similar scenario-weighted upside, but much larger bear-case impairment risk.
- **Camtek** and **FormFactor** remain excellent franchises, but the current share prices demand too much post-2027 earnings compounding for a strong margin of safety.

---

## 5. Reverse valuation test

To earn a **12% annual return** through end-2030 at the base terminal P/E, current prices require approximately:

| Company | Required 2027–30 EPS CAGR |
|---|---:|
| Onto Innovation | **17%** |
| SUSS | **20%** |
| Camtek | **28%** |
| FormFactor | **30%** |

**INTERPRETATION:** Onto's hurdle is demanding but plausible if HBM/AP process-control growth persists. SUSS can clear its hurdle in a strong execution case but carries much greater customer/process risk. Camtek and FormFactor need exceptionally strong earnings compounding for several years after the current earnings step-up.

---

## 6. Monitoring / valuation zones

These are **research thresholds, not buy recommendations**. They are the approximate entry prices at which the base scenario would produce a 12% annualized return to end-2030, assuming the earnings thesis does not deteriorate.

| Company | Current reference | ~12% base-return zone | Approx. reset needed |
|---|---:|---:|---:|
| **Onto Innovation** | $268 | **~$252** | ~6% |
| **SUSS** | €72 | **~€64** | ~12% |
| **Camtek** | $146 | **~$106** | ~28% |
| **FormFactor** | $104 | **~$68** | ~34% |

A 15% base-return hurdle would require roughly $225 for Onto, €57 for SUSS, $94 for Camtek and $61 for FormFactor.

---

## 7. Why Onto now ranks first for capital allocation

**FACT:** Onto's Q2 revenue reached $343.1m, +35.3% y/y, backlog exceeded $1bn, non-GAAP gross margin was 57.0%, and Q3 non-GAAP operating-margin guidance was 31.5–32.5%.

**FACT:** It has direct HBM4 process-control evidence and a >$240m HBM volume agreement through 2027.

**INTERPRETATION:** Onto combines evidence quality comparable to FormFactor/Camtek with a lower 2027 EPS multiple and a stronger base-case return. It therefore moves from the top *research* tier to the top *capital-allocation watch* position.

**Evidence against:** current market cap has already rerated sharply; HBM customer concentration is meaningful; $1bn backlog could still contain pull-forward; KLA/Camtek/Applied remain strong competitors.

---

## 8. Why SUSS remains second rather than first

SUSS is the only primary candidate with a market value near €1.4bn, record backlog and direct HBM temporary-bonding exposure. That creates the greatest percentage upside if execution goes right.

But 2027 consensus already assumes a large recovery: €591.7m sales, 15.5% EBIT margin and €3.41 EPS versus a 2026 guidance trough. The downside distribution is therefore much wider than Onto's, and process-of-record competition at a Korean HBM customer remains unresolved.

**INTERPRETATION:** SUSS is the best asymmetric *watch*, not the best risk-adjusted allocation at the current price.

---

## 9. Why FormFactor and Camtek fall in capital rank despite strong research scores

### FormFactor

The HBM test thesis remains intact: volume at all three memory makers, strong revenue/margin growth and a structural test bottleneck. The problem is price. At roughly 30x the 2027 consensus EPS anchor, a normalized 22x terminal P/E requires ~30% annual EPS growth from 2027–2030 to generate a 12% return.

### Camtek

Camtek has exceptionally visible HBM/OSAT/AP orders and strong margins. But its roughly 30x 2027 EPS anchor and order-pull-forward risk leave insufficient downside protection. A 12% return at a 23x terminal multiple requires ~28% 2027–2030 EPS CAGR.

Neither thesis is rejected. Both remain `Watch`; the required entry price or earnings-estimate upgrade is simply much larger.

---

## 10. ASMPT, Montage, Hanmi and DISCO

- **ASMPT:** screened in #27; current ~28x published forward P/E and broader-company dilution do not improve the allocation frontier. Remains `Watch`.
- **Montage:** excellent franchise and improving new-product revenue, but already-large market value and premium valuation keep it below the allocation shortlist.
- **Hanmi:** extraordinary current margins and HBM sensitivity, but concentration and transition risk make normalized valuation difficult to defend.
- **DISCO:** remains a high-quality benchmark; HBM-specific revenue/share is still insufficiently quantified for dedicated capital allocation.

---

## 11. Falsification / what changes the capital ranking

### Onto moves toward Gate C if

- price reaches roughly the low-$250s or below without thesis deterioration;
- 2027/2028 backlog visibility rises enough to justify >17% post-2027 EPS compounding;
- HBM process-control share expands across more than one major customer.

### SUSS moves toward Gate C if

- price approaches the mid-€60s or lower;
- 2027 backlog conversion supports ≥15% EBIT margin;
- temporary-bonding share is defended and HBM hybrid-bond production qualification becomes explicit.

### Camtek moves toward Gate C if

- price approaches ~$105 or normalized earnings estimates rise materially;
- the 2026 order surge converts cleanly into 2027/2028 revenue rather than pulling demand forward;
- Hawk retains high-value HBM/hybrid-bond share.

### FormFactor moves toward Gate C if

- price approaches ~$68 or normalized EPS rises enough to reduce the earnings-growth hurdle materially;
- HBM probe-card content/share continues to rise while gross margins remain durable.

---

## 12. Current working conclusion

We have validated the core “picks and shovels of memory complexity” thesis, but **business quality and stock attractiveness have now separated**.

The highest-value next action is not more supplier discovery. It is monitoring prices, earnings estimates, backlog conversion and architecture/customer evidence.

**Capital watch order today:**

**Onto → SUSS → Camtek → FormFactor.**

No company is a `High-conviction research candidate` yet. A better price or stronger normalized-earnings evidence is required before capital-allocation conviction increases.
