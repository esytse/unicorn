# Research Changelog

This file records substantive changes to research conclusions, confidence, prioritisation and governance. Minor wording or formatting edits do not need an entry.

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

- **AI memory:** evidence now supports a chain of constraints across advanced DRAM capacity, HBM stack yield/thermal, advanced package integration, test and system-level memory interfaces. The broader investment hypothesis — that smaller enabling suppliers will capture disproportionate value — remains to be tested company by company.
- **Robotics actuators:** research stream opened; value-chain and company analysis still to be built.
