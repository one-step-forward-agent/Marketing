from pathlib import Path

import pandas as pd

from src.overserved_analysis import classify_overserved
from src.satisfaction_analysis import aggregate_jtbd_scores
from src.solution_job_fit import solution_job_fit
from src.underserved_analysis import classify_underserved

EXPECTED_JTBD = {"context-restoration", "decision-support", "time-feedback"}


def test_classification_rules_are_deterministic():
    assert classify_underserved(9, 4) is True
    assert classify_underserved(6, 4) is False
    assert classify_overserved(5, 9) is True
    assert classify_overserved(8, 9) is False


def test_solution_job_fit_is_ratio_and_zero_safe():
    assert solution_job_fit(8, 4) == 0.5
    assert solution_job_fit(0, 4) == 0.0


def test_aggregate_preserves_three_canonical_jtbd_labels(tmp_path: Path):
    source = tmp_path / "features.csv"
    pd.DataFrame(
        [
            {"interview_id": "001", "jtbd": "context-restoration", "importance": 9, "satisfaction": 3, "confidence": 0.8},
            {"interview_id": "002", "jtbd": "decision-support", "importance": 8, "satisfaction": 4, "confidence": 0.8},
            {"interview_id": "003", "jtbd": "time-feedback", "importance": 7, "satisfaction": 5, "confidence": 0.7},
        ]
    ).to_csv(source, index=False)
    result = aggregate_jtbd_scores(source)
    assert set(result["jtbd"]) == EXPECTED_JTBD
    assert list(result.sort_values(["opportunity", "jtbd"], ascending=[False, True])["opportunity"]) == sorted(result["opportunity"], reverse=True)


def test_generate_all_diagrams_creates_six_nonempty_pngs(tmp_path: Path):
    from src.generate_all_diagrams import generate_all_diagrams

    outputs = generate_all_diagrams("data/jtbd_scores.csv", tmp_path)
    expected = {
        "jtbd-prioritization.png",
        "importance-vs-satisfaction.png",
        "underserved-jobs.png",
        "overserved-jobs.png",
        "opportunity-map.png",
        "solution-job-fit.png",
    }
    assert {path.name for path in outputs} == expected
    assert all(path.exists() and path.stat().st_size > 1000 for path in outputs)
