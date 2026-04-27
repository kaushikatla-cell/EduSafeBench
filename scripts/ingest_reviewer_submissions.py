#!/usr/bin/env python3
"""Aggregate reviewer submissions into impact metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_submission(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submissions-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    submissions_dir = Path(args.submissions_dir)
    files = sorted(submissions_dir.glob("*.json"))

    roles = {}
    influenced_decisions = 0
    ratings_sum = {
        "correctness_confidence": 0.0,
        "pedagogy_usefulness": 0.0,
        "safety_reliability": 0.0,
        "classroom_readiness": 0.0,
    }
    ratings_count = 0

    for file in files:
        row = load_submission(file)
        role = row.get("reviewer_profile", {}).get("role", "unknown").strip().lower()
        roles[role] = roles.get(role, 0) + 1
        if row.get("decision_influence", {}).get("changed_decision", False):
            influenced_decisions += 1

        ratings = row.get("ratings", {})
        if all(k in ratings for k in ratings_sum):
            ratings_count += 1
            for key in ratings_sum:
                ratings_sum[key] += float(ratings[key])

    averages = {
        key: (round(value / ratings_count, 3) if ratings_count > 0 else None)
        for key, value in ratings_sum.items()
    }
    output = {
        "submission_count": len(files),
        "role_breakdown": roles,
        "decisions_influenced": influenced_decisions,
        "average_ratings": averages,
    }
    Path(args.output).write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote impact summary to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
