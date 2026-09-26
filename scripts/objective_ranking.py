#!/usr/bin/env python3
"""Validate the canonical dual-axis objective ranking."""
import re
from pathlib import Path

RANKING = Path('research/ranked-universe.md')
START = '<!-- OBJECTIVE-RANKING:START -->'
END = '<!-- OBJECTIVE-RANKING:END -->'
EXPECTED_COUNT = 65
EXPECTED_ACTIONS = {
    'TAI-TECH Advanced Electronics',
    'Laifual Drive',
    'Impro Precision Industries',
}
KEY_MONITORS = {
    'TAI-TECH Advanced Electronics': 'ACTION',
    'Laifual Drive': 'ACTION',
    'Impro Precision Industries': 'ACTION',
    'Namuga': 'WAIT',
    'Grid Dynamics': 'REASSESS',
    'Vicor': 'WATCH',
    'AP Memory': 'LATE DISCOVERY',
}


def _clean(cell):
    return cell.strip().replace('**', '')


def parse(root='.'):
    path = Path(root) / RANKING
    body = path.read_text(encoding='utf-8')
    if body.count(START) != 1 or body.count(END) != 1:
        raise ValueError('objective ranking requires exactly one bounded table')
    section = body.split(START, 1)[1].split(END, 1)[0]
    rows = []
    for line in section.splitlines():
        if not re.match(r'^\|\s*\*\*\d+\*\*\s*\|', line):
            continue
        cells = [_clean(value) for value in line.strip().strip('|').split('|')]
        if len(cells) != 7:
            raise ValueError(f'objective ranking row has {len(cells)} cells: {line}')
        rows.append({
            'capital_rank': int(cells[0]),
            'structural_rank': int(cells[1]),
            'company': cells[2],
            'exposure': cells[3],
            'tier': cells[4],
            'state': cells[5],
            'reason': cells[6],
        })
    return body, rows


def validate(root='.'):
    errors = []
    try:
        body, rows = parse(root)
    except (OSError, ValueError) as exc:
        return [f'OBJECTIVE_RANKING: {exc}']

    companies = [row['company'] for row in rows]
    capital = [row['capital_rank'] for row in rows]
    structural = [row['structural_rank'] for row in rows]
    if len(rows) != EXPECTED_COUNT:
        errors.append(f'OBJECTIVE_RANKING: expected {EXPECTED_COUNT} rows, got {len(rows)}')
    if len(set(companies)) != len(companies):
        errors.append('OBJECTIVE_RANKING: companies must appear exactly once')
    expected = list(range(1, EXPECTED_COUNT + 1))
    if capital != expected:
        errors.append('OBJECTIVE_RANKING: capital ranks must be ordered and continuous 1..65')
    if sorted(structural) != expected:
        errors.append('OBJECTIVE_RANKING: structural ranks must be unique and continuous 1..65')

    states = {row['company']: row['state'] for row in rows}
    for company, expected_state in KEY_MONITORS.items():
        if states.get(company) != expected_state:
            errors.append(f'OBJECTIVE_RANKING: {company} state must be {expected_state}; got {states.get(company)}')

    action_rows = [row for row in rows if row['state'] == 'ACTION']
    if {row['company'] for row in action_rows} != EXPECTED_ACTIONS:
        errors.append('OBJECTIVE_RANKING: ACTION set disagrees with canonical monitors')
    if action_rows and [row['capital_rank'] for row in action_rows] != list(range(1, len(action_rows) + 1)):
        errors.append('OBJECTIVE_RANKING: ACTION candidates must lead capital priority contiguously')
    if any(row['tier'] != 'Current ACTION' for row in action_rows):
        errors.append('OBJECTIVE_RANKING: ACTION candidates must use Current ACTION tier')
    if any(row['tier'] == 'Current ACTION' and row['state'] != 'ACTION' for row in rows):
        errors.append('OBJECTIVE_RANKING: non-ACTION row cannot use Current ACTION tier')

    required_language = (
        'Structural research priority',
        'March-2028 capital priority',
        'sole complete 65-company inventory',
        'PORTFOLIO.md',
        'AUTOMATION.md',
        'shareholder alpha remains data-limited',
    )
    for phrase in required_language:
        if phrase not in body:
            errors.append(f'OBJECTIVE_RANKING: missing authority/boundary text: {phrase}')
    return errors


if __name__ == '__main__':
    problems = validate()
    for problem in problems:
        print('ERROR', problem)
    print(f'Objective ranking: {len(problems)} error(s)')
    raise SystemExit(bool(problems))
