# Hypotheses

This branch converts JTBD observations into a traceable, experiment-oriented Product Backlog and HLA v0.1.

## What changed in v0.2

- every hypothesis links to explicit `CustomerDevelopment` source IDs;
- current evidence state is `synthetic-only`;
- confidence values are intentionally reduced/capped until empirical evidence exists;
- each hypothesis now has a behavioral prediction, pre-registered threshold and negative evidence to capture;
- `evidence-to-hypothesis-map.csv` provides machine-readable lineage;
- `experiment-register.md` and `learning-roadmap.md` sequence learning instead of feature accumulation;
- `docs/architecture/research-to-product-flow.md` defines promotion gates from research to build.

## Prioritization

```text
Priority = (Expected Impact × Confidence) / Implementation Complexity
```

The ranking determines experiment order. It is not evidence of product-market fit and does not authorize implementation by itself.
