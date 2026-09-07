# Research Changelog

This file records substantive changes to research conclusions, confidence, prioritisation and governance. Minor wording or formatting edits do not need an entry.

## 2026-09-07

### Integrated thermal chain validated as AI usable-compute bottleneck

- Completed **#49** and added `research/energy/deep-dives/cooling-heat-rejection.md`.
- **Integrated thermal chain / qualified cooling capacity passes Gate A at 4.4/5 with Medium-High confidence.** Cooling is part of the capacity path: essentially every compute MW becomes heat that must be captured, transported and rejected before electrical capacity becomes usable AI compute.
- **Direct-to-chip liquid cooling and facility heat rejection each pass at 4.2/5 as technical functions**, but generic cold-plate / CDU / manifold supplier scarcity is only about **3.8/5** because OCP standardisation, multi-sourcing and rapid capacity additions weaken component-level lock-in.
- **The strongest revealed-preference evidence is Modine's >$4bn 2027–2029 cooling-capacity agreement and $165m upfront customer payment** to fund supply expansion. Subsequent Data Centers revenue grew 90% y/y while expansion / supply-chain costs pressured margins, showing both real scarcity and real execution risk.
- Eaton's ~$9.5bn Boyd Thermal acquisition and Schneider / Vertiv thermal-platform expansion support the strategic value of owning the chip-to-ambient thermal chain, but demanding M&A valuations are evidence against assuming easy investment asymmetry.
- **Heat rejection is architecture-resilient; chillers are not.** Warm-water DTC can shift facilities toward dry / hybrid cooling and reduce conventional chiller or water dependence, so later underwriting should favour suppliers that span thermal functions across architectures.
- Broad non-nuclear bottleneck discovery is now complete. The programme proceeds to **nuclear supply-chain decomposition #50**, then the canonical **E2E bottleneck-migration refresh #51**, common-basis ranking #52, supplier Investment Capture #53 and capital allocation #54.

### Behind-the-meter integration validated as moderate speed-to-power bottleneck

- Completed **#47** and added `research/energy/deep-dives/behind-the-meter-microgrids.md`.
- **Integrated BTM power / microgrid architecture passes Gate A narrowly at 4.1/5, Medium confidence.** The durable function is site-specific power architecture, controls, protection, orchestration and execution that can bring an AI campus online before or beyond a conventional grid connection — not generic onsite generation.
- **Strategic revealed preference is now strong.** Vertiv agreed to acquire UtilityInnovation Group for about **$1.45bn upfront plus up to $1.15bn contingent consideration**, explicitly to add microgrid controls, BTM architecture, generation/storage orchestration and microgrid switchgear to its grid-to-rack portfolio.
- Commercial alternatives are real: Siemens Energy + Eaton offer a standardized 500 MW onsite architecture; Mitsubishi Power's Cheyenne Power Hub targets ~1.15 GW of dedicated data-centre power; Bloom/Brookfield expanded an AI-power financing framework to **$25bn**.
- **Falsification materially narrows the thesis.** IEA analysis says reliable onsite gas for variable critical loads can require **30–70% overbuild**, turbine supply remains constrained and only a minority of announced onsite-gas projects have entered physical construction. BTM therefore often **moves** scarcity into turbine slots, gas pipelines, permitting, land, redundancy, electrical equipment and controls rather than eliminating it.
- **Generic BESS / battery hardware scores 3.4/5 and does not pass Gate A; gensets remain 3.6/5; fuel cells are a credible commercial alternative but not a validated scarce broad function.** Large gas turbines retain their prior 4.6/5 Gate-A result inside many BTM architectures.
- No BTM supplier is promoted before common-basis Investment Capture. The only remaining broad bottleneck validation is **cooling / heat rejection**, after which the energy programme should synthesize the frontier and move to supplier underwriting.

### Data-centre electrical backbone validated; 800 VDC supplier scarcity not yet proven

