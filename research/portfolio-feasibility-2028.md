# March-2028 portfolio feasibility and contribution paths

**Lifecycle:** DERIVED
**Upstream authorities:** `PORTFOLIO.md`, `AUTOMATION.md`, `research/ranked-universe.md`, canonical company underwrites and live issue monitors
**As of:** 2026-09-26
**Issue:** #357
**Machine model:** [portfolio-feasibility-2028.json](portfolio-feasibility-2028.json)

## Decision

The **£40,000 → £80,000 March-2028 objective is TRIGGER-DEPENDENT, not evidence-supported today**. The current three 5% starters produce a controlled upside boundary of only **£48,600**. An evidence-led six-position construction reaches **£66,880** in its controlled upside. Even the maximum credible seven-position construction reaches **£78,440**, £1,560 short of the primary hurdle.

This is a probability-free feasibility exercise—not a forecast, promise, price target or trade instruction. It uses existing scenario boundaries and entry/add ceilings without refreshing prices or changing any company state. Actual brokerage execution remains manual.

The constraint is not a shortage of attractive themes. It is the absence of enough **currently deployable, independent, evidence-supported return capacity**. Operating capture does not automatically become durable per-share capture; #326–#328 did not validate an early-promotion rule or shareholder alpha.

## Controlled scenario method

Each sleeve uses a representative multiplier inside its existing governed bear/base/upside range at the documented entry condition. Cash remains 1.0x. The construction arithmetic is:

`portfolio value = £40,000 × (cash weight + Σ position weight × scenario multiple)`

The selected points are conservative controls for reconciliation, not expected values. No probability is attached. A position enters a staged construction only after its existing trigger fires, and its weight never exceeds the documented ceiling in the machine model.

| Candidate | State | Ceiling used | Bear / base / upside multiplier | Operating/earnings versus rerating bridge | Main permanent-loss exposure |
|---|---|---:|---:|---|---|
| TAI-TECH | ACTION | 7.5% | 0.85x / 2.00x / 3.00x | Primarily EPS growth; premium retention contributes in upside | AI attribution, TLVR pricing and architecture substitution |
| Laifual | ACTION | 8.0% | 0.625x / 1.35x / 2.30x | Large earnings/cash conversion plus growth valuation | Pre-profit valuation, ASP pressure, concentration and capacity |
| Impro | ACTION | 7.5% | 0.60x / 1.35x / 2.00x | Mostly earnings and mix; moderate rerating in upside | Capital intensity, certification and weak free-cash conversion |
| Modine | WAIT | 15.0% after proof | 0.80x / 1.55x / 2.20x | Revenue/margin/FCF recovery first; post-spin rerating second | Concentration, margin pressure, separation and capacity cycle |
| Centrus | REASSESS | 12.0% after proof | 0.75x / 1.55x / 2.45x | Mainly funded-franchise de-risking/rerating before 2029 earnings | Project finance, policy, timing and dilution |
| JEM | WAIT | 14.0% after proof | 0.68x / 1.35x / 2.00x | EPS/mix/FCF plus HBM-evidence rerating | Memory cycle, concentration, cash conversion and dilution |
| SUSS | WAIT | 12.0% after proof | 0.95x / 1.55x / 2.15x | Backlog-led EPS/margin plus multiple retention | Process/customer concentration and architecture transition |

## Portfolio 1 — current governed signals

Initial and staged deployment are both **15% / £6,000**: 5% each in TAI-TECH, Laifual and Impro, only if their executable conditions and thesis checks hold. **85% / £34,000 remains tactical cash.** No later deployment is assumed without a governed trigger.

