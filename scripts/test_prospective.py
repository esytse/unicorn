"""Prospective contract, including intentionally invalid records in isolated copies."""
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from prospective import validate

SOURCE = Path(__file__).resolve().parents[1]

class ProspectiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(SOURCE / 'research/prospective', self.root / 'research/prospective')
        shutil.copytree(SOURCE / 'research/backtests/261', self.root / 'research/backtests/261')
        self.home = self.root / 'research/prospective'
        (self.home / 'decisions').mkdir(exist_ok=True)
        (self.home / 'checkpoints').mkdir(exist_ok=True)
        self.record = json.loads((self.home / 'T0.template.json').read_text())
        self.record['decision_id'] = 'P-20260925-TEST-001'
        self.record['candidate_id'] = 'TEST:001'
        self.record['evidence_t0'][0]['source'] = 'https://example.org/dated-primary'
        self.path = self.home / 'decisions/P-20260925-TEST-001.json'
        self.write()

    def write(self):
        self.path.write_text(json.dumps(self.record, indent=2) + '\n')
        (self.home / 'seals.json').write_text(json.dumps({self.record['decision_id']: hashlib.sha256(self.path.read_bytes()).hexdigest()}))

    def assert_bad(self, phrase):
        self.assertTrue(any(phrase in e for e in validate(self.root)), validate(self.root))

    def test_valid_t0_and_checkpoint(self):
        checkpoint = json.loads((self.home / 'CHECKPOINT.template.json').read_text())
        checkpoint['decision_id'] = self.record['decision_id']
        checkpoint['raw_equity_return'] = .12
        checkpoint['benchmark_return'] = .05
        checkpoint['benchmark_adjusted_return'] = .07
        (self.home / 'checkpoints/P-20260925-TEST-001-03.json').write_text(json.dumps(checkpoint))
        self.assertEqual(validate(self.root), [])

    def test_missing_and_invalid_version(self):
        del self.record['scarce_complement']
        self.write()
        self.assert_bad('missing T0 fields')
        self.record['scarce_complement'] = 'test'
        self.record['methodology_version'] = 'v9-unknown'
        self.write()
        self.assert_bad('invalid methodology version')

    def test_duplicate_id_and_mutation(self):
        (self.home / 'decisions/OTHER-ID.json').write_bytes(self.path.read_bytes())
        self.assert_bad('duplicate decision ID')
        (self.home / 'decisions/OTHER-ID.json').unlink()
        self.path.write_text(self.path.read_text() + ' ')
        self.assert_bad('T0 seal mismatch')

    def test_orphan_early_and_invalid_returns(self):
        checkpoint = json.loads((self.home / 'CHECKPOINT.template.json').read_text())
        checkpoint['decision_id'] = 'P-UNKNOWN-001'
        p = self.home / 'checkpoints/P-UNKNOWN-001-03.json'
        p.write_text(json.dumps(checkpoint))
        self.assert_bad('orphan checkpoint')
        p.unlink()
        checkpoint['decision_id'] = self.record['decision_id']
        checkpoint['checkpoint_date'] = '2026-12-24'
        p = self.home / 'checkpoints/P-20260925-TEST-001-03.json'
        p.write_text(json.dumps(checkpoint))
        self.assert_bad('before scheduled date')
        checkpoint['checkpoint_date'] = '2026-12-25'
        checkpoint['benchmark_adjusted_return'] = .2
        p.write_text(json.dumps(checkpoint))
        self.assert_bad('returns must be numeric or all DATA-LIMITED')

    def test_future_evidence_and_schedule(self):
        self.record['evidence_t0'][0]['published_at'] = '2026-09-26'
        self.record['checkpoint_dates']['3'] = '2026-12-24'
        self.write()
        self.assert_bad('published after T0')
        self.assert_bad('checkpoint schedule differs')

if __name__ == '__main__':
    unittest.main()
