# CustomerDevelopment branch

This branch contains 30 **synthetic** CustDev fixtures used to validate the research pipeline. It now follows stricter research-quality rules inspired by customer-research and interview-to-JTBD workflows.

## Contents
- `interviews/` — 30 structured fixtures with functional/emotional/social jobs, switching forces, alternatives, evidence type and interpretation risk.
- `analysis/evidence-matrix.csv` — normalized traceability table.
- `analysis/segment-analysis.md` — fixture coverage and why it cannot estimate market prevalence.
- `analysis/research-quality.md` — confidence/evidence policy.
- `analysis/research-gaps.md` — highest-risk unknowns to replace with empirical evidence.
- `analysis/next-interview-guide.md` — episode-based guide for the next real CustDev round.
- `analysis/language-hypotheses.md` — synthetic wording to test, explicitly not VOC proof.
- `validate_interviews.py` — schema/integrity validator.

## Integrity rule
No synthetic sentence in this branch may be published as a customer quote, testimonial, prevalence claim, or evidence of product-market fit.
