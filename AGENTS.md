# AGENTS.md — Unicorn Research

These instructions apply to every AI agent interacting with this repository.

## Purpose

This repository is a collaborative research system for identifying high-upside companies, technologies and structural bottlenecks across themes such as AI memory and robotics actuators.

The goal is not to generate persuasive narratives. The goal is to maintain a traceable, evidence-based body of research that humans can inspect, challenge and revise over time.

## Mandatory workflow

Before making any substantive change:

1. Read this file.
2. Read `README.md`.
3. Read the relevant theme's existing documents.
4. Read `watchlist.md` if a company or investment conclusion is involved.
5. Read `CHANGELOG.md` for recent changes.
6. Inspect related company files and the source register where relevant.

For substantive research updates:

1. Work on a branch, not directly on `main`.
2. Update existing canonical documents instead of creating versioned duplicates.
3. Add or update sources.
4. Clearly distinguish **FACT**, **INTERPRETATION**, **HYPOTHESIS** and **OPEN QUESTION**.
5. Update confidence when the evidence changes.
6. Update `CHANGELOG.md` if the thesis, watchlist status, confidence, ranking or other material conclusion changes.
7. Open a pull request explaining what changed, the evidence, unresolved uncertainty and any changed conclusions.
8. Do not merge your own substantive research pull request.

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

Agents may automate research collection, comparison, document maintenance and drafting. They must not hide uncertainty, fabricate evidence, or silently promote a company on the watchlist.

Human review is required before substantive research changes are merged into `main`.
