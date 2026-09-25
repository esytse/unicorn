import json
import shutil
import tempfile
import unittest
from pathlib import Path

from performance import DL, cohort_metrics, scorecards, validate

SOURCE = Path(__file__).resolve().parents[1]


class PerformanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / 'research/prospective'
        shutil.copytree(SOURCE / 'research/prospective', self.home)
        for name in ('decisions', 'checkpoints', 'performance'):
            (self.home / name).mkdir(exist_ok=True)
        self.ident = 'P-20260925-TEST-001'
        self.t0 = json.loads((self.home / 'T0.template.json').read_text())
        self.t0['decision_id'] = self.ident
        self.t0['candidate_id'] = 'ISSUER-001:OLD-LISTING'
        (self.home / 'decisions' / (self.ident+'.json')).write_text(json.dumps(self.t0))
        self.cp = json.loads((self.home / 'CHECKPOINT.template.json').read_text())
        self.cp.update(decision_id=self.ident, raw_equity_return=.1, benchmark_return=.05,
                       benchmark_adjusted_return=.05, maximum_drawdown=-.25)
        self.cp_path = self.home / 'checkpoints' / (self.ident+'-03.json')
        self.cp_path.write_text(json.dumps(self.cp))
        self.extra = json.loads((self.home / 'PERFORMANCE.template.json').read_text())
        self.extra.update(decision_id=self.ident, issuer_id='ISSUER-001',
                          security_id='ISSUER-001:OLD-LISTING', security_lifecycle='ACQUIRED',
                          corporate_actions=[{'date':'2026-12-15','source':'https://example.org/merger',
                                              'treatment':'cash consideration carried to checkpoint'}],
                          return_series={
                              'status':'COMPLETE', 'source':'https://example.org/total-return',
                              'coverage':'all trading sessions; fixture excerpt is synthetic',
                              'currency':'GBP', 'reinvestment_policy':'dividends reinvested',
                              'post_delisting_policy':'cash proceeds carried',
                              'equity_points':[{'date':d,'wealth':v} for d,v in
                                               [('2026-09-25',1),('2026-10-25',1.2),
                                                ('2026-11-25',.9),('2026-12-25',1.1)]],
                              'benchmark_points':[{'date':d,'wealth':v} for d,v in
                                                  [('2026-09-25',1),('2026-12-25',1.05)]]},
                          cash_return=.01, cash_source='https://example.org/cash-rate',
                          cash_window_start='2026-09-25', cash_window_end='2026-12-25',
                          events=[{'kind':'MATERIAL_ECONOMIC_EVIDENCE','date':'2026-10-25',
                                   'source':'https://example.org/filing','fact':'material profit'},
                                  {'kind':'MARKET_RECOGNITION','date':'2026-11-25',
                                   'source':'https://example.org/price','fact':'predeclared repricing event'}],
                          economic_capture='YES', transformation='YES')
        self.extra_path = self.home / 'performance' / (self.ident+'-03.json')
        self.write()

    def write(self):
        self.cp_path.write_text(json.dumps(self.cp))
        self.extra_path.write_text(json.dumps(self.extra))

    def test_acquisition_returns_drawdown_timing_and_opportunity_cost(self):
        self.assertEqual(validate(self.root), [])
        card, = scorecards(self.root)
        self.assertEqual((card['raw_return'], card['benchmark_adjusted_return'], card['maximum_drawdown']),
                         (.1, .05, -.25))
        self.assertEqual((card['days_to_material_evidence'], card['days_to_market_recognition']), (30, 61))
        self.assertAlmostEqual(card['opportunity_vs_cash'], .09)
        self.assertEqual(card['opportunity_vs_competing_candidate'], DL)
        self.assertEqual(card['security_lifecycle'], 'ACQUIRED')

    def test_data_limited_retains_observation(self):
        for key in ('raw_equity_return','benchmark_return','benchmark_adjusted_return','maximum_drawdown'):
            self.cp[key] = DL
        self.extra['return_series'] = json.loads((self.home / 'PERFORMANCE.template.json').read_text())['return_series']
        self.extra.update(security_lifecycle='DELISTED', cash_return=DL,
                          corporate_actions=[{'date':'2026-12-15','source':'https://example.org/delist',
                                              'treatment':'delisting adjustment unavailable'}])
        self.write()
        self.assertEqual(validate(self.root), [])
        card, = scorecards(self.root)
        self.assertEqual(card['opportunity_vs_cash'], DL)
        self.assertEqual(card['security_lifecycle'], 'DELISTED')

    def test_rejects_fabricated_or_mismatched_returns_and_missing_record(self):
        self.extra['return_series']['equity_points'][2]['wealth'] = .5
        self.write()
        self.assertTrue(any('return/drawdown mismatch' in x for x in validate(self.root)))
        self.extra['return_series']['status'] = DL
        self.extra['return_series']['reason'] = 'missing'
        self.extra['return_series']['equity_points'] = []
        self.extra['return_series']['benchmark_points'] = []
        self.write()
        self.assertTrue(any('fabricated return' in x for x in validate(self.root)))
        self.extra_path.unlink()
        self.assertTrue(any('missing/orphan supplements' in x for x in validate(self.root)))

    def test_cohort_denominators_are_explicit(self):
        card, = scorecards(self.root)
        self.assertEqual(cohort_metrics([card])['precision'], DL)
        cohort = [dict(card, decision_id=f'P-{i}', classification='PROMOTE' if i < 5 else 'REJECT',
                       economic_capture='YES' if i < 5 else 'NO', transformation='YES') for i in range(10)]
        self.assertEqual(cohort_metrics(cohort, complete_universe=True, min_n=5)['precision'], 1)
        self.assertEqual(cohort_metrics(cohort, complete_universe=True, min_n=5)['recall'], 1)
        self.assertEqual(cohort_metrics(cohort, complete_universe=False, min_n=5)['recall'], DL)


if __name__ == '__main__':
    unittest.main()
