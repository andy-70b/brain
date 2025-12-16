import unittest
from andy.evaluation.runner import evaluate

class EvaluationTests(unittest.TestCase):
    def test_continuity_suite(self):
        result = evaluate("evals/suites/continuity.json")
        self.assertTrue(result["passed"])
        self.assertEqual(result["mode"], "replay-contract")

    def test_boundary_suite(self):
        self.assertTrue(evaluate("evals/suites/boundary.json")["passed"])
