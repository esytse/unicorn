# Aggressive Dynamic Portfolio Strategy — Gate E

**Status:** Active  
**Strategy reference:** 2026-09-09  
**Live decision surface refreshed:** 2026-09-24  
**Target date:** March 2028  
**Backlog:** #117  
**Automation:** LIVE — #120 / `AUTOMATION.md`  
**Upstream research:** #110; historical Gate-D baseline #114  

> This is a research and portfolio-management framework, not automatic trading instructions.

## Objective

Manage a starting capital pool of **£40,000** over **18 months**, targeting:

- **minimum objective: 2x → £80,000 by March 2028**;
- **intermediate milestones: 3x → £120,000; 4x → £160,000**;
- **stretch objective: 5x → £200,000**.

The mathematically implied annualized portfolio hurdles are approximately:

- **2x in 18 months: 58.7% annualized**;
- **3x: 108.0% annualized**;
- **4x: 152.0% annualized**;
- **5x: 192.4% annualized**.

The **2x objective is the primary design target**. The 5x outcome is a stretch objective, not a base-case forecast. The shorter horizon deliberately increases risk tolerance, concentration and turnover, but it does **not** justify lowering evidence standards or inventing unsupported upside.

## Core interpretation

The target applies to the **portfolio**, not to every security bought today.

This is explicitly a **dynamic, concentrated portfolio**. Expect:

- staged entries rather than all-at-once deployment;
- additions when evidence, catalyst probability and forward return improve;
- trims when valuation outruns evidence or concentration becomes excessive;
- exits when a thesis breaks, a catalyst is harvested or a superior opportunity emerges;
- active capital rotation between companies, themes and migrating bottlenecks;
- tactical cash when no setup clears the hurdle.

Cost basis is not the decision anchor after purchase. Every holding must continuously compete for capital based on **forward expected return from the current price and the remaining 18-month window**.

## What “more aggressive” means

The aggressive mandate changes portfolio construction in five ways:

1. **Concentration:** favour **4–7 meaningful positions** over a diluted ten-name basket once evidence supports deployment.
2. **Catalyst speed:** prefer situations with a material **3–12 month catalyst path** that can affect earnings, cash flow, qualification, royalties, utilization, funding or rerating inside the 18-month window.
3. **Asymmetry:** prioritise candidates where a successful catalyst can materially transform per-share economics or market expectations.
4. **Rotation:** be willing to recycle capital quickly when forward return falls or a stronger bottleneck/catalyst emerges.
5. **Risk acceptance:** tolerate wider volatility and higher company-specific risk in exchange for genuine upside asymmetry, while retaining explicit thesis-break and dilution controls.

Aggressive does **not** mean indiscriminate leverage, averaging down without evidence, or holding broken theses.

## Relationship to Gate D

`research/top10-capital-allocation.md` and closed issue **#114** preserve the dated Gate-D valuation baseline. Their 10/12/15% normalized-return work remains useful for downside analysis, valuation discipline and understanding what was priced in on the reference date.

Gate D is now **historical context, not the active action framework**. Old four-year or normalized-return price zones must not be treated as current Buy/Add/Trim/Sell triggers unless a current Gate-E company underwrite explicitly re-adopts an evidence-supported condition.

Gate E asks:

1. Can this position plausibly contribute to a **2x portfolio outcome by March 2028**?
2. What specific catalyst sequence could create that return inside 18 months?
3. Is there a defensible **3–5x path** for the highest-asymmetry positions without unsupported TAM assumptions?
4. What probability and evidence are required?
5. What is the bear/permanent-capital-loss case?
6. Is this still the best use of capital versus the other active candidates?

A strong long-duration business with no near-term rerating or earnings catalyst may be a good investment generally but a poor fit for this mandate.

## Position roles

Every active candidate or holding should be assigned one role:

- **Core asymmetric** — relatively stronger evidence with a credible near-term earnings/rerating path and meaningful upside.
- **Catalyst asymmetric** — higher-risk position where a defined 3–12 month catalyst can materially change valuation or economics.
- **Speculative option** — small position with potentially very large payoff but unresolved commercialization, funding, architecture or execution evidence.
- **Watch** — structurally interesting but the current price, catalyst timing or evidence does not justify capital.
- **Avoid** — current return potential, timing, downside or thesis quality is inadequate for the mandate.

Role and position size are separate from the cross-theme `watchlist.md` research status.

## Concentration framework

The portfolio should not be equal weighted by default.

Working design principles for the initial portfolio:

