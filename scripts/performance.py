#!/usr/bin/env python3
"""Prospective #329 scorecards; no external price lookup or imputation."""
import argparse
import json
import math
import subprocess
from datetime import date, datetime
from pathlib import Path

from prospective import HOME

DL = 'DATA-LIMITED'
KINDS = ('MATERIAL_ECONOMIC_EVIDENCE', 'MARKET_RECOGNITION', 'THESIS_BREAK')
LIFECYCLES = ('ACTIVE', 'DELISTED', 'ACQUIRED', 'RESTRUCTURED')


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def drawdown(points):
    peak = points[0]['wealth']
    result = 0.0
    for point in points:
        peak = max(peak, point['wealth'])
        result = min(result, point['wealth'] / peak - 1)
    return result


def validate(root=Path('.'), base_ref=None):
    root = Path(root)
    home = root / HOME
    errors = []
    decisions = {p.stem: json.loads(p.read_text()) for p in (home / 'decisions').glob('*.json')}
    checkpoints = {p.stem: json.loads(p.read_text()) for p in (home / 'checkpoints').glob('*.json')}
    supplements = {p.stem: json.loads(p.read_text()) for p in (home / 'performance').glob('*.json')}
    if supplements.keys() != checkpoints.keys():
        errors.append(f'PERFORMANCE: missing/orphan supplements {sorted(checkpoints.keys() ^ supplements.keys())}')
    for key, record in supplements.items():
        if key not in checkpoints:
            continue
        cp = checkpoints[key]
        ident = cp['decision_id']
        if ident not in decisions:
            errors.append(f'PERFORMANCE: orphan decision {key}')
            continue
        t0 = decisions[ident]
        if record.get('decision_id') != ident or record.get('checkpoint_month') != cp['checkpoint_month'] or key != f"{ident}-{cp['checkpoint_month']:02d}":
            errors.append(f'PERFORMANCE: checkpoint relationship {key}')
            continue
        if not record.get('issuer_id') or not record.get('security_id') or record.get('security_lifecycle') not in LIFECYCLES:
            errors.append(f'PERFORMANCE: missing survivorship identifiers/lifecycle {key}')
        if record.get('security_id') != t0['candidate_id']:
            errors.append(f'PERFORMANCE: security identifier differs from sealed T0 {key}')
        if record.get('security_lifecycle') != 'ACTIVE' and not record.get('corporate_actions'):
            errors.append(f'PERFORMANCE: corporate action provenance required {key}')
        if record.get('economic_capture') not in ('YES', 'NO', DL) or record.get('transformation') not in ('YES', 'NO', DL):
            errors.append(f'PERFORMANCE: invalid economic/transformation outcome {key}')
        try:
            start = datetime.fromisoformat(t0['decision_timestamp']).date()
            end = date.fromisoformat(cp['checkpoint_date'])
            for event in record['events']:
                when = date.fromisoformat(event['date'])
                if event['kind'] not in KINDS or not event.get('source') or not event.get('fact') or not start <= when <= end:
                    errors.append(f'PERFORMANCE: invalid dated event {key}')
            if len({event['kind'] for event in record['events']}) != len(record['events']):
                errors.append(f'PERFORMANCE: duplicate event kind {key}; record first occurrence')
            for action in record['corporate_actions']:
                when = date.fromisoformat(action['date'])
                if not action.get('source') or not action.get('treatment') or not start <= when <= end:
                    errors.append(f'PERFORMANCE: invalid corporate action {key}')
            series = record['return_series']
            if series['status'] == DL:
                if series.get('equity_points') or series.get('benchmark_points') or not series.get('reason'):
                    errors.append(f'PERFORMANCE: invalid missing-series treatment {key}')
                if any(cp[field] != DL for field in ('raw_equity_return', 'benchmark_return', 'benchmark_adjusted_return', 'maximum_drawdown')):
                    errors.append(f'PERFORMANCE: fabricated return/drawdown without series {key}')
            elif series['status'] == 'COMPLETE':
                if not all(series.get(field) for field in ('source', 'coverage', 'currency', 'reinvestment_policy', 'post_delisting_policy')):
                    errors.append(f'PERFORMANCE: missing series provenance/treatment {key}')
                values = []
                for family in ('equity_points', 'benchmark_points'):
                    points = series[family]
                    dates = [date.fromisoformat(point['date']) for point in points]
                    if len(points) < 2 or dates != sorted(set(dates)) or dates[0] < start or dates[-1] != end or any(not number(x['wealth']) or x['wealth'] <= 0 for x in points):
                        errors.append(f'PERFORMANCE: incomplete/invalid {family} {key}')
                        break
                    values.append(points)
                if len(values) == 2:
                    eq, bench = values
                    if eq[0]['date'] != bench[0]['date'] or eq[-1]['date'] != bench[-1]['date']:
                        errors.append(f'PERFORMANCE: unmatched benchmark window {key}')
                    expected = (eq[-1]['wealth']/eq[0]['wealth']-1,
                                bench[-1]['wealth']/bench[0]['wealth']-1,
                                eq[-1]['wealth']/eq[0]['wealth']-bench[-1]['wealth']/bench[0]['wealth'],
                                drawdown(eq))
                    actual = tuple(cp[field] for field in ('raw_equity_return', 'benchmark_return', 'benchmark_adjusted_return', 'maximum_drawdown'))
                    if any(not number(a) or abs(a-b) > 1e-6 for a, b in zip(actual, expected)):
                        errors.append(f'PERFORMANCE: checkpoint return/drawdown mismatch {key}')
            else:
                errors.append(f'PERFORMANCE: invalid series status {key}')
            if not (number(record['cash_return']) or record['cash_return'] == DL):
                errors.append(f'PERFORMANCE: invalid cash comparator {key}')
            if number(record['cash_return']) and not record.get('cash_source'):
                errors.append(f'PERFORMANCE: cash comparator lacks source {key}')
            if number(record['cash_return']) and (series['status'] != 'COMPLETE' or
                                                  record.get('cash_window_start') != series['equity_points'][0]['date'] or
                                                  record.get('cash_window_end') != cp['checkpoint_date']):
                errors.append(f'PERFORMANCE: unmatched cash window {key}')
            comp = record['competing_candidate']
            if comp != DL and (not isinstance(comp, dict) or not comp.get('decision_id') or not comp.get('source') or not number(comp.get('return')) or
                               comp.get('checkpoint_month') != cp['checkpoint_month'] or
                               comp.get('currency') != series.get('currency') or
                               comp.get('window_start') != series.get('equity_points', [{}])[0].get('date') or
                               comp.get('window_end') != cp['checkpoint_date']):
                errors.append(f'PERFORMANCE: invalid competing candidate comparator {key}')
            elif isinstance(comp, dict) and (comp['decision_id'] not in decisions or comp['decision_id'] == ident or
                                             datetime.fromisoformat(decisions[comp['decision_id']]['decision_timestamp']) >
                                             datetime.fromisoformat(t0['decision_timestamp'])):
                errors.append(f'PERFORMANCE: competing candidate unavailable at T0 {key}')
        except (KeyError, ValueError, TypeError, IndexError, ZeroDivisionError) as exc:
            errors.append(f'PERFORMANCE: malformed supplement {key}: {exc}')
    if base_ref:
        folder = HOME / 'performance'
        prior = subprocess.run(['git', 'ls-tree', '-r', '--name-only', base_ref, '--', str(folder)],
                               cwd=root, capture_output=True, check=True, text=True).stdout.splitlines()
        for name in prior:
            old = subprocess.run(['git', 'show', f'{base_ref}:{name}'], cwd=root,
                                 capture_output=True, check=True).stdout
            if not (root / name).is_file() or (root / name).read_bytes() != old:
                errors.append(f'PERFORMANCE: committed supplement replaced/deleted {name}')
    return errors


