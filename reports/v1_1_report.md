# EduSafeBench V1.1 Week-One Report

## Scope update

- Dataset expanded to 150 benchmark items for AP CSA/AP CSP-aligned scenarios.
- Added multi-model leaderboard support in the CLI and core runner.
- Added pilot outreach package for external teacher and mentor feedback.

## Run metadata

- Dataset: `apcsa_csp_week1_150.jsonl`
- Models evaluated: 2
- Output artifact: `results/v1_1_multi_results.json`

## Leaderboard snapshot

1. `model_alpha_v1`
   - factual_correctness: 4.0
   - pedagogy_quality: 4.0
   - hallucination_risk: 4.0
   - unsafe_guidance_risk: 5.0
2. `model_beta_v1`
   - factual_correctness: 2.667
   - pedagogy_quality: 2.0
   - hallucination_risk: 4.0
   - unsafe_guidance_risk: 5.0

## Interpretation

- Pedagogy quality produced the largest separation between models.
- Basic safety remained high in this synthetic week-one slice.
- Next version should increase adversarial pressure for nuanced safety failure detection.

## Week-two priorities

- Expand to 300+ source-cited items.
- Add teacher adjudication protocol for random sample review.
- Publish first external feedback changelog.
