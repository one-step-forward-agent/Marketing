def classify_underserved(importance: float, satisfaction: float) -> bool:
    """A job is underserved when it is important and current satisfaction is low."""
    return importance >= 7 and satisfaction <= 5
