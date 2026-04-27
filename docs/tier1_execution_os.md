# Tier-1 Execution OS (6 Weeks)

## Weekly cadence

1. **Monday (build)**: add 20-40 benchmark items and run all eval pipelines.
2. **Wednesday (validate)**: adjudication spot checks and reviewer outreach follow-ups.
3. **Friday (publish)**: update changelog, impact summary, and public site links.

## Non-negotiable metrics

- Reviewer submissions: +2 per week
- Decisions influenced: +1 every 2 weeks
- Benchmark items: +40 per week (mix of standard + hard misconception)
- Public release artifacts: one tagged update every 2 weeks

## Operating commands

```bash
python scripts/generate_week1_assets.py
python scripts/generate_hard_slice_v1_5.py
python scripts/ingest_reviewer_submissions.py --submissions-dir data/reviewer_submissions --output results/impact_summary.json
python scripts/build_admissions_packet.py
```

## Weekly release checklist

- [ ] New benchmark items merged with citations
- [ ] Multi-model runs generated and saved
- [ ] Reviewer submissions ingested
- [ ] Changelog updated with feedback -> change mapping
- [ ] Admissions evidence packet refreshed