| Sleeve | Weight | Start £ | Bear £ | Base £ | Upside £ | Base gain/(loss) | Upside gain/(loss) |
|---|---:|---:|---:|---:|---:|---:|---:|
| TAI-TECH | 5% | 2,000 | 1,700 | 4,000 | 6,000 | +2,000 | +4,000 |
| Laifual | 5% | 2,000 | 1,250 | 2,700 | 4,600 | +700 | +2,600 |
| Impro | 5% | 2,000 | 1,200 | 2,700 | 4,000 | +700 | +2,000 |
| Tactical cash | 85% | 34,000 | 34,000 | 34,000 | 34,000 | — | — |
| **Portfolio** | **100%** | **40,000** | **38,150** | **43,400** | **48,600** | **+3,400** | **+8,600** |

If deployment remains 15%, the deployed portion must reach about **7.67x** merely for the whole pool to double: `0.85 + 0.15x = 2`. The three ACTION signals therefore do not establish portfolio feasibility by themselves.

**Two-failure stress:** if TAI-TECH and Laifual have zero terminal value while Impro reaches base, the portfolio is **£36,700**. This is deliberately harsher than the bear cases and illustrates why starter sizing matters.

**Catalyst sequence:** TAI-TECH revenue/mix/qualification; Laifual repeat orders, margin and cash; Impro certification, cooling growth and cash conversion. Cash becomes deployable only through these add rules or an existing company monitor's entry trigger.

## Portfolio 2 — evidence-led deployment

Initial deployment remains **15%**. Possible staged deployment reaches **54% / £21,600** across six positions only after existing triggers; **46% / £18,400 remains cash**. Modine supplies the most useful independent cooling engine; JEM and SUSS add stronger earnings/backlog evidence but share an HBM/cycle correlation.

| Sleeve | Initial | Staged | Staged £ | Bear £ | Base £ | Upside £ | Base gain | Upside gain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TAI-TECH | 5.0% | 7.5% | 3,000 | 2,550 | 6,000 | 9,000 | +3,000 | +6,000 |
| Laifual | 5.0% | 8.0% | 3,200 | 2,000 | 4,320 | 7,360 | +1,120 | +4,160 |
| Impro | 5.0% | 7.5% | 3,000 | 1,800 | 4,050 | 6,000 | +1,050 | +3,000 |
| Modine | 0% | 9.0% | 3,600 | 2,880 | 5,580 | 7,920 | +1,980 | +4,320 |
| JEM | 0% | 12.0% | 4,800 | 3,264 | 6,480 | 9,600 | +1,680 | +4,800 |
| SUSS | 0% | 10.0% | 4,000 | 3,800 | 6,200 | 8,600 | +2,200 | +4,600 |
| Tactical cash | 46.0% | 46.0% | 18,400 | 18,400 | 18,400 | 18,400 | — | — |
| **Portfolio** | **15%** | **100%** | **40,000** | **34,694** | **51,030** | **66,880** | **+11,030** | **+26,880** |

**Two-failure stress:** Laifual and SUSS at zero with all other sleeves at base leaves **£40,510**. The construction survives because cash and independent engines offset correlated/speculative loss, but it does not compound fast enough to double.

**Catalyst sequence:** current-trio add proof; Modine clean close and post-spin margin/FCF; JEM HBM production/FCF; SUSS backlog conversion/process share. Tactical cash remains preferable until each trigger fires. The best independent alternatives are Modine first and Centrus after funded-capacity proof; forcing another memory sleeve does not solve correlation.

## Portfolio 3 — maximum credible asymmetry

Initial deployment remains **15%**. The highest-risk construction that still respects documented ceilings and proof gates reaches **76% / £30,400 deployed** and keeps **24% / £9,600 cash**. It uses seven positions: the current trio plus maximum post-proof allocations in Modine, Centrus, JEM and SUSS.