- Completed **#45** and added `research/energy/deep-dives/electrical-backbone-800vdc.md`.
- **The integrated data-centre electrical backbone passes Gate A at 4.3/5 with Medium-High confidence.** Eaton, Schneider Electric and Vertiv show strong 2026 order / backlog growth alongside attractive or expanding electrical / critical-infrastructure margins, while ABB confirms investment across MV distribution, UPS and next-generation source-to-rack architecture.
- **800 VDC is now a validated architecture transition but not a validated broad supplier bottleneck.** Google, Microsoft and NVIDIA are standardising 800 VDC through OCP; the technical need is strong as rack power moves toward MW scale, but more than 80 ecosystem participants and explicit interoperability goals reduce broad supplier scarcity to roughly **3.6/5** today.
- The likely future 800 VDC profit pools are narrower: **MW-scale MVAC-to-DC conversion / transformer-rectifier or SST power blocks, DC fault protection / solid-state breakers, high-power DC busway / connectors, high-density DC/DC conversion and DC-native storage / UPS integration**. None is promoted without direct qualification / pricing evidence.
- The architecture is likely to **redistribute rather than eliminate** electrical value. MV equipment, protection, transformation / conversion, busway and integrated power-system engineering remain relatively architecture-resilient; some legacy AC PDU / rack-PSU / repeated-conversion layers face bypass risk.
- No Eaton, Schneider, Vertiv, ABB or other supplier is promoted before common-basis Investment Capture and valuation work. The next validation priority is **behind-the-meter / microgrid + storage**, then **cooling / heat rejection**, followed by an interim energy synthesis.

### Large gas-turbine equipment bottleneck validated

- Completed **#41** and added `research/energy/deep-dives/dispatchable-generation.md`.
- **Large gas-turbine equipment / manufacturing slots pass Gate A at 4.6/5 with High confidence on current scarcity.** GE Vernova reported 116 GW of gas-power backlog / slot reservations at Q2 2026 versus roughly 20 GW of 2026 annual output; Siemens Energy is sold out through FY2028 with FY2029 filling rapidly and identifies blades / vanes as a principal production bottleneck.
- **Economic-capture evidence is unusually direct.** Multi-year reservations, favorable new-unit pricing, concentrated advanced-class OEM supply, gradual capacity expansion and long-lived aftermarket / service economics make this the strongest concentrated merchant profit-pool candidate in the energy work so far.
- Mitsubishi Power provides a third credible advanced-class supplier and direct dedicated data-centre deployment evidence, preventing a duopoly conclusion while preserving high supplier concentration.
- **Reciprocating gensets / distributed generation score 3.6/5 and do not pass Gate A.** Data-centre demand is strong, but modularity, broader supplier choice and substitution make supply more elastic.
- AI is treated as an **important marginal accelerator rather than the sole cause** of the turbine cycle; grid reliability, replacement generation, industrial growth and regional power demand also matter.
- No turbine OEM is promoted to `Watch` before common-basis Investment Capture and valuation work. The next validation priority moves closer to the data centre: **electrical backbone / grid-to-rack architecture**, followed by 800 VDC, behind-the-meter integration and cooling.

### Physical transmission deliverability validated; queue friction separated

