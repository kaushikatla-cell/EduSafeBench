import json
import tempfile
import unittest
from pathlib import Path

from edusafebench.runner import run_multi_benchmark


class TestMultiRunner(unittest.TestCase):
    def test_multi_model_leaderboard(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            dataset_path = Path(tmpdir) / "dataset.jsonl"
            pred_a_path = Path(tmpdir) / "model_a.jsonl"
            pred_b_path = Path(tmpdir) / "model_b.jsonl"
            output_path = Path(tmpdir) / "out.json"

            dataset_path.write_text(
                '{"item_id":"X1","topic_bucket":"java_fundamentals","prompt":"p","gold_answer":"Use equals for content.","rubric":{"factual_correctness":5,"pedagogy_quality":4,"hallucination_risk":5,"unsafe_guidance_risk":5},"risk_tags":["debugging_misdirection"],"citations":["https://apstudents.collegeboard.org/courses/ap-computer-science-a"]}\n',
                encoding="utf-8",
            )
            pred_a_path.write_text('{"item_id":"X1","model_answer":"Use equals for content because == compares references."}\n', encoding="utf-8")
            pred_b_path.write_text('{"item_id":"X1","model_answer":"Unknown answer."}\n', encoding="utf-8")

            result = run_multi_benchmark(str(dataset_path), [str(pred_a_path), str(pred_b_path)], str(output_path))
            self.assertEqual(result["models_evaluated"], 2)
            self.assertEqual(len(result["leaderboard"]), 2)
            self.assertGreaterEqual(
                result["leaderboard"][0]["aggregate_scores"]["factual_correctness"],
                result["leaderboard"][1]["aggregate_scores"]["factual_correctness"],
            )
            loaded = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(loaded["models_evaluated"], 2)


if __name__ == "__main__":
    unittest.main()
