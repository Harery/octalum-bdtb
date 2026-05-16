# Tasks — dotsync — dotfile sync across machines without git

> Ordered, executable task list. `[P]` marks tasks that can run in
> parallel with the previous one. Dependencies noted inline. Composes
> with `/speckit.implement`.

## Phase 0 — Discovery (US-* setup)

- [ ] **T001** Validate the problem statement with 3+ potential users.
- [ ] **T002** [P] Define success metrics (1 north-star + 2 supporting).
- [ ] **T003** Resolve open questions in `research.md` (or explicitly defer).

## Phase 1 — Architecture

- [ ] **T010** Lock the tech stack in `plan.md` (after `/speckit.plan`).
- [ ] **T011** [P] Draft `data-model.md` entities + relationships.
- [ ] **T012** [P] Draft `contracts/` (API/event specs).

## Phase 2 — Design & spike

- [ ] **T020** Wireframe the primary user flow.
- [ ] **T021** [P] Define the API contract end-to-end.
- [ ] **T022** 1-day spike on the highest-risk feature (see `research.md`).

## Phase 3 — Build (feature work)

- [ ] **T030** Implement: `dotsync add ~/.zshrc` registers a file
- [ ] **T031** [P] Implement: `dotsync push` encrypts and uploads diff
- [ ] **T032** [P] Implement: `dotsync pull` fetches and merges, prompting on conflict
- [ ] **T033** [P] Implement: `dotsync watch` runs in background and pushes on save
- [ ] **T034** [P] Implement: Secrets detected via gitleaks-style rules before upload (bail loudly)
- [ ] **T035** [P] Implement: Single binary, no python runtime required on target machines
- [ ] **T036** [P] Implement: Encryption: age (https://age-encryption.org) — battle-tested

## Phase 4 — Integration & test

- [ ] **T040** Contract tests for every entry in `contracts/`.
- [ ] **T041** [P] End-to-end happy-path test for each US-* in `spec.md`.
- [ ] **T042** [P] Dependency scan (Trivy / Snyk / pip-audit).

## Phase 5 — Hardening

- [ ] **T050** Threat-model (STRIDE).
- [ ] **T051** [P] Confirm secrets never hit git (gitleaks in CI).
- [ ] **T052** [P] Accessibility pass (WCAG 2.1 AA).

## Phase 6 — Release

- [ ] **T060** CI: build → test → deploy.
- [ ] **T061** [P] Wire structured logs + traces.
- [ ] **T062** Define rollback procedure.

## Phase 7 — Operate

- [ ] **T070** SLOs + error budget defined.
- [ ] **T071** [P] Alerting wired (PagerDuty / Better Stack / equivalent).
- [ ] **T072** Monthly roadmap review scheduled.

---

_Phase numbering follows the OCTALUM 8-phase SDLC framework so this file
is readable as both a spec-kit `tasks.md` and an OCTALUM phase plan._
