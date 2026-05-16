# Implementation Plan — dotsync — dotfile sync across machines without git

> **How** we will build what `spec.md` describes. Tech stack, architecture,
> and the cross-walk to the OCTALUM 8-phase SDLC framework.

## Tech stack (recommended)

| Concern | Choice |
|---------|--------|
| language | Python 3.11+ with Click or Typer |
| packaging | pyproject.toml, pipx-distributable |
| testing | pytest |
| ci | GitHub Actions |

_Rationale: optimised for time-to-first-deploy on `cli` workloads.
Every entry is swappable — see `research.md` for the trade-offs._

## Architecture sketch

- **Entry point(s):** depends on domain — for `cli`, see the tree below.
- **State / persistence:** see `data-model.md`.
- **External contracts:** see `contracts/` (API specs, event schemas).
- **Deployment target:** see the "hosting" / "ci" row in the stack table above.

## Suggested repo layout

See [`spec.md`](spec.md) "out of scope" before committing to this tree.
A starter layout for `cli` projects:

```
dotsync-dotfile-sync-across-machines-without-git/
├── src/
├── tests/
├── docs/
└── README.md
```

(For a fuller domain-specific tree, run `octalum-bdtb … --target octalum-classic`
and consult the generated `STRUCTURE.md`.)

## OCTALUM 8-phase mapping

> `octalum-bdtb` was born inside the OCTALUM family. The 8 phases below are
> preserved here so the OCTALUM methodology *composes* with spec-kit's
> `/speckit.tasks` and `/speckit.implement` commands — they don't conflict.

- **Phase 0 — Discovery & Framing** — Refine the brain-dump into a problem statement, success metrics, scope.
- **Phase 1 — Requirements & Architecture** — Translate features into user stories; sketch C4 diagrams; pick stack.
- **Phase 2 — Design & Prototyping** — Wireframes / API contracts / data model; spike risky unknowns.
- **Phase 3 — Build & Implementation** — Iterative implementation in vertical slices.
- **Phase 4 — Integration & Testing** — End-to-end tests, contract tests, security scans.
- **Phase 5 — Hardening & Compliance** — Threat-model, secrets management, accessibility, perf.
- **Phase 6 — Deployment & Release** — CI/CD, blue-green or canary, observability wired.
- **Phase 7 — Operate & Iterate** — SLO dashboards, on-call, feedback loops, roadmap refresh.

`tasks.md` (in this same directory) is the spec-kit-native flattening of
phases 0–3; phases 4–7 are tracked at the OCTALUM workspace level. See
https://github.com/Harery/OCTALUME for the parent framework.

## Open questions blocking this plan

- Rust vs Go?
- Daemon (launchd/systemd) or polling cron?
- How do I distribute the encryption key safely across machines on first setup?
- - Rust vs Go?
- - Daemon (launchd/systemd) or polling cron?
- - How do I distribute the encryption key safely across machines on first setup?

---

_Next: refine with `/speckit.plan`, then generate `tasks.md` with `/speckit.tasks`._
