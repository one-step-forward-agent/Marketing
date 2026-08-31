# Initial Product Backlog — 24 hypotheses

> Research integrity: all current evidence links resolve to synthetic fixtures. Confidence is deliberately capped below 0.5 until empirical evidence replaces or corroborates the fixtures.

## Prioritization

- Expected impact: 1–10.
- Implementation complexity: 1–10.
- Confidence: evidence-weighted 0.00–1.00; current values are synthetic-stage and therefore low.
- Priority: `(Expected Impact × Confidence) / Implementation Complexity`.
- Tie-breaker: hypothesis ID ascending.

| ID | Hypothesis | JTBD | Impact | Complexity | Confidence | Priority | Evidence |
|---|---|---|---:|---:|---:|---:|---|
| H009 | Explicit decision criteria matrix | `decision-support` | 10 | 4 | 0.34 | 0.850 | synthetic-only |
| H017 | Goal-vs-time weekly review | `time-feedback` | 10 | 4 | 0.34 | 0.850 | synthetic-only |
| H002 | Source-linked decision history | `context-restoration` | 9 | 4 | 0.33 | 0.743 | synthetic-only |
| H007 | Context confidence indicator | `context-restoration` | 7 | 3 | 0.30 | 0.700 | synthetic-only |
| H001 | Automatic task context recap | `context-restoration` | 10 | 5 | 0.34 | 0.680 | synthetic-only |
| H014 | Decision deadline guardrail | `decision-support` | 7 | 3 | 0.28 | 0.653 | synthetic-only |
| H024 | Evidence-linked coaching prompt | `time-feedback` | 7 | 3 | 0.27 | 0.630 | synthetic-only |
| H011 | Reversible decision mode | `decision-support` | 8 | 4 | 0.31 | 0.620 | synthetic-only |
| H010 | Evidence-backed recommendation | `decision-support` | 9 | 5 | 0.34 | 0.612 | synthetic-only |
| H003 | Next meaningful step suggestion | `context-restoration` | 9 | 5 | 0.31 | 0.558 | synthetic-only |
| H021 | Deep-work evidence window | `time-feedback` | 7 | 4 | 0.28 | 0.490 | synthetic-only |
| H015 | Alternative generation with constraints | `decision-support` | 8 | 5 | 0.30 | 0.480 | synthetic-only |
| H018 | Unplanned work classification | `time-feedback` | 9 | 6 | 0.31 | 0.465 | synthetic-only |
| H019 | Attention fragmentation score | `time-feedback` | 8 | 5 | 0.29 | 0.464 | synthetic-only |
| H016 | Pre-mortem on selected option | `decision-support` | 7 | 4 | 0.26 | 0.455 | synthetic-only |
| H020 | Priority drift alerts | `time-feedback` | 8 | 5 | 0.28 | 0.448 | synthetic-only |
| H005 | Context snapshot on task switch | `context-restoration` | 8 | 6 | 0.30 | 0.400 | synthetic-only |
| H012 | Decision journal with outcome review | `decision-support` | 8 | 6 | 0.29 | 0.387 | synthetic-only |
| H006 | Open-loop detection | `context-restoration` | 8 | 6 | 0.28 | 0.373 | synthetic-only |
| H004 | Cross-source context timeline | `context-restoration` | 8 | 7 | 0.29 | 0.331 | synthetic-only |
| H013 | Contradiction detector | `decision-support` | 8 | 7 | 0.27 | 0.309 | synthetic-only |
| H008 | Selective context forgetting | `context-restoration` | 6 | 5 | 0.25 | 0.300 | synthetic-only |
| H023 | Behavioral baseline and trend | `time-feedback` | 8 | 7 | 0.26 | 0.297 | synthetic-only |
| H022 | Meeting cost reflection | `time-feedback` | 7 | 6 | 0.25 | 0.292 | synthetic-only |

## Decision rule

This ranking decides **experiment order**, not what to build. A hypothesis may only move toward implementation when real evidence raises confidence and the pre-registered experiment threshold is met without violating trust/privacy guardrails.
