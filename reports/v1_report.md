# EduSafeBench V1 Report

## Run metadata

- Dataset: `apcsa_csp_v1.jsonl`
- Evaluated items: 6
- Run type: deterministic baseline

## Aggregate scores

- factual_correctness: 4.0
- pedagogy_quality: 2.833
- hallucination_risk: 4.0
- unsafe_guidance_risk: 5.0

## Top findings

1. Baseline answers were generally safe, with no direct unsafe guidance patterns detected.
2. Pedagogy quality lagged factual quality on short, non-stepwise responses.
3. Debugging items revealed the highest variance in clarity and remediation depth.

## Limitations

- Small pilot dataset size.
- Rule-based evaluator is a baseline, not a full semantic judge.
- No inter-rater adjudication in this seed run.

## Next benchmark upgrades

- Expand to 300+ items with source grounding.
- Add adversarial subsets for ambiguity and edge-case traps.
- Add manual spot-check protocol for inter-rater consistency.
