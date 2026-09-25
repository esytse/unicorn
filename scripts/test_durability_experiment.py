import json
import shutil
import tempfile
import unittest
from pathlib import Path
from durability_experiment import validate, PROBES, FROZEN

SOURCE = Path(__file__).resolve().parents[1]

class DurabilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / PROBES).parent.mkdir(parents=True)
        shutil.copy2(SOURCE / PROBES, self.root / PROBES)
        shutil.copytree(SOURCE / FROZEN, self.root / FROZEN)
        self.probes = json.loads((self.root / PROBES).read_text())

    def write(self):
        (self.root / PROBES).write_text(json.dumps(self.probes))

    def test_full_frozen_join_and_probes(self):
        errors, predictions, probes = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual((len(predictions), len(probes)), (63, 30))

    def test_rejects_post_t0_hindsight_and_wrong_outcome(self):
        self.probes[0]['t0_evidence'] = '2024 hindsight'
        self.probes[1]['outcome_evidence'] = 'winner'
        self.write()
        errors, _, _ = validate(self.root)
        self.assertTrue(any('post-T0' in x for x in errors))
        self.assertTrue(any('mismatched outcome' in x for x in errors))

    def test_rejects_missing_case_and_duplicate(self):
        self.probes = [x for x in self.probes if x['case'] != 'H05']
        self.probes.append(dict(self.probes[0]))
        self.write()
        errors, _, _ = validate(self.root)
        self.assertTrue(any('duplicate probe' in x for x in errors))
        self.assertTrue(any('lacks one' in x for x in errors))

if __name__ == '__main__':
    unittest.main()
