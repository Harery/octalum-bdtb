---
name: brain-dump-to-build
description: Use this skill when a user shares a raw, unstructured idea, brain-dump, voice-memo transcript, or rambling project description and wants to turn it into a structured, buildable project plan. Triggers include "I have an idea for...", "here's a brain dump", "help me plan this", "turn this into a project", "what should I build first", or when the user pastes a long unstructured chunk of project thoughts. Produces STRUCTURE.md, STACK.md, PHASES.md, RISKS.md, and an optional BUILD_NOW.sh bootstrap, mapped onto the OCTALUME 8-phase SDLC framework.
version: 0.1.0
---

# brain-dump-to-build

## When to use

The user has an unstructured idea and needs structure. They have NOT yet:
- decided on a stack
- written user stories
- broken the work into phases
- identified explicit risks

If they already have a spec, skip this skill and go straight to implementation.

## What this skill does

Turns raw text into 5 markdown artifacts:

| File | Purpose |
|------|---------|
| `STRUCTURE.md` | Proposed file/folder tree + rationale |
| `STACK.md`     | Recommended tech stack |
| `PHASES.md`    | Task list mapped onto OCTALUME's 8 SDLC phases |
| `RISKS.md`     | Risks, unknowns, open decisions |
| `BUILD_NOW.sh` | Optional bootstrap script |

## How to invoke (preferred)

If the `brain-dump-to-build` CLI is installed (`pipx install brain-dump-to-build`):

```bash
brain-dump-to-build path/to/dump.md --output-dir ./plan
```

For interactive Q&A when the user hasn't written the dump yet:

```bash
brain-dump-to-build --mode interactive --output-dir ./plan
```

## How to invoke (inline fallback)

If the CLI is not installed, Claude should perform the same work inline:

1. **Detect the primary domain** from keyword signals:
   - saas: users, billing, stripe, dashboard, auth, tenant
   - cli: command line, terminal, stdin, pipe, unix
   - iot: sensor, esp32, mqtt, firmware, gpio
   - data: etl, warehouse, dbt, airflow, pandas
   - mobile: ios, android, react native, flutter
   - ml: model, training, embedding, pytorch

2. **Extract** title (first heading or sentence), summary (first paragraph),
   features (bullets without risk/question markers), risks (bullets containing
   "risk/concern/scary"), unknowns (questions, "unclear", "tbd"),
   constraints (must/cannot/deadline/budget).

3. **Render the 5 artifacts** following the templates in
   `brain_dump_to_build/templates.py` — STRUCTURE.md gets a domain-appropriate
   tree, STACK.md a table, PHASES.md the 8 OCTALUME phases with concrete
   per-phase tasks seeded from the detected features.

4. **Write the files** to a user-chosen output directory. Print a summary:
   project title, primary domain, list of files written.

## OCTALUME phase mapping

The 8 phases the generated PHASES.md must reference, in order:

0. Discovery & Framing
1. Requirements & Architecture
2. Design & Prototyping
3. Build & Implementation
4. Integration & Testing
5. Hardening & Compliance
6. Deployment & Release
7. Operate & Iterate

## Quality checks before handing back

- [ ] All 5 files exist in `--output-dir`
- [ ] `BUILD_NOW.sh` is `chmod +x`
- [ ] STACK.md picks one concrete option per concern (not "X or Y or Z")
- [ ] RISKS.md has at least 3 risks (synthesise reasonable ones if the dump didn't supply any)
- [ ] PHASES.md references OCTALUME by name and links to Harery/OCTALUME

## Out of scope

- Generating actual code (use OCTALUME Phase 3 for that)
- LLM-based deep reasoning (gated behind `--llm` flag with explicit opt-in)
- Posting anything publicly
