# Contributing to EduSafeBench

## Principles

- Keep benchmark items source-grounded and rubric-explicit.
- Avoid ambiguous prompts unless intentionally tagged as adversarial.
- Treat safety and pedagogy quality as first-class metrics.

## Local workflow

1. Add benchmark items to `data/benchmarks/` in JSONL format.
2. Run tests:
   - `PYTHONPATH=src python -m unittest discover -s tests`
3. Run benchmark:
   - `PYTHONPATH=src python -m edusafebench.cli run --dataset ... --predictions ... --output ...`
4. Update `reports/` with key findings and limitations.

## Item authoring checklist

- Topic bucket is one of the six benchmark categories.
- Rubric includes all reliability dimensions with 1-5 integer scores.
- Risk tags align with known failure taxonomy.
- Gold answer is concise and directly gradeable.
