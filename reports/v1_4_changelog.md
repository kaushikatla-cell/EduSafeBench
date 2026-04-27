# EduSafeBench V1.4 Changelog

## Release goals

- [x] Increase reviewer coverage and agreement quality workflow readiness.
- [x] Expand high-risk scenario depth (debugging + ethics).
- [x] Convert external feedback signals into measurable benchmark and distribution changes.

## Changes in this release

### Dataset updates

- Items added: hard misconception slice with 6 high-risk prompts (`hard_misconception_slice_v1_4.jsonl`).
- Items revised: none in core 300-item set.
- New citation sources: existing AP CSA/AP CSP and pedagogy sources retained for hard slice.

### Evaluation updates

- Scoring logic changes: none.
- New risk tags or dimensions: reused current risk taxonomy with harder prompt framing.
- Backward-compatibility notes: compatible with existing runner and schema.

### External validation updates

- Reviewer submissions count: 1 structured sample submission (real reviewers pending).
- Reviewer role breakdown: teacher=1.
- Decisions influenced: 1 (sample record).
- Agreement metrics (MAE by dimension): unchanged from v1.2 example workflow until real adjudication files arrive.

## Feedback -> Change mapping

1. Feedback:
   - Need better public distribution for local/community visibility.
   - Change made: added Patch publication draft and documented Patch posting route in external signals.
   - Expected impact: improves odds of attracting authentic reviewers from local educator/community channels.
2. Feedback:
   - Need tougher beginner misconception tests to separate model quality.
   - Change made: added hard misconception benchmark slice and published v1.4 hard leaderboard artifact.
   - Expected impact: clearer model differentiation on nuanced correctness/pedagogy pitfalls.

## New artifacts

- External signal evidence: `data/external_signals/public_feedback_signals.json`
- Patch story draft: `docs/patch_story_draft.md`
- Hard benchmark slice: `data/benchmarks/hard_misconception_slice_v1_4.jsonl`
- Hard-slice predictions: `data/predictions/v1_4_hard/`
- Hard-slice results: `results/v1_4_hard_multi_results.json`

## Risk and limitations

- External evidence is currently publication/distribution signal, not a substitute for direct reviewer submissions.
- Hard slice is intentionally small and should be expanded in v1.5 for stronger statistical confidence.

## Next sprint priorities

- Collect 5+ real reviewer submissions and regenerate impact summary.
- Run adjudication agreement on real reviewer-scored files.
- Expand hard misconception slice from 6 to 50+ items.
