# JTBD opportunity methodology v0.2

## Purpose
This branch is a **reproducible descriptive research pipeline**. It turns the canonical `CustomerDevelopment` branch into normalized JTBD fields, scores and diagrams while keeping evidence provenance explicit.

The current input is synthetic. Therefore the workflow can validate data flow and falsifiable hypotheses, but it cannot scientifically prove demand or rank market opportunities.

## Scientific-method discipline

1. **Observation:** preserve source episode, trigger, pain, workaround, functional/emotional/social job and evidence type.
2. **Hypothesis:** state a falsifiable product/marketing claim before testing.
3. **Prediction:** define a behavioral threshold (return, time saved, choice commitment, willingness to pay).
4. **Experiment:** run on real users with a coherent segment and pre-declared metric.
5. **Result:** store observed data without redefining success after the fact.
6. **Update:** strengthen, weaken, split or reject the hypothesis.

## Descriptive metrics

Importance and satisfaction use the 1–10 fixture scale. The ODI-style opportunity score is:

```text
Opportunity = Importance + max(Importance - Satisfaction, 0)
```

This is a prioritization heuristic, not a statistical estimator.

Classification rules:
- **Underserved:** importance ≥ 7 and satisfaction ≤ 5.
- **Overserved:** importance ≤ 6 and satisfaction ≥ 8.
- **Balanced:** everything else.

`solution_job_fit = satisfaction / importance` is only a descriptive ratio.

## Evidence grade is separate from score

A high opportunity score cannot compensate for weak evidence.

- `synthetic-only`: zero empirical sources.
- `low`: 1–2 empirical sources.
- `medium`: 3–4 empirical sources.
- `high`: 5+ empirical sources, still subject to segment/source-quality review.

The current three JTBD are all `synthetic-only`.

## Uncertainty

`importance_sd` and `satisfaction_sd` describe variation inside the generated fixture corpus. They are **not** sampling uncertainty for a real population. Confidence intervals, significance tests and prevalence estimates must wait for empirical data collected with an appropriate sampling design.

## Interpretation limit

Differences such as 14.1 vs 13.9 are not meaningful evidence of one job being more important than another because the synthetic sample and scores were deliberately constructed. Treat all three as candidate problem spaces until real episodes replace fixtures.
