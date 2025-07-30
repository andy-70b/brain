import unittest
from andy.memory.ledger import Evidence, Ledger
from andy.memory.retrieval import retrieve

class MemoryTests(unittest.TestCase):
    def test_quarantine_never_reaches_retrieval(self):
        ledger = Ledger()
        ledger.append(Evidence("a", "archive", "the room remembers", "quarantined"))
        ledger.append(Evidence("b", "archive", "the room", "admitted"))
        self.assertEqual([e.id for e in retrieve(ledger, "room remembers")], ["b"])

    def test_duplicate_identity_cannot_overwrite(self):
        ledger = Ledger()
        ledger.append(Evidence("a", "archive", "first"))
        with self.assertRaises(ValueError):
            ledger.append(Evidence("a", "archive", "second"))

    def test_no_overlap_returns_empty(self):
        ledger = Ledger()
        ledger.append(Evidence("a", "archive", "room", "admitted"))
        self.assertEqual(retrieve(ledger, "outside"), ())

    def test_negative_limit_rejected(self):
        with self.assertRaises(ValueError):
            retrieve(Ledger(), "room", -1)
