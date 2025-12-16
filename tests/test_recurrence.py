import unittest
from andy.evaluation.recurrence import repeated_ngrams

class RecurrenceTests(unittest.TestCase):
    def test_counts_distinct_records_not_repetitions_within_record(self):
        self.assertEqual(repeated_ngrams(["the room the room"], 2), {})
        self.assertEqual(repeated_ngrams(["the room the room", "the room"], 2), {"the room": 2})

    def test_invalid_width_rejected(self):
        with self.assertRaises(ValueError):
            repeated_ngrams(["room"], 0)
