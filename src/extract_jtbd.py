"""Normalize synthetic CustDev fixture scores from the CustomerDevelopment Git branch."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pandas as pd

DISCLOSURE = "This is a generated research fixture, not a transcript from a real respondent."


def _git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"CustomerDevelopment:{path}"], text=True, encoding="utf-8"
    )


def _extract(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Could not parse pattern: {pattern}")
    return match.group(1).strip()


def extract_features(output: str | Path = "data/interview_features.csv") -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for index in range(1, 31):
        interview_id = f"{index:03d}"
        text = _git_show(f"interviews/{interview_id}-interview.md")
        if DISCLOSURE not in text:
            raise ValueError(f"Interview {interview_id} lacks synthetic-data disclosure")
        jtbd = _extract(r"Primary: `([^`]+)`", text)
        importance = float(_extract(r"## Importance score\n([0-9.]+)/10", text))
        satisfaction = float(_extract(r"## Satisfaction score\n([0-9.]+)/10", text))
        confidence = float(_extract(r"## Confidence score\n([0-9.]+)", text))
        rows.append(
            {
                "interview_id": interview_id,
                "jtbd": jtbd,
                "importance": importance,
                "satisfaction": satisfaction,
                "confidence": confidence,
            }
        )
    frame = pd.DataFrame(rows)
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)
    return frame


if __name__ == "__main__":
    extract_features()
