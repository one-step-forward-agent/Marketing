# ADR 0003 — LLM provider abstraction

## Status
Accepted for v0.1.

## Context
The first provider is GigaChat, but product/domain code should not depend on provider-specific HTTP contracts.

## Decision
Define an internal `LLMProvider` interface. Implement `GigaChatProvider` as an adapter. FastAPI routes call application services that depend on the interface.

## Alternatives considered
- Call GigaChat directly from routes: fastest first request, highest coupling.
- Multi-provider router immediately: unnecessary complexity before a real second provider exists.

## Consequences
Provider replacement is isolated. Contract tests can use a fake provider without external credentials or network access.
