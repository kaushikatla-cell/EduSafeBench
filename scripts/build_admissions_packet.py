#!/usr/bin/env python3
"""Build a one-page admissions evidence packet from project artifacts."""

from __future__ import annotations

import json
from pathlib import Path


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    impact = read_json(root / "results" / "impact_summary.json")
    v13 = read_json(root / "results" / "v1_3_multi_results.json")
    hard = read_json(root / "results" / "v1_4_hard_multi_results.json")

    reviewers = impact.get("submission_count", 0)
    decisions = impact.get("decisions_influenced", 0)
    models_v13 = v13.get("models_evaluated", 0)
    models_hard = hard.get("models_evaluated", 0)

    packet = f"""# EduSafeBench Admissions Evidence Packet

## Problem
AI coding assistants are widely used by beginner CS learners, but trustworthiness is rarely audited with transparent, reproducible methods.

## What I built
- Open benchmark infrastructure for AP CSA/AP CSP reliability.
- Public datasets with citations, eval tooling, CI, reports, and a live project website.
- External review workflow with impact tracking and adjudication pipeline.

## Measurable Outputs
- Core cited benchmark set: 300 items (`apcsa_csp_v1_3_300.jsonl`)
- Hard misconception benchmark: 6 items in v1.4, expanded pipeline prepared for 60 items in v1.5
- Models evaluated: {models_v13} (v1.3 leaderboard), {models_hard} (v1.4 hard leaderboard)
- Reviewer submissions logged: {reviewers}
- Decisions influenced: {decisions}

## Public Artifacts
- Site: https://kaushikatla-cell.github.io/EduSafeBench/
- Repo: https://github.com/kaushikatla-cell/EduSafeBench
- v1.3 report: `reports/v1_3_report.md`
- v1.4 changelog: `reports/v1_4_changelog.md`

## Why this is high-impact
- Niche focus: reliability and pedagogy safety for beginner CS AI assistants.
- Reproducible engineering: versioned data, scripts, CI workflows, result artifacts.
- Community pathway: reviewer submissions, impact dashboard, and local publication outreach.

## Next 6-week targets
- Reach 10 real reviewer submissions with role diversity.
- Publish real adjudication agreement metrics.
- Expand hard misconception benchmark to 60+ items and publish v1.5 report.
"""
    output = root / "reports" / "admissions_evidence_packet.md"
    output.write_text(packet, encoding="utf-8")
    print(f"Wrote admissions packet to {output}")


if __name__ == "__main__":
    main()
