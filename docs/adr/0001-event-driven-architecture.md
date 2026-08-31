# ADR 0001 — Event-driven architecture

## Status
Accepted for v0.1.

## Context
Context restoration, decision records, analytics and LLM derivations must react to user actions without tightly coupling all bounded contexts.

## Decision
Represent meaningful state transitions as domain events. Persist durable domain state in PostgreSQL; use Redis as lightweight queue/event transport where asynchronous processing is useful.

## Alternatives considered
- Direct synchronous calls between all contexts: simpler initially but creates coupling and weakens lineage.
- Kafka/RabbitMQ: stronger broker semantics but unjustified operational complexity for v0.1.

## Consequences
Events become explicit contracts and lineage anchors. Consumers must be idempotent where retries are possible. Redis delivery limitations are accepted until measured requirements justify a dedicated broker.
