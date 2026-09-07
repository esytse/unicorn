# Weebit Nano

**Research stream:** AI memory — emerging NVM / architectural optionality  
**Ticker:** ASX: WBT  
**Status:** Watch  
**Confidence:** Medium  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #5

## Snapshot

**CONCLUSION:** Weebit Nano has crossed an important threshold: it is no longer just promising ReRAM technology. It now has credible foundry/IDM licensing, qualified production processes, Tier-1 customers, revenue-generating product agreements and multiple customer tape-outs.

It has **not** crossed the more important investment threshold: **commercial royalties from customer mass production are not yet proven**. FY26 revenue is licensing and non-recurring engineering (NRE), the company remains heavily loss-making, and the current equity value already discounts a large future royalty business.

**Current view:** move from `Research queue` to **`Watch`**, but do **not** treat Weebit as a current AI-memory bottleneck or a Gate-C capital candidate. The base thesis is embedded non-volatile-memory replacement; AI / in-memory compute is additional optionality.

---

## 1. What the company actually sells

**FACT:** Weebit is a semiconductor-IP company rather than a chip manufacturer. It licenses embedded resistive RAM (ReRAM / RRAM) memory IP to foundries, integrated device manufacturers (IDMs) and product companies.

The commercial model has three economic stages:

1. licensing fees;
2. NRE / technology-transfer / qualification payments;
3. royalties once customers reach volume production.

**FACT:** FY26 revenue was **A$15.276m**, up from A$4.409m in FY25, and was driven by **IP licensing and NRE payments**. The company expects the revenue mix and profitability to change materially once commercial products reach mass production and generate royalties.

**INTERPRETATION:** The royalty stage is the core of the asymmetric-upside thesis because incremental royalty revenue should carry much higher margins than the current development-heavy business. It is also the stage that has **not yet been demonstrated**.

---

## 2. Commercial adoption — much stronger than the original thesis implied

### Foundry / IDM path

**SkyWater — production-ready platform**

**FACT:** SkyWater licensed Weebit ReRAM in 2021. The 130nm S130 module was fully qualified in 2023 and is marketed as available for customer integration and production. The product page states the module is qualified to JEDEC and AEC-Q100 requirements.

**Important caveat:** the reviewed public evidence does not show material royalty revenue from SkyWater customer mass production despite the platform having been production-ready for several years.

### DB HiTek — qualified foundry platform

**FACT:** DB HiTek licensed Weebit ReRAM in 2023. Weebit completed JEDEC-based qualification at DB HiTek in late 2025 / early 2026 on a 130nm BCD process, making the technology available to DB HiTek customers.

**FACT:** Product customer Overlord Labs taped out a smart-battery-management chip using Weebit ReRAM at DB HiTek during 2026.

### onsemi — Tier-1 IDM

**FACT:** onsemi licensed Weebit ReRAM in January 2025 for integration into its Treo BCD platform. By FY26, test chips manufactured in onsemi's production fab were functional and performing as expected.

**FACT:** The technology-transfer / qualification program remains in progress; company materials reviewed in 2026 expected qualification around the end of CY26.

### Texas Instruments — largest customer to date

**FACT:** Texas Instruments licensed Weebit ReRAM in December 2025. The agreement covers IP licensing, technology transfer, design and qualification in TI advanced process nodes. Weebit describes TI as its largest customer to date.

**INTERPRETATION:** TI and onsemi materially improve the evidence quality. These are not lab partners or speculative MOUs: they are major semiconductor IDMs paying Weebit to integrate the technology into production process flows.

---

## 3. Product-customer evidence

**FACT:** By June 2026, **three product customers had taped out chip designs** incorporating Weebit ReRAM and intended for eventual mass production. One design had already returned from the fab and was functional, including running software.

**FACT:** Disclosed applications include smart battery management and cybersecurity. The company says product qualification after tape-out can take **12–18 months**.

**FACT:** The FY26 annual report says the company hopes its **first customer reaches mass production within CY27**.

