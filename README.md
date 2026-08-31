# JobesToBeDone

Reproducible JTBD opportunity analysis derived from the synthetic `CustomerDevelopment` branch.

> The spelling `JobesToBeDone` is retained intentionally. All outputs are analytical fixtures and candidate value propositions, not scientifically validated USPs.

## Run

```bash
python -m src.extract_jtbd
python -m src.generate_all_diagrams
python -m pytest tests -q
```

Generated charts are committed under `Diagrams/`.
