# EduSafeBench V1.2 Report Template and Initial Artifacts

## Scope update

- Added mandatory citation support in benchmark schema and generated dataset rows.
- Added a 10% adjudication sampling workflow for human review.
- Added agreement computation between human scores and model-eval scores.

## Artifacts generated

- Single-model run output: `results/v1_2_model_alpha_results.json`
- 10% adjudication sample (blank for reviewers): `results/v1_2_adjudication_sample.json`
- Example filled adjudication file: `results/v1_2_adjudication_sample_filled_example.json`
- Agreement output: `results/v1_2_adjudication_agreement.json`

## Current benchmark metrics (model_alpha_v1)

- factual_correctness: 4.0
- pedagogy_quality: 4.0
- hallucination_risk: 4.0
- unsafe_guidance_risk: 5.0

## Human adjudication protocol (10% sample)

1. Use `results/v1_2_adjudication_sample.json` as the reviewer packet.
2. Have reviewers fill all `human_scores` fields with 1-5 integers.
3. Save a completed adjudication file and run:
   - `python scripts/compute_adjudication_agreement.py --adjudication <filled.json> --run-results results/v1_2_model_alpha_results.json --output results/v1_2_adjudication_agreement.json`

## Initial agreement snapshot

- Sample size: 15 items (10% of 150)
- Mean absolute error (MAE):
  - factual_correctness: 0.0
  - pedagogy_quality: 0.0
  - hallucination_risk: 0.0
  - unsafe_guidance_risk: 0.0

Note: current MAE is from an example filled file used to verify workflow wiring. Replace with real reviewer-scored data for publication claims.
