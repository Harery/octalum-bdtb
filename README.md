# brain-dump-to-build

> **From brain to build in 60 seconds.**
> Turn a messy, unstructured idea-dump into a structured, buildable project plan — feeding straight into [OCTALUME](https://github.com/Harery/OCTALUME)'s 8-phase SDLC framework.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/Harery/brain-dump-to-build/actions/workflows/ci.yml/badge.svg)](https://github.com/Harery/brain-dump-to-build/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![pipx](https://img.shields.io/badge/install-pipx-3776AB.svg)](https://pypa.github.io/pipx/)

## The pitch (30 seconds)

You had a great idea in the shower. You opened a text file. You typed for 20 minutes. Now you have a wall of text and no plan.

`brain-dump-to-build` reads that wall of text and gives you back five files: a folder structure, a stack recommendation, a phased task list, a risks register, and a bootstrap script. Deterministic, offline, no API keys required. Add `--llm` if you want a model to enrich it.

<!--
TODO(owner): record a 20-second asciinema or terminalizer GIF and drop it at docs/demo.gif:
  1. pipx install brain-dump-to-build
  2. brain-dump-to-build examples/saas/brain-dump.md --output-dir /tmp/out
  3. ls /tmp/out
  4. head -40 /tmp/out/PHASES.md
Then reference it here:
  ![demo](docs/demo.gif)
-->

## Install

```bash
pipx install brain-dump-to-build
```

Prefer a local clone?

```bash
git clone https://github.com/Harery/brain-dump-to-build
cd brain-dump-to-build
pip install -e .
```

## Quickstart (3 commands)

```bash
echo "# My idea\n\nA SaaS for cat owners with billing and dashboards" > dump.md
brain-dump-to-build dump.md --output-dir ./plan
ls ./plan
# STRUCTURE.md  STACK.md  PHASES.md  RISKS.md  BUILD_NOW.sh
```

Or pipe:

```bash
pbpaste | brain-dump-to-build - --output-dir ./plan
```

Or interactive Q&A:

```bash
brain-dump-to-build --mode interactive --output-dir ./plan
```

## Before & after

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
  - [ ] Implement: log sessions with clients (super basic notes, encrypted at rest)
  - [ ] Implement: send invoices via Stripe
  - [ ] Implement: schedule appointments (calendar sync — google + apple)
  …
```

Browse the full output in [`examples/saas/output/`](examples/saas/output/), [`examples/cli-tool/output/`](examples/cli-tool/output/), and [`examples/iot/output/`](examples/iot/output/).

## Claude Code Skill

This project ships as a **Claude Code Skill** too. Install:

```bash
cp SKILL.md ~/.claude/skills/brain-dump-to-build.md
```

Then in any Claude Code session say *"I have a brain dump, turn it into a project plan"* and Claude will invoke the skill — calling the CLI if installed, or producing the same artifacts inline if not.

## Modes

| Mode          | Use when                                              |
|---------------|-------------------------------------------------------|
| `quick`       | You have a written dump — just give me the plan.      |
| `bootstrap`   | Also generate a runnable `BUILD_NOW.sh` to scaffold.  |
| `interactive` | You don't have a dump yet — walk me through Q&A.      |

## LLM enrichment (optional)

The base path is 100% deterministic and offline. Pass `--llm` to enrich:

```bash
export ANTHROPIC_API_KEY=sk-ant-…
brain-dump-to-build dump.md --llm claude-sonnet
```

The `--llm` flag is **wired but not implemented** in v0.1.0 — the stub prints a notice and falls back to deterministic templates. PRs welcome (see [Roadmap](#roadmap)).

## Comparison

| | brain-dump-to-build | gpt-engineer | Aider | Cookiecutter |
|---|---|---|---|---|
| Input | Free-form text | Spec prompt | Existing repo | Variables |
| Output | Plan + scaffold | Full app code | Diffs to existing code | Templated repo |
| Offline | **Yes (default)** | No (LLM required) | No | Yes |
| OCTALUME-aware | **Yes** | No | No | No |
| Claude Code Skill | **Yes** | No | No | No |
| Sweet spot | Phase 0 / pre-spec | Phase 3 build | Phase 3-4 edit | Phase 1 scaffold |

`brain-dump-to-build` is deliberately the *earliest* tool in your toolchain — before you know your stack, before you have a spec.

## The OCTALUME family

This project is **Phase 0 / Pre-Phase** for [OCTALUME](https://github.com/Harery/OCTALUME), an 8-phase SDLC framework by the same author. The generated `PHASES.md` is structured to drop straight into an OCTALUME workspace.

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
2. `pytest` must pass.
3. New domain? Add a fixture in `examples/` showing input + output.

See [SECURITY.md](.github/SECURITY.md) for vulnerability disclosure (`mohamed@harery.com`).

## License

MIT © 2026 Mohamed Harery — [harery.com](https://harery.com)
