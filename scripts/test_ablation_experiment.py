import json
import shutil
import tempfile
import unittest
from pathlib import Path

from ablation_experiment import validate_experiment
from early_promotion_experiment import HOME, FROZEN

SOURCE = Path(__file__).resolve().parents[1]


class AblationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(SOURCE / FROZEN, self.root / FROZEN)
        (self.root / HOME).mkdir(parents=True)
        shutil.copy2(SOURCE / HOME / 'observations.json', self.root / HOME / 'observations.json')

    def test_ablation_and_single_case_dependence(self):
        errors, result = validate_experiment(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(result['without Q'], result['Q+P'])
        self.assertEqual(result['without P']['outcomes']['FAILED_FUNDED'], 2)
        self.assertEqual(result['Q+P+V+D']['holdout'], ['H04 SK hynix'])
        self.assertEqual(result['Q+P+A+M+V+D']['holdout'], [])
        self.assertEqual(result['leave_one_case_out']['H04']['Q+P+V+D'], [])
        self.assertEqual(result['mix_boundary']['30'], ['D01 Oclaro', 'D01 NeoPhotonics'])
        self.assertEqual(result['mix_boundary']['50'], ['D01 NeoPhotonics'])

    def test_durability_warning_must_stay_t0_quote(self):
        path = self.root / HOME / 'observations.json'
        data = json.loads(path.read_text())
        pacbio = next(x for x in data if x['candidate'] == 'Pacific Biosciences')
        pacbio['t0_disconfirming'] = 'no risk'
        path.write_text(json.dumps(data))
        errors, _ = validate_experiment(self.root)
        self.assertTrue(any('altered T0 quotation' in x for x in errors))


if __name__ == '__main__':
    unittest.main()
