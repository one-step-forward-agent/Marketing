# Primary data flows

## Canonical flow

```text
User Action
  -> Domain Command
  -> State Change
  -> Domain Event
  -> Data Lineage Record
  -> Derived Context / Analytics / LLM Processing
```

## Context restoration

1. User requests context for a task/entity.
2. API validates identity and request scope.
3. Context Management loads durable snapshots/events from PostgreSQL and eligible cached fragments from Redis.
4. Event/Data Lineage supplies provenance links.
5. LLM Orchestration may summarize the selected evidence through `LLMProvider`.
6. Response includes reconstructed context, evidence references and next-step candidate.

## Decision support

1. User submits decision question/options/constraints.
2. Decision Support creates or updates a decision record.
3. Relevant context and prior evidence are resolved through Context Management.
4. LLM Orchestration produces structured alternatives/criteria/recommendation through the provider interface.
5. Decision and derivation metadata persist to PostgreSQL; lightweight async work may be queued in Redis.

## Time & behaviour feedback

1. Activity events are ingested or synthesized into normalized records.
2. Time & Behaviour Analytics aggregates time allocation and fragmentation metrics.
3. Results persist durably in PostgreSQL.
4. Redis can cache recent summaries.
5. User-facing explanations are derived with lineage references so metrics remain inspectable.
