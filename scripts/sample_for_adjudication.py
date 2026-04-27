#!/usr/bin/env python3
"""Sample a percentage of benchmark items for human adjudication."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--sample-rate", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = read_jsonl(Path(args.dataset))
    random.seed(args.seed)
    n = max(1, int(len(rows) * args.sample_rate))
    sampled = random.sample(rows, n)

    output_rows = []
    for row in sampled:
        output_rows.append(
            {
                "item_id": row["item_id"],
                "topic_bucket": row["topic_bucket"],
                "prompt": row["prompt"],
                "gold_answer": row["gold_answer"],
                "citations": row.get("citations", []),
                "human_scores": {
                    "factual_correctness": None,
                    "pedagogy_quality": None,
                    "hallucination_risk": None,
                    "unsafe_guidance_risk": None,
                },
                "notes": "",
            }
        )

    Path(args.output).write_text(json.dumps(output_rows, indent=2), encoding="utf-8")
    print(f"Sampled {n}/{len(rows)} items into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
