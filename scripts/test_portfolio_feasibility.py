#!/usr/bin/env python3
"""Positive and deliberately failing tests for #357 portfolio feasibility."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from portfolio_feasibility import validate

SOURCE = Path(__file__).resolve().parents[1]


class PortfolioFeasibilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'research').mkdir()
        for name in ('portfolio-feasibility-2028.json', 'portfolio-feasibility-2028.md'):
            shutil.copy2(SOURCE / 'research' / name, self.root / 'research' / name)

    def mutate(self, fn):
        path = self.root / 'research/portfolio-feasibility-2028.json'
        data = json.loads(path.read_text())
        fn(data)
        path.write_text(json.dumps(data))

    def assert_detects(self, fragment):
        problems = validate(self.root)
        self.assertTrue(any(fragment in problem for problem in problems), problems)

    def test_current_model_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_weight_and_cash_error_is_detected(self):
        self.mutate(lambda data: data['portfolios'][1].update(cash_pct=45))
        self.assert_detects('weights plus cash must equal 100')

    def test_ceiling_breach_is_detected(self):
        self.mutate(lambda data: data['portfolios'][2]['positions'][0].update(staged_weight_pct=9))
        self.assert_detects('exceeds ceiling')

    def test_contribution_error_is_detected(self):
        self.mutate(lambda data: data['portfolios'][0]['scenario_values_gbp'].update(base=99999))
        self.assert_detects('base value')

    def test_transaction_rule_gap_is_detected(self):
        self.mutate(lambda data: data['candidates']['Modine'].update(sell=''))
        self.assert_detects('missing entry/add/trim/sell/thesis-break rule')

    def test_hurdle_classification_error_is_detected(self):
        self.mutate(lambda data: data['hurdles'][0].update(classification='LIKELY'))
        self.assert_detects('invalid hurdle classification')

    def test_two_failure_stress_error_is_detected(self):
        self.mutate(lambda data: data['portfolios'][2]['two_failure_stress'].update(value_gbp=80000))
        self.assert_detects('two-failure value does not reconcile')


if __name__ == '__main__':
    unittest.main()
