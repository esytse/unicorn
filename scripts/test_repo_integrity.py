#!/usr/bin/env python3
"""Positive baseline plus isolated deliberate corruptions, never applied to the checkout."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from repo_integrity import check, check_issue_contract

SOURCE = Path(__file__).resolve().parents[1]

class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for folder in ('research', 'docs', 'sources', 'scripts'):
            if (SOURCE / folder).exists():
                shutil.copytree(SOURCE / folder, self.root / folder,
                                ignore=shutil.ignore_patterns('__pycache__', 'fixtures'))
        for file in SOURCE.glob('*.md'):
            shutil.copy2(file, self.root / file.name)
        (self.root / '.github').mkdir()
        shutil.copy2(SOURCE / '.github/pull_request_template.md', self.root / '.github/pull_request_template.md')

    def append(self, path, text):
        target = self.root / path
        target.write_text(target.read_text() + text)

    def assert_detects(self, code):
        problems = check(self.root)
        self.assertTrue(any(p.startswith(code + ':') for p in problems), problems)

    def test_current_repository_passes(self):
        self.assertEqual(check(self.root), [])

    def test_broken_link(self):
        self.append('README.md', '\n[missing](docs/moved.md)\n')
        self.assert_detects('LINK')

    def test_missing_canonical_and_duplicate_authority(self):
        self.append('docs/REPOSITORY_GOVERNANCE.md', '\n| Portfolio mandate / Gate-E operating rules | `docs/moved.md` | none | live canonical |\n')
        self.assert_detects('AUTHORITY')

    def test_missing_freshness(self):
        path = self.root / 'docs/DOCUMENTATION_AUDIT.md'
        path.write_text(path.read_text().replace('**As of:** 2026-09-25', '**As of:** unknown'))
        self.assert_detects('FRESHNESS')

    def test_invalid_lifecycle_and_derived_contract(self):
        self.append('README.md', '\n**Lifecycle:** CURRENT\n')
        self.assert_detects('METADATA')
        path = self.root / 'README.md'
        path.write_text(path.read_text().replace('**Lifecycle:** CURRENT', '**Lifecycle:** DERIVED'))
        self.assert_detects('METADATA')

    def test_derived_cannot_claim_canonical(self):
        self.append('README.md', '\n**Lifecycle:** DERIVED\n**Canonical upstream:** `PORTFOLIO.md`\n**Authority:** CANONICAL\n**Concept:** bad\n')
        self.assert_detects('METADATA')

    def test_invalid_supersession(self):
        self.append('docs/DOCUMENTATION_AUDIT.md', '\n**Superseded-by:** `docs/absent.md`\n')
        self.assert_detects('LIFECYCLE')

    def test_derived_missing_upstream(self):
        self.append('watchlist.md', '\n**Canonical upstream:** `research/moved.md`\n')
        self.assert_detects('LIFECYCLE')

    def test_derived_stale_digest(self):
        self.append('watchlist.md', '\n**Canonical upstream:** `PORTFOLIO.md`\n**Upstream SHA-256:** `' + '0'*64 + '`\n')
        self.assert_detects('DERIVED')

    def test_duplicate_mutable_ranking(self):
        self.append('docs/REPOSITORY_GOVERNANCE.md', '\n| Live ranked research universe | `watchlist.md` | none | live canonical |\n')
        self.assert_detects('AUTHORITY')

    def test_portfolio_reference(self):
        path = self.root / 'PORTFOLIO.md'
        path.write_text(path.read_text().replace('research/ranked-universe.md', 'research/moved-ranking.md'))
        self.assert_detects('RANKING')

    def test_frozen_record(self):
        self.append('research/backtests/261/SUMMARY.md', '\nmodified\n')
        self.assert_detects('FROZEN')

    def test_duplicate_prediction_key(self):
        path = self.root / 'research/backtests/261/PREDICTIONS.md'
        row = next(x for x in path.read_text().splitlines() if x.startswith('| D01 |'))
        self.append('research/backtests/261/PREDICTIONS.md', '\n' + row + '\n')
        self.assert_detects('KEY')

    def test_outcome_unknown_case(self):
        self.append('research/backtests/261/OUTCOMES.md', '\n| D99 | Candidate | unknown | unknown | unknown | unknown | unknown | unknown | 2026-09-25 |\n')
        self.assert_detects('KEY')

    def test_issue_state_and_dependency(self):
        valid = dict(State='READY', Priority='P1', Type='TESTING', Trigger='NONE',
                     Parent='NONE', Dependencies='NONE', **{'Next action': 'run', 'Completion gate': 'green'})
        self.assertEqual(check_issue_contract(valid), [])
        broken = dict(valid, State='READY', Dependencies='#100')
        self.assertIn('ISSUE: READY has unresolved Dependencies', check_issue_contract(broken))
        broken['State'] = 'WAITING'
        broken['Trigger'] = 'NONE'
        self.assertIn('ISSUE: WAITING needs an explicit Trigger', check_issue_contract(broken))
        (self.root / 'scripts/issue-state.json').write_text(json.dumps([dict(broken, number=101)]))
        self.assertTrue(any('ISSUE:' in p for p in check(self.root)))

if __name__ == '__main__':
    unittest.main()
