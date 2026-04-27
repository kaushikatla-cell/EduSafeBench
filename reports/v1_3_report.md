# EduSafeBench V1.3 Report (300 Cited Items)

## Scope update

- Expanded benchmark dataset to 300 source-cited AP CSA/AP CSP items.
- Ran a clean two-model leaderboard on isolated `v1.3` prediction files.
- Generated a 10% adjudication sample for reviewer scoring.

## Artifacts

- Dataset: `data/benchmarks/apcsa_csp_v1_3_300.jsonl`
- Predictions directory: `data/predictions/v1_3/`
- Multi-model results: `results/v1_3_multi_results.json`
- Adjudication sample (30 items): `results/v1_3_adjudication_sample.json`
- Reviewer template: `docs/reviewer_submission_template.md`

## Leaderboard snapshot

1. `model_alpha_v1_3`
   - factual_correctness: 4.0
   - pedagogy_quality: 4.0
   - hallucination_risk: 4.0
   - unsafe_guidance_risk: 5.0
2. `model_beta_v1_3`
   - factual_correctness: 2.667
   - pedagogy_quality: 2.0
   - hallucination_risk: 4.0
   - unsafe_guidance_risk: 5.0

## External review instructions

1. Share `results/v1_3_adjudication_sample.json` with reviewers.
2. Ask reviewers to submit using `docs/reviewer_submission_template.md`.
3. Convert reviewer scores into filled adjudication JSON and compute agreement with:
   - `python scripts/compute_adjudication_agreement.py --adjudication <filled.json> --run-results <single-model-run-results.json> --output results/v1_3_adjudication_agreement.json`
