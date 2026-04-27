#!/usr/bin/env python3
"""Compare aggregate scores between two run artifacts."""

import json
import sys
from pathlib import Path


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/track_drift.py <old_results.json> <new_results.json>")
        return 1

    old_path, new_path = sys.argv[1], sys.argv[2]
    old_data = load(old_path)
    new_data = load(new_path)

    print(f"Comparing {Path(old_path).name} -> {Path(new_path).name}")
    for key, old_val in old_data["aggregate_scores"].items():
        new_val = new_data["aggregate_scores"][key]
        delta = round(new_val - old_val, 3)
        sign = "+" if delta >= 0 else ""
        print(f"{key}: {old_val} -> {new_val} ({sign}{delta})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
