# STACK — dotsync — dotfile sync across machines without git

> Recommended stack for a **cli** project.

| Concern | Recommendation |
|---------|----------------|
| language | Python 3.11+ with Click or Typer |
| packaging | pyproject.toml, pipx-distributable |
| testing | pytest |
| ci | GitHub Actions |

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
