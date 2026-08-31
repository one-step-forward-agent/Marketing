def opportunity_score(importance: float, satisfaction: float) -> float:
    """Return ODI-style opportunity score for bounded importance/satisfaction values."""
    return importance + max(importance - satisfaction, 0)
