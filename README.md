# EduSafeBench

EduSafeBench is a public, reproducible reliability benchmark for K-12 CS learning assistants, with a focus on AP CSA and AP CSP workflows.

Website (GitHub Pages): `https://kaushikatla-cell.github.io/EduSafeBench/`

## What this project ships

- A structured benchmark dataset with rubric-guided grading fields.
- A deterministic evaluator that scores correctness, pedagogy, and safety.
- A reproducible leaderboard pipeline that writes machine-readable outputs.
- Public benchmark reports that can be shared with educators and students.

## Repository layout

- `src/edusafebench/` core benchmark and evaluation logic.
- `data/benchmarks/` versioned benchmark items in JSONL format.
- `configs/` run configuration examples.
- `results/` benchmark result artifacts.
- `reports/` public-facing benchmark reports.
- `docs/` methodology and reliability notes.
- `scripts/` utility scripts such as longitudinal drift tracking.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests
python -m edusafebench.cli run \
  --dataset data/benchmarks/apcsa_csp_v1.jsonl \
  --predictions data/benchmarks/sample_predictions_v1.jsonl \
  --output results/v1_results_generated.json

python scripts/generate_week1_assets.py
python -m edusafebench.cli run-multi \
  --dataset data/benchmarks/apcsa_csp_week1_150.jsonl \
  --predictions-dir data/predictions/week1 \
  --output results/v1_1_multi_results.json
```

## Benchmark scope

Topic buckets:

1. Java fundamentals and AP CSA syntax accuracy
2. Algorithms and tracing
3. Debugging and error diagnosis
4. AP CSP conceptual reasoning and ethics
5. Data and abstraction
6. Pedagogical feedback quality

Reliability dimensions:

- `factual_correctness`
- `pedagogy_quality`
- `hallucination_risk`
- `unsafe_guidance_risk`

## Admissions-facing impact checklist

- Open-source releases with transparent methodology.
- Reproducible benchmark runs and published result artifacts.
- External educator feedback loops and pilot reporting.
- Longitudinal tracking across benchmark versions.

## External validation workflow

- Open educator feedback issues using `.github/ISSUE_TEMPLATE/educator_feedback.md`.
- Record pilot outcomes in `reports/` and link evidence in release notes.
- Compare benchmark versions with:

```bash
python scripts/track_drift.py results/v1_results_generated.json results/v1_results_generated.json
```

## Week 1 sprint artifacts

- Expanded dataset: `data/benchmarks/apcsa_csp_week1_150.jsonl`
- Multi-model predictions: `data/predictions/week1/`
- Multi-model result artifact: `results/v1_1_multi_results.json`
- Week-one report: `reports/v1_1_report.md`
- Outreach plan: `docs/outreach.md`
