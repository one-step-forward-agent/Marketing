# JTBD opportunity methodology

This branch uses synthetic research fixtures to validate an analytical workflow. Results are **candidate USP hypotheses**, not scientific proof of demand.

## Metrics

All importance and satisfaction scores use the 1–10 scale. Confidence uses 0.0–1.0.

ODI-style opportunity score:

```text
Opportunity = Importance + max(Importance - Satisfaction, 0)
```

Classification rules:

- **Underserved:** importance ≥ 7 and satisfaction ≤ 5.
- **Overserved:** importance ≤ 6 and satisfaction ≥ 8.
- **Balanced:** all other combinations.

`solution_job_fit = satisfaction / importance`; a lower ratio with high importance indicates larger solution headroom. This ratio is descriptive and is not a validation statistic.

## Interpretation limit

The generated corpus can validate scoring, sorting, visualizations, and downstream hypothesis generation. It cannot establish population prevalence, causal effects, statistical significance, or product-market fit.
