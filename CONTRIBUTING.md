# Contributing without learning Git first

You can contribute to this repository mainly by working through an AI agent. You do not need to know branches, commits or pull-request mechanics to contribute safely.

## The simplest workflow

Tell the agent what you want researched or updated, and include this instruction:

> Read `AGENTS.md` first. Work on a branch, update the canonical research documents with sources, update `CHANGELOG.md` when required, open a pull request, and merge only after required checks pass.

The agent should handle the Git mechanics. The pull request remains available as a permanent record of what changed and why.

## Optional review

Human approval is not required by default. If you want to inspect something before it lands, say:

> Leave the pull request open for my review. Do not merge it.

Otherwise, the normal path is automated checks followed by merge.

## Useful prompts

### Add new research

> Read `AGENTS.md`. Research [topic/company], place it in the correct research stream, preserve source provenance, open a pull request, and merge after required checks pass.

### Update existing research

> Read `AGENTS.md` and the existing [topic] research. Check for important new evidence, update only what the evidence supports, record any changed conclusion in `CHANGELOG.md`, open a pull request, and merge after required checks pass.

### Challenge the thesis

> Read `AGENTS.md` and the current thesis. Actively search for evidence that could falsify it. Update the research with both supporting and contradictory evidence, then open a pull request and merge after required checks pass.

### Compare companies

> Read `AGENTS.md`. Compare [company A] and [company B] against the same value-chain, moat, adoption, financial, risk and thesis-breaker criteria. Update the canonical files, open a pull request, and merge after required checks pass.

## If you do review a pull request

Check four things:

1. **Evidence** — are important claims sourced?
2. **Reasoning** — are facts separated from interpretation and hypothesis?
3. **Changes** — did the agent explain any changed conclusion or confidence?
4. **Uncertainty** — are unresolved questions visible rather than glossed over?

If something is wrong, tell the agent what to correct on the same branch rather than creating another copy of the document.

## Avoid

Do not ask an agent to "just update main", "rewrite everything", "make the thesis stronger" or bypass failed checks. Ask it to improve the evidence, preserve uncertainty and let the repository retain the history.
