<!-- KEYWORDS: idea to code generator, github spec-kit, spec-driven development, spec-kit planner, brain dump to spec, claude code skill, gpt-engineer alternative, brain dump to project plan, unstructured idea to spec, AI project planner, cookiecutter alternative, agentic project generator, phase-0 SDLC, octalum, octalume, project specification generator, brainstorm to backlog, /speckit.plan, /speckit.tasks, /speckit.implement -->

# octalum-bdtb — Brain-Dump → spec-kit-shaped plan

> **Turn a messy brain-dump into a [github/spec-kit](https://github.com/github/spec-kit)-ready feature spec in 60 seconds.** A Claude Code Skill + zero-dependency Python CLI that converts an unstructured idea into `memory/constitution.md` + `specs/<feature>/{spec,plan,research,data-model,quickstart,tasks}.md` — fully offline, no API key required, then hand off to `/speckit.plan` or `/speckit.implement`.

Member of the **OCTALUM** family (siblings: [OCTALUME](https://github.com/Harery/OCTALUME) · [OCTALUM-PYLAB](https://github.com/Harery/OCTALUM-PYLAB) · [OCTALUM-PULSE](https://github.com/Harery/OCTALUM-PULSE)).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/Harery/octalum-bdtb/actions/workflows/ci.yml/badge.svg)](https://github.com/Harery/octalum-bdtb/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![pipx](https://img.shields.io/badge/install-pipx-3776AB.svg)](https://pypa.github.io/pipx/)
[![PyPI](https://img.shields.io/pypi/v/octalum-bdtb.svg)](https://pypi.org/project/octalum-bdtb/)

`octalum-bdtb` is an **AI project planner** for the messiest moment in a project — between "I had an idea in the shower" and "I'm ready to write code." It is the **Phase-0 feeder** for [github/spec-kit](https://github.com/github/spec-kit)'s spec-driven-development workflow: instead of you hand-authoring `spec.md`/`plan.md`/`tasks.md`, you paste your brain dump and the tool emits a complete spec-kit feature folder, plus an `OCTALUM 8-phase` overlay inside `plan.md` so the two methodologies compose.

## Composes with github/spec-kit

```
brain dump ── octalum-bdtb ──▶ specs/<feature>/spec.md
                             │
                             ├─▶ specs/<feature>/plan.md         (incl. OCTALUM 8-phase overlay)
                             ├─▶ specs/<feature>/research.md
                             ├─▶ specs/<feature>/data-model.md
                             ├─▶ specs/<feature>/quickstart.md
                             ├─▶ specs/<feature>/tasks.md
                             ├─▶ specs/<feature>/contracts/
                             └─▶ memory/constitution.md
                                          │
                                          └─▶ /speckit.plan ▶ /speckit.tasks ▶ /speckit.implement
```

A worked example lives at [`examples/saas/output-spec-kit/`](examples/saas/output-spec-kit/) — every file the spec-kit `/speckit.*` commands expect, generated from a single 30-line brain dump.

See [ALIGNMENT.md](ALIGNMENT.md) for the full mapping table and the gaps closed in v0.2.0.

## Two output targets

| `--target` | When to use | Writes to `<output-dir>/` |
|---|---|---|
| `spec-kit` *(default)* | You're using github/spec-kit, Claude Code, or any agentic tool that consumes spec-kit-shaped Markdown. | `memory/constitution.md` + `specs/<feature>/{spec,plan,research,data-model,quickstart,tasks}.md` + `contracts/` |
| `octalum-classic` | You want the original 5-file output for human review or to feed straight into [OCTALUME](https://github.com/Harery/OCTALUME) without spec-kit. | `STRUCTURE.md` · `STACK.md` · `PHASES.md` · `RISKS.md` · `BUILD_NOW.sh` |

Both targets are deterministic, offline, and use zero LLM tokens. Pass `--llm` to enrich (stub today; wired in v0.2.x).

## Install

```bash
pipx install octalum-bdtb
```

Or pip / from source:

```bash
pip install octalum-bdtb
# or
git clone https://github.com/Harery/octalum-bdtb
cd octalum-bdtb && pip install -e .
```

## Quickstart — from prompt to project in 3 commands

```bash
echo "# Cat-sitter SaaS\nA marketplace for indie cat-sitters with Stripe billing." > dump.md
octalum-bdtb dump.md --output-dir ./plan
ls ./plan/specs/*/
# spec.md  plan.md  research.md  data-model.md  quickstart.md  tasks.md  contracts/
# Plus ./plan/memory/constitution.md — drop the whole tree into your spec-kit-enabled repo.
```

Need the classic 5-file output instead? Add `--target octalum-classic`:

```bash
octalum-bdtb dump.md --target octalum-classic --output-dir ./plan
# STRUCTURE.md  STACK.md  PHASES.md  RISKS.md  BUILD_NOW.sh
```

Pipe from clipboard or another command:

```bash
pbpaste | octalum-bdtb - --output-dir ./plan
```

Don't have a dump yet? Use **interactive Q&A mode**:

```bash
octalum-bdtb --mode interactive --output-dir ./plan
```

## Before & after — unstructured idea to spec

**Input** (`examples/saas/brain-dump.md`, excerpt):

```text
# SaaS for indie therapists

My sister is a therapist and she keeps complaining that all the
practice-management SaaS out there is bloated…

She wants to:
- log sessions with clients (encrypted at rest)
- send invoices via Stripe
- schedule appointments (calendar sync)
- HIPAA-ish privacy even though we're not pursuing full compliance day 1

Risks:
- Scary thing: HIPAA. If I screw up encryption I am toast.
- Risk: Stripe taking 3% on already-tight margins.
```

**Output** (`examples/saas/output/PHASES.md`, excerpt):

```markdown
# PHASES — SaaS for indie therapists

> Mapped onto **OCTALUME**'s 8-phase SDLC framework.

### Phase 0 — Discovery & Framing
  - [ ] Validate problem statement with 3+ potential users
  - [ ] Define success metric (1 north-star + 2 supporting)
  - [ ] Decide build vs. buy for risky components
  - [ ] Resolve open questions (see RISKS.md)

### Phase 3 — Build & Implementation
  - [ ] Implement: log sessions with clients (encrypted at rest)
  - [ ] Implement: send invoices via Stripe
  - [ ] Implement: schedule appointments (calendar sync)
  …
```

Full outputs: [`examples/saas/output/`](examples/saas/output/), [`examples/cli-tool/output/`](examples/cli-tool/output/), [`examples/iot/output/`](examples/iot/output/).

## Use it as a Claude Code Skill

This project ships as a **Claude Code Skill**, so you can call it from inside any Claude Code conversation:

```bash
cp SKILL.md ~/.claude/skills/octalum-bdtb.md
```

Then say *"I have a brain dump, turn it into a project plan"* and Claude will invoke the skill — calling the CLI if installed, or producing the same artifacts inline if not. See [SKILL.md](SKILL.md) for the skill manifest.

## Modes

| Mode | Use when |
|---|---|
| `quick` (default) | You have a written dump — just give me the plan. |
| `bootstrap` | Also generate a runnable `BUILD_NOW.sh` to scaffold. |
| `interactive` | You don't have a dump yet — walk me through a Q&A. |

## Comparison — how it stacks up

|  | octalum-bdtb | gpt-engineer | Aider | Cookiecutter |
|---|---|---|---|---|
| Input | Free-form text | Spec prompt | Existing repo | Variables |
| Output | Plan + scaffold | Full app code | Diffs to existing code | Templated repo |
| Offline (no API key) | **Yes (default)** | No | No | Yes |
| OCTALUME-aware | **Yes** | No | No | No |
| Claude Code Skill | **Yes** | No | No | No |
| Sweet spot | Phase 0 / pre-spec | Phase 3 build | Phase 3-4 edit | Phase 1 scaffold |

`octalum-bdtb` is deliberately the *earliest* tool in your toolchain — before you know your stack, before you have a spec.

## FAQ

### How is this different from gpt-engineer?

**gpt-engineer** takes a polished prompt and *writes the app*. `octalum-bdtb` takes a messy idea and *writes the plan*. Different phase, different deliverable. Use octalum-bdtb first, then feed `STRUCTURE.md` and `PHASES.md` into gpt-engineer (or Aider, or Claude Code) as the spec.

### Do I need an API key?

**No.** The default path is 100% deterministic templates — no LLM, no key, no network. The optional `--llm` flag (Claude / OpenAI / Ollama) is opt-in.

### Can I use it with Claude Code?

**Yes.** Copy [`SKILL.md`](SKILL.md) into `~/.claude/skills/` and Claude Code will invoke the skill automatically when you describe an idea. No subscription required beyond Claude itself.

### What gets generated?

Five files: `STRUCTURE.md` (folder layout), `STACK.md` (tech picks), `PHASES.md` (OCTALUME phased task list), `RISKS.md` (risks register), and `BUILD_NOW.sh` (executable scaffold script). See [the outputs section](#what-you-get-the-5-outputs) above.

### Does it support language X?

The tool itself is language-agnostic — it picks a stack from your dump (Python, TypeScript, Go, Rust, embedded C, etc.). v0.1.0 ships templates for 6 domains: SaaS, CLI tool, IoT, browser extension, ML pipeline, and generic. Submit a PR to add yours; see `examples/` for the fixture format.

### Is this a cookiecutter alternative?

Partly. Cookiecutter scaffolds from a *known* template with variables. octalum-bdtb *picks the template* from prose first, then scaffolds. Use cookiecutter when you know what you want; use this when you don't.

### Why "Phase 0"?

OCTALUME (the parent framework) numbers SDLC stages 0–7. Phase 0 is *Discovery & Framing* — the only phase that starts with no artifacts at all. That's the gap this tool fills.

### How big can my brain-dump be?

Tested up to 10 MB. The parser is O(n) and ships no LLM tokens, so cost scales with disk I/O, not API bill.

## LLM enrichment (optional)

```bash
export ANTHROPIC_API_KEY=sk-ant-…
octalum-bdtb dump.md --llm claude-sonnet
```

The `--llm` flag is **wired but not implemented** in v0.1.0 — the stub prints a notice and falls back to deterministic templates. v0.2.0 will wire Claude + Ollama.

## The OCTALUME family

This project is **Phase 0** for [OCTALUME](https://github.com/Harery/OCTALUME), an 8-phase SDLC framework by the same author. The generated `PHASES.md` is structured to drop straight into an OCTALUME workspace.

```
octalum-bdtb  →  OCTALUME  →  ship
  (Phase 0)             (Phases 1-7)
```

## Roadmap

- **v0.1** (2026-05): Deterministic templates, 6 domains, Claude Code Skill. *(this release)*
- **v0.2** (2026-06): `--llm` actually wired (Anthropic + Ollama).
- **v0.3** (2026-07): More domains (browser ext, game dev, agent).
- **v0.4** (2026-08): OCTALUME workspace exporter (`--export octalume`).
- **v0.5** (2026-09): VS Code extension.
- **v1.0** (2026-Q4): Stable schema, plugin API for custom templates.

## Contributing

PRs welcome. Please:

1. Open an issue first for non-trivial changes.
2. `pytest -q --cov=octalum_bdtb` must pass with ≥80% coverage.
3. `ruff check src tests` and `mypy src` must be clean.
4. New domain? Add a fixture in `examples/` showing input + output.

See [PUBLISHING.md](PUBLISHING.md) for the PyPI/OIDC release flow.

## License

MIT © 2026 Mohamed Harery — [harery.com](https://harery.com)
