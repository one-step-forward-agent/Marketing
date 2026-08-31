# ADR 0004 — Context snapshot model

## Status
Accepted for v0.1.

## Context
Raw event history can be too large and noisy for fast context restoration, while summaries alone lose traceability.

## Decision
Maintain source-linked context snapshots as derived durable records. A snapshot contains scope/entity, summary, open loops, source lineage identifiers, creation time and evidence coverage metadata.

## Alternatives considered
- Reconstruct from all raw events on every request: simple storage model but high latency/cost.
- Keep summaries only in cache: low latency but weak durability and lineage guarantees.

## Consequences
Snapshots require invalidation/recomputation rules. Their source links let users inspect why a reconstructed context contains each claim.
