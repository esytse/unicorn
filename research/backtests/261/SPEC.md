# #261 Point-in-Time Historical Validation — Frozen v1 Specification

**Frozen:** 25 September 2026  
**Parent:** #261  
**Execution:** #300  
**Status:** FROZEN — do not amend selection rules during the v1 run.

## Question

Would the #261 architecture-first discovery mechanism have identified company-transforming listed suppliers before broad financial/market recognition, using only information available at the historical decision date?

This is a falsification exercise, not a search for historical winners.

## Frozen discovery chain

**World / architecture change -> scarce complement / emerging constraint -> listed supplier state change -> potential company materiality -> economic capture -> market recognition**

A candidate is interesting only when the new engine could plausibly transform total-company economics. Market-cap cutoffs are secondary.

## Point-in-time protocol

For each case:

1. Freeze **T0** before company discovery.
2. Construct an evidence packet containing only material published on or before T0.
3. Describe the architecture change without naming later winners.
4. Map the scarce physical/economic complements.
5. Search the contemporaneously listed supplier universe, including obscure and subsequently failed/delisted names where practicable.
6. Record negative searches.
7. For every candidate, test state-change evidence: qualification/design win, first production, new capacity tied to demand, LTA/prepayment/reservation, 5–15% emerging revenue engine, backlog/order acceleration, margin inflection, recurring content/royalty, customer diversification.
8. Test substitution, integration and commoditisation risk.
9. Freeze one state: **PROMOTE**, **EVIDENCE-BUILD**, or **REJECT**.
10. Only after the prediction commit is frozen may post-T0 evidence be inspected.

## Evidence boundary

- Publication date, not fiscal period, controls admissibility.
- Later terminology may not be used to discover an earlier candidate if the term was not reasonably available at T0.
- Today's Unicorn ranked universe may be used only after candidate formation as a comparison set.
- Later company success/failure must not influence candidate generation.
- If historical evidence cannot be recovered reliably, classify the case **DATA-LIMITED** rather than fill gaps with hindsight.

## Frozen decision tests

### Structural bottleneck
Is the architecture change real, and does it create a specific constraint rather than generic sector growth?

### Company capture
Is there evidence the supplier owns qualification, process know-how, capacity, IP, customer position or another mechanism that can retain economics?

### Financial materiality
Could the new activity plausibly move from roughly 5–15% of company revenue toward 30–50%, or otherwise transform group profit/FCF?

### Equity/valuation
At T0, was enough success still unrecognised that operating conversion could plausibly produce asymmetric equity returns? Valuation cannot rescue a failed bottleneck/capture/materiality test.

## Frozen outputs per candidate

- decision state: PROMOTE / EVIDENCE-BUILD / REJECT
- confidence: Low / Medium / High
- strongest confirming evidence
- strongest disconfirming evidence
- missing bridge
- expected observable next state change
- no numerical probability unless independently calibrated

## Outcome reveal

After freezing the prediction, record:
- whether the bottleneck strengthened, weakened, migrated or disappeared;
- whether the supplier captured economics;
- whether the activity became financially material;
- revenue/margin/FCF evidence;
- substitution/integration/dilution;
- 6/12/18/24/36-month equity outcomes where point-in-time prices can be recovered reliably;
- maximum drawdown where reliable;
- thesis breaker;
- retrospective lesson.

Share-price success alone does not validate the thesis.

## Aggregate metrics

1. **Promotion precision:** promoted candidates that later show genuine economic conversion / promoted candidates with sufficient follow-up.
2. **False-positive rate:** promoted candidates that fail bottleneck/capture/materiality.
3. **Transformation Capture Rate:** emerging engines identified at T0 that later become materially more important to total-company economics.
4. **Lead time:** T0 to observable financial inflection / broad recognition.
5. **False negatives:** important transforming suppliers discoverable at T0 but rejected or missed.
6. **Equity outcome distribution:** secondary validation, benchmarked where practical.

## Failure taxonomy

- architecture/bottleneck wrong
- bottleneck migrated
- supplier capture failed
- vertical integration/substitution
- financial materiality too small
- valuation already recognised success
- dilution/capital intensity
- timing outside useful window
- data-limited / non-investable

## Development vs holdout

Development cases may generate observations but **cannot change v1 rules**. Holdout cases remain sealed until development cases are completed. Any v2 rule proposal must be written after development results and before holdout reveal.

## Completion gate

v1 is complete only when every registered case is either revealed or explicitly DATA-LIMITED, aggregate results and failures are reported, and the holdout set has been evaluated without changing this specification.
