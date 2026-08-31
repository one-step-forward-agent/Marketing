from pathlib import Path

from src.extract_jtbd import extract_features
from src.satisfaction_analysis import aggregate_jtbd_scores


def test_extraction_preserves_traceability_fields(tmp_path: Path):
    output = tmp_path / 'features.csv'
    frame = extract_features(output)
    assert len(frame) == 30
    assert {'segment','trigger','evidence_type','functional_job','emotional_job','social_job'} <= set(frame.columns)
    assert set(frame['evidence_type']) == {'synthetic-fixture'}


def test_aggregate_exposes_uncertainty_and_evidence_grade(tmp_path: Path):
    output = tmp_path / 'features.csv'
    frame = extract_features(output)
    scores = aggregate_jtbd_scores(output)
    assert len(scores) == 3
    assert {'n_fixtures','importance_sd','satisfaction_sd','empirical_sources','evidence_grade'} <= set(scores.columns)
    assert set(scores['n_fixtures']) == {10}
    assert set(scores['empirical_sources']) == {0}
    assert set(scores['evidence_grade']) == {'synthetic-only'}
