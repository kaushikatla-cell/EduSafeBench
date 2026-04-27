#!/usr/bin/env python3
"""Compute agreement between human adjudication and model-eval scores."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DIMENSIONS = [
    "factual_correctness",
    "pedagogy_quality",
    "hallucination_risk",
    "unsafe_guidance_risk",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--adjudication", required=True)
    parser.add_argument("--run-results", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    adjudication_rows = json.loads(Path(args.adjudication).read_text(encoding="utf-8"))
    run_results = json.loads(Path(args.run_results).read_text(encoding="utf-8"))
    per_item = {row["item_id"]: row["score"] for row in run_results["per_item"]}

    totals = {dim: {"count": 0, "abs_error_sum": 0.0} for dim in DIMENSIONS}
    for row in adjudication_rows:
        item_id = row["item_id"]
        if item_id not in per_item:
            continue
        for dim in DIMENSIONS:
            human = row["human_scores"].get(dim)
            model = per_item[item_id].get(dim)
            if human is None or model is None:
                continue
            totals[dim]["count"] += 1
            totals[dim]["abs_error_sum"] += abs(float(human) - float(model))

    agreement = {}
    for dim, stats in totals.items():
        if stats["count"] == 0:
            agreement[dim] = {"samples": 0, "mae": None}
        else:
            agreement[dim] = {"samples": stats["count"], "mae": round(stats["abs_error_sum"] / stats["count"], 3)}

    Path(args.output).write_text(json.dumps({"agreement": agreement}, indent=2), encoding="utf-8")
    print(f"Wrote agreement report to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