- **4–7 active positions** once deployable opportunities exist;
- the highest-confidence/highest-asymmetry names may receive materially larger weights than lower-confidence options;
- speculative positions should remain smaller than evidence-backed catalyst positions;
- position ceilings must reflect liquidity, dilution risk, downside and evidence confidence;
- thematic duplication should be counted as correlated exposure even when securities are different;
- cash can remain available for event-driven entries, but should not become a permanent default when qualifying setups exist.

Initial evidence-backed portfolio construction was completed in **#131**. The live portfolio remains conditional rather than fully deployed: position weights are activated only when governed company-level entry conditions are met, and **#132** re-ranks candidates as prices, evidence and catalysts change. Do not force deployment merely to fill 4–7 slots.

## Live portfolio checkpoint — 24 September 2026

The authoritative live ranking is `research/top10-unicorn-priority.md`; this strategy file defines the rules rather than duplicating a static ranking.

Since the 15 Sep checkpoint, the scarce-complements remap has increased the marginal-research hurdle for additional correlated memory exposure. QNX FY27 Q2 has been assessed: operating quality/backlog improved materially, but the current state remains **REASSESS / WAIT**, with a first price-led re-underwrite condition around <=~US$7 or materially stronger non-auto evidence. Ouster has completed Gate-E valuation work and remains **REASSESS / WAIT outside the Top 10**, with valuation/margin/FCF proof still the gating evidence.

Laifual remains the only governed research-level ACTION in the current decision surface: a 5% starter only at executable <=HK$48 with thesis intact. No brokerage execution is assumed by the repository.

## Transaction rules

Every deployable position must define:

### Entry
- evidence threshold;
- valuation / price zone;
- intended initial size;
- expected 18-month return at entry;
- catalyst sequence and timing;
- downside if the catalyst fails.

### Add
Add only when at least one of the following improves without a compensating deterioration:
- evidence quality;
- operating capture;
- valuation / forward return;
- bottleneck strength;
- probability or timing of the catalyst path.

Do not add solely because price fell below cost basis.

### Trim
Consider trimming when:
- price rises materially faster than normalized earnings or evidence;
- a major catalyst is substantially priced before realization;
- forward expected return falls below competing uses of capital;
- position concentration becomes disproportionate to evidence confidence;
- bottleneck strength weakens or begins to migrate.

### Sell
Sell or materially reduce when:
- a defined thesis breaker occurs;
- a catalyst fails and the remaining 18-month return no longer clears the portfolio hurdle;
- the structural bottleneck is being commoditized or bypassed;
- company capture deteriorates even if the broader theme remains correct;
- dilution or capital intensity destroys per-share economics;
- a materially superior risk-adjusted opportunity emerges.

A successful original thesis is **not** a reason to keep holding if the forward bottleneck, catalyst or expected return has migrated elsewhere.

## Bottleneck-migration framework

Assume bottlenecks **move as technology and supply chains mature**.

For each theme, re-test the full value chain rather than extrapolating current scarcity indefinitely.

Track whether each important bottleneck is:

- **Strengthening** — scarcity, qualification, pricing power or switching cost is increasing;
- **Stable** — constraint and economic capture remain broadly intact;
- **Weakening** — capacity, competition or standardization is eroding scarcity;
- **Migrating** — value is moving to another layer of the stack.

### Migration mechanisms to monitor

- capacity additions and yield learning;
- new qualified competitors;
- open standards / modular architectures;
- customer or OEM vertical integration;
- substitution by a new technical architecture;
- movement upstream/downstream in the value chain;
- shift from hardware into software, data, safety, qualification, services, power, test or orchestration;
- regulatory or policy changes that create/remove scarcity;
- capital-market funding that accelerates supply response.

The current Top 10 is a **live ranked hunting universe, not a permanent portfolio list**. New names should enter when bottleneck migration or new evidence creates better 18-month asymmetry than the weakest incumbent.

## Review cadence

### Hourly alert-first monitoring
The live **Unicorn Portfolio Ops** scheduler runs hourly from **00:00 through 22:00 Europe/London** under `AUTOMATION.md`.

Every run performs a cheap trigger/action scan first. User notifications are quiet by default and are emitted only for a new/material:
- `ACTION`;
- `REASSESS`;
- `THESIS BREAK`;
- `CATALYST`;
- `SYSTEM DEGRADED`.

Hourly monitoring does **not** imply hourly full research. Normally no more than one non-triggered heavy research item is started per rolling 24 hours; P0/P1 trigger-driven work may override that when needed for a decision-useful alert.

### Event-driven
Refresh affected holdings/candidates after:
- earnings and regulatory filings;
- major qualification wins/losses;
- production or royalty milestones;
- capital raises, M&A or material dilution;
- large capacity additions;
- architecture / standard changes;
- major policy or regulatory changes.