- Completed **#38** and added `research/energy/deep-dives/transmission-large-load.md`.
- **Physical transmission deliverability passes Gate A at 4.7/5 with High confidence.** DOE's 2026 National Transmission Needs Study identifies pressing transmission needs driven partly by data centres and other large loads, while major regions are approving some of their largest transmission portfolios.
- **Large-load interconnection-process friction is deliberately separated from physical scarcity.** FERC's June 2026 reforms, flexible / non-firm service, co-location and electrically proximate generation can reduce study delays and network upgrades; SPP and ERCOT are already redesigning large-load processes.
- **Ghost demand materially weakens raw queue forecasts.** U.S. large-load requests reportedly exceed 700 GW, and stronger deposits / project-maturity requirements are removing speculative requests. Queue MW is therefore not treated as a credible demand forecast by itself.
- Advanced reconductoring, dynamic line rating and power-flow control can unlock existing corridors faster than greenfield lines. This is evidence against a simplistic "more transmission lines" thesis but supports a broader **speed-to-power** profit pool in physical network upgrades.
- The likely investable layers are **EPC / engineering, grid equipment, advanced conductors / GETs, substations and onsite alternatives**, not the interconnection queue itself. Quanta's Q2 2026 backlog of ~$53.4bn is an early signal of construction / execution demand, but no company is promoted before common-basis Investment Capture.
- The next validation priority becomes **dispatchable generation equipment**, followed by data-centre electrical backbone / 800 VDC / behind-the-meter power.

### Transformer and MV/HV switchgear bottlenecks validated

- Completed **#36** and added `research/energy/deep-dives/transformers-grid-equipment.md`.
- **Transformers pass Gate A at 4.7/5 with High confidence.** DOE still reports roughly 1–2+ year distribution-transformer and 3–4 year large-transformer lead times; custom engineering, factory/test capacity, utility qualification, heavy transport, GOES/component dependence and regional manufacturing make qualified capacity slow to expand.
- **MV/HV switchgear passes Gate A at 4.4/5 with Medium-High confidence.** The function is architecture-resilient and 2026 order/backlog evidence is strong, but the global qualified supplier base is broader and capacity can expand somewhat faster than for large transformers.
- **The strongest revealed-preference evidence is speed-to-power:** Hitachi Energy air-freighted >80-tonne large transformers from Europe to a U.S. hyperscale data-centre project, showing that schedule value can dominate logistics cost.
- Supplier economics are already visible: GE Vernova's data-centre Electrification orders exceeded $5bn YTD by Q2 2026; Eaton's Electrical order/backlog growth remained very strong; leading suppliers are expanding capacity while maintaining attractive electrical margins.
- **Falsification is material but does not overturn the thesis.** Hitachi Energy's >$9bn global investment program, GE Vernova / Prolec expansion, Eaton capacity additions and DOE standardisation should reduce scarcity gradually through 2027–2030. The conclusion is **structural scarcity through the late 2020s, not permanent shortage**.
- No energy supplier is promoted to `Watch`. The next validation priority is **large-load interconnection / transmission**, followed by dispatchable generation equipment, before company-level Investment Capture begins.

### AI energy / power-delivery value chain opened

- Opened **#34** and created `research/energy/` with an initial thesis, end-to-end value-chain map and validation plan.
- **Working thesis:** the critical AI-energy constraint is more likely to be **speed-to-power / deliverable connected megawatts** than aggregate electricity volume. Large-load interconnection / transmission deliverability and transformers / substation equipment each score **~4.8/5 preliminarily**, with bulk transmission **4.7**, MV/HV switchgear **4.5**, large gas-turbine slots **4.4** and the data-centre electrical backbone **4.4**.
- Evidence includes IEA's updated projection of data-centre electricity demand roughly doubling from ~485 TWh in 2025 to ~950 TWh in 2030; FERC's June 2026 large-load integration reforms; US DOE transformer lead times of roughly 1–2 years for distribution units and 3–4 years for large transformers; and strong 2026 backlog/order evidence across GE Vernova, Eaton, Schneider and ABB.
- Added the **AC → hybrid → 800 VDC** architecture transition as a rising technical bottleneck, but supplier concentration is not yet proven because NVIDIA's open ecosystem already includes 80+ participants.
- Cooling / heat rejection is treated as a **coupled capacity constraint** rather than a simple downstream auxiliary system.
- No energy company is promoted to `Watch` or high conviction. The next work is to validate the highest-scoring functions before company-level Investment Capture and valuation analysis.

### Weebit Nano moves to Watch as commercial adoption becomes real

