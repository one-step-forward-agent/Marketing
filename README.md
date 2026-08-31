# JobesToBeDone

Reproducible JTBD/outcome analysis derived directly from the `CustomerDevelopment` Git branch.

> The spelling `JobesToBeDone` is intentionally preserved from the project requirement. All current scores and diagrams are synthetic pipeline outputs, not validated market evidence.

## Run

```bash
python -m src.extract_jtbd
python -m src.generate_all_diagrams
python -m pytest tests -q
```

The canonical `data/jtbd_scores.csv` is produced by `aggregate_jtbd_scores()` from the extracted branch data before diagrams are regenerated.

## Research artifacts
- `outcome-map.md` — functional/emotional/social jobs and measurable outcomes.
- `methodology.md` — scientific-method guardrails and evidence grading.
- `evidence-readiness.md` — explicit synthetic-vs-empirical state.
- `validation-protocol.md` — falsifiable tests with pre-declared thresholds.
- `candidate-usp.md` — candidate value propositions and combined evidence-layer hypothesis.
- `Diagrams/` — six required descriptive charts, each marked as synthetic.
