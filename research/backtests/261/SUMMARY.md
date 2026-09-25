# #261 Point-in-time historical validation — final report

**Completed:** 25 September 2026. **Method:** frozen v1 `SPEC.md`; pre-registered `CASE_REGISTER.md`; D01–D10 prediction/reveal cycles; development-only `DEVELOPMENT_REVIEW.md` and `V2_PROPOSAL.md` written/merged before H01–H05 candidate research; five holdout predictions merged together before any holdout outcome reveal. The source register and per-case files preserve contemporaneous and post-freeze evidence separately. **No frozen state was revised after reveal.**

## Audit sequence

| Stage | Artifact / gate |
|---|---|
| Protocol and 15-case register | `SPEC.md`, `CASE_REGISTER.md` frozen before predictions |
| Development predictions/reveals | D01–D05 sequential PRs; D06–D10 prediction PR #319 merged before outcome PR #320 |
| Development review and v2 hypothesis | PR #321 merged before holdouts were unsealed; v2 never used to score v1 |
| Holdout predictions | 17 states frozen in PR #322, governance success and merged before outcome research |
| Holdout outcomes | PR #323 merged after governance success; all 17 rows in `OUTCOMES.md` |

## Aggregate results

| Measure | Development D01–D10 | Holdout H01–H05 | Overall / interpretation |
|---|---:|---:|---|
| Registered cases revealed | 10/10 | 5/5 | 15/15; no case dropped |
| Frozen candidate states | 46 | 17 | 63, including some repeated companies in distinct cases and scope comparators |
| PROMOTE / EVIDENCE-BUILD / REJECT | 2 / 25 / 19 | 0 / 9 / 8 | 2 / 34 / 27 |
| Initial economic conversion of PROMOTE | 2/2 | 0/0, undefined | 2/2 observed in a selected small development sample; no holdout estimate |
| Initial economic failure of PROMOTE | 0/2 | 0/0, undefined | 0/2 within initial forecast window; both later suffered material durability impairments |
| Clear economically material false negative | no unambiguous scored one; several possible | at least 1 (SK hynix HBM) | A frozen EVIDENCE-BUILD production socket reached >40% of Q4 2024 DRAM sales and strong group earnings; West's later 17% quarterly GLP-1 sales is a possible second, but pre-T0 drug-specific qualification was unrecovered |
| Transformation Capture Rate | DATA-LIMITED | DATA-LIMITED | No independently enumerated universe of all transforming listed suppliers; cases condition on a known transition, with contaminated/excluded names and weak product attribution |
| Lead time to financial inflection/market recognition | DATA-LIMITED | DATA-LIMITED | Inconsistent product reporting and no reliable recognition timestamps; SK hynix T0-to-Q4 2024 mix is ~24 months but is one observable interval, not a sample metric |
| Adjusted equity return / drawdown vs benchmark | 0/46 | 0/17 | 0/63 fully scored at prescribed 6/12/18/24/36m checkpoints; acquisition consideration is known for some names, but no consistent adjustment, delisting, spin, FX/dividend and benchmark series was assembled |

The 63 rows are **candidate-case observations**, not 63 independent stock selections. Precision and false-positive fractions use only the two initial PROMOTE states with follow-up; they are not calibrated probabilities, and a zero holdout PROMOTE denominator cannot validate predictive precision. The two initial PROMOTEs were Applied Optoelectronics (100G) and Q Technology (multi-camera). Both converted economically, then encountered concentration/architecture or ASP/margin durability failures. See `OUTCOMES.md` for every frozen row and `FAILURES.md` for mistakes, exclusions and disconfirmers.

## What the test learned

1. **Architecture identification was easier than investable supplier selection.** Many transitions strengthened, but TSMC's captive packaging, Novo's fill-site acquisition, broad incumbent mix and later product-mode changes impeded independent supplier attribution.
2. **Strong production evidence can be a missed early signal.** SK hynix named HBM3 mass production for H100 before T0; v1 still withheld promotion for missing group mix/valuation. HBM later exceeded 40% of DRAM quarterly sales, making this a clear *operating* miss. It does not establish a T0 equity opportunity without prices and market recognition.
3. **Revenue can rise while shareholder capture fails.** Akoustis and Wolfspeed needed financing despite product growth; PacBio grew instruments/consumables with heavy losses. Asetek's data-centre revenue went to zero even as direct-liquid demand strengthened elsewhere. Advanced Energy exited solar inverters.
4. **Durability and timing are separate from initial conversion.** Applied Optoelectronics and Q Technology converted first and then deteriorated. Enphase showed near-term losses after its 2014 improvement before a later multi-year profitable scale-up. A 2022 pandemic/AI demand discontinuity cannot be assumed at earlier T0 cutoffs.
5. **Broad incumbents may be missed by a strict new-engine rule.** Cognex, Arista, Modine, Hammond, Ypsomed and West showed later relevant scale, with varying degrees of case-specific attribution. These are not all clean false negatives. The 5–15% heuristic is not independently validated as a universal filter.
6. **Coverage limits are material.** D02 Largan and D06 Besi were excluded after post-T0 search-snippet leakage; H04 Hanmi lacked a verified pre-T0 primary commercial packet; H05 SolarEdge was unlisted at its T0. Exclusions cannot be quietly counted as successful discoveries or false negatives.

## Decision for #261

**INTERPRETATION:** The frozen v1 chain demonstrated two early operating conversions and useful negative controls, but **did not validate a repeatable pre-recognition equity discovery strategy**. The holdout set provided no PROMOTE to test precision and exposed a clear economic miss. The method remains suitable as an architecture-first *research triage* discipline with explicit uncertainty, not a calibrated ranking, market-timing or capital-deployment signal. Do not change live portfolio statuses or claim investment alpha from this study.

**HYPOTHESIS / next validation:** `V2_PROPOSAL.md` proposes funded-scale, durability, incumbent-upgrade and attribution gates for a **new independently registered prospective sample**. It was authored before holdout research but is not validated by H01–H05, which were judged only under v1. Do not adopt v2 as a proven rule on these data. Any future equity assessment requires a survivorship/corporate-action-aware adjusted series and a predeclared benchmark; the missing return analysis is a material limitation of this completed operating backtest.

## Completion boundary

Every registered case was revealed and every candidate row has an outcome. The failure ledger, source register, aggregate denominators, holdout v1 evaluation and methodology decision are documented. The specific question of **before broad market recognition and asymmetric equity returns remains DATA-LIMITED**, rather than answered in the affirmative. No further testing is scheduled in this execution run; a separate future sample and price-data protocol would be new work.
