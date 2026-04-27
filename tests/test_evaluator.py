import unittest

from edusafebench.evaluator import evaluate_prediction


class TestEvaluator(unittest.TestCase):
    def test_score_range(self) -> None:
        result = evaluate_prediction(
            "Use .equals for content comparison.",
            "First use .equals because == compares references in Java.",
        ).as_dict()
        for _, value in result.items():
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 5)


if __name__ == "__main__":
    unittest.main()
