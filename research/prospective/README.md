# Prospective decision records

Read [PROTOCOL.md](PROTOCOL.md) for registration, checkpoints and version changes. `versions.json` is the append-only version registry; `decisions/` holds sealed T0 predictions, `checkpoints/` holds appended outcomes, and `seals.json` pins exact T0 bytes. Empty directories acquire records on the first prospective candidate. This does not replace the live qualitative [calibration ledger](../prediction-calibration-ledger.md) or the frozen [#261 corpus](../backtests/261/SUMMARY.md).

For each filed checkpoint, add a matching `performance/<ID>-MM.json` from [PERFORMANCE.template.json](PERFORMANCE.template.json). The [measurement protocol](MEASUREMENT.md) defines identifiers, adjusted series, missingness, event timing, corporate actions and cohort denominators. `python3 scripts/performance.py` produces derived scorecards; CI rejects a checkpoint without its supplement. Neither file rewrites T0 or historical #261.
