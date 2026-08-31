def classify_overserved(importance: float, satisfaction: float) -> bool:
    """A job is overserved when importance is modest while satisfaction is already high."""
    return importance <= 6 and satisfaction >= 8