**INTERPRETATION:** Product tape-out is a genuine commercial milestone because it means customers have committed engineering resources and silicon to Weebit's IP. It is still several steps short of a recurring royalty stream: manufacturing, testing, qualification, customer product launch and sustained production must all follow.

---

## 4. Technology differentiation

### Why ReRAM matters

**FACT:** Embedded flash becomes increasingly difficult and costly to integrate at smaller process nodes. Weebit's ReRAM is a back-end-of-line memory technology using common fab materials, reducing the process changes required to add non-volatile memory.

**FACT:** Weebit has demonstrated ReRAM arrays at **28nm** and functional development silicon at **22nm FD-SOI**. Its currently commercial, fully qualified public foundry offerings are at **130nm** through SkyWater and DB HiTek; TI's advanced-node integration is still in technology transfer / qualification.

### Claimed manufacturing advantages

Company materials cite:

- a **2-mask adder** versus roughly 10 for embedded flash;
- materially faster programming;
- lower write energy;
- high-temperature operation including automotive-grade conditions;
- standard CMOS-compatible / fab-friendly materials;
- no rare-earth-material requirement.

These are **company claims supported by its development and qualification work**, not proof that Weebit wins every design versus other NVM technologies.

### AI optionality

**FACT:** Weebit was selected for a Korean government-funded analog compute-in-memory program with DB HiTek in 2026. It is also investing in near-memory / in-memory-compute development and established a Systems and AI team.

**FACT:** Earlier 2026 materials listed a **first AI customer engagement** as a target. The reviewed FY26 annual report and July/August updates do not identify a named commercial AI customer as having achieved that milestone.

**CONCLUSION:** AI is **not the base case today**. The current commercial opportunity is replacement / augmentation of embedded flash in analog, power-management, automotive, industrial, secure and embedded-processing applications. AI compute-in-memory could create a much larger second option if it becomes commercially validated.

---

## 5. IP and moat

**FACT:** Weebit has filed **more than 80 patents and patent applications** and also protects some technology as proprietary know-how when infringement would be difficult to detect.

**FACT:** The company has worked with CEA-Leti since 2016. Historical technical materials state Weebit has commercial rights to the ReRAM-related IP developed through the collaboration.

**FACT:** Patents cover device physics, process techniques, programming algorithms, reliability and circuit/design methods.

**INTERPRETATION:** The moat is broader than one material stack. Qualification know-how, process-transfer recipes, module design, algorithms and customer-specific integration can compound switching costs once a foundry/IDM has qualified the technology.

**Evidence against:** semiconductor memory IP is intensely competitive. A patent portfolio does not prevent large foundries or memory specialists from deploying their own ReRAM or alternative NVMs.

---

## 6. Competition and substitutes

Weebit is competing against several categories, not one direct peer.

### Captive / foundry ReRAM

**FACT:** Weebit's FY26 annual report notes that foundries including **TSMC and UMC have qualified their own ReRAM**. Their solutions validate the market but can also eliminate the need for third-party IP inside those foundries.

**INTERPRETATION:** Weebit's independence is useful to foundries and IDMs that do not want to build ReRAM internally, but it is not a universal moat. A large foundry can prefer its own process-specific technology.

### Other emerging NVM

The annual report explicitly identifies **MRAM, FRAM and PCM** as competing emerging NVM technologies, while OTP/MTP and improved flash can remain viable in some applications.

Key competitive variables include:

- process-node scalability;
- endurance and retention;
- high-temperature reliability;
- write/read speed;
- density;
- added masks / wafer cost;
- analog-process compatibility;
- qualification history;
- supplier/IP risk.

**CONCLUSION:** ReRAM appears credible as an embedded-flash successor, but **Weebit does not own the category**. The investable moat depends on accumulating qualified foundry/IDM platforms and customer production before alternatives become equally convenient.

---

## 7. Financial evidence

### FY26

| Metric | FY26 |
|---|---:|
| Revenue | **A$15.3m** |
| FY25 revenue | A$4.4m |
| Net loss | **A$54.9m** |
| R&D expense | **A$47.6m** |
| Operating cash outflow | **A$18.4m** |
| Customer cash receipts | ~A$20m |
| Cash at 30 Jun 2026 | **A$168.3m** |
| Share-based payments | **A$19.0m** |