### Material price move
Recalculate expected return when a current Gate-E underwrite defines a relevant price/valuation condition or a move materially changes the remaining-window case. Do not anchor to the original purchase price or prior high.

### Monthly portfolio re-rank
Issue **#132** becomes executable when the monthly review is due. Rank all holdings and highest-priority candidates on:
1. remaining 18-month forward return;
2. catalyst timing/probability;
3. downside/permanent-loss risk;
4. bottleneck direction;
5. best alternative use of capital.

Stay quiet if the re-rank is materially unchanged; notify only if it creates an `ACTION` or `REASSESS` condition.

### Quarterly full-universe challenge
Issue **#133** becomes executable when the quarterly challenge is due. Re-test:
1. current holdings;
2. Top-10 candidates;
3. important benchmark companies;
4. newly surfaced companies from migrating bottlenecks.

The recurring question is: **where is the best risk-adjusted asymmetry for the remaining time to March 2028?**

## Live automation and backlog execution

Gate E is operated through `AUTOMATION.md` and automation epic **#120**.

**Deployment status:**
- #121 backlog normalization — completed;
- #122 hourly Portfolio Ops deployment — completed;
- one live scheduler is enabled;
- actual brokerage execution remains manual.

### Current company decision surface — 15 Sep 2026
- **#86 Laifual — WAITING P0 ACTION monitor:** governed starter **5% research sleeve (~£2,000)** at executable <=HK$48 with thesis intact; 8% pre-proof ceiling. Brokerage execution remains manual.
- **#125 JEM — WAITING P1:** fresh/recurrent <=~¥6,100 condition or stronger HBM4/HBM4E / cash evidence.
- **#126 SUSS — WAITING P1:** ~€60–62 condition or stronger backlog/process/hybrid-bond evidence.
- **#127 Weebit — WAITING P1:** ~A$2.5–2.7 or recurring production royalty/adoption evidence.
- **#128 Micronics Japan — WAITING P1:** ~¥10,000–10,800 or stronger HBM4/HBM4E/customer/FCF evidence; high quality but correlated.
- **#106 BlackBerry/QNX — WAITING P0:** Q2 FY2027 due 24 Sep 2026 or earlier material non-auto economics.
- **#108 FORT — WAITING P1:** S-4/equivalent / transaction disclosure.
- **#129 Centrus — WAITING P1:** ~US$120–130 or specific funded-capacity / construction / customer / DOE evidence after the September financing reset.
- **#130 Jinpan — WAITING P1:** ~CNY54–57 or stronger global AIDC qualification/cash evidence.
- **#146 Modine / Modexus — WAITING P1:** ~US$155–165 or 1 Oct 2026 separation close / material post-spin evidence.
- **#85 Harmonic Drive — PARKED P2.**
- **#109 QNX vs FORT — BLOCKED P1** until both event-driven underwrites are fresh.

### Portfolio / recurring work
- **#131 — DONE P0:** initial construction baseline completed.
- **#132 — WAITING P1 after early 15 Sep re-rank:** next normal monthly review around 15 Oct 2026, or earlier on a material portfolio-wide trigger.
- **#133 — WAITING P2:** quarterly full-universe challenge.

### Early re-rank conclusion — 15 Sep 2026

**FACT:** the candidate set is broader than the original four-name #131 construction: current governed Gate-E underwrites now also exist for Jinpan, Modine, Micronics Japan and Centrus.

**CONCLUSION:** Laifual is now the first governed **`ACTION`** in the current Gate-E cycle: a **starter 5% research allocation signal only at an executable price <=HK$48**. No brokerage order has been placed, so the actual brokerage portfolio remains unchanged until manual execution. The other 95% of the research capital remains tactical cash plus conditional sleeves.

**INTERPRETATION:** marginal portfolio contribution now matters more than the old static Top-10 order. Independent-return-engine candidates — especially Laifual, Centrus, Modine and Jinpan — deserve capital/research priority when their conditions fire because the original portfolio already carries substantial memory/HBM correlation.

Current conditional allocation priority, assuming each company's documented trigger is freshly confirmed:
1. **Laifual — ACTION:** starter 5% research sleeve at executable <=HK$48. Do not chase above the governed price condition; re-underwrite before any add above 5%.
2. **Centrus** — independent strategic-fuel optionality after a major financing/enterprise-value reset; base case still does not clear 2x, so funded-capacity proof remains decisive.
3. **Modine / Modexus** — independent data-centre cooling engine with a dated 1 Oct structural catalyst; base case still below the 2x hurdle at the latest underwrite.
4. **JEM** — strongest current memory valuation/evidence balance; close to its governed price condition, but portfolio correlation caps its marginal priority.
5. **SUSS** — similarly close to its governed zone with strong backlog visibility, offset by process/customer concentration and memory-cycle correlation.
6. **Jinpan** — independent AI-power sensitivity and exceptional order growth, but weaker cash conversion/global qualification evidence.
7. **Weebit Nano** — highest venture-style memory optionality, still gated by recurring production royalties and dilution.
8. **BlackBerry/QNX** — attractive diversification quality but a 2x path still needs evidence; 24 Sep results are the next P0 information event.
9. **Micronics Japan** — strongest probe-card operating quality but current valuation/customer concentration and memory correlation reduce marginal portfolio value.
10. **FORT Robotics** — high Physical-AI purity and optionality, but final transaction/dilution/recurring economics remain unavailable until the filing.

