#!/usr/bin/env python3
"""Positive and deliberately failing tests for objective ranking governance."""
import shutil
import tempfile
import unittest
from pathlib import Path

from objective_ranking import validate

SOURCE = Path(__file__).resolve().parents[1]


class ObjectiveRankingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'research').mkdir()
        shutil.copy2(SOURCE / 'research/ranked-universe.md', self.root / 'research/ranked-universe.md')

    def replace(self, old, new):
        path = self.root / 'research/ranked-universe.md'
        path.write_text(path.read_text().replace(old, new))

    def assert_detects(self, fragment):
        problems = validate(self.root)
        self.assertTrue(any(fragment in problem for problem in problems), problems)

    def test_current_ranking_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_duplicate_company_is_detected(self):
        self.replace('**Danaher**', '**Thermo Fisher Scientific**')
        self.assert_detects('companies must appear exactly once')

    def test_broken_capital_order_is_detected(self):
        self.replace('| **1** | **10** | **Impro Precision Industries**', '| **60** | **10** | **Impro Precision Industries**')
        self.assert_detects('capital ranks must be ordered and continuous')

    def test_monitor_state_drift_is_detected(self):
        self.replace('| REASSESS | Thermal revenue attribution', '| WAIT | Thermal revenue attribution')
        self.assert_detects('Impro Precision Industries state must be REASSESS')

    def test_historical_action_cannot_be_reactivated(self):
        self.replace('| REASSESS | Thermal revenue attribution', '| ACTION | Thermal revenue attribution')
        self.assert_detects('ACTION set disagrees with canonical monitors')

    def test_axis_boundary_is_required(self):
        self.replace('March-2028 capital priority', 'capital list')
        self.assert_detects('missing authority/boundary text')


if __name__ == '__main__':
    unittest.main()
