"""Prospective decision contract. No external dependencies or market-data lookups."""
import calendar
import hashlib
import json
import re
import subprocess
from datetime import datetime, date
from pathlib import Path

HOME = Path('research/prospective')
MONTHS = (3, 6, 12, 18)
T0_FIELDS = ('decision_id', 'methodology_version', 'decision_timestamp', 'candidate_id',
             'discovery_source', 'architecture_change', 'scarce_complement',
             'bottleneck_migration', 'company_capture', 'financial_materiality',
             'shareholder_capture', 'classification', 'confidence', 'evidence_t0',
             'missing_evidence', 'price_valuation', 'catalysts', 'thesis_breakers',
             'inclusion_rationale', 'benchmark_id', 'checkpoint_dates')
OUTCOME_FIELDS = ('decision_id', 'checkpoint_month', 'checkpoint_date', 'raw_equity_return',
                  'benchmark_return', 'benchmark_adjusted_return', 'maximum_drawdown',
                  'new_evidence', 'catalyst_outcome', 'architecture_outcome',
                  'company_capture_outcome', 'financial_conversion_outcome',
                  'shareholder_capture_outcome', 'thesis_break_evidence', 'lesson')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def month_after(day, n):
    year, month = divmod(day.year * 12 + day.month - 1 + n, 12)
    return date(year, month + 1, min(day.day, calendar.monthrange(year, month + 1)[1]))


def _date(value):
    return date.fromisoformat(value)


