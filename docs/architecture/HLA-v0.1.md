# High-Level Architecture v0.1

## Objective

Support three product outcomes: restore context, support evidence-based decisions, and provide objective time-use feedback while preserving traceability from derived insight back to source events.

## Bounded contexts

1. **Interaction / Frontend** — presentation, navigation, user input, explanation surfaces.
2. **API / Identity** — HTTP boundary, request validation, minimal identity/session abstraction.
3. **Context Management** — context snapshots, open loops, source-linked reconstruction.
4. **Decision Support** — alternatives, criteria, evidence, recommendations, decision records.
5. **Time & Behaviour Analytics** — activity aggregation, time allocation, fragmentation and trend metrics.
6. **LLM Orchestration** — prompt construction, provider boundary, structured generation, provider errors.
7. **Event / Data Lineage** — domain-event capture, provenance metadata, derivation links and auditability.

## Logical component view

```text
Interaction / Frontend
        |
        v
API / Identity
   |         |
   v         v
Context   Decision Support
   |         |
   +----+----+
        |
        v
Time & Behaviour Analytics
        |
        +----------> LLM Orchestration
        |                    |
        +----------+---------+
                   v
            Event / Data Lineage
               |          |
               v          v
           PostgreSQL    Redis
```

## Storage ownership

- **PostgreSQL:** durable primary state, domain entities, decision records, context snapshots, analytics records and lineage metadata.
- **Redis:** ephemeral cache plus lightweight queue/event transport for v0.1. Cache and queue namespaces are separated.

## Architecture constraints

- Domain/application code depends on an `LLMProvider` interface, never a concrete GigaChat HTTP client.
- Every derived recommendation or analytics result should be able to reference input event/record identifiers through lineage metadata.
- Redis is not the system of record.
- Kafka/RabbitMQ are excluded until measured delivery or throughput requirements justify them.
