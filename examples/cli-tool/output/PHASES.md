# PHASES — dotsync — dotfile sync across machines without git

> Mapped onto **OCTALUME**'s 8-phase SDLC framework
> (see https://github.com/Harery/OCTALUME).

## Goals

_(none detected — please review)_

## Features detected

- `dotsync add ~/.zshrc` registers a file
- `dotsync push` encrypts and uploads diff
- `dotsync pull` fetches and merges, prompting on conflict
- `dotsync watch` runs in background and pushes on save
- Secrets detected via gitleaks-style rules before upload (bail loudly)
- Single binary, no python runtime required on target machines
- Encryption: age (https://age-encryption.org) — battle-tested

---

### Phase 0 — Discovery & Framing

*Refine the brain-dump into a problem statement, success metrics, scope.*

  - [ ] Validate problem statement with 3+ potential users
  - [ ] Define success metric (1 north-star + 2 supporting)
  - [ ] Decide build vs. buy for risky components
  - [ ] Resolve open questions (see RISKS.md)

### Phase 1 — Requirements & Architecture

*Translate features into user stories; sketch C4 diagrams; pick stack.*

  - [ ] Pick concrete stack (see STACK.md)
  - [ ] Sketch system context + container diagrams
  - [ ] Write 5 highest-value user stories

### Phase 2 — Design & Prototyping

*Wireframes / API contracts / data model; spike risky unknowns.*

  - [ ] Wireframe primary flow
  - [ ] Define API contract (OpenAPI / GraphQL schema)
  - [ ] Spike highest-risk feature for 1 day

### Phase 3 — Build & Implementation

*Iterative implementation in vertical slices.*

  - [ ] Implement: `dotsync add ~/.zshrc` registers a file
  - [ ] Implement: `dotsync push` encrypts and uploads diff
  - [ ] Implement: `dotsync pull` fetches and merges, prompting on conflict
  - [ ] Implement: `dotsync watch` runs in background and pushes on save
  - [ ] Implement: Secrets detected via gitleaks-style rules before upload (bail loudly)

### Phase 4 — Integration & Testing

*End-to-end tests, contract tests, security scans.*

  - [ ] Add contract tests for public API
  - [ ] End-to-end happy-path test
  - [ ] Run dependency scan (e.g. Snyk, Trivy)

### Phase 5 — Hardening & Compliance

*Threat-model, secrets management, accessibility, perf.*

  - [ ] Threat-model with STRIDE
  - [ ] Confirm secrets never hit git (gitleaks in CI)
  - [ ] Accessibility pass (WCAG 2.1 AA)

### Phase 6 — Deployment & Release

*CI/CD, blue-green or canary, observability wired.*

  - [ ] GitHub Actions: build → test → deploy
  - [ ] Wire structured logs + traces
  - [ ] Define rollback procedure

### Phase 7 — Operate & Iterate

*SLO dashboards, on-call, feedback loops, roadmap refresh.*

  - [ ] Define SLOs and error budget
  - [ ] Set up alerting (PagerDuty / Better Stack)
  - [ ] Schedule monthly roadmap review
