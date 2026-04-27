"""Benchmark runner and aggregation logic."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .evaluator import evaluate_prediction
from .schema import BenchmarkItem
from .taxonomy import RELIABILITY_DIMENSIONS


def _read_jsonl(path: str) -> List[Dict]:
    rows: List[Dict] = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _evaluate(dataset_path: str, predictions_path: str) -> Dict:
    dataset_rows = _read_jsonl(dataset_path)
    prediction_rows = _read_jsonl(predictions_path)
    pred_by_id = {row["item_id"]: row["model_answer"] for row in prediction_rows}

    per_item = []
    aggregate = {dim: 0.0 for dim in RELIABILITY_DIMENSIONS}
    total_items = 0

    for row in dataset_rows:
        item = BenchmarkItem(
            item_id=row["item_id"],
            topic_bucket=row["topic_bucket"],
            prompt=row["prompt"],
            gold_answer=row["gold_answer"],
            rubric=row["rubric"],
            risk_tags=row["risk_tags"],
            citations=row.get("citations", []),
        )
        item.validate()
        if item.item_id not in pred_by_id:
            continue

        total_items += 1
        score = evaluate_prediction(item.gold_answer, pred_by_id[item.item_id]).as_dict()
        for dim in RELIABILITY_DIMENSIONS:
            aggregate[dim] += score[dim]
        per_item.append(
            {
                "item_id": item.item_id,
                "topic_bucket": item.topic_bucket,
                "score": score,
                "risk_tags": item.risk_tags,
                "citations": item.citations,
            }
        )

    if total_items > 0:
        for dim in RELIABILITY_DIMENSIONS:
            aggregate[dim] = round(aggregate[dim] / total_items, 3)

    return {
        "dataset": Path(dataset_path).name,
        "predictions": Path(predictions_path).name,
        "evaluated_items": total_items,
        "aggregate_scores": aggregate,
        "per_item": per_item,
    }


def run_benchmark(dataset_path: str, predictions_path: str, output_path: str) -> Dict:
    result = _evaluate(dataset_path, predictions_path)
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
    return result


def run_multi_benchmark(dataset_path: str, predictions_paths: List[str], output_path: str) -> Dict:
    leaderboard = []
    for prediction_path in predictions_paths:
        temp_result = _evaluate(dataset_path, prediction_path)
        leaderboard.append(
            {
                "model": Path(prediction_path).stem,
                "predictions": Path(prediction_path).name,
                "evaluated_items": temp_result["evaluated_items"],
                "aggregate_scores": temp_result["aggregate_scores"],
            }
        )

    leaderboard.sort(
        key=lambda row: (
            row["aggregate_scores"]["factual_correctness"],
            row["aggregate_scores"]["pedagogy_quality"],
            row["aggregate_scores"]["hallucination_risk"],
            row["aggregate_scores"]["unsafe_guidance_risk"],
        ),
        reverse=True,
    )
    result = {
        "dataset": Path(dataset_path).name,
        "models_evaluated": len(leaderboard),
        "leaderboard": leaderboard,
    }
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
    return result
