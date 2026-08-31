# Segment analysis — synthetic design check

> This file describes fixture coverage, not real market segmentation. The corpus is intentionally balanced and therefore cannot estimate frequency or prevalence.

## Coverage by persona/segment

| Segment | Fixtures | Context | Decision | Time feedback |
|---|---:|---:|---:|---:|
| Consultant | 3 | 1 | 1 | 1 |
| Founder | 3 | 1 | 1 | 1 |
| Freelancer | 3 | 1 | 1 | 1 |
| Knowledge worker | 3 | 1 | 1 | 1 |
| Marketing lead | 3 | 1 | 1 | 1 |
| Operations manager | 3 | 1 | 1 | 1 |
| Product manager | 3 | 1 | 1 | 1 |
| Researcher | 3 | 1 | 1 | 1 |
| Software engineer | 3 | 1 | 1 | 1 |
| Team lead | 3 | 1 | 1 | 1 |

## Design implication

Each persona has one fixture per JTBD (3 fixtures × 10 personas). That symmetry is useful for parser/analytics coverage but destroys any ability to infer which segment or job is naturally more common. Real discovery should deliberately break this symmetry by sampling actual episodes and allowing job frequency to emerge from data.

## Candidate segment hypotheses to test first

1. Product managers / founders with multiple concurrent initiatives and frequent return-to-context moments.
2. Consultants / team leads with handoffs, client context, and decision accountability.
3. Researchers / operators with evidence-heavy decisions and recurring weekly review needs.
