# AGENTS.md — Unicorn Research

These instructions apply to every AI agent interacting with this repository.

## Purpose

This repository is a collaborative research system for identifying high-upside companies, technologies and structural bottlenecks across themes such as AI memory and robotics actuators.

The goal is not to generate persuasive narratives. The goal is to maintain a traceable, evidence-based body of research that humans can inspect, challenge and revise over time.

## Mandatory workflow

Before making any substantive change:

1. Read this file.
2. Read `README.md`.
3. Read `AUTOMATION.md` when work is selected from a GitHub backlog item or scheduled automation.
4. Read the relevant theme's existing documents.
5. Read `watchlist.md` if a company or investment conclusion is involved.
6. Read `CHANGELOG.md` for recent changes.
7. Inspect related company files and the source register where relevant.

For substantive research updates:

1. Work on a branch, not directly on `main`.
2. Update existing canonical documents instead of creating versioned duplicates.
3. Add or update sources.
4. Clearly distinguish **FACT**, **INTERPRETATION**, **HYPOTHESIS** and **OPEN QUESTION**.
5. Update confidence when the evidence changes.
6. Update `CHANGELOG.md` if the thesis, watchlist status, confidence, ranking or other material conclusion changes.
7. Open a pull request explaining what changed, the evidence, unresolved uncertainty and any changed conclusions.
8. Treat the pull request as the audit record. Human approval is not required by default.
9. Never merge while required checks are pending or failing.
10. Once required checks pass, enable auto-merge where available. If auto-merge is unavailable and the user has not requested manual review, the agent may merge the PR after verifying the checks passed.

If the user explicitly asks for review before merge, leave the PR open.

## Backlog-driven automation rules

When an agent is operating from a scheduler or GitHub backlog, `AUTOMATION.md` is mandatory operating context.

GitHub issues are the authoritative execution state. Chat history is not a substitute for queue state.

The agent must:

1. Select only an issue whose automation state is `READY`.
2. Never execute an `EPIC`, `WAITING`, `BLOCKED` or `PARKED` issue unless its state is explicitly changed first for a valid reason.
3. Mark the selected item `RUNNING` before substantive work and record enough context to avoid duplicate execution.
4. Check for an existing branch, PR or recent live claim before reclaiming a `RUNNING` item.
5. Default to one bounded substantive backlog item per scheduler run; short administrative updates may be batched.
6. After execution, set a truthful resulting state and a concrete next action, trigger or dependency. Do not leave vague statements such as “more research needed.”
7. Create follow-up backlog only when the new question can materially change portfolio allocation, ranking, bottleneck direction, evidence confidence, catalyst timing/probability or a thesis breaker.
8. Prefer the highest-priority actionable work. Do not displace P0/P1 decision work with lower-priority exploratory research.
9. **Within the same priority, optimize for marginal portfolio contribution rather than standalone company attractiveness.** Prefer work that can materially improve the probability of the active portfolio objective after considering remaining-window upside, downside/permanent-loss risk, catalyst timing/probability, evidence confidence, responsible position-size ceiling, thematic/catalyst correlation with existing candidates, and the best alternative use of capital. A highly correlated candidate should not outrank an independent candidate merely because its standalone business quality is higher; it should either offer clearly superior asymmetry to the incumbent exposure or remain lower priority.
10. Treat **decisions as upstream of issues**: portfolio gaps and decision uncertainty should create research questions; research questions should create or reprioritize issues. Do not let queue order substitute for strategy.
11. Measure scheduler sufficiency using the definitions in `AUTOMATION.md`; do not add workers merely because more automation feels desirable.
12. Never allow scheduler pressure to justify weaker sourcing, incomplete governance or bypassing checks.

## Versioning rules

Git commit history is the authoritative detailed version history.

Do not create files named like:

- `final.md`
- `final-v2.md`
- `revised-final.md`
- `thesis-new.md`
- `latest-copy.md`

Update the canonical file instead.

Use repository tags only for meaningful milestones such as `v0.1`, `v0.2` or `v1.0`; do not tag every edit.

## Research integrity

Every material factual claim should have a recoverable source wherever practical.

Prefer primary sources, regulatory filings, company materials, technical papers and high-quality industry sources over unsourced summaries.

When sources conflict:

- preserve the disagreement;
- do not silently choose the more convenient source;
- explain why one source may be more credible;
- lower confidence if the discrepancy cannot be resolved.

Never invent a citation, figure, market size, customer, partnership, product capability or commercial status.

If reliable evidence cannot be found, say so explicitly.

## Thesis changes

Never silently change an investment or technology conclusion.

When a substantive conclusion changes, record:

- previous conclusion;
- new conclusion;
- evidence that caused the change;
- confidence before and after, where useful;
- implications for the watchlist.

Material changes belong in `CHANGELOG.md`.

## Confidence convention

Use one of:

- **Low** — limited, indirect or conflicting evidence
- **Medium** — multiple credible sources but meaningful uncertainty remains
- **High** — strong, direct and consistent evidence

Confidence is confidence in the stated conclusion, not a prediction of investment returns.

## Company research

Company files should distinguish, where relevant:

- what the company actually sells;
- where it sits in the value chain;
- customers or adoption evidence;
- moat or dependency thesis;
- competitors and substitutes;
- financial/commercial evidence;
- valuation or investability considerations;
- catalysts;
- thesis breakers;
- open questions;
- current confidence.

Do not describe a company as a "unicorn", "winner" or similar conclusion solely because it operates in an attractive theme.

## Cross-theme watchlist

`watchlist.md` is a research prioritisation tool, not a recommendation list.

A company can move between statuses only when the supporting evidence is recorded. Suggested statuses:

- `Research queue`
- `Investigating`
- `Watch`
- `High-conviction research candidate`
- `Deprioritised`
- `Rejected thesis`

If a status changes, update the changelog.

## Commit messages

Prefer clear messages such as:

- `research(memory): update Weebit Nano evidence`
- `research(actuators): add competitive landscape`
- `thesis(memory): revise bottleneck hypothesis`
- `sources: add primary evidence`
- `governance: tighten research checks`

## Pull request summary

Every substantive research PR should include:

- **What changed**
- **Why it changed**
- **Key evidence added**
- **Conclusion changes**
- **Confidence changes**
- **Open questions**
- **Files changed**

## Safety rule for automation

Agents may automate research collection, comparison, document maintenance, backlog maintenance, PR creation and merging after required checks pass. They must not hide uncertainty, fabricate evidence, silently promote a company on the watchlist, bypass required checks, force-push protected history, or delete research history to make a thesis look cleaner.

Automation may generate research-level Buy/Add/Trim/Sell signals and thesis-break alerts, but it must **not place brokerage trades or securities orders**. Actual capital execution remains manual unless repository governance is explicitly changed by the user in the future.
