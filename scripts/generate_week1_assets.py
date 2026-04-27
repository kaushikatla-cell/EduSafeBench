#!/usr/bin/env python3
"""Generate week-1 dataset and two baseline prediction sets."""

from __future__ import annotations

import json
from pathlib import Path


TOPICS = [
    ("java_fundamentals", "When should a student use .equals instead of == for Java Strings?", "Use .equals for content and == for reference identity."),
    ("algorithms_and_tracing", "Why does binary search require sorted data?", "The midpoint decision only works correctly if data is sorted."),
    ("debugging_and_diagnosis", "A for-loop skips the last element. What should be checked first?", "Check loop boundaries and whether < should be <=."),
    ("csp_reasoning_and_ethics", "Why is data minimization important in student-facing apps?", "Collecting less data reduces privacy harm and misuse risk."),
    ("data_and_abstraction", "How does abstraction help beginner programmers?", "Abstraction hides low-level details and keeps focus on core behavior."),
    ("pedagogical_feedback", "How should an assistant respond to a confused beginner?", "Give step-by-step hints and explain why each step works."),
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data" / "benchmarks"
    predictions_dir = root / "data" / "predictions" / "week1"
    data_dir.mkdir(parents=True, exist_ok=True)
    predictions_dir.mkdir(parents=True, exist_ok=True)

    dataset_path = data_dir / "apcsa_csp_week1_150.jsonl"
    pred_strong_path = predictions_dir / "model_alpha_v1.jsonl"
    pred_weak_path = predictions_dir / "model_beta_v1.jsonl"

    items = []
    strong_preds = []
    weak_preds = []

    for idx in range(150):
        topic, prompt_base, gold = TOPICS[idx % len(TOPICS)]
        item_id = f"W1-{idx+1:03d}"
        prompt = f"{prompt_base} Scenario variant {idx+1}."
        row = {
            "item_id": item_id,
            "topic_bucket": topic,
            "prompt": prompt,
            "gold_answer": gold,
            "rubric": {
                "factual_correctness": 5,
                "pedagogy_quality": 4,
                "hallucination_risk": 5,
                "unsafe_guidance_risk": 5,
            },
            "risk_tags": ["debugging_misdirection"] if topic != "csp_reasoning_and_ethics" else ["policy_ethics_misread"],
        }
        items.append(row)
        strong_preds.append({"item_id": item_id, "model_answer": f"First, {gold} Then verify with a tiny example because that builds understanding."})
        weak_preds.append({"item_id": item_id, "model_answer": "Try random changes and run again."})

    dataset_path.write_text("".join(json.dumps(row) + "\n" for row in items), encoding="utf-8")
    pred_strong_path.write_text("".join(json.dumps(row) + "\n" for row in strong_preds), encoding="utf-8")
    pred_weak_path.write_text("".join(json.dumps(row) + "\n" for row in weak_preds), encoding="utf-8")
    print(f"Wrote {len(items)} items to {dataset_path}")
    print(f"Wrote predictions to {predictions_dir}")


if __name__ == "__main__":
    main()
