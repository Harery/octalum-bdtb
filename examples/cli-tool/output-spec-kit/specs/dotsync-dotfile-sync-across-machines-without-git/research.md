# Research — dotsync — dotfile sync across machines without git

> Investigation log: what's known, what's rapidly changing, what needs a spike.
> Spec-kit treats this as a first-class artifact alongside `plan.md`.

## Stack decisions (from `plan.md`)

For each row in `plan.md`'s tech-stack table, document:

1. **Why this** (over the obvious alternatives).
2. **Lock-in score** (1 = trivial swap, 5 = year-long migration).
3. **Last reviewed** (date — re-evaluate quarterly).

| Component | Why | Lock-in | Alternatives | Last reviewed |
|-----------|-----|---------|--------------|---------------|
| _(fill from plan.md)_ |   |   |   | 2026-05-16 |

## Open questions (extracted from brain-dump)

- Rust vs Go?
- Daemon (launchd/systemd) or polling cron?
- How do I distribute the encryption key safely across machines on first setup?
- - Rust vs Go?
- - Daemon (launchd/systemd) or polling cron?
- - How do I distribute the encryption key safely across machines on first setup?

## Risks (extracted from brain-dump)

- Risk: conflict resolution UX is the hardest part. Could ship and have it suck.
- Worry: people will use this as a password manager. It is not one.
- Scary: key loss = total data loss. Need a recovery story.

## Rapidly-changing areas to re-check

- LLM providers and pricing (refresh monthly if `--llm` is used)
- Frontend framework majors (Next.js, React)
- Cloud provider managed offerings (managed Postgres, managed auth)

## Spikes scheduled

- [ ] _(1-day spike on the highest-risk feature — see RISKS section)_

---

_Decisions captured here flow back into `plan.md` (Section: Tech stack)._