| Sleeve | Initial | Staged | Staged £ | Bear £ | Base £ | Upside £ | Base gain | Upside gain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TAI-TECH | 5.0% | 7.5% | 3,000 | 2,550 | 6,000 | 9,000 | +3,000 | +6,000 |
| Laifual | 5.0% | 8.0% | 3,200 | 2,000 | 4,320 | 7,360 | +1,120 | +4,160 |
| Impro | 5.0% | 7.5% | 3,000 | 1,800 | 4,050 | 6,000 | +1,050 | +3,000 |
| Modine | 0% | 15.0% | 6,000 | 4,800 | 9,300 | 13,200 | +3,300 | +7,200 |
| Centrus | 0% | 12.0% | 4,800 | 3,600 | 7,440 | 11,760 | +2,640 | +6,960 |
| JEM | 0% | 14.0% | 5,600 | 3,808 | 7,560 | 11,200 | +1,960 | +5,600 |
| SUSS | 0% | 12.0% | 4,800 | 4,560 | 7,440 | 10,320 | +2,640 | +5,520 |
| Tactical cash | 24.0% | 24.0% | 9,600 | 9,600 | 9,600 | 9,600 | — | — |
| **Portfolio** | **15%** | **100%** | **40,000** | **32,718** | **55,710** | **78,440** | **+15,710** | **+38,440** |

**Two-failure stress:** Laifual and Centrus at zero with all other sleeves at base leaves **£43,950**. This is survivable but converts the objective into capital preservation, not doubling.

**Correlation and sequencing:** TAI-TECH/Impro/Modine share AI-infrastructure demand but have different product/catalyst paths; JEM/SUSS are the explicit correlated HBM pair; Laifual is robotics/China; Centrus is the strongest independent policy/nuclear engine. Deployment order should follow proof, not the target: current starters → Modine post-spin evidence → Centrus funded capacity → only then the best triggered memory sleeve(s). Cash remains deployable for failed-trigger replacement or a demonstrably superior independent engine.

## Reverse-underwritten hurdles

| Hurdle | Classification | What must become true |
|---:|---|---|
| **£80,000 / 2x** | **TRIGGER-DEPENDENT** | All major staged triggers must fire, 76% must become responsibly deployable, and the controlled maximum-asymmetry upside must improve by **£1,560** through upper-band delivery or governed rotation. This is close mathematically but not supported by today's deployable state. |
| **£120,000 / 3x** | **MATHEMATICALLY POSSIBLE BUT OPERATIONALLY IMPLAUSIBLE** | Above the £78,440 controlled upside, the remaining £9,600 cash would need about **5.33x** by itself, or several independent sleeves must reach stretch outcomes plus successful rotation. |
| **£160,000 / 4x** | **MATHEMATICALLY POSSIBLE BUT OPERATIONALLY IMPLAUSIBLE** | The remaining cash would need about **9.50x** above the controlled upside, or repeated multi-bagger rotation without permanent-loss interruption. |
| **£200,000 / 5x** | **UNSUPPORTED BY CURRENT EVIDENCE** | Current governed underwrites provide no responsible path to the additional **£121,560**; a cash-only bridge would require about **13.66x**. |

No hurdle is **EVIDENCE-SUPPORTED** today. The £80k classification can improve only when staged triggers convert into deployable capital and the resulting underwrites reconcile above 2x without heroic concentration. A lower share price alone does not solve missing company economics.

## Minimum follow-up

Existing company monitors already own the evidence needed for current-starter adds and for Modine, Centrus, JEM, SUSS and Jinpan entries. Duplicating those research tasks would create competing workflow state. The only new bounded follow-up is a portfolio-level re-test triggered when the opportunity set, rather than one company narrative, becomes materially more deployable:

- re-run contribution arithmetic when governed deployable ceilings reach at least 50% of the pool **or** two independent non-starter candidates become ACTION;
- compare the triggered candidates with tactical cash and the current trio;
- change composition, size, capital rank or hurdle class only if the reconciled portfolio bridge changes.

This preserves the original chain: **Abundant Intelligence → Scarce Complements → Bottleneck Migration → Economic Capture → Capital Allocation**. It does not force capital allocation merely because structural research is attractive.
