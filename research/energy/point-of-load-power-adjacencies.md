# Point-of-load power adjacency scan — 25 September 2026

**Backlog:** #253  
**Origin:** #249 → #251 Vicor VPD discovery/underwrite  
**Question:** if VPD/point-of-load power becomes structurally scarce, which adjacent listed suppliers can capture a disproportionate economic inflection?

## Architecture map

The bottleneck is moving **inside the package** as AI accelerators exceed traditional lateral-power limits:

**rack/bus power → VRM/point-of-load conversion → high-current magnetics → package-level power integrity → vertical/integrated delivery → accelerator silicon**

This scan deliberately searched the component layers rather than starting from company names.

## 1. High-current magnetics — TAI-TECH Advanced Electronics (TPEX:3357)

### Primary evidence

TAI-TECH explicitly markets proprietary TLVR coupled inductors for AI GPU/ASIC power delivery, including >400A applications, and says AI GPU currents have surpassed 1,000A. Its product architecture targets fast transient response, low DCR and high saturation current—the exact characteristics stressed as power moves closer to increasingly dense accelerators.

The company's own monthly revenue series shows a clear 2026 acceleration:
- May: NT$709m, **+37.8% y/y**
- Jun: NT$765m, **+57.4%**
- Jul: NT$876m, **+63.3%**
- Aug: NT$815m, **+53.1%**
- Jan–Aug total: NT$5.605bn, **+32.2% y/y**

### Financial scale

Secondary current financial data places TAI-TECH at roughly NT$23.4bn market capitalization around 11 Sep, with LTM revenue ~NT$7.37bn. 2025 revenue was NT$6.62bn and net income ~NT$1.06bn.

### Interpretation

**INTERPRETATION:** This is a materially better original-Unicorn shape than Vicor: the same architectural migration points toward a much smaller listed company, while reported revenue is already accelerating sharply.

The missing link is attribution. Current primary disclosures prove AI-server/TLVR capability and company-wide acceleration separately, but do **not yet prove how much of the acceleration is AI/TLVR, which accelerator platforms qualify it, or whether capacity/pricing is constrained.**

### State

**PROMOTE TO BOUNDED COMPANY UNDERWRITE.**

Required next evidence:
- AI/server/TLVR revenue mix and customer/platform qualifications;
- order/backlog/capacity and gross-margin evidence;
- share count/current valuation and 3x feasibility;
- competitor/substitution risk as vertical power reduces some conventional VRM content.

## 2. Package power integrity — AP Memory (TWSE:6531)

### Primary evidence

AP Memory's S-SiCap portfolio is explicitly aimed at AI/HPC power integrity:
- discrete S-SiCap Gen4 increased capacitance density >50% versus the prior generation;
- Gen4 is designed for embedded-substrate packaging and was in sampling/process validation, with progressive mass production from 2026;
- its S-SiCap Interposer completed customer packaging/reliability validation and entered four-reticle mass production at end-Q3 2025;
- the technology integrates silicon capacitors close to HBM/high-speed I/O and advanced packaging.

### External state-change corroboration

Samsung Electro-Mechanics disclosed a **KRW1.5tn** two-year silicon-capacitor supply contract for 2027–28 with a global large-scale customer, calling it its first large-scale supply achievement in the business. This is powerful evidence that silicon capacitors are crossing from technical option into economically material AI-package content.

### Interpretation

**INTERPRETATION:** Silicon capacitors are a genuine adjacent scarce-complement candidate because qualification is difficult, supply is limited and power integrity is moving into the package. AP Memory is much smaller/purer than Samsung Electro-Mechanics and has already passed customer reliability validation on one architecture.

**OPEN QUESTION:** AP Memory has not yet disclosed enough Si-Cap revenue/order economics in the evidence reviewed here to establish company transformation.

### State

**PROMOTE TO BOUNDED EVIDENCE/COMPANY PASS.**

Required next evidence:
- S-SiCap revenue/order contribution and customer qualification;
- manufacturing partner/capacity constraints;
- margin/royalty economics;
- current equity value and dilution;
- whether Samsung/other integrated competitors commoditize the opportunity.

## 3. Private-company validation — do not add to equity universe

Powerlattice, EnaChip and Lotus Microsystems independently validate the same architecture direction: move voltage regulation/magnetics closer to or inside the processor package. They are useful technical comparators but are not listed-equity candidates for the current universe.

Their presence is also a counter-case: the technology layer is attracting new entrants, so scarcity must be demonstrated at qualification/IP/manufacturing rather than assumed.

## Discovery result

This second iteration improves on the Vicor finding:

- **Vicor:** strong bottleneck validation, but ~US$13bn starting equity value already prices substantial success.
- **TAI-TECH:** smaller listed company + directly relevant high-current/TLVR products + sharp company-wide revenue acceleration. **Highest-information next underwrite.**
- **AP Memory:** small listed package-power-integrity exposure with validated/mass-production Si-Cap technology; economic materiality still missing.
- **Samsung Electro-Mechanics:** decisive industry demand validation, but much more diversified and therefore primarily a comparator for this thesis.

## Negative / falsification record

- Do not infer that all conventional inductors benefit indefinitely: deeper vertical integration may reduce some board-level VRM/passive content.
- Do not infer AP Memory wins because silicon capacitors win; Samsung's KRW1.5tn contract proves the market while also proving formidable competition.
- Private VPD/integrated-magnetics startups show architectural competition is broadening.
- The key discovery question is now **who owns a qualified, hard-to-substitute component whose content or economics rise as power delivery moves inside the package?**

## Next action

Deep-underwrite **TAI-TECH first**, then AP Memory if TAI-TECH confirms the architecture-to-financial bridge. This sequence is thesis-driven, not universe-driven.
