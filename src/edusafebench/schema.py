"""Schema helpers for benchmark records."""

from dataclasses import dataclass
from typing import Dict, List

from .taxonomy import RELIABILITY_DIMENSIONS, TOPIC_BUCKETS


@dataclass
class BenchmarkItem:
    item_id: str
    topic_bucket: str
    prompt: str
    gold_answer: str
    rubric: Dict[str, int]
    risk_tags: List[str]

    def validate(self) -> None:
        if self.topic_bucket not in TOPIC_BUCKETS:
            raise ValueError(f"Unknown topic bucket: {self.topic_bucket}")
        missing_dims = [d for d in RELIABILITY_DIMENSIONS if d not in self.rubric]
        if missing_dims:
            raise ValueError(f"Missing rubric dimensions: {missing_dims}")
        for key in RELIABILITY_DIMENSIONS:
            score = self.rubric[key]
            if not isinstance(score, int) or score < 1 or score > 5:
                raise ValueError(f"Rubric score for {key} must be integer in [1, 5]")
