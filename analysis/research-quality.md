# Research quality and evidence policy

## Current evidence level

The repository contains **30 synthetic fixtures**, not 30 empirical interviews. They validate:
- Markdown schema and parsing;
- evidence/JTBD field normalization;
- score aggregation;
- downstream charts and hypothesis generation;
- branch-to-branch data lineage.

They do **not** validate:
- problem prevalence or segment size;
- real customer language;
- willingness to pay;
- switching behavior;
- retention potential;
- relative priority of the three JTBD;
- causal impact of any solution.

## Confidence semantics

The existing `Confidence score` is treated as **coding/scenario confidence inside the synthetic fixture**, not confidence that a market claim is true. Empirical insight confidence must be recalculated from real sources.

## Empirical confidence rubric

- **High:** ≥3 independent real sources, unprompted recurrence, consistent trigger/workaround, and no major contradictory evidence.
- **Medium:** 2 real sources or evidence concentrated in one segment / prompted discussion.
- **Low:** single source, proxy source, synthetic fixture, or unsupported inference.

## Analysis guardrails

1. Separate observation, inference, assumption, and recommendation.
2. Keep verbatim quotes only when a real source exists; never manufacture quotes.
3. Record a concrete recent episode, not general opinions.
4. Capture alternatives including "do nothing" and manual workflows.
5. Record contradictions and negative cases instead of averaging them away.
6. Weight recency and source quality; do not treat online reviews and direct interviews as identical evidence.
7. Require at least 5–10 real data points in a coherent segment before creating a persona or messaging claim.
