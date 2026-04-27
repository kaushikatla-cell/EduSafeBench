"""CLI entrypoint for EduSafeBench."""

import argparse
import json

from .runner import run_benchmark


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="edusafebench")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run benchmark on predictions")
    run_parser.add_argument("--dataset", required=True)
    run_parser.add_argument("--predictions", required=True)
    run_parser.add_argument("--output", required=True)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "run":
        result = run_benchmark(args.dataset, args.predictions, args.output)
        print(json.dumps(result["aggregate_scores"], indent=2))


if __name__ == "__main__":
    main()
