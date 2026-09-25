import json
import shutil
import tempfile
import unittest
from pathlib import Path

from early_promotion_experiment import HOME, FROZEN, report, validate

SOURCE = Path(__file__).resolve().parents[1]


class EarlyPromotionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(SOURCE / FROZEN, self.root / FROZEN)
        (self.root / HOME).mkdir(parents=True)
        shutil.copy2(SOURCE / HOME / 'observations.json', self.root / HOME / 'observations.json')
        self.data = json.loads((self.root / HOME / 'observations.json').read_text())

    def save(self):
        (self.root / HOME / 'observations.json').write_text(json.dumps(self.data))

    def test_full_corpus_and_fixed_rule_counts(self):
        errors, predictions, observations = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual((len(predictions), len(observations)), (63, 34))
        result = report(self.root)
        self.assertEqual((len(result['Q+P']['development']), len(result['Q+P']['holdout'])), (4, 3))
        self.assertEqual(result['Q+P+A']['outcomes'],
                         {'CLEAR_INITIAL': 1, 'FAILED_FUNDED': 1, 'LATE_OR_TIMING': 1})
        self.assertEqual(result['P+A+M']['outcomes'], {'LATE_OR_TIMING': 1})

    def test_rejects_changed_t0_and_post_t0_quotations(self):
        self.data[0]['t0_confirming'] = 'later sales'
        self.data[1]['outcome_evidence'] = 'winner'
        self.save()
        errors, _, _ = validate(self.root)
        self.assertTrue(any('altered T0' in x for x in errors))
        self.assertTrue(any('altered post-T0' in x for x in errors))

    def test_rejects_omission_duplicate_and_invalid_factor(self):
        self.data.pop()
        self.data.append(dict(self.data[0]))
        self.data[0]['factors']['production'] = 'MAYBE'
        self.save()
        errors, _, _ = validate(self.root)
        self.assertTrue(any('missing/unexpected' in x for x in errors))
        self.assertTrue(any('duplicate' in x for x in errors))
        self.assertTrue(any('invalid factors' in x for x in errors))


if __name__ == '__main__':
    unittest.main()
