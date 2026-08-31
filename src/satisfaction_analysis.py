from pathlib import Path

import pandas as pd

from src.opportunity_score import opportunity_score
from src.overserved_analysis import classify_overserved
from src.solution_job_fit import solution_job_fit
from src.underserved_analysis import classify_underserved


def _classification(importance: float, satisfaction: float) -> str:
    if classify_underserved(importance, satisfaction):
        return "underserved"
    if classify_overserved(importance, satisfaction):
        return "overserved"
    return "balanced"


def aggregate_jtbd_scores(source: str | Path) -> pd.DataFrame:
    """Aggregate interview feature rows into one deterministic record per JTBD."""
    frame = pd.read_csv(source)
    grouped = (
        frame.groupby("jtbd", as_index=False)
        .agg(
            importance=("importance", "mean"),
            satisfaction=("satisfaction", "mean"),
            confidence=("confidence", "mean"),
        )
        .sort_values("jtbd")
        .reset_index(drop=True)
    )
    grouped["opportunity"] = grouped.apply(
        lambda row: opportunity_score(float(row["importance"]), float(row["satisfaction"])),
        axis=1,
    )
    grouped["classification"] = grouped.apply(
        lambda row: _classification(float(row["importance"]), float(row["satisfaction"])),
        axis=1,
    )
    grouped["solution_job_fit"] = grouped.apply(
        lambda row: solution_job_fit(float(row["importance"]), float(row["satisfaction"])),
        axis=1,
    )
    return grouped
