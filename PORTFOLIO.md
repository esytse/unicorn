# Dynamic Portfolio Strategy — Gate E

**Status:** Active  
**Reference date:** 2026-09-09  
**Backlog:** #117  
**Upstream research:** #110 / #114  

> This is a research and portfolio-management framework, not automatic trading instructions.

## Objective

Manage a starting capital pool of **£40,000** over **four years**, targeting:

- **minimum objective: 2x → £80,000 by September 2030**;
- **intermediate milestones: 3x → £120,000; 4x → £160,000**;
- **stretch objective: 5x → £200,000**.

The mathematically implied annualized portfolio hurdles are approximately:

- **2x in four years: 18.9% CAGR**;
- **3x: 31.6% CAGR**;
- **4x: 41.4% CAGR**;
- **5x: 49.5% CAGR**.

The 5x outcome is a stretch objective, not a base-case forecast. The portfolio should not lower evidence standards or force risk merely to manufacture a 5x narrative.

## Core interpretation

The target applies to the **portfolio**, not to every security bought today.

This is explicitly a **dynamic portfolio**. Expect:

- buys and staged entries;
- additions when evidence and forward return improve;
- trims when valuation outruns evidence or concentration becomes excessive;
- exits when the thesis breaks, the return is harvested, or a better use of capital emerges;
- capital rotation between themes and bottlenecks;
- periods of cash when no opportunity clears the hurdle.

Cost basis is not the decision anchor after purchase. Every holding must continue to compete for capital based on **forward expected return from the current price**.

## Relationship to Gate D

`research/top10-capital-allocation.md` remains the dated Gate-D valuation layer. Its 10/12/15% normalized-return work remains useful for valuation discipline, downside comparison and identifying attractive entry prices.

However, a ~12% expected return does **not** by itself satisfy the new portfolio objective. Gate E adds a stronger test:

1. Can the proposed entry plausibly contribute to a **2x portfolio outcome within four years**?
2. Is there a defensible **3–5x upside path** for asymmetric positions without unsupported TAM assumptions?
3. What probability, evidence and catalyst sequence are required?
4. What is the permanent-capital-loss case?
5. Is this still the best available use of capital versus cash and alternative candidates?

## Position roles

Every active candidate or holding should be assigned one role:

- **Core** — higher-confidence business/economic capture with a credible four-year return path and tolerable downside.
- **Asymmetric growth** — stronger upside sensitivity with meaningful operating/valuation risk.
- **Speculative option** — small position where payoff can be large but commercialization, funding or architecture evidence remains incomplete.
- **Watch** — research is interesting but price/evidence does not currently justify capital.
- **Avoid** — current expected return, downside or thesis quality is inadequate.

Role and position size are separate from the cross-theme `watchlist.md` research status.

## Transaction rules

Every deployable position must define:

### Entry
- evidence threshold;
- valuation / price zone;
- intended initial size;
- expected four-year return at entry;
- catalyst timing.

### Add
Add only when at least one of the following improves without a compensating deterioration:
- evidence quality;
- operating capture;
- valuation / forward return;
- bottleneck strength;
- probability of the catalyst path.

Do not add solely because price fell below cost basis.

### Trim
Consider trimming when:
- price rises materially faster than normalized earnings / evidence;
- forward expected return falls below competing uses of capital;
- position concentration becomes disproportionate to evidence confidence;
- the catalyst is substantially priced in before realization;
- bottleneck strength begins to weaken or migrate.

### Sell
Sell or materially reduce when:
- a defined thesis breaker occurs;
- the structural bottleneck is being commoditized or bypassed;
- company capture deteriorates even if the broader theme remains correct;
- dilution/capital intensity destroys per-share economics;
- the four-year forward return becomes inadequate;
- a materially superior risk-adjusted opportunity emerges.

A successful original thesis is **not** a reason to keep holding if the forward bottleneck or forward return has migrated elsewhere.

## Bottleneck-migration framework

Assume that bottlenecks **move as technology and supply chains mature**.

For each theme, re-test the full value chain rather than extrapolating the original scarcity indefinitely.

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

The research universe must be allowed to change. The current Top 10 is a **live ranked hunting universe, not a permanent portfolio list**.

## Review cadence

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
Recalculate forward return. Do not anchor to the original purchase price or prior high.

### Quarterly
Re-rank:
1. current holdings;
2. Top-10 candidates;
3. important benchmark companies;
4. newly surfaced companies from migrating bottlenecks.

The quarterly question is: **where is the best four-year forward return now, given current evidence and current price?**

## Initial Gate-E work programme

### Phase 1 — re-underwrite the current Top 10 for four years
For every current Top-10 name add:
- portfolio role;
- explicit four-year 2x hurdle;
- realistic 3–5x stretch case where supported;
- bear/permanent-loss case;
- entry/add/trim/sell rules;
- initial size range and maximum size ceiling;
- catalyst calendar;
- current bottleneck direction;
- best alternative use of capital.

### Phase 2 — construct candidate £40k portfolios
Build at least three versions:

1. **Conservative asymmetric** — greater evidence quality and meaningful cash.
2. **Balanced** — mixture of higher-confidence compounders and asymmetric specialists.
3. **Aggressive** — greater concentration in high-upside names with stricter loss/rotation rules.

For each portfolio, model the combinations of winners, partial winners and losers required to reach £80k, £120k and £200k.

### Phase 3 — live decision surface
Track:
- holdings and cash;
- cost basis;
- current value;
- forward expected return from current price;
- position role and size ceiling;
- bottleneck score/direction;
- entry/add/trim/sell trigger status;
- next catalyst;
- best alternative use of capital;
- portfolio value versus £80k / £120k / £160k / £200k milestones.

## Current conclusion

**INTERPRETATION:** The research programme has enough structure to move from broad discovery into portfolio construction, but the current Top 10 should not be assumed to fill the £40k immediately. Gate D currently contains no full-size `Buy now` candidate at the dated reference prices.

**HYPOTHESIS:** A dynamic process that combines disciplined entry prices, asymmetric exposures, bottleneck migration and active capital rotation has a better chance of meeting the four-year objective than a static equal-weight Top-10 basket.

**OPEN QUESTION:** Which current Top-10 combination—and what initial cash level—provides the strongest credible path to at least £80,000 by September 2030 without requiring the stretch assumptions of the 5x case?

## Governance

- #117 is the active Gate-E backlog.
- Gate D (#114) remains the company-level valuation/evidence layer.
- #110 remains the cross-theme hunting-universe ranking.
- `watchlist.md` remains a separate research-prioritisation surface.
- No company receives a watchlist promotion solely from portfolio-role assignment.
- New factual investment evidence must continue to follow `AGENTS.md` source and confidence rules.
