# ADR 0002 — Data lineage model

## Status
Accepted for v0.1.

## Context
The product must provide objective feedback and AI-assisted conclusions without making those conclusions opaque.

## Decision
Every derived record carries identifiers for its source events/records, derivation type, timestamp and producer. Lineage metadata is durable in PostgreSQL.

## Alternatives considered
- Store only final summaries: lower storage cost but no explainability/audit path.
- Full external data-catalog platform: excessive for v0.1.

## Consequences
Derived insights can be inspected and recomputed. Data retention and source-identifier handling become explicit engineering concerns.