**FACT:** Revenue grew 246% y/y, but losses also widened as the company accelerated R&D, technology-transfer programs, commercial expansion and AI investment.

**FACT:** Weebit raised approximately **A$102m** during 2026 through institutional placements and an SPP. Ordinary shares increased from roughly **208.4m at June 2025 to 240.2m at June 2026**.

**FACT:** At FY26 year-end there were also **~12.9m unlisted options** outstanding plus a material pool of restricted/performance share rights. Not all will vest or exercise, but dilution should be modeled rather than ignored.

**INTERPRETATION:** Liquidity risk is low in the near term. Dilution risk is not. The company is funding a long semiconductor-commercialisation cycle with equity while royalty revenue remains prospective.

---

## 8. Valuation / investability

### Point-in-time reference

**4 September 2026:**

- share price: **A$3.53**;
- market capitalization: **~A$849m**;
- enterprise value: **~A$681m**;
- FY26 revenue: **A$15.3m**.

That is roughly **45x EV / FY26 revenue**.

The share price closed around **A$3.59 on 7 September**, versus a 52-week range of roughly A$2.47–A$8.89.

**CONCLUSION:** The stock is already priced as a successful future royalty platform, not as an early-stage IP company with A$15m of revenue.

### Reverse commercialization hurdle

A conventional earnings valuation is not credible before royalties begin, so use a reverse hurdle instead.

**HYPOTHESIS:** If enterprise value must compound at roughly 12% annually from the September 2026 reference to end-2030, it would need to reach about **A$1.1bn** before allowing for future cash burn or dilution.

At illustrative future EV/revenue multiples:

- **10x revenue** implies roughly **A$110m** annual revenue;
- **15x revenue** implies roughly **A$73m** annual revenue.

That means the business would need to grow revenue roughly **5–7x from FY26** while shifting meaningfully toward high-margin recurring royalties to support an attractive return without relying on an even more aggressive terminal multiple.

This is **not a price target or forecast**. It is a reminder that the current valuation requires genuine mass-production success.

---

## 9. Commercialisation scorecard

| Milestone | State | Evidence |
|---|---|---|
| Technology works in silicon | **Passed** | multiple nodes / wafers / demo chips |
| Production-fab qualification | **Passed on SkyWater + DB HiTek** | JEDEC; automotive qualification available on SkyWater |
| Tier-1 IDM licensing | **Passed** | onsemi + Texas Instruments |
| Product-customer design-in | **Passed** | multiple revenue-generating agreements |
| Customer tape-out | **Passed** | three designs by June 2026 |
| Functional commercial prototype | **Passed for at least one** | chip returned and running software |
| First product mass production | **Not yet** | company hopes first customer reaches it in CY27 |
| Recurring royalty revenue | **Not yet demonstrated** | current revenue is licensing / NRE |
| Named commercial AI customer | **Not demonstrated in reviewed disclosures** | AI program/R&D exists; commercial milestone unverified |
| Broad multi-foundry adoption | **Not yet** | SkyWater / DB HiTek plus onsemi/TI; additional Tier-1 deals have taken longer than targeted |

**INTERPRETATION:** The thesis has moved from **technology risk** toward **adoption-speed and economics risk**.

---

## 10. Catalysts

1. First customer enters mass production and Weebit reports royalty revenue.
2. onsemi completes qualification and makes ReRAM available commercially on Treo.
3. TI reaches silicon / qualification milestones and identifies production programs.
4. Another Tier-1 foundry or IDM licenses Weebit ReRAM.
5. More product customers tape out and complete qualification.
6. A named commercial AI / compute-in-memory customer validates the AI option.
7. Royalty revenue begins scaling faster than R&D and stock-based compensation.

---

## 11. Thesis breakers

