#!/usr/bin/env python3
"""Audit fixed, qualitative #326 T0 feature annotations against frozen #261 rows."""
import json
from collections import Counter
from pathlib import Path

from durability_experiment import rows

HOME = Path('research/experiments/early-promotion-326')
FROZEN = Path('research/backtests/261')
FACTORS = ('qualification', 'production', 'acceleration', 'capacity', 'orders',
           'materiality', 'financial_inflection')
ALLOWED = ('YES', 'NO', 'UNKNOWN')
OUTCOMES = ('CLEAR_INITIAL', 'PARTIAL', 'FAILED_FUNDED', 'FAILED_DURABLE',
            'LATE_OR_TIMING', 'REGIME_SHOCK', 'DATA_LIMITED')


def rules(row):
    f = row['factors']
    yes = lambda *keys: all(f[k] == 'YES' for k in keys)
    return {
        'Q+P': yes('qualification', 'production'),
        'Q+P+A': yes('qualification', 'production', 'acceleration'),
        'P+A+M': yes('production', 'acceleration', 'materiality'),
    }


def validate(root=Path('.')):
    root = Path(root)
    pred = rows(root / FROZEN / 'PREDICTIONS.md', 3)
    outcomes = rows(root / FROZEN / 'OUTCOMES.md', 1)
    annotations = json.loads((root / HOME / 'observations.json').read_text())
    errors = []
    if pred.keys() != outcomes.keys() or len(pred) != 63:
        errors.append('EARLY: frozen join/count mismatch')
    expected = {key for key, cells in pred.items() if cells[4] == 'EVIDENCE-BUILD'}
    if len(expected) != 34:
        errors.append('EARLY: expected 34 EVIDENCE-BUILD rows')
    seen = set()
    for row in annotations:
        key = row['case'], row['candidate']
        if key in seen:
            errors.append(f'EARLY: duplicate {key}')
        seen.add(key)
        if key not in expected:
            errors.append(f'EARLY: unexpected/non-EVIDENCE-BUILD {key}')
            continue
        if row['t0_date'] != pred[key][1] or row['t0_confirming'] != pred[key][6] or row['t0_disconfirming'] != pred[key][7]:
            errors.append(f'EARLY: altered T0 quotation {key}')
        if row['outcome_evidence'] != outcomes[key][-2]:
            errors.append(f'EARLY: altered post-T0 outcome {key}')
        if set(row['factors']) != set(FACTORS) or any(x not in ALLOWED for x in row['factors'].values()):
            errors.append(f'EARLY: invalid factors {key}')
        if row['outcome_class'] not in OUTCOMES:
            errors.append(f'EARLY: invalid outcome class {key}')
        if row['valuation_t0'] not in ('RERATED', 'LATE_STAGE', 'UNKNOWN'):
            errors.append(f'EARLY: invalid valuation {key}')
        if row['concentration_t0'] not in ALLOWED or not row['evidence_gaps_t0']:
            errors.append(f'EARLY: incomplete T0 risk/gap {key}')
    if seen != expected:
        errors.append(f'EARLY: missing/unexpected rows {sorted(expected-seen)} {sorted(seen-expected)}')
    return errors, pred, annotations


def report(root=Path('.')):
    errors, predictions, observations = validate(root)
    if errors:
        raise ValueError('\n'.join(errors))
    summary = {}
    for rule in rules(observations[0]):
        affected = [x for x in observations if rules(x)[rule]]
        summary[rule] = {
            'development': [(x['case'], x['candidate']) for x in affected if x['case'].startswith('D')],
            'holdout': [(x['case'], x['candidate']) for x in affected if x['case'].startswith('H')],
            'outcomes': dict(Counter(x['outcome_class'] for x in affected)),
        }
    return summary


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
