# Research Changelog

This file records substantive changes to research conclusions, confidence, prioritisation and governance. Minor wording or formatting edits do not need an entry.

## 2026-09-07

### Memory research reprioritised after three Gate A validations

- Updated the active research plan after HBM stacking, advanced packaging and test all passed Gate A.
- Shifted the programme from broad bottleneck discovery toward **Investment Capture underwriting** plus one strategically different system-level bottleneck test.
- Promoted **interfaces / MRDIMM / CXL (#13)** to the next system-level priority so Montage and the wider interface layer can be compared against the validated manufacturing-side bottlenecks.
- Narrowed **wafer processing (#12)** from a broad TSV/thinning deep dive to a targeted economic-capture gap analysis focused on DISCO/precision processing, ultra-thin dicing, temporary-carrier gaps and hybrid-bond implications.
- Prioritised first-wave company deep dives for **FormFactor (#21), Camtek (#22) and SUSS (#15)**, followed by Onto Innovation, Hanmi Semiconductor and ASMPT.
- Added an **interim synthesis gate**: after #13 and at least three company Investment Capture deep dives, rank candidates before opening many more research streams.
- No investment conclusion or company conviction level changed as a result of this reprioritisation.

### Test / known-good-die bottleneck validated

- Completed the HBM test / known-good-die / burn-in deep dive from issue #11.
- **Bottleneck Strength Score: 4.6/5** — Gate A passed. The structural driver is not simply more chips being tested; it is the rising economic cost of an escaped defect as HBM, compute dies, interposers and substrates are integrated into expensive heterogeneous packages.
- Identified four high-priority sub-layers: HBM wafer/probe-card test, dedicated HBM memory ATE, known-good-everything/module-level test, and thermal/system-level validation.
- **FormFactor** moves to `Investigating`: it ships HBM probe cards in volume to all three major HBM manufacturers, has record HBM-driven DRAM revenue, and faces increasingly demanding HBM probe density/speed/thermal requirements.
- **Advantest** and **Teradyne** enter `Watch` as large-cap benchmarks with strong direct evidence that AI/HBM complexity is increasing test content, revenue, capacity and margins.
- The strongest strategic conclusion is that advanced packaging pushes test both **left** (earlier die/module screening) and **right** (system-level reliability), increasing the number and value of test insertion points.
- No company is promoted to high conviction; Investment Capture still requires valuation and competitive-underwriting work.

### Advanced packaging bottleneck validated

- Completed the advanced packaging/interposer deep dive from issue #10.
- **Bottleneck Strength Score: 4.7/5** — Gate A passed. The constraint is broader than CoWoS capacity and includes large-area interposer/RDL yield, high-performance package substrates, inspection/metrology/process control, bonding/CMP/plating and final heterogeneous assembly.
- The strongest strategic conclusion is that the bottleneck is likely to **persist through architecture transitions**. Silicon interposers may migrate toward RDL, bridges, panel-level, organic/glass or hybrid-bond architectures, but larger package area and higher interconnect density continue to create process-control and substrate challenges.
- Inspection/metrology emerged as the highest-priority supplier hunting ground. **Camtek** and **Onto Innovation** move to `Investigating` based on direct 2026 HBM/CoWoS-like order and qualification evidence.
- **Ibiden** and **Amkor** enter the research queue as substrate/capacity benchmarks with strong demand evidence but higher capital intensity and less certain economic asymmetry.
- No company is promoted to high conviction; company-level Investment Capture Scores still require separate underwriting.

### HBM stacking / bonding / thermal bottleneck validated

- Completed the first HBM stacking/bonding/thermal/yield deep dive from issue #9.
- **Bottleneck Strength Score: 4.6/5** — Gate A passed. The constraint is driven by thinner dies, warpage, placement/bonding precision, interconnect quality, thermal resistance and compounding yield risk as stack height rises.
- Refined the bottleneck into four especially important sub-layers: (1) die bonding/stacking process control, (2) wafer thinning plus temporary bonding/debonding, (3) underfill/molding/warpage-control materials, and (4) surface preparation/alignment/metrology for future hybrid bonding.
- The strongest new strategic conclusion is that the bottleneck is likely to **migrate rather than disappear** as HBM moves from TCB/MR-MUF/TC-NCF toward hybrid copper bonding. Current TCB leadership therefore carries technology-transition risk.
- Added **SUSS** and **Hanmi Semiconductor** to `Investigating` on the watchlist. SUSS has disclosed HBM penetration in temporary bonding/debonding and a hybrid-bonding roadmap; Hanmi has direct HBM4 TC-bonder orders and strong current HBM revenue sensitivity.
- Added **ASMPT** to the research queue as a cross-architecture benchmark/candidate because it has production evidence with multiple HBM customers and capabilities spanning TCB, mass reflow and hybrid bonding.
- Opened follow-up company deep dives for SUSS (#15) and Hanmi Semiconductor (#16).
- No company is promoted to high conviction; company-level Investment Capture Scores still require separate underwriting.

### AI memory bottleneck research plan added

- Added a structured execution plan for validating the strongest bottlenecks in the AI-memory value chain.
- Separated **Bottleneck Strength** from **Investment Capture** so technical scarcity is not automatically treated as an attractive investment.
- Prioritised HBM stacking/bonding/thermal/yield first, followed by advanced packaging and test, then wafer processing/TSV and interfaces/MRDIMM/CXL.
- Added evidence standards, falsification requirements, completion gates and a parallel agent/collaborator workflow.
- No investment conclusion or watchlist status changed as a result of the planning update.

## 2026-09-06

### Repository governance established

- Established `unicorn` as the single repository for multiple research streams.
- Added mandatory agent operating rules and pull-request workflow.
- Pull requests are the audit and safety boundary; human approval is optional rather than required by default.
- Agents must wait for required automated checks to pass before merging or enabling auto-merge.
- Added cross-theme watchlist and source-provenance structure.
- Added initial research streams for AI memory and robotics actuators.
- Added automated pull-request governance checks.
- Aligned the GitHub Actions job name with the required `Research governance` status check so auto-merge can satisfy the ruleset without manual intervention.

### AI memory value-chain map added

- Added the first evidence-backed end-to-end AI memory value-chain map.
- Current strongest bottleneck candidates are HBM stacking/bonding/thermal/yield, advanced packaging/interposers, DRAM/HBM wafer capacity, and test.
- Wafer thinning/TSV processing, package materials, memory-interface chips and CXL are retained as high-priority areas to validate rather than established conclusions.
- Clarified that Weebit Nano is an emerging-memory architectural option, not a current mainstream AI-memory bottleneck.
- Recommended the next deep dives: HBM stacking/thermal, advanced packaging, test, and DDR5/MRDIMM/CXL interfaces.

### Current working research state

- **AI memory:** HBM stacking, advanced packaging and test have now passed Gate A. The research focus is shifting from validating bottlenecks to identifying which smaller suppliers capture enough of the economics to create asymmetric investment potential.
- **Robotics actuators:** research stream opened; value-chain and company analysis still to be built.
