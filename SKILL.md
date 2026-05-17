---
name: octalum-bdtb
description: Use this skill when a user shares a raw, unstructured idea, brain-dump, voice-memo transcript, or rambling project description and wants to turn it into a structured set of Markdown specs compatible with github/spec-kit's spec-driven-development workflow. Triggers include "I have an idea for...", "here's a brain dump", "help me plan this", "turn this into a project", "scaffold a spec-kit feature for...", "octalum-bdtb", or when the user pastes a long unstructured chunk of project thoughts and mentions spec-kit, /speckit.plan, /speckit.tasks, or /speckit.implement. Produces memory/constitution.md and specs/<feature>/{spec,plan,research,data-model,quickstart,tasks}.md plus contracts/, with the OCTALUM 8-phase SDLC mapping preserved inside plan.md.
version: 0.2.0
---

# octalum-bdtb — Brain-Dump → spec-kit-shaped plan

Member of the OCTALUM family (sibling: OCTALUME, OCTALUM-PYLAB, OCTALUM-PULSE).

## When to use

The user has an unstructured idea and wants to feed it into the
[github/spec-kit](https://github.com/github/spec-kit) workflow. They have
NOT yet:

- written a feature spec (`spec.md`)
- locked a tech stack (`plan.md`)
- broken the work into ordered tasks (`tasks.md`)
- captured project principles (`memory/constitution.md`)

If they already have those, skip this skill and route them to
`/speckit.plan`, `/speckit.tasks`, or `/speckit.implement` directly.

## What this skill produces

A spec-kit-compatible filesystem layout, deterministically generated from
the brain-dump:

```
<output-dir>/
├── memory/
│   └── constitution.md      ← 6 governing principles, edit before locking
└── specs/<feature-slug>/
    ├── spec.md              ← What & why (user stories, requirements)
    ├── plan.md              ← How (tech stack + OCTALUM 8-phase mapping)
    ├── research.md          ← Stack decisions, unknowns, spikes
    ├── data-model.md        ← Entities, relations, PII
    ├── quickstart.md        ← Local setup in <10 min
    ├── contracts/README.md  ← Placeholder for API specs
    └── tasks.md             ← Ordered [P]-marked task list
```

Drop `<output-dir>/*` straight into a spec-kit-initialised repo and run
`/speckit.plan` / `/speckit.tasks` / `/speckit.implement`.

## How to invoke (preferred — installed CLI)

If `octalum-bdtb` is installed (`pipx install octalum-bdtb`):

```bash
octalum-bdtb path/to/dump.md --output-dir .            # spec-kit (default)
octalum-bdtb path/to/dump.md --output-dir ./plan \
             --target octalum-classic                  # legacy 5-file shape
```

For a Q&A wizard when the user hasn't written the dump yet:

```bash
octalum-bdtb --mode interactive --output-dir .
```

## How to invoke (inline fallback — no CLI installed)

Claude should perform the same work inline, in this order:

1. **Detect the primary domain** from keyword signals:
   - `saas`: users, billing, stripe, dashboard, auth, tenant
   - `cli`: command line, terminal, stdin, pipe, unix
   - `iot`: sensor, esp32, mqtt, firmware, gpio
   - `data`: etl, warehouse, dbt, airflow, pandas
   - `mobile`: ios, android, react native, flutter
   - `ml`: model, training, embedding, pytorch

2. **Extract** title (first heading or sentence), summary (first paragraph),
   features (bullets without risk/question markers), risks (bullets containing
   "risk/concern/scary"), unknowns (questions, "unclear", "tbd"),
   constraints (must/cannot/deadline/budget).

3. **Render the 8 spec-kit artifacts** following `src/octalum_bdtb/speckit.py`:
   - `memory/constitution.md`: 6 sections (Code Quality, Testing, UX, Performance, Security, Decision Hygiene).
   - `specs/<slug>/spec.md`: summary + user stories synthesised from features (US-01…US-05) + functional requirements + acceptance criteria.
   - `specs/<slug>/plan.md`: tech-stack table from the domain + OCTALUM 8-phase mapping section.
   - `specs/<slug>/research.md`: stack-decision rubric + open questions + risks + spikes.
   - `specs/<slug>/data-model.md`: domain-appropriate entity starter table.
   - `specs/<slug>/quickstart.md`: prerequisites + setup + run + verify.
   - `specs/<slug>/contracts/README.md`: conventions for API/event specs.
   - `specs/<slug>/tasks.md`: Phase 0–7 ordered list with **T0NN** ids and `[P]` parallelism markers.

4. **Write the files** to the user-chosen output directory and print a
   summary: project title, primary domain, list of files written, the
   suggested next step (`open specs/<slug>/spec.md`, then run
   `/speckit.plan`).

## OCTALUM phase mapping (preserved inside `plan.md`)

The 8 phases the generated `plan.md` and `tasks.md` must reference, in order:

0. Discovery & Framing
1. Requirements & Architecture
2. Design & Prototyping
3. Build & Implementation
4. Integration & Testing
5. Hardening & Compliance
6. Deployment & Release
7. Operate & Iterate

## Quality checks before handing back

- [ ] `memory/constitution.md` exists with 6 numbered principles.
- [ ] `specs/<slug>/` contains all 7 expected files (+ `contracts/README.md`).
- [ ] `plan.md` contains an "OCTALUM 8-phase mapping" section that references all 8 phases by number.
- [ ] `tasks.md` uses **T0NN** task ids and includes at least one `[P]` parallel marker.
- [ ] `data-model.md` picked the right starter for the detected domain.
- [ ] `spec.md` synthesised at least 1 user story (US-01) from the brain-dump.

## Composing with spec-kit

The intended downstream workflow:

```text
brain dump  →  octalum-bdtb  →  specs/<feature>/*.md  →  /speckit.plan
                                                      →  /speckit.tasks
                                                      →  /speckit.implement
```

This skill fills the gap **before** `/speckit.specify` — it converts
unstructured prose into structured spec-kit input so the spec-kit
commands have something concrete to refine.

## Out of scope

- Generating actual implementation code (use `/speckit.implement` for that)
- LLM-based deep reasoning (gated behind the `--llm` flag with explicit opt-in)
- Posting anything publicly
- Modifying an existing spec-kit project (`--force` is needed to overwrite)