- Completed **#5** and added `research/memory/companies/weebit-nano.md`.
- **Weebit moves `Research queue` → `Watch`; confidence Low → Medium.** The commercial bridge is materially more advanced than the original thesis assumed: SkyWater and DB HiTek have qualified ReRAM processes, onsemi and Texas Instruments have licensed the technology, three product customers had taped out designs by June 2026, and at least one returned chip was functional and running software.
- FY26 revenue reached **A$15.3m** versus A$4.4m in FY25, but revenue is still licensing/NRE rather than recurring royalties. First customer mass production is hoped for in CY27, so the decisive economics remain unproven.
- **Valuation remains the binding investment risk.** At the 4 September reference WBT was ~A$3.53, market cap ~A$849m and EV ~A$681m, about **45x FY26 revenue**. FY26 also recorded a ~A$54.9m net loss, operating cash burn, material stock-based compensation and roughly A$102m of equity funding.
- A reverse commercialization screen indicates the business likely needs roughly **5–7x FY26 revenue by end-2030 plus a material shift to royalty economics** to support an attractive return under illustrative normalized revenue multiples.
- AI / compute-in-memory remains **upside optionality**, not the current commercial base case. The base thesis is embedded non-volatile-memory replacement in analog, power, automotive, industrial/security and embedded applications.
- Weebit does **not** enter the current HBM Bottleneck × Investment Capture or Gate-C ranking. The next substantive discovery stream is **robotics actuators (#3)**.

### Probe-card capital allocation normalized; JEM remains an investigation

- Opened **#31** and added `research/memory/probe-card-capital-allocation.md` to test JEM, Micronics Japan, FormFactor and Technoprobe on a common normalized-return basis.
- **JEM is the strongest new valuation lead but does not pass Gate C.** At the 4 September ¥6,230 reference, the initial EPS-normalized screen gives roughly **9.4% base CAGR**, **-9.8% bear CAGR** and a **~¥5,640** 12% base-return monitoring zone. The 7 September close of ¥6,650 widened the gap to that zone.
- **The HBM link strengthened but remains incomplete.** A JEM company-controlled page says DRAM share is increasing around HBM; FY2026 major-customer disclosures show Micron Memory Japan + Taiwan were roughly **31% of sales**. Exact HBM production sockets, HBM revenue and share are still not disclosed.
- **Falsification materially weakens the simple low-P/E thesis.** The top three customers were ~44.7% of FY2026 sales; TTM FCF through June was only ~¥2.24bn; FY2026 financing included ~¥12.15bn of new equity issuance; shares outstanding increased materially; and competitor evidence on JEM's DRAM position is mixed.
- JEM remains **`Investigating`** and does **not** outrank the fully underwritten Onto / SUSS capital watch. The provisional research order is **Onto → SUSS → JEM → Micronics / Technoprobe → Camtek → FormFactor**.
- The active backlog is reprioritized to **#31 JEM/probe-card evidence gap → #5 Weebit Nano → #3 robotics actuators**. No company is promoted to `High-conviction research candidate`.

### Probe-card peer screen surfaces JEM as a valuation lead

- Added `research/memory/deep-dives/probe-card-peer-value.md` to compare **Japan Electronic Materials (JEM), Micronics Japan (MJC), FormFactor and Technoprobe** on HBM-test exposure, operating evidence and valuation asymmetry.
- **Japan Electronic Materials enters `Investigating`.** FY2027 guidance was raised to ¥36.4bn revenue / ¥9.45bn operating profit as memory-probe-card demand and factory utilisation strengthened. At roughly a ¥97bn 7 September equity value, JEM is the highest-priority new valuation lead, but HBM-specific customers/share and normalized-cycle economics remain unverified.
- **Micronics Japan enters `Investigating`.** MJC says HBM drove strong DRAM probe-card demand and describes itself as the leading memory probe-card supplier; FV26 targets ¥80bn revenue / ¥20bn operating profit / 25% margin. It becomes the primary quality/value comparator for JEM and FormFactor.
- **Technoprobe enters `Watch` as the operating benchmark.** H1 2026 revenue rose 42.4% and EBITDA 93.8%, with 44.4% EBITDA margin; raised 2026 guidance implies €1.05–1.10bn revenue and 46–48% EBITDA margin. The research will normalize these exceptional margins rather than capitalize them indefinitely.
- **FormFactor remains `Watch`, but its valuation case weakens on relative comparison.** Direct HBM evidence remains excellent, yet JEM/MJC now provide listed memory-probe alternatives that may offer better valuation asymmetry.
- No company is promoted to `High-conviction research candidate`. The next probe-card work is a common-basis valuation / normalized-cycle comparison, with JEM first and MJC second.

### Capital allocation scenarios completed; no Gate C candidate at current prices

- Completed **#27** and added `research/memory/capital-allocation.md` with explicit bear/base/bull scenarios, normalized terminal multiples, return hurdles and monitoring thresholds.
- **No company is promoted to `High-conviction research candidate`.** At the 4 September 2026 reference prices, none of the primary candidates provides enough base-case return plus downside protection to pass Gate C.
- **Onto Innovation becomes the preferred capital-allocation watch.** The base scenario produces roughly **10.4% annualized return** to end-2030; a ~12% base-return hurdle is reached around **$252** under the current earnings assumptions. Onto is closest to Gate C because its HBM/AP evidence, margins and valuation are better balanced than the other high-quality US names.
- **SUSS ranks second as the higher-risk asymmetric watch.** Base scenario return is roughly **8.8%**; the ~12% base-return zone is about **€64**. Upside is larger if backlog and HBM qualification convert, but the bear case is materially worse because of customer/process concentration and margin volatility.
- **Camtek and FormFactor remain strong businesses but fail the current margin-of-safety test.** Base scenarios are roughly **3.8%** and **1.5%** annualized. At normalized terminal multiples, a 12% return requires roughly **28% Camtek** and **30% FormFactor** 2027–2030 EPS CAGR; corresponding monitoring zones are approximately **$106** and **$68** unless normalized earnings estimates rise materially.
- **ASMPT was screened as an optional comparator but does not improve the current allocation frontier** because its premium multiple combines with diluted HBM earnings sensitivity across the broader Group.
- The active research plan moves from broad AI-memory supplier discovery into **valuation monitoring / selective optionality**. The next selective AI-memory backlog item is **Weebit Nano (#5)**, followed separately by the **robotics-actuator value-chain stream (#3)**.
- Watchlist statuses remain `Watch`; the change is ranking, valuation discipline and research priority rather than a thesis rejection.

### Second Investment Capture wave completed; research moves to capital allocation

- Completed company-level underwriting for **Montage Technology (#25), Onto Innovation (#23), Hanmi Semiconductor (#16) and ASMPT (#18)** and closed the targeted wafer-processing gap analysis (#12).
- **Onto Innovation: Investment Capture 4.0/5 → `Watch`.** A leading HBM manufacturer selected Dragonfly G5 for HBM4 after competitive evaluation; a >$240m HBM volume agreement, >$1bn backlog and strong margins move Onto into the top research tier alongside FormFactor and Camtek.
- **Montage Technology: Investment Capture 3.8/5 → `Watch`.** The interface franchise is exceptionally strong — ~36.8% reported global share and ~65% interconnect gross margin — but HK$268bn point-in-time market cap and ~52x forward P/E materially weaken the original asymmetric-upside framing.
- **ASMPT: Investment Capture 3.7/5 → `Watch`.** Multi-customer HBM4 orders and capabilities spanning TCB, AOR fluxless processing and hybrid bonding improve architecture-transition durability, but HBM earnings are diluted by the broader Group.
- **Hanmi Semiconductor: Investment Capture 3.6/5 → `Watch`.** Current HBM capture is extraordinary, including a 51.9% Q2 operating margin and material SK hynix orders, but customer/TCB concentration, hybrid-bonding uncertainty and extreme valuation substantially reduce durability.
- **Wafer processing (#12): completed without opening a DISCO company deep dive.** Precision thinning/grinding/singulation are validated sub-steps across HBM/2.5D packaging, but DISCO's HBM-specific revenue/share is not disclosed and its large market value reduces asymmetry. DISCO enters `Watch` as a process benchmark.
- Refreshed `synthesis-ranking.md`. The current research-priority top tier is **Onto Innovation, FormFactor and Camtek**, with **SUSS** as the smaller-cap asymmetric wildcard.
- Opened **#27 — Capital allocation: value top AI-memory candidates with scenarios and margin of safety**. The programme now moves from technical/company screening to explicit bear/base/bull expected-return analysis.
- No company is promoted to `High-conviction research candidate`; Gate C now requires explicit valuation, normalized-cycle scenarios and margin-of-safety evidence.

### First Investment Capture wave completed and interim ranking created

- Completed company-level underwriting for **FormFactor (#21), Camtek (#22) and SUSS (#15)** after their underlying bottlenecks had passed Gate A.
- **FormFactor: Investment Capture 4.0/5 → `Watch`.** Strongest current evidence of direct HBM economic capture: volume shipments to all three HBM manufacturers, share gains, >50% first-half HBM probe-card growth and substantial operating leverage. The main constraint is the post-rerating valuation rather than technical evidence.
- **Camtek: Investment Capture 3.9/5 → `Watch`.** Direct HBM/CoWoS-like inspection orders, >$600m 2026 YTD orders and rising AP mix support durable process-control exposure; premium valuation and strong competitors remain the main limits.
- **SUSS: Investment Capture 3.7/5 → `Watch`.** Temporary bonding/debonding has real HBM qualification and high small-cap sensitivity, but management also reports competition at a Korean HBM customer and SUSS remains a follower in hybrid bonding.
- Added `research/memory/synthesis-ranking.md` as the canonical interim cross-bottleneck/company comparison. Current completed-company order is **FormFactor > Camtek > SUSS**, with no High-conviction research candidate yet.
- The synthesis explicitly preserves the strongest contradictory evidence and separates bottleneck quality from valuation/architecture risk.

### Memory-interface bottleneck validated; CXL remains optionality

- Completed the interfaces / MRDIMM / CXL deep dive from issue #13.
- **DDR5/MRDIMM interface silicon: Bottleneck Strength 4.4/5 — Gate A passed.** Server-memory electrical limits make qualified RCD/MRCD/MDB silicon structurally important, and the merchant supplier base is concentrated.
- **CXL memory-expander controllers: 3.2/5 — Gate A not yet passed.** CXL addresses a real memory-capacity/tiering problem, but the controller market is broader and CXL-attached memory remains optional for most systems today.
- Montage Technology's technical exposure is materially stronger than the prior low-confidence thesis suggested, but its market value and valuation are already substantial. Opened **#25** for company-level Investment Capture underwriting rather than promoting the stock on bottleneck evidence alone.
- The value-chain map, watchlist and active research plan are updated to treat memory interfaces as the fourth validated bottleneck while keeping CXL as emerging optionality.

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
- No investment conclusion or company conviction level changed as a result of this reprioritisation.

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

- **AI memory:** four workstreams pass Gate A: advanced packaging (4.7), HBM stacking (4.6), test (4.6) and DDR5/MRDIMM interface silicon (4.4). Two company-underwriting waves, capital allocation, probe-card peer normalization and the Weebit architectural-optionality deep dive are complete; no company passes Gate C, so the programme is now primarily a monitoring system.
- **Robotics actuators:** next substantive research stream; value-chain and company analysis still to be built.
