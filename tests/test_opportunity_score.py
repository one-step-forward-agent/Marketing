from src.opportunity_score import opportunity_score


def test_opportunity_score_penalizes_satisfaction_gap():
    assert opportunity_score(9, 3) == 15


def test_opportunity_score_has_no_negative_gap_bonus():
    assert opportunity_score(5, 8) == 5
