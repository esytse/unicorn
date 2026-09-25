#!/usr/bin/env python3
"""Validate #330's architecture-first coverage and negative-search ledger."""
import json
import re
from collections import Counter
from pathlib import Path

LEDGER = Path('research/discovery/coverage-ledger.json')
RANKING = Path('research/ranked-universe.md')
RESULTS = {'ACTIVE_CANDIDATES', 'CANDIDATES_FOUND_BUT_REJECTED',
           'NO_CREDIBLE_LISTED_CAPTURE', 'COVERAGE_INCOMPLETE',
           'INTENTIONALLY_EXCLUDED'}
COVERAGE = {'CROWDED', 'STRONG', 'MEDIUM_STRONG', 'MEDIUM', 'EMERGING',
            'UNDER_COVERED', 'BLIND_SPOT', 'EXCLUDED'}
REQUIRED = {'id', 'world_change', 'scarce_complement', 'coverage', 'search_result',
            'searched_families', 'active_listed_examples', 'rejected_or_parked_examples',
            'private_or_uninvestable_benchmarks', 'remaining_gap', 'rescan_triggers', 'sources'}


def ranked_top(path, n=20):
    rows = []
    in_live_table = False
    for line in path.read_text().splitlines():
        if line.startswith('## Authoritative live ranking'):
            in_live_table = True
            continue
        if not in_live_table:
            continue
        cells = [x.strip().strip('*') for x in line.strip('|').split('|')]
        if len(cells) < 2 or not re.fullmatch(r'\d+', cells[0]):
            continue
        rank = int(cells[0])
        if rank <= n:
            rows.append((rank, cells[1]))
        if rank == n:
            break
    rows.sort()
    return [name for _, name in rows]


def validate(root=Path('.')):
    root = Path(root)
    data = json.loads((root / LEDGER).read_text())
    errors = []
    if set(data.get('allowed_results', [])) != RESULTS:
        errors.append('COVERAGE: allowed result registry differs from validator')
    lanes = data.get('lanes', [])
    if len(lanes) < 12:
        errors.append('COVERAGE: fewer than 12 cross-theme lanes')
    ids = [x.get('id') for x in lanes]
    if len(ids) != len(set(ids)):
        errors.append('COVERAGE: duplicate lane ID')
    for row in lanes:
        ident = row.get('id', '?')
        if set(row) != REQUIRED:
            errors.append(f'COVERAGE: {ident} fields differ from contract')
            continue
        if row['coverage'] not in COVERAGE or row['search_result'] not in RESULTS:
            errors.append(f'COVERAGE: {ident} invalid coverage/result')
        for field in ('searched_families', 'rescan_triggers', 'sources'):
            if not row[field]:
                errors.append(f'COVERAGE: {ident} empty {field}')
        for source in row['sources']:
            if not source.startswith('research/') or not (root / source).is_file():
                errors.append(f'COVERAGE: {ident} missing/non-research source {source}')
        if row['search_result'] == 'ACTIVE_CANDIDATES' and not row['active_listed_examples']:
            errors.append(f'COVERAGE: {ident} active result without listed candidates')
        if row['search_result'] in {'NO_CREDIBLE_LISTED_CAPTURE', 'INTENTIONALLY_EXCLUDED'} and row['active_listed_examples']:
            errors.append(f'COVERAGE: {ident} no-capture/excluded result has active candidates')
        if row['search_result'] == 'CANDIDATES_FOUND_BUT_REJECTED' and not row['rejected_or_parked_examples']:
            errors.append(f'COVERAGE: {ident} rejected result lacks rejected candidates')
        if row['search_result'] == 'INTENTIONALLY_EXCLUDED' and row['coverage'] != 'EXCLUDED':
            errors.append(f'COVERAGE: {ident} excluded result lacks EXCLUDED coverage')
    audit = data.get('familiarity_audit', {})
    buckets = audit.get('buckets', {})
    members = [name for group in buckets.values() for name in group]
    top = ranked_top(root / RANKING, audit.get('total', 0))
    if len(top) != audit.get('total') or Counter(top) != Counter(members):
        errors.append(f'COVERAGE: familiarity audit does not partition ranked top {audit.get("total")}')
    if len(members) != len(set(members)):
        errors.append('COVERAGE: familiarity audit duplicates a ranked company')
    return errors, data


if __name__ == '__main__':
    problems, data = validate()
    counts = Counter(x['search_result'] for x in data['lanes'])
    for problem in problems:
        print('ERROR', problem)
    print(f'Discovery coverage: {len(data["lanes"])} lanes; results {dict(counts)}; {len(problems)} error(s)')
    raise SystemExit(bool(problems))