def validate(root, base_ref=None):
    root = Path(root)
    home = root / HOME
    errors = []
    def fail(message):
        errors.append('PROSPECTIVE: ' + message)
    try:
        versions = json.loads((home / 'versions.json').read_text())
        seal = json.loads((home / 'seals.json').read_text())
    except (OSError, ValueError) as exc:
        return [f'PROSPECTIVE: missing/invalid registry: {exc}']
    if not isinstance(versions, dict) or 'v1-261-frozen-2026-09-25' not in versions:
        fail('missing historical v1 version')
        versions = {}
    for key, version in versions.items():
        if not re.fullmatch(r'v\d+-[a-z0-9-]+', key) or not isinstance(version, dict):
            fail(f'invalid methodology version {key}')
        elif not version.get('protocol') or not (root / version['protocol']).is_file():
            fail(f'{key}: missing protocol')
    if not isinstance(seal, dict):
        return errors + ['PROSPECTIVE: seals must be an object']
    decisions = {}
    for path in sorted((home / 'decisions').glob('*.json')):
        try:
            raw = path.read_bytes()
            obj = json.loads(raw)
        except (OSError, ValueError) as exc:
            fail(f'{path.name}: invalid JSON: {exc}')
            continue
        ident = obj.get('decision_id')
        if ident in decisions:
            fail(f'duplicate decision ID {ident}')
        decisions[ident] = obj
        if path.stem != ident or not re.fullmatch(r'[A-Z0-9][A-Z0-9-]{5,79}', str(ident)):
            fail(f'{path.name}: invalid decision ID/filename')
        missing = [field for field in T0_FIELDS if field not in obj or obj[field] in ('', None, [])]
        if missing:
            fail(f'{ident}: missing T0 fields {missing}')
            continue
        if obj['methodology_version'] not in versions:
            fail(f'{ident}: invalid methodology version')
        if obj['classification'] not in ('PROMOTE', 'EVIDENCE-BUILD', 'REJECT') or obj['confidence'] not in ('Low', 'Medium', 'High'):
            fail(f'{ident}: invalid classification/confidence')
        try:
            stamp = datetime.fromisoformat(obj['decision_timestamp'])
            if stamp.tzinfo is None:
                raise ValueError('timezone required')
            expected = {str(n): month_after(stamp.date(), n).isoformat() for n in MONTHS}
            if obj['checkpoint_dates'] != expected:
                fail(f'{ident}: checkpoint schedule differs from T0 + 3/6/12/18 calendar months')
            for evidence in obj['evidence_t0']:
                if not isinstance(evidence, dict) or not evidence.get('source') or not evidence.get('fact') or _date(evidence['published_at']) > stamp.date():
                    fail(f'{ident}: evidence missing provenance or published after T0')
        except (TypeError, ValueError, OverflowError) as exc:
            fail(f'{ident}: invalid timestamp/checkpoint dates: {exc}')
        if seal.get(ident) != digest(raw):
            fail(f'{ident}: T0 seal mismatch')
    for ident in seal.keys() - decisions.keys():
        fail(f'{ident}: seal without T0')
    seen = set()
    observed_dates = {}
    for path in sorted((home / 'checkpoints').glob('*.json')):
        try:
            obj = json.loads(path.read_text())
        except (OSError, ValueError) as exc:
            fail(f'{path.name}: invalid JSON: {exc}')
            continue
        missing = [field for field in OUTCOME_FIELDS if field not in obj or obj[field] is None]
        if missing:
            fail(f'{path.name}: missing outcome fields {missing}')
            continue
        ident, n = obj['decision_id'], obj['checkpoint_month']
        if ident not in decisions:
            fail(f'{path.name}: orphan checkpoint {ident}')
            continue
        if n not in MONTHS or path.stem != f'{ident}-{n:02d}':
            fail(f'{path.name}: malformed checkpoint relationship')
            continue
        if (ident, n) in seen:
            fail(f'{path.name}: duplicate checkpoint')
        seen.add((ident, n))
        try:
            scheduled = _date(decisions[ident]['checkpoint_dates'][str(n)])
            observed = _date(obj['checkpoint_date'])
            if observed < scheduled:
                fail(f'{path.name}: checkpoint before scheduled date')
            observed_dates[(ident, n)] = observed
            values = (obj['raw_equity_return'], obj['benchmark_return'], obj['benchmark_adjusted_return'])
            if all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in values):
                if abs(values[0] - values[1] - values[2]) > 1e-8:
                    fail(f'{path.name}: benchmark-adjusted return inconsistent')
            elif not all(v == 'DATA-LIMITED' for v in values):
                fail(f'{path.name}: returns must be numeric or all DATA-LIMITED')
        except (ValueError, KeyError, TypeError) as exc:
            fail(f'{path.name}: invalid date/returns: {exc}')
    for (ident, n), observed in observed_dates.items():
        if any(other < n and earlier > observed for (key, other), earlier in observed_dates.items() if key == ident):
            fail(f'{ident}-{n:02d}: invalid checkpoint ordering')
    # A seal alone cannot protect against replacing both record and seal. CI compares
    # existing committed records to the PR base; new files are append-only thereafter.
    if base_ref:
        prior = subprocess.run(['git', 'ls-tree', '-r', '--name-only', base_ref, '--', str(HOME / 'decisions'), str(HOME / 'checkpoints')],
                               cwd=root, capture_output=True, check=True, text=True).stdout.splitlines()
        for name in prior:
            if not (root / name).is_file():
                fail(f'committed record deleted: {name}')
        for relative in [*sorted((HOME / 'decisions').glob('*.json')),
                         *sorted((HOME / 'checkpoints').glob('*.json'))]:
            relative = Path(relative)
            if relative.is_absolute():
                relative = relative.relative_to(root)
            try:
                old = subprocess.run(['git', 'show', f'{base_ref}:{relative.as_posix()}'], cwd=root,
                                     capture_output=True, check=True).stdout
            except subprocess.CalledProcessError:
                continue  # New record on this branch.
            current = root / relative
            if not current.is_file() or current.read_bytes() != old:
                fail(f'committed record replaced: {relative}')
        for registry in ('versions.json', 'seals.json'):
            try:
                old = json.loads(subprocess.run(['git', 'show', f'{base_ref}:{(HOME / registry).as_posix()}'],
                                                cwd=root, capture_output=True, check=True).stdout)
                new = json.loads((home / registry).read_text())
                if any(key not in new or new[key] != value for key, value in old.items()):
                    fail(f'committed registry entries replaced: {registry}')
            except subprocess.CalledProcessError:
                pass
    return errors
