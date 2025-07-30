import unittest
from andy.inference.replay import ReplayDecoder

class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.decoder = ReplayDecoder("data/fixtures/continuity.jsonl")

    def test_normalized_match_retains_record_identity(self):
        result = self.decoder.complete("  IDENTIFY   yourself. ")
        self.assertEqual(result.record_id, "c001")
        self.assertEqual(result.source, "replay")

    def test_unknown_input_does_not_generate(self):
        result = self.decoder.complete("unrecorded input")
        self.assertEqual(result.source, "replay-miss")
        self.assertIsNone(result.record_id)
