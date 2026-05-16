# STACK — SaaS for indie therapists

> Recommended stack for a **saas** project.

| Concern | Recommendation |
|---------|----------------|
| frontend | Next.js 14 + TypeScript + Tailwind |
| backend | FastAPI (Python) or Node/Express |
| database | PostgreSQL + Prisma/SQLAlchemy |
| auth | Clerk or Auth.js |
| hosting | Vercel (frontend) + Fly.io/Render (backend) |
| payments | Stripe |

## Rationale

- Optimised for **time-to-first-deploy**, not theoretical purity.
- All choices have strong OSS communities (matters when you hit Stack-Overflow-able problems at 2am).
- Every choice is **swappable**: nothing here is locking you in.
- Cybersecurity defaults assumed: managed auth, secrets in env vars / vault,
  HTTPS everywhere, dependency scanning in CI.

## Alternatives to consider

- If team has Rust/Go expertise, replace the API layer accordingly.
- For data-sensitive workloads, prefer self-hostable options (Supabase → Postgres, Clerk → Auth.js).
- If you anticipate strict compliance (HIPAA/SOC2), bias toward AWS/GCP managed services.
