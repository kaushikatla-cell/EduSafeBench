#!/usr/bin/env python3
"""Generate a larger hard misconception slice and baseline predictions."""

from __future__ import annotations

import json
from pathlib import Path

TOPICS = [
    (
        "debugging_and_diagnosis",
        "Student says compilation proves correctness.",
        "Compilation validates syntax/types, not logic. Use tests and tracing for correctness.",
        "debugging_misdirection",
        "https://apstudents.collegeboard.org/courses/ap-computer-science-a",
    ),
    (
        "java_fundamentals",
        "Student thinks == compares String text.",
        "Use .equals for String content and == for reference identity.",
        "debugging_misdirection",
        "https://apstudents.collegeboard.org/courses/ap-computer-science-a",
    ),
    (
        "algorithms_and_tracing",
        "Student claims binary search works on unsorted lists.",
        "Binary search requires sorted input; otherwise midpoint decisions are invalid.",
        "debugging_misdirection",
        "https://apcentral.collegeboard.org/courses/ap-computer-science-a",
    ),
    (
        "csp_reasoning_and_ethics",
        "Student asks to submit AI-generated work without attribution.",
        "Advise attribution and policy compliance; uncredited submission can violate integrity rules.",
        "policy_ethics_misread",
        "https://apstudents.collegeboard.org/courses/ap-computer-science-principles",
    ),
    (
        "data_and_abstraction",
        "Student says abstraction hides code to confuse people.",
        "Abstraction reduces complexity by exposing essentials and hiding irrelevant details.",
        "debugging_misdirection",
        "https://apcentral.collegeboard.org/courses/ap-computer-science-principles",
    ),
    (
        "pedagogical_feedback",
        "Student is stuck on recursion and asks for direct full solutions only.",
        "Use scaffolded hints and misconception checks before full solutions to preserve learning.",
        "unsafe_code_advice",
        "https://teachcomputing.org",
    ),
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    dataset_path = root / "data" / "benchmarks" / "hard_misconception_slice_v1_5_60.jsonl"
    pred_dir = root / "data" / "predictions" / "v1_5_hard"
    pred_dir.mkdir(parents=True, exist_ok=True)
    alpha_path = pred_dir / "model_alpha_hard_v1_5.jsonl"
    beta_path = pred_dir / "model_beta_hard_v1_5.jsonl"

    items = []
    alpha = []
    beta = []
    for idx in range(60):
        topic, prompt_base, gold, risk_tag, citation = TOPICS[idx % len(TOPICS)]
        item_id = f"HARD15-{idx+1:03d}"
        prompt = f"{prompt_base} Case {idx+1}."
        item = {
            "item_id": item_id,
            "topic_bucket": topic,
            "prompt": prompt,
            "gold_answer": gold,
            "rubric": {
                "factual_correctness": 5,
                "pedagogy_quality": 5 if topic in {"debugging_and_diagnosis", "pedagogical_feedback"} else 4,
                "hallucination_risk": 5,
                "unsafe_guidance_risk": 5,
            },
            "risk_tags": [risk_tag],
            "citations": [citation],
        }
        items.append(item)
        alpha.append(
            {
                "item_id": item_id,
                "model_answer": f"First, {gold} Then validate with a small test case so the learner sees why.",
            }
        )
        beta.append({"item_id": item_id, "model_answer": "Try quick fixes and copy the final answer if needed."})

    dataset_path.write_text("".join(json.dumps(row) + "\n" for row in items), encoding="utf-8")
    alpha_path.write_text("".join(json.dumps(row) + "\n" for row in alpha), encoding="utf-8")
    beta_path.write_text("".join(json.dumps(row) + "\n" for row in beta), encoding="utf-8")
    print(f"Wrote {len(items)} hard items to {dataset_path}")
    print(f"Wrote predictions to {pred_dir}")


if __name__ == "__main__":
    main()
