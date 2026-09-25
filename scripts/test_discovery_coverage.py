import json
import shutil
import tempfile
import unittest
from pathlib import Path

from discovery_coverage import LEDGER, RANKING, validate

SOURCE = Path(__file__).resolve().parents[1]


class DiscoveryCoverageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(SOURCE / 'research', self.root / 'research')
        (self.root / 'scripts').mkdir()
        self.path = self.root / LEDGER
        self.data = json.loads(self.path.read_text())

    def write(self):
        self.path.write_text(json.dumps(self.data))

    def test_current_ledger_and_search_outcome_distinctions(self):
        errors, data = validate(self.root)
        self.assertEqual(errors, [])
        results = {row['search_result'] for row in data['lanes']}
        self.assertEqual(results, set(data['allowed_results']))
        self.assertGreaterEqual(len(data['lanes']), 12)

    def test_rejects_missing_source_and_contradictory_no_capture(self):
        lane = next(x for x in self.data['lanes'] if x['search_result'] == 'NO_CREDIBLE_LISTED_CAPTURE')
        lane['active_listed_examples'] = ['hindsight winner']
        lane['sources'] = ['research/missing.md']
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any('missing/non-research source' in x for x in errors))
        self.assertTrue(any('no-capture/excluded result has active' in x for x in errors))

    def test_rejects_rejected_state_without_evidence_or_rescan(self):
        lane = next(x for x in self.data['lanes'] if x['search_result'] == 'CANDIDATES_FOUND_BUT_REJECTED')
        lane['rejected_or_parked_examples'] = []
        lane['rescan_triggers'] = []
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any('rejected result lacks' in x for x in errors))
        self.assertTrue(any('empty rescan_triggers' in x for x in errors))

    def test_rejects_familiarity_partition_drift(self):
        self.data['familiarity_audit']['buckets']['memory_data_movement'].pop()
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any('does not partition ranked top' in x for x in errors))


if __name__ == '__main__':
    unittest.main()
