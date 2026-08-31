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


def _evidence_grade(empirical_sources: int) -> str:
    if empirical_sources == 0:
        return "synthetic-only"
    if empirical_sources < 3:
        return "low"
    if empirical_sources < 5:
        return "medium"
    return "high"


def aggregate_jtbd_scores(source: str | Path) -> pd.DataFrame:
    """Aggregate research rows into descriptive records per JTBD.

    Scores are descriptive. Evidence grade is deliberately separated from the numeric
    opportunity score so synthetic volume cannot masquerade as empirical confidence.
    """
    frame = pd.read_csv(source)
    frame["is_empirical"] = frame.get("evidence_type", "synthetic-fixture") != "synthetic-fixture"
    grouped = (
        frame.groupby("jtbd", as_index=False)
        .agg(
            importance=("importance", "mean"),
            satisfaction=("satisfaction", "mean"),
            confidence=("confidence", "mean"),
            n_fixtures=("interview_id", "count"),
            importance_sd=("importance", lambda s: float(s.std(ddof=0))),
            satisfaction_sd=("satisfaction", lambda s: float(s.std(ddof=0))),
            empirical_sources=("is_empirical", "sum"),
        )
        .sort_values("jtbd")
        .reset_index(drop=True)
    )
    grouped["opportunity"] = grouped.apply(
        lambda row: opportunity_score(float(row["importance"]), float(row["satisfaction"])), axis=1
    )
    grouped["classification"] = grouped.apply(
        lambda row: _classification(float(row["importance"]), float(row["satisfaction"])), axis=1
    )
    grouped["solution_job_fit"] = grouped.apply(
        lambda row: solution_job_fit(float(row["importance"]), float(row["satisfaction"])), axis=1
    )
    grouped["evidence_grade"] = grouped["empirical_sources"].map(lambda value: _evidence_grade(int(value)))
    return grouped