def scorecards(root=Path('.')):
    errors = validate(root)
    if errors:
        raise ValueError('\n'.join(errors))
    home = Path(root) / HOME
    decisions = {p.stem: json.loads(p.read_text()) for p in (home / 'decisions').glob('*.json')}
    result = []
    for path in sorted((home / 'checkpoints').glob('*.json')):
        cp = json.loads(path.read_text())
        extra = json.loads((home / 'performance' / path.name).read_text())
        t0 = decisions[cp['decision_id']]
        start = datetime.fromisoformat(t0['decision_timestamp']).date()
        events = {event['kind']: event for event in extra['events']}
        def elapsed(kind):
            return (date.fromisoformat(events[kind]['date']) - start).days if kind in events else DL
        raw = cp['raw_equity_return']
        cash = extra['cash_return']
        comp = extra['competing_candidate']
        result.append({
            'decision_id': cp['decision_id'], 'methodology_version': t0['methodology_version'],
            'classification': t0['classification'], 'checkpoint_month': cp['checkpoint_month'],
            'issuer_id': extra['issuer_id'], 'security_id': extra['security_id'],
            'security_lifecycle': extra['security_lifecycle'],
            'raw_return': raw, 'benchmark_return': cp['benchmark_return'],
            'benchmark_adjusted_return': cp['benchmark_adjusted_return'],
            'maximum_drawdown': cp['maximum_drawdown'],
            'days_to_material_evidence': elapsed('MATERIAL_ECONOMIC_EVIDENCE'),
            'days_to_market_recognition': elapsed('MARKET_RECOGNITION'),
            'days_to_thesis_break': elapsed('THESIS_BREAK'),
            'economic_capture': extra['economic_capture'],
            'transformation': extra['transformation'],
            'opportunity_vs_cash': raw-cash if number(raw) and number(cash) else DL,
            'opportunity_vs_benchmark': cp['benchmark_adjusted_return'],
            'opportunity_vs_competing_candidate': raw-comp['return'] if number(raw) and isinstance(comp, dict) else DL,
        })
    return result


def cohort_metrics(cards, *, complete_universe=False, min_n=10):
    """One horizon/version cohort only; never infer recall from a partial universe."""
    if not cards or len({(x['methodology_version'], x['checkpoint_month']) for x in cards}) != 1:
        raise ValueError('one methodology version and checkpoint horizon required')
    known = [x for x in cards if x['economic_capture'] in ('YES', 'NO')]
    promotes = [x for x in known if x['classification'] == 'PROMOTE']
    transformed = [x for x in known if x['transformation'] == 'YES']
    adequate = len(known) == len(cards) and len(known) >= min_n
    return {
        'observations': len(cards), 'known_economic_outcomes': len(known),
        'precision': sum(x['economic_capture'] == 'YES' for x in promotes)/len(promotes)
                     if adequate and len(promotes) >= min_n else DL,
        'recall': sum(x['classification'] == 'PROMOTE' for x in known if x['economic_capture'] == 'YES') /
                  sum(x['economic_capture'] == 'YES' for x in known)
                  if adequate and complete_universe and sum(x['economic_capture'] == 'YES' for x in known) >= min_n else DL,
        'transformation_capture_rate': sum(x['classification'] == 'PROMOTE' for x in transformed)/len(transformed)
                  if adequate and complete_universe and len(transformed) >= min_n else DL,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path('.'))
    args = parser.parse_args()
    print(json.dumps(scorecards(args.root), indent=2))
