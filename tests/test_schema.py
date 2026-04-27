import unittest

from edusafebench.schema import BenchmarkItem


class TestSchema(unittest.TestCase):
    def test_valid_item_passes(self) -> None:
        item = BenchmarkItem(
            item_id="x",
            topic_bucket="java_fundamentals",
            prompt="p",
            gold_answer="g",
            rubric={
                "factual_correctness": 5,
                "pedagogy_quality": 4,
                "hallucination_risk": 5,
                "unsafe_guidance_risk": 5,
            },
            risk_tags=["off_by_one_logic"],
            citations=["https://apstudents.collegeboard.org/courses/ap-computer-science-a"],
        )
        item.validate()

    def test_invalid_score_fails(self) -> None:
        item = BenchmarkItem(
            item_id="x",
            topic_bucket="java_fundamentals",
            prompt="p",
            gold_answer="g",
            rubric={
                "factual_correctness": 6,
                "pedagogy_quality": 4,
                "hallucination_risk": 5,
                "unsafe_guidance_risk": 5,
            },
            risk_tags=[],
            citations=["https://apstudents.collegeboard.org/courses/ap-computer-science-a"],
        )
        with self.assertRaises(ValueError):
            item.validate()

    def test_missing_citations_fails(self) -> None:
        item = BenchmarkItem(
            item_id="x",
            topic_bucket="java_fundamentals",
            prompt="p",
            gold_answer="g",
            rubric={
                "factual_correctness": 5,
                "pedagogy_quality": 4,
                "hallucination_risk": 5,
                "unsafe_guidance_risk": 5,
            },
            risk_tags=[],
            citations=[],
        )
        with self.assertRaises(ValueError):
            item.validate()


if __name__ == "__main__":
    unittest.main()
