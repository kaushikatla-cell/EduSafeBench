"""CLI entrypoint for EduSafeBench."""

import argparse
import json
from pathlib import Path

from .runner import run_benchmark, run_multi_benchmark


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="edusafebench")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run benchmark on predictions")
    run_parser.add_argument("--dataset", required=True)
    run_parser.add_argument("--predictions", required=True)
    run_parser.add_argument("--output", required=True)

    run_multi_parser = subparsers.add_parser("run-multi", help="Run benchmark for multiple prediction files")
    run_multi_parser.add_argument("--dataset", required=True)
    run_multi_parser.add_argument("--predictions-dir", required=True)
    run_multi_parser.add_argument("--output", required=True)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "run":
        result = run_benchmark(args.dataset, args.predictions, args.output)
        print(json.dumps(result["aggregate_scores"], indent=2))
    if args.command == "run-multi":
        predictions_paths = sorted(str(path) for path in Path(args.predictions_dir).glob("*.jsonl"))
        result = run_multi_benchmark(args.dataset, predictions_paths, args.output)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
