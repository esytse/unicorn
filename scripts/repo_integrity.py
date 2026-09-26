#!/usr/bin/env python3
"""Deterministic repository contract checks; standard library only."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from prospective import validate as validate_prospective
from performance import validate as validate_performance
from discovery_coverage import validate as validate_discovery_coverage
from objective_ranking import validate as validate_objective_ranking

MAP = Path('docs/REPOSITORY_GOVERNANCE.md')
FROZEN = Path('scripts/frozen-261.json')
REQUIRED_DATES = (MAP, Path('docs/DOCUMENTATION_AUDIT.md'), Path('docs/BACKLOG_AUDIT.md'))
REQUIRED_CANONICAL = {'Portfolio mandate / Gate-E operating rules': 'PORTFOLIO.md',
                      'Live ranked research universe': 'research/ranked-universe.md',
                      'Live prospective calibration checkpoints': 'research/prediction-calibration-ledger.md'}


def check_issue_contract(issue):
    """Validate an exported issue record when supplied (CI has no live issue API)."""
    errors = []
    required = ('State', 'Priority', 'Type', 'Trigger', 'Parent', 'Dependencies', 'Next action', 'Completion gate')
    for key in required:
        if not str(issue.get(key, '')).strip():
            errors.append(f'ISSUE: missing {key}')
    state = issue.get('State')
    if state not in {'READY', 'RUNNING', 'WAITING', 'BLOCKED', 'PARKED', 'EPIC', 'DONE'}:
        errors.append(f'ISSUE: invalid State {state}')
    if issue.get('Priority') not in {'P0', 'P1', 'P2'}:
        errors.append(f'ISSUE: invalid Priority {issue.get("Priority")}')
    if state == 'READY' and issue.get('Dependencies') not in (None, 'NONE'):
        errors.append('ISSUE: READY has unresolved Dependencies')
    if state == 'RUNNING' and issue.get('Trigger') not in (None, 'NONE'):
        errors.append('ISSUE: RUNNING has unmet Trigger')
    if state == 'BLOCKED' and issue.get('Dependencies') in (None, 'NONE'):
        errors.append('ISSUE: BLOCKED needs an explicit Dependency')
    if state == 'WAITING' and issue.get('Trigger') in (None, 'NONE'):
        errors.append('ISSUE: WAITING needs an explicit Trigger')
    return errors


def check(root, base_ref=None):
    root = Path(root)
    errors = []
    def fail(code, message):
        errors.append(f'{code}: {message}')
    markdown = sorted(root.rglob('*.md'))
    markdown = [p for p in markdown if '.git' not in p.parts and 'scripts/fixtures' not in str(p)]
    for path in markdown:
        body = path.read_text(encoding='utf-8')
        # Ordinary inline links and images; external URLs, fragments, mailto and issue URLs are not local paths.
        for target in re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)', body):
            target = target.split('#', 1)[0].split('?', 1)[0].strip().strip('<>')
            if not target or re.match(r'^[a-z][a-z\d+.-]*:', target, re.I):
                continue
            resolved = (root / unquote(target).lstrip('/') if target.startswith('/') else path.parent / unquote(target))
            if not resolved.exists():
                fail('LINK', f'{path.relative_to(root)} -> {target}: missing local target')
        # Metadata applies only where an explicit lifecycle contract is declared.
        lifecycle = re.search(r'^\*\*Lifecycle:\*\*\s*(CANONICAL|DERIVED|HISTORICAL|GUIDANCE|LOG|ARCHIVE)\b', body, re.M | re.I)
        declared = re.search(r'^\*\*Lifecycle:\*\*\s*(\S+)', body, re.M | re.I)
        if declared and not lifecycle:
            fail('METADATA', f'{path.relative_to(root)} invalid Lifecycle {declared.group(1)}')
        if lifecycle and lifecycle.group(1).upper() == 'DERIVED':
            if re.search(r'^\*\*Authority:\*\*\s*CANONICAL\b', body, re.M):
                fail('METADATA', f'{path.relative_to(root)} DERIVED cannot declare CANONICAL authority')
            if not (re.search(r'^\*\*Canonical upstream:\*\*', body, re.M) or re.search(r'^\*\*Upstream authorities:\*\*', body, re.M)):
                fail('METADATA', f'{path.relative_to(root)} DERIVED requires upstream authority metadata')
        for key in ('Supersedes', 'Superseded-by', 'Canonical upstream'):
            for target in re.findall(r'^\*\*' + key + r':\*\*\s*`([^`]+)`', body, re.M):
                if not (root / target).is_file():
                    fail('LIFECYCLE', f'{path.relative_to(root)} {key} points to missing {target}')
                if key == 'Canonical upstream' and target == str(path.relative_to(root)):
                    fail('LIFECYCLE', f'{path.relative_to(root)} cannot derive from itself')
        if re.search(r'^\*\*Authority:\*\*\s*CANONICAL\b', body, re.M):
            concept = re.search(r'^\*\*Concept:\*\*\s*(.+)$', body, re.M)
            if not concept:
                fail('METADATA', f'{path.relative_to(root)} canonical authority requires **Concept:**')
    for path in REQUIRED_DATES:
        if (root / path).exists() and not re.search(r'^\*\*As of:\*\*\s*\d{4}-\d{2}-\d{2}\b', (root / path).read_text(), re.M):
            fail('FRESHNESS', f'{path} requires YYYY-MM-DD As of metadata')
    source = root / MAP
    if source.exists():
        rows = {}
        for line in source.read_text().splitlines():
            cells = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(cells) != 4 or not cells[3].startswith('live canonical'):
                continue
            concept, canonical = cells[:2]
            match = re.fullmatch(r'`([^`]+)`', canonical)
            if not match:
                continue  # generalized pattern entries (per theme/company) are not paths
            target = match.group(1)
            if concept in rows:
                fail('AUTHORITY', f'duplicate live canonical declaration for {concept}: {rows[concept]}, {target}')
            rows[concept] = target
            if not (root / target).is_file():
                fail('AUTHORITY', f'{concept} canonical path missing: {target}')
        for concept, path in REQUIRED_CANONICAL.items():
            if rows.get(concept) != path:
                fail('AUTHORITY', f'{concept} must resolve to {path}; got {rows.get(concept)}')
        # Backtick references on governed map must resolve when written as a concrete repo path.
        for path in re.findall(r'`((?:research|sources|docs)/[^`*]+\.md)`', source.read_text()):
            if not (root / path).is_file():
                fail('AUTHORITY', f'canonical map references missing {path}')
    for name in ('PORTFOLIO.md', 'research/ranked-universe.md'):
        path = root / name
        if path.is_file():
            body = path.read_text()
            if name.startswith('research/') and not re.search(r'Status:\*\* Active canonical cross-theme ranking', body):
                fail('RANKING', f'{name} missing canonical ranking status')
            if name == 'PORTFOLIO.md' and 'research/ranked-universe.md' not in body:
                fail('RANKING', 'PORTFOLIO.md must reference canonical ranked universe')
    # Optional machine-readable issue export is validated only when present; issue state lives on GitHub.
    issue_export = root / 'scripts/issue-state.json'
    if issue_export.exists():
        for issue in json.loads(issue_export.read_text()):
            errors.extend(f'#{issue.get("number", "?")} {e}' for e in check_issue_contract(issue))
    # Derived output can pin an upstream digest; a mismatch means regeneration is needed.
    for path in markdown:
        body = path.read_text()
        upstream = re.search(r'^\*\*Canonical upstream:\*\* `([^`]+)`', body, re.M)
        digest = re.search(r'^\*\*Upstream SHA-256:\*\* `([a-f0-9]{64})`', body, re.M)
        if digest and not upstream:
            fail('DERIVED', f'{path.relative_to(root)} digest without canonical upstream')
        if upstream and digest and (root / upstream.group(1)).is_file():
            actual = hashlib.sha256((root / upstream.group(1)).read_bytes()).hexdigest()
            if digest.group(1) != actual:
                fail('DERIVED', f'{path.relative_to(root)} stale against {upstream.group(1)}')
    frozen = root / FROZEN
    if frozen.is_file():
        baseline = json.loads(frozen.read_text())
        actual = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in (root / 'research/backtests/261').rglob('*') if p.is_file()}
        for name in sorted(set(baseline) | set(actual)):
            if actual.get(name) != baseline.get(name):
                fail('FROZEN', f'#261 historical file added/removed/changed: {name}')
    else:
        fail('FROZEN', f'missing {FROZEN}')
    cases = set()
    for name in ('CASE_REGISTER', 'PREDICTIONS', 'OUTCOMES'):
        path = root / f'research/backtests/261/{name}.md'
        if not path.is_file():
            continue
        seen = set()
        for line in path.read_text().splitlines():
            if not re.match(r'^\|\s*[DH]\d', line):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            case = cells[0]
            if not re.fullmatch(r'[DH]\d{2}', case):
                fail('KEY', f'{name}: malformed case {case}')
            key = case if name == 'CASE_REGISTER' else (case, cells[3] if name == 'PREDICTIONS' else cells[1])
            if key in seen:
                fail('KEY', f'{name}: duplicate key {key}')
            seen.add(key)
        if name == 'CASE_REGISTER':
            cases = seen
        else:
            for key in seen:
                if key[0] not in cases:
                    fail('KEY', f'{name}: unknown case {key[0]}')
    errors.extend(validate_prospective(root, base_ref))
    errors.extend(validate_performance(root, base_ref))
    discovery_errors, _ = validate_discovery_coverage(root)
    errors.extend(discovery_errors)
    errors.extend(validate_objective_ranking(root))
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--base-ref', default=None, help='PR base commit/ref for append-only comparison')
    args = parser.parse_args()
    problems = check(args.root, args.base_ref)
    for problem in problems:
        print('ERROR', problem)
    print(f'Repository integrity: {len(problems)} error(s)')
    raise SystemExit(bool(problems))
