# Contracts — SaaS for indie therapists

> External-facing contracts. Drop API specs, event schemas, and RPC
> definitions here. Spec-kit's `/speckit.implement` reads from this folder.

## Conventions

- One file per externally-visible surface.
- OpenAPI 3.1 → `api-spec.yaml` or `api-spec.json`.
- AsyncAPI 2.x → `events.yaml`.
- Proto / gRPC → `*.proto`.
- WebSocket / SignalR → `signalr-spec.md`.

## What lives here vs. inline

- **Lives here:** anything another team / system consumes.
- **Inline (in code):** internal-only DTOs, private RPCs.

## Starter

Replace this file with the appropriate spec for `saas`:

- `saas` → `api-spec.yaml` (REST) + optional `events.yaml`
- `iot`  → MQTT topic catalog (`mqtt-topics.md`)
- `data` → `events.yaml` (Kafka/PubSub) + `dbt-contracts.yaml`
- `cli`  → `cli-contract.md` (flag/arg surface — yes, that's a contract too)
- `ml`   → `inference-api.yaml`
