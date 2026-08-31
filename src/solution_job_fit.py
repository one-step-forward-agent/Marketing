def solution_job_fit(importance: float, satisfaction: float) -> float:
    """Return satisfaction-to-importance ratio, zero-safe for malformed/empty importance."""
    if importance == 0:
        return 0.0
    return satisfaction / importance