1. **No meaningful royalty revenue by 2028** despite multiple 2026 tape-outs.
2. onsemi/TI qualification or production programs stall materially.
3. Product-customer tape-outs fail qualification or never reach volume.
4. Major foundries choose captive ReRAM / MRAM or another NVM rather than licensing independent IP.
5. Weebit requires repeated large equity raises before royalties cover operating investment.
6. Share-based compensation / dilution remains large relative to revenue creation.
7. AI compute-in-memory remains research-only while valuation continues to price in an AI platform.
8. A technical reliability, endurance or manufacturability problem appears at a production customer.

---

## 12. What would justify a higher status?

Weebit should not move to `High-conviction research candidate` on another licensing announcement alone.

A stronger case requires several of:

- first meaningful royalty revenue;
- evidence of recurring production volumes;
- onsemi and/or TI reaching commercial product availability;
- a second large royalty-generating product family;
- royalty gross profit scaling faster than R&D / SBC;
- further foundry adoption without repeated large dilution;
- a valuation reset that gives room for execution risk.

---

## 13. Current conclusion

**Previous view:** Weebit was a low-confidence research-queue name whose ReRAM thesis still needed evidence of commercial adoption.

**New view:** **commercial adoption is real but early.** Tier-1 licensing, foundry qualification, product tape-outs and A$15.3m FY26 revenue materially de-risk the technology-to-customer bridge.

The unsolved step is the one that matters most for valuation: **turning design-ins into recurring royalties at scale**.

**Status change:** `Research queue` → **`Watch`**.  
**Confidence:** Low → **Medium**.

Weebit is therefore a credible asymmetric **optionality** name, but not yet the strongest capital-allocation candidate in the repository. At the current ~A$0.85bn market value, investors are already paying for a meaningful portion of the future royalty story.

## Sources

Primary / regulatory / company:

- FY26 Annual Report / Appendix 4E: https://financialfilings.com/filings/weebit-nano-ltd/annual-report/2026/57856331/
- Q4 FY26 activities report: https://financialfilings.com/filings/weebit-nano-ltd/interim-quarterly-report/2026/49814161/
- Weebit 2026 press-release index: https://www.weebit-nano.com/news/press-releases-2026/
- TI / DB HiTek Q2 FY26 update: https://www.weebit-nano.com/news/press-releases/weebit-nano-signs-largest-customer-to-date-technology-qualified-at-db-hitek/
- Product-customer tape-outs: https://www.weebit-nano.com/news/press-releases/two-weebit-nano-product-customers-tape-out-one-already-demonstrating-a-functional-prototype/
- onsemi licence: https://www.weebit-nano.com/news/press-releases/weebit-nano-licenses-its-reram-technology-to-onsemi/
- SkyWater qualified product: https://www.weebit-nano.com/products/embedded-reram-ip/weebit-reram-nvm-in-skywater-130nm-cmos/
- Korean AI compute-in-memory program: https://www.weebit-nano.com/news/press-releases/weebit-nanos-reram-selected-for-korean-national-compute-in-memory-program/
- 28nm scaling demonstration: https://www.weebit-nano.com/news/press-releases/weebit-demonstrates-successful-scaling-of-its-reram-technology-to-28nm/
- 22nm tape-out: https://www.weebit-nano.com/news/press-releases/weebit-nano-tapes-out-first-22nm-demo-chip-reram-rram-embedded-nvm-for-iot-ai-applications/
- ReRAM technical / cost comparison, March 2026 investor presentation: https://www.weebit-nano.com/wp-content/uploads/2026/03/260326.-Accelerating-commercial-progress-AI-innovation.pdf
- Patent / IP approach: https://www.weebit-nano.com/wp-content/uploads/2025/08/2508_NEW_ESG-Report.pdf

Point-in-time market data:

- WBT valuation / share statistics: https://stockanalysis.com/quote/asx/WBT/statistics/
- WBT market-cap history: https://stockanalysis.com/quote/asx/WBT/market-cap/
- WBT price history: https://stockanalysis.com/quote/asx/WBT/history/

## Change history

2026-09-07 — Completed issue #5 deep dive. Commercial evidence is materially stronger than the original research-queue thesis; moved Weebit to `Watch` / Medium confidence while preserving pre-royalty, valuation and dilution risks.