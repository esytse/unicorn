#!/usr/bin/env python3
"""Validate #357 portfolio-feasibility weights, rules and arithmetic."""
import json
from decimal import Decimal
from pathlib import Path

MODEL = Path('research/portfolio-feasibility-2028.json')
REPORT = Path('research/portfolio-feasibility-2028.md')
SCENARIOS = ('bear', 'base', 'upside')
RULES = ('entry', 'add', 'trim', 'sell', 'thesis_break')
CLASSES = {
    'EVIDENCE-SUPPORTED',
    'TRIGGER-DEPENDENT',
    'MATHEMATICALLY POSSIBLE BUT OPERATIONALLY IMPLAUSIBLE',
    'UNSUPPORTED BY CURRENT EVIDENCE',
}
EXPECTED_STATES = {
    'TAI-TECH': 'ACTION',
    'Laifual': 'ACTION',
    'Impro': 'ACTION',
    'Modine': 'WAIT',
    'Centrus': 'REASSESS',
    'JEM': 'WAIT',
    'SUSS': 'WAIT',
}


def D(value):
    return Decimal(str(value))


def validate(root='.'):
    root = Path(root)
    errors = []
    try:
        data = json.loads((root / MODEL).read_text(encoding='utf-8'))
        report = (root / REPORT).read_text(encoding='utf-8')
    except (OSError, json.JSONDecodeError) as exc:
        return [f'FEASIBILITY: {exc}']

    start = D(data.get('starting_capital_gbp', 0))
    candidates = data.get('candidates', {})
    for key, expected_state in EXPECTED_STATES.items():
        candidate = candidates.get(key, {})
        if candidate.get('state') != expected_state:
            errors.append(f'FEASIBILITY: {key} state must be {expected_state}')
        if any(not str(candidate.get(rule, '')).strip() for rule in RULES):
            errors.append(f'FEASIBILITY: {key} missing entry/add/trim/sell/thesis-break rule')
        if set(candidate.get('scenario_multiples', {})) != set(SCENARIOS):
            errors.append(f'FEASIBILITY: {key} needs bear/base/upside multiples')

    seen_ids = set()
    for portfolio in data.get('portfolios', []):
        ident = portfolio.get('id', '?')
        if ident in seen_ids:
            errors.append(f'FEASIBILITY: duplicate portfolio {ident}')
        seen_ids.add(ident)
        positions = portfolio.get('positions', [])
        initial = sum(D(row.get('initial_weight_pct', 0)) for row in positions)
        staged = sum(D(row.get('staged_weight_pct', 0)) for row in positions)
        cash = D(portfolio.get('cash_pct', 0))
        if initial != D(portfolio.get('initial_deployment_pct', -1)):
            errors.append(f'FEASIBILITY: {ident} initial weights do not reconcile')
        if staged != D(portfolio.get('staged_deployment_pct', -1)):
            errors.append(f'FEASIBILITY: {ident} staged weights do not reconcile')
        if staged + cash != D(100):
            errors.append(f'FEASIBILITY: {ident} staged weights plus cash must equal 100')
        if not str(portfolio.get('cash_deployment_condition', '')).strip():
            errors.append(f'FEASIBILITY: {ident} cash condition missing')
        keys = [row.get('candidate') for row in positions]
        if len(keys) != len(set(keys)):
            errors.append(f'FEASIBILITY: {ident} duplicate candidate')
        for row in positions:
            key = row.get('candidate')
            if key not in candidates:
                errors.append(f'FEASIBILITY: {ident} unknown candidate {key}')
                continue
            if D(row.get('initial_weight_pct', 0)) > D(row.get('staged_weight_pct', 0)):
                errors.append(f'FEASIBILITY: {ident} {key} initial exceeds staged')
            if D(row.get('staged_weight_pct', 0)) > D(candidates[key].get('ceiling_pct', 0)):
                errors.append(f'FEASIBILITY: {ident} {key} exceeds ceiling')
        for scenario in SCENARIOS:
            multiple = cash / D(100)
            for row in positions:
                key = row.get('candidate')
                if key in candidates:
                    multiple += (D(row.get('staged_weight_pct', 0)) / D(100) *
                                 D(candidates[key]['scenario_multiples'][scenario]))
            calculated = (start * multiple).quantize(D('1'))
            recorded = D(portfolio.get('scenario_values_gbp', {}).get(scenario, -1))
            if calculated != recorded:
                errors.append(f'FEASIBILITY: {ident} {scenario} value {recorded} != {calculated}')
        stress = portfolio.get('two_failure_stress', {})
        failed = stress.get('failed_candidates', [])
        if len(failed) != 2 or any(key not in keys for key in failed):
            errors.append(f'FEASIBILITY: {ident} stress must name two held candidates')
        else:
            multiple = cash / D(100)
            for row in positions:
                key = row['candidate']
                if key not in failed:
                    multiple += (D(row['staged_weight_pct']) / D(100) *
                                 D(candidates[key]['scenario_multiples']['base']))
            calculated = (start * multiple).quantize(D('1'))
            if calculated != D(stress.get('value_gbp', -1)):
                errors.append(f'FEASIBILITY: {ident} two-failure value does not reconcile')

    hurdles = data.get('hurdles', [])
    if [row.get('target_gbp') for row in hurdles] != [80000, 120000, 160000, 200000]:
        errors.append('FEASIBILITY: all four ordered hurdles are required')
    for row in hurdles:
        if row.get('classification') not in CLASSES:
            errors.append(f'FEASIBILITY: invalid hurdle classification {row.get("classification")}')
        if not str(row.get('requirement', '')).strip():
            errors.append(f'FEASIBILITY: hurdle {row.get("target_gbp")} lacks reverse requirement')
    if 'research/ranked-universe.md' not in data.get('upstream_authorities', []):
        errors.append('FEASIBILITY: objective-aligned ranking authority missing')
    required_report = (
        'TRIGGER-DEPENDENT, not evidence-supported today',
        'not a forecast, promise, price target or trade instruction',
        'Two-failure stress',
        'Operating/earnings versus rerating bridge',
        'Tactical cash',
    )
    for phrase in required_report:
        if phrase not in report:
            errors.append(f'FEASIBILITY: report missing boundary/detail: {phrase}')
    return errors


if __name__ == '__main__':
    problems = validate()
    for problem in problems:
        print('ERROR', problem)
    print(f'Portfolio feasibility: {len(problems)} error(s)')
    raise SystemExit(bool(problems))
