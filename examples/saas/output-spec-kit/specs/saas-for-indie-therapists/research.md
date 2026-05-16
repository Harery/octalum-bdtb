# Research — SaaS for indie therapists

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

- Do I really need separate web + mobile, or is PWA enough?
- Should I use Supabase auth or roll my own?
- Is e2e encryption overkill for session notes?
- - Do I really need separate web + mobile, or is PWA enough?
- - Should I use Supabase auth or roll my own?
- - Is e2e encryption overkill for session notes?

## Risks (extracted from brain-dump)

- Scary thing: HIPAA. If I screw up encryption I am toast.
- Risk: Stripe taking 3% on already-tight margins.

## Rapidly-changing areas to re-check

- LLM providers and pricing (refresh monthly if `--llm` is used)
- Frontend framework majors (Next.js, React)
- Cloud provider managed offerings (managed Postgres, managed auth)

## Spikes scheduled

- [ ] _(1-day spike on the highest-risk feature — see RISKS section)_

---

_Decisions captured here flow back into `plan.md` (Section: Tech stack)._
