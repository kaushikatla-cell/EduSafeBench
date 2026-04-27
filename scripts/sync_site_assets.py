#!/usr/bin/env python3
"""Copy public artifacts into docs/ for GitHub Pages hosting."""

from __future__ import annotations

import shutil
from pathlib import Path


def copy_file(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def copy_glob(src_dir: Path, pattern: str, dest_dir: Path) -> int:
    count = 0
    for path in sorted(src_dir.glob(pattern)):
        if path.is_file():
            copy_file(path, dest_dir / path.name)
            count += 1
    return count


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"

    reports_src = root / "reports"
    results_src = root / "results"

    reports_dest = docs / "reports"
    results_dest = docs / "results"

    # Clean old copies to avoid stale artifacts lingering on the site.
    if reports_dest.exists():
        shutil.rmtree(reports_dest)
    if results_dest.exists():
        shutil.rmtree(results_dest)

    report_count = copy_glob(reports_src, "*.md", reports_dest)
    result_count = copy_glob(results_src, "*.json", results_dest)

    # Copy a small set of top-level docs that the site links to.
    for name in [
        "methodology.md",
        "outreach.md",
        "patch_story_draft.md",
        "tier1_execution_os.md",
        "reviewer_submission_template.md",
    ]:
        src = docs / name
        if src.exists():
            copy_file(src, docs / "public_docs" / name)

    print(f"Synced {report_count} report markdown files to {reports_dest}")
    print(f"Synced {result_count} result json files to {results_dest}")


if __name__ == "__main__":
    main()
