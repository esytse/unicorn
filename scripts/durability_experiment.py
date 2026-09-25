#!/usr/bin/env python3
"""Audit #327 probes against immutable #261 prediction/outcome rows."""
import json
from collections import Counter
from pathlib import Path

PROBES = Path('research/experiments/durability-327/probes.json')
FROZEN = Path('research/backtests/261')


def rows(path, candidate_column):
    result = {}
    for line in path.read_text().splitlines():
        if not line.startswith(('| D', '| H')):
            continue
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        key = (cells[0], cells[candidate_column])
        if key in result:
            raise ValueError(f'duplicate frozen key {key}')
        result[key] = cells
    return result


def validate(root=Path('.')):
    root = Path(root)
    predictions = rows(root / FROZEN / 'PREDICTIONS.md', 3)
    outcomes = rows(root / FROZEN / 'OUTCOMES.md', 1)
    probes = json.loads((root / PROBES).read_text())
    errors = []
    if predictions.keys() != outcomes.keys() or len(predictions) != 63:
        errors.append('DURABILITY: frozen candidate join/count mismatch')
    seen = set()
    for probe in probes:
        key = (probe['case'], probe['candidate'])
        if key in seen:
            errors.append(f'DURABILITY: duplicate probe {key}')
        seen.add(key)
        if key not in predictions or key not in outcomes:
            errors.append(f'DURABILITY: unknown candidate {key}')
            continue
        if probe['t0_state'] != predictions[key][4] or probe['t0_evidence'] != predictions[key][7]:
            errors.append(f'DURABILITY: post-T0 or misquoted evidence {key}')
        if probe['outcome_evidence'] != outcomes[key][-2]:
            errors.append(f'DURABILITY: mismatched outcome {key}')
        if probe['assessment'] not in {'RISK_OBSERVED', 'NON_DISCRIMINATING', 'DATA_LIMITED'}:
            errors.append(f'DURABILITY: invalid assessment {key}')
        if not probe['lesson'] or not probe['factor']:
            errors.append(f'DURABILITY: incomplete interpretation {key}')
    if {case for case, _ in seen} != {case for case, _ in predictions}:
        errors.append('DURABILITY: probe lacks one or more frozen cases')
    return errors, predictions, probes


if __name__ == '__main__':
    problems, predictions, probes = validate()
    for problem in problems:
        print('ERROR', problem)
    print(f'Durability experiment: {len(predictions)} candidate-case rows, '
          f'{len(probes)} explicit probes in 15 cases, {len(problems)} errors; '
          f'assessments {dict(Counter(x["assessment"] for x in probes))}')
    raise SystemExit(bool(problems))
