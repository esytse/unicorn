# Contributing without learning Git first

You can contribute to this repository mainly by working through an AI agent.

## The simplest workflow

Tell the agent what you want researched or updated, and include this instruction:

> Read `AGENTS.md` first. Work on a branch, update the canonical research documents with sources, update `CHANGELOG.md` if conclusions change, and open a pull request. Do not merge it.

The agent should handle the Git mechanics. Your main job is to review the pull request.

## What to review in a pull request

Check four things:

1. **Evidence** — are important claims sourced?
2. **Reasoning** — are facts separated from interpretation and hypothesis?
3. **Changes** — did the agent explain any changed conclusion or confidence?
4. **Uncertainty** — are unresolved questions visible rather than glossed over?

If something is wrong, tell the agent what to correct on the same branch rather than creating another copy of the document.

## Useful prompts

### Add new research

> Read `AGENTS.md`. Research [topic/company], place it in the correct research stream, preserve source provenance, and open a pull request for review.

### Update existing research

> Read `AGENTS.md` and the existing [topic] research. Check for important new evidence, update only what the evidence supports, record any changed conclusion in `CHANGELOG.md`, and open a pull request.

### Challenge the thesis

> Read `AGENTS.md` and the current thesis. Actively search for evidence that could falsify it. Update the research with both supporting and contradictory evidence, then open a pull request.

### Compare companies

> Read `AGENTS.md`. Compare [company A] and [company B] against the same value-chain, moat, adoption, financial, risk and thesis-breaker criteria. Update the canonical files and open a pull request.

## Avoid

Do not ask an agent to "just update main", "rewrite everything", or "make the thesis stronger". Ask it to improve the evidence and preserve uncertainty instead.