**Best alternative use of capital today:** after the Laifual starter signal, **95% tactical cash** remains the best research allocation for undeployed capital. Any further candidate should displace cash only after its governed condition fires and a fresh check confirms better remaining-window asymmetry than the alternatives.


## Scheduler sufficiency

Whether one scheduler remains sufficient must be measured rather than assumed. Track:

- in-window P0/P1 alert detection-to-notification latency — target **<=2h**;
- P0/P1 trigger-to-substantive-action latency — target **<=24h**;
- substantive `READY` backlog depth — healthy range usually **0–3**; >5 is a warning;
- oldest P0/P1 READY age — target **<=48h**;
- 7-day Backlog Pressure Ratio (new executable work / completed executable work);
- substantive-work saturation — warning if >80%.

Keep one scheduler unless **any two** documented capacity/latency thresholds persist for **two weeks**. If scaling is required, split into:
1. **Alert / Trigger / Triage**;
2. **Research Worker**.

Do not create one scheduler per company/theme by default.

## Initial Gate-E work programme

### Phase 1 — re-underwrite the current Top 10 for 18 months
For every current Top-10 name add:
- portfolio role;
- explicit 18-month 2x path or reason it cannot clear the hurdle;
- realistic 3–5x stretch case only where supported;
- bear/permanent-loss case;
- catalyst sequence and expected timing;
- entry/add/trim/sell rules;
- initial size range and maximum size ceiling;
- current bottleneck direction;
- best alternative use of capital;
- explicit monitorable alert triggers where evidence supports them.

### Phase 2 — construct aggressive £40k portfolios
Tracked in #131. Build three versions:

1. **Aggressive baseline** — 4–7 concentrated asymmetric positions with strict catalyst/rotation discipline.
2. **Aggressive + tactical cash** — same hurdle but preserves more capital for specific price/evidence triggers.
3. **Maximum-asymmetry stress case** — tests what would need to happen to reach 3–5x; this is a scenario boundary, not the default recommended portfolio.

For each portfolio, model the combinations of winners, partial winners and losers required to reach **£80k, £120k and £200k by March 2028**.

### Phase 3 — live decision surface
Track:
- holdings and cash;
- cost basis;
- current value;
- remaining-window expected return from current price;
- position role and size ceiling;
- bottleneck score/direction;
- entry/add/trim/sell trigger status;
- next dated catalyst and time to resolution;
- best alternative use of capital;
- portfolio value versus £80k / £120k / £160k / £200k milestones.

## Current conclusion

**INTERPRETATION:** The move from four years to 18 months makes the mandate substantially more demanding. Ordinary compounding is unlikely to be sufficient; portfolio success will depend more heavily on asymmetric starting valuations, identifiable near-term catalysts, concentration in the best evidence-backed opportunities and active capital rotation.

**HYPOTHESIS:** A concentrated, catalyst-aware process that follows migrating bottlenecks and continually reallocates toward the best remaining 18-month asymmetry offers a better chance of reaching £80,000 than a static diversified basket.

**OPEN QUESTION:** Which 4–7 names — and what tactical cash level — provide the strongest evidence-backed path to at least £80,000 by March 2028 without requiring the 5x stretch assumptions?

## Governance

- #117 is the active Gate-E portfolio epic.
- #120 is the live automation/orchestration epic; `AUTOMATION.md` defines machine-readable queue state, alerts and scheduler-sufficiency rules.
- #121 and #122 are completed deployment work.
- #114 / `research/top10-capital-allocation.md` are **historical Gate-D baseline/context**, not current action rules.
- #110 remains the cross-theme hunting-universe epic.
- #131 is the initial portfolio-construction gate; #132/#133 provide recurring monthly/quarterly work without extra schedulers.
- `watchlist.md` remains a separate research-prioritisation surface.
- No company receives a watchlist promotion solely from portfolio-role assignment.
- New factual investment evidence must continue to follow `AGENTS.md` source and confidence rules.
- Actual brokerage orders remain manual; automation may produce research-level signals but must not execute trades.
