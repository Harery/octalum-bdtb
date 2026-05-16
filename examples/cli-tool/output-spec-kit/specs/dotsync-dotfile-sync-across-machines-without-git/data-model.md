# Data Model — dotsync — dotfile sync across machines without git

> Schema and core entities. Populate before `/speckit.implement`.

## Entities

| Entity | Fields | Notes |
|--------|--------|-------|
| _(define your core entities here)_ | | |


## Relationships

- _(Draw the foreign-key graph. Mermaid `erDiagram` works in GitHub-rendered MD.)_

```mermaid
erDiagram
    USER ||--o{ SESSION : has
```

## Migrations / change discipline

- Schema changes ship with an explicit migration file.
- Backwards-incompatible columns get a 2-deploy cycle (add → backfill → switch reads → drop).
- Every table has `created_at` and (where mutable) `updated_at`.

## PII / sensitive fields

- Mark every column carrying PII.
- Encryption-at-rest is the default; encryption-in-use only where threat-model demands it.
- Document retention policy per table.
