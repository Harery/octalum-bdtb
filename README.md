<!-- KEYWORDS: idea to code generator, gpt-engineer alternative, claude code skill, brain dump to project plan, unstructured idea to spec, project scaffolding tool, AI project planner, cookiecutter alternative, from prompt to project, agentic project generator, phase-0 SDLC, project specification generator, idea to spec, brainstorm to backlog, project bootstrap CLI -->

# brain-dump-to-build — idea to code generator and project planner

> **Turn a messy brain-dump into a structured, buildable project in 60 seconds.** A Claude Code Skill + zero-dependency Python CLI that converts an unstructured idea into a folder structure, stack pick, phased task list, risks register, and bootstrap script — fully offline, no API key required.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/Harery/brain-dump-to-build/actions/workflows/ci.yml/badge.svg)](https://github.com/Harery/brain-dump-to-build/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![pipx](https://img.shields.io/badge/install-pipx-3776AB.svg)](https://pypa.github.io/pipx/)
[![PyPI](https://img.shields.io/pypi/v/brain-dump-to-build.svg)](https://pypi.org/project/brain-dump-to-build/)

`brain-dump-to-build` is an **AI project planner** for the messiest moment in a project — the moment between "I had an idea in the shower" and "I'm ready to write code." It is a [gpt-engineer alternative](#how-is-this-different-from-gpt-engineer) for **Phase 0** of the SDLC: instead of generating an entire app, it generates a *plan* you can hand to humans, to [OCTALUME](https://github.com/Harery/OCTALUME), or to any agentic coding tool.

## What you get (the 5 outputs)

Run it on a rambling markdown file and get back, in `./plan/`:

| File | What it is |
|---|---|
| `STRUCTURE.md` | Recommended folder/file layout for the project |
| `STACK.md` | Language, framework, datastore, deploy target picks with rationale |
| `PHASES.md` | Task list mapped onto OCTALUME's 8-phase SDLC framework |
| `RISKS.md` | Risks, unknowns, and constraints extracted from your dump |
| `BUILD_NOW.sh` | Executable shell script to scaffold the repo on disk |

Deterministic, offline, zero LLM tokens spent. Pass `--llm` to enrich with Claude/GPT/Ollama (stub in v0.1.0, wired in v0.2.0).

## Install

```bash
pipx install brain-dump-to-build
```

Or pip / from source:

```bash
pip install brain-dump-to-build
# or
git clone https://github.com/Harery/brain-dump-to-build
cd brain-dump-to-build && pip install -e .
```

## Quickstart — from prompt to project in 3 commands

```bash
echo "# Cat-sitter SaaS\nA marketplace for indie cat-sitters with Stripe billing." > dump.md
brain-dump-to-build dump.md --output-dir ./plan
ls ./plan
# STRUCTURE.md  STACK.md  PHASES.md  RISKS.md  BUILD_NOW.sh
```

Pipe from clipboard or another command:

```bash
pbpaste | brain-dump-to-build - --output-dir ./plan
```

Don't have a dump yet? Use **interactive Q&A mode**:

```bash
brain-dump-to-build --mode interactive --output-dir ./plan
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
cp SKILL.md ~/.claude/skills/brain-dump-to-build.md
```

Then say *"I have a brain dump, turn it into a project plan"* and Claude will invoke the skill — calling the CLI if installed, or producing the same artifacts inline if not. See [SKILL.md](SKILL.md) for the skill manifest.

## Modes

| Mode | Use when |
|---|---|
| `quick` (default) | You have a written dump — just give me the plan. |
| `bootstrap` | Also generate a runnable `BUILD_NOW.sh` to scaffold. |
| `interactive` | You don't have a dump yet — walk me through a Q&A. |

## Comparison — how it stacks up

|  | brain-dump-to-build | gpt-engineer | Aider | Cookiecutter |
|---|---|---|---|---|
| Input | Free-form text | Spec prompt | Existing repo | Variables |
| Output | Plan + scaffold | Full app code | Diffs to existing code | Templated repo |
| Offline (no API key) | **Yes (default)** | No | No | Yes |
| OCTALUME-aware | **Yes** | No | No | No |
| Claude Code Skill | **Yes** | No | No | No |
| Sweet spot | Phase 0 / pre-spec | Phase 3 build | Phase 3-4 edit | Phase 1 scaffold |

`brain-dump-to-build` is deliberately the *earliest* tool in your toolchain — before you know your stack, before you have a spec.

## FAQ

### How is this different from gpt-engineer?

**gpt-engineer** takes a polished prompt and *writes the app*. `brain-dump-to-build` takes a messy idea and *writes the plan*. Different phase, different deliverable. Use brain-dump-to-build first, then feed `STRUCTURE.md` and `PHASES.md` into gpt-engineer (or Aider, or Claude Code) as the spec.

### Do I need an API key?

**No.** The default path is 100% deterministic templates — no LLM, no key, no network. The optional `--llm` flag (Claude / OpenAI / Ollama) is opt-in.

### Can I use it with Claude Code?

**Yes.** Copy [`SKILL.md`](SKILL.md) into `~/.claude/skills/` and Claude Code will invoke the skill automatically when you describe an idea. No subscription required beyond Claude itself.

### What gets generated?

Five files: `STRUCTURE.md` (folder layout), `STACK.md` (tech picks), `PHASES.md` (OCTALUME phased task list), `RISKS.md` (risks register), and `BUILD_NOW.sh` (executable scaffold script). See [the outputs section](#what-you-get-the-5-outputs) above.

### Does it support language X?

The tool itself is language-agnostic — it picks a stack from your dump (Python, TypeScript, Go, Rust, embedded C, etc.). v0.1.0 ships templates for 6 domains: SaaS, CLI tool, IoT, browser extension, ML pipeline, and generic. Submit a PR to add yours; see `examples/` for the fixture format.

### Is this a cookiecutter alternative?

Partly. Cookiecutter scaffolds from a *known* template with variables. brain-dump-to-build *picks the template* from prose first, then scaffolds. Use cookiecutter when you know what you want; use this when you don't.

### Why "Phase 0"?

OCTALUME (the parent framework) numbers SDLC stages 0–7. Phase 0 is *Discovery & Framing* — the only phase that starts with no artifacts at all. That's the gap this tool fills.

### How big can my brain-dump be?

Tested up to 10 MB. The parser is O(n) and ships no LLM tokens, so cost scales with disk I/O, not API bill.

## LLM enrichment (optional)

```bash
export ANTHROPIC_API_KEY=sk-ant-…
brain-dump-to-build dump.md --llm claude-sonnet
```

The `--llm` flag is **wired but not implemented** in v0.1.0 — the stub prints a notice and falls back to deterministic templates. v0.2.0 will wire Claude + Ollama.

## The OCTALUME family

This project is **Phase 0** for [OCTALUME](https://github.com/Harery/OCTALUME), an 8-phase SDLC framework by the same author. The generated `PHASES.md` is structured to drop straight into an OCTALUME workspace.

```
brain-dump-to-build  →  OCTALUME  →  ship
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
2. `pytest -q --cov=brain_dump_to_build` must pass with ≥80% coverage.
3. `ruff check src tests` and `mypy src` must be clean.
4. New domain? Add a fixture in `examples/` showing input + output.

See [PUBLISHING.md](PUBLISHING.md) for the PyPI/OIDC release flow.

## License

MIT © 2026 Mohamed Harery — [harery.com](https://harery.com)
