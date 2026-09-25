# Prospective validation protocol

**Status:** EXPERIMENTAL, canonical prospective record contract. **Start:** 2026-09-25. **Issue:** #325.

The tested chain is **Abundant Intelligence → Scarce Complements → Bottleneck Migration → Economic Capture → Capital Allocation**. These records measure prospective discrimination; they do not authorize trades or establish alpha.

## Register T0

1. Start from a dated architecture/scarcity question, record discovery source and bounded negative search. Include each listed supplier with a plausible specific bottleneck/capture bridge, even when the decision is REJECT. Exclude only with a T0 reason (outside complement scope, unavailable listing, no recoverable evidence); retain an explicit excluded T0 record when evaluated, rather than deleting a later loser. Never use subsequent results to form the candidate set.
2. Copy `T0.template.json` to `decisions/<unique-ID>.json`. Replace all example text with recoverable facts and clearly marked inferences; capture timestamps and publication dates before outcomes. Select a version from `versions.json`. `v1-261-frozen-2026-09-25` points to the frozen historical #261 rules at commit `96a92b37442cd828ac8cbf2b957ec237bd02e05d`; new prospective research uses the experimental v2 protocol unless a new predeclared version exists. Do not turn v2 hypotheses into live portfolio rules.
3. Predeclare listing, currency, adjusted total-return price treatment (dividends, splits, mergers, delistings), benchmark and currency alignment. Write `DATA-LIMITED` with reason if unavailable. Set 3/6/12/18 calendar-month dates from the decision timestamp; a nontrading day uses the next available close consistently, with actual observation date recorded in evidence. Register both included and excluded decisions. The validator checks presence and chronology, not truth of cited evidence.
4. Before any checkpoint, hash the exact T0 bytes (SHA-256) into `seals.json`, commit via PR and run `python3 scripts/repo_integrity.py --base-ref origin/main`. A later PR cannot alter a committed T0 or its seal. No silent corrections: append a separately identified correction/withdrawal decision and link the old ID in rationale; retain the original.

## Append outcomes

Copy `CHECKPOINT.template.json` to `checkpoints/<ID>-03.json` (then `-06`, `-12`, `-18`). Join to the exact parent ID; leave returns and drawdown as `DATA-LIMITED` with a reason in `new_evidence` if adjusted series are not recoverable. Numeric returns are decimal total returns, e.g. 0.10 for 10%; adjusted return = equity minus benchmark in the same currency/period. Preserve acquisition/delisting cases and account for distributions and dilution. Record architecture, company profit/cash, and shareholder capture independently. Each checkpoint is append-only and cannot be filed early. A correction is a new linked observation, not replacement of a committed checkpoint.

## Change methodology

Add a new `vN-...` key to `versions.json` and a new frozen protocol document *before* decisions under it. State changed inclusion, promotion and capture rules, hypotheses, effective date, and independent future sample. Existing entries, T0s, checkpoints and the #261 historical corpus remain unchanged. Compare by version/cohort; never rescore or retroactively migrate old decisions. A version change requires a governed PR and cannot claim validation on the 15 historical cases. Live methodology, rankings and portfolio authority remain in their existing canonical documents until independently justified.
