#!/usr/bin/env python3
"""Fixed categorical sensitivity and factor-ablation challenge for #328."""
import json
from collections import Counter
from pathlib import Path

from early_promotion_experiment import validate

# Explicit frozen T0 warnings; these are qualitative questions, never
# calibrated exclusions. A missing warning is UNKNOWN, not proof of safety.
RISK_PHRASES = ('low module margin', 'gross margin lower', 'capital risk',
                'warranty-adjusted fcf')
# Only architecture-specific numerical T0 group mix recovered in the selected
# Q+P rows. Broader/mixed segment shares are deliberately not imputed.
ATTRIBUTABLE_MIX = {('D01', 'Oclaro'): 47, ('D01', 'NeoPhotonics'): 57}


def factors(row):
    f = row['factors']
    q, p, a, m, f0 = (f[key] == 'YES' for key in
                      ('qualification', 'production', 'acceleration', 'materiality',
                       'financial_inflection'))
    v = row['valuation_t0'] not in ('RERATED', 'LATE_STAGE')
    d = not any(phrase in row['t0_disconfirming'].lower() for phrase in RISK_PHRASES)
    return {'Q': q, 'P': p, 'A': a, 'M': m, 'F': f0, 'V': v, 'D': d}


def selected(rows, required):
    return [row for row in rows if all(factors(row)[factor] for factor in required)]


def summary(rows):
    # Q+P is the minimal early-production hypothesis. Each factor is removed
    # from a rule that actually contains it; no coefficient/threshold tuning.
    variants = {
        'v1': '', 'Q+P': 'QP', 'without Q': 'P', 'without P': 'Q',
        'Q+P+A': 'QPA', 'without A': 'QP',
        'Q+P+M': 'QPM', 'without M': 'QP',
        'Q+P+F': 'QPF', 'without F': 'QP',
        'Q+P+V': 'QPV', 'without V': 'QP',
        'Q+P+D': 'QPD', 'without D': 'QP',
        'Q+P+V+D': 'QPVD', 'Q+P+A+M+V+D': 'QPAMVD',
    }
    result = {}
    for name, required in variants.items():
        affected = [] if name == 'v1' else selected(rows, required)
        result[name] = {
            'development': [f"{x['case']} {x['candidate']}" for x in affected if x['case'].startswith('D')],
            'holdout': [f"{x['case']} {x['candidate']}" for x in affected if x['case'].startswith('H')],
            'outcomes': dict(Counter(x['outcome_class'] for x in affected)),
        }
    result['mix_boundary'] = {
        str(threshold): [f'{case} {candidate}' for (case, candidate), mix in ATTRIBUTABLE_MIX.items()
                         if mix >= threshold]
        for threshold in (5, 15, 30, 50)
    }
    result['leave_one_case_out'] = {
        case: {
            name: [f"{x['case']} {x['candidate']}" for x in selected(
                [row for row in rows if row['case'] != case], required)]
            for name, required in (('Q+P', 'QP'), ('Q+P+V+D', 'QPVD'))
        }
        for case in ('D01', 'D05', 'H02', 'H04', 'H05')
    }
    return result


def validate_experiment(root=Path('.')):
    errors, pred, rows = validate(root)
    if errors:
        return errors, {}
    # Guard the manually selected T0 warning bridge against accidental drift.
    risks = {(x['case'], x['candidate']) for x in rows if not factors(x)['D']}
    expected = {('D02', 'Sunny Optical'), ('D05', 'Cognex'),
                ('H02', 'Pacific Biosciences'), ('H05', 'Enphase Energy')}
    if risks != expected:
        errors.append(f'ABLATION: T0 warning set changed: {risks ^ expected}')
    return errors, summary(rows)


if __name__ == '__main__':
    problems, result = validate_experiment()
    for problem in problems:
        print('ERROR', problem)
    if not problems:
        print(json.dumps(result, indent=2))
    raise SystemExit(bool(problems))
