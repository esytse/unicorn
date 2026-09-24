# Evidence Quality & Calibration — Corpus Audit

**As of:** 2026-09-24  
**Parent:** #193 / #196 / #204

## Structural coverage test

Main contains **94 markdown files under `research/`**: 26 canonical company files, 30 technical/thematic deep dives, 6 cross-theme/capture/ranking surfaces, and **32 other research surfaces**.

**TEST RESULT: FAIL-CLOSED.** Waves 1–4 do not yet prove full-corpus coverage because 32/94 files fall outside the calibrated structural classes.

## Residual-risk test

The residual class includes decision-bearing work: scientific-AI company/screens and execution bottlenecks, Physical-AI evaluation/verification economics, Gate-E portfolio construction, fusion infrastructure/candidate work, and theme theses/value chains/synthesis/capital-allocation surfaces.

**TEST RESULT: FAIL-CLOSED.** These require calibration or an explicit N/A rationale.

## Reasoning-integrity test

The Laifual pilot and live Gate-E retrofit can weaken or strengthen individual confidence layers without mechanically changing company state.

**TEST RESULT: PASS.**

## False-precision test

Live Gate-E work now treats governed price conditions as reassessment bands/regions where evidence does not justify point precision.

**TEST RESULT: PARTIAL PASS.** Residual decision surfaces remain to be checked.

## Technical-importance vs equity-capture test

Waves 3–4 require a separate bridge from bottleneck evidence to company capture, financial materiality and valuation.

**TEST RESULT: PASS for calibrated surfaces; residual surfaces remain untested.**

## Governance test

PRs #194, #195, #197, #199, #201 and #203 passed Research governance on their latest tested heads before merge.

**TEST RESULT: PASS.**

## What testing changed

Testing disproved the assumption that companies + deep dives + six cross-theme surfaces represented the entire research corpus. The correct denominator is the complete research tree. The programme remains open until **94/94 files are accounted for**.

## Next tests

1. Classify all 32 residual files as decision-bearing, supporting/contextual, template, or obsolete.
2. Calibrate every decision-bearing residual file.
3. Record explicit N/A rationale where calibration adds no decision value.
4. Seed the decision/outcome ledger from current live Gate-E decisions.
5. Re-run the denominator test and require 94/94 accounted for before #196 closes.
6. Sample-test source tier, evidence freshness, counter-evidence and fundamental-vs-rerating separation.

## Residual classification — execution pass

The 32-file residual class was classified rather than blindly given identical treatment.

- **23 decision-bearing residual surfaces** were calibrated in this pass: allocation/ranking/thesis/value-chain surfaces, Gate-E portfolio construction, fusion decision surfaces, Physical-AI evaluation/verification economics, and scientific-AI company/theme work.
- **7 research-plan / monitoring / screening files** are workflow-control surfaces rather than investment conclusions: energy research plan; fusion backlog; fusion monitoring triggers; fusion screening rules; memory research plan; Physical-AI research plan; robotics-actuators research plan. Their governing role is procedural; evidence-chain conclusions live in the linked research artifacts.
- **2 templates** (`research/_templates/company.md`, `research/_templates/theme.md`) are structural authoring controls rather than evidence claims. The company template already carries the Gate-E evidence-chain standard; the theme template is an authoring scaffold and is N/A for decision calibration.

**ACCOUNTING TEST: 94/94 structurally accounted for** = 26 company + 30 deep dives + 6 cross-theme surfaces + 23 calibrated residual decision surfaces + 7 procedural controls + 2 templates.

This closes the structural-denominator gap found by the first Wave-5 test. It does **not** prove every factual claim is fresh or high quality; source-tier/freshness sampling and future outcome calibration remain ongoing controls.
