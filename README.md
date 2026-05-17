<!-- KEYWORDS: brain dump to spec, github spec-kit, spec-driven development, phase-0 feeder, claude code skill, spec-kit planner, /speckit.plan, /speckit.tasks, /speckit.implement, offline project planner, zero-dependency cli, deterministic spec generator, octalum, octalume, gpt-engineer alternative, aider alternative, cookiecutter alternative, agentic project bootstrap, constitution.md, tasks.md, plan.md, idea to plan in 60 seconds -->

<div align="center">

# octalum-bdtb

**Paste a messy brain-dump. Get a full spec-kit feature folder in 60 seconds.**

[![CI](https://github.com/Harery/octalum-bdtb/actions/workflows/ci.yml/badge.svg)](https://github.com/Harery/octalum-bdtb/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Coverage](https://img.shields.io/badge/coverage-96%25-brightgreen.svg)](#)
[![GitHub stars](https://img.shields.io/github/stars/Harery/octalum-bdtb?style=social)](https://github.com/Harery/octalum-bdtb)

</div>

> The Phase-0 feeder for [github/spec-kit](https://github.com/github/spec-kit). Drop in an unstructured idea; out comes `memory/constitution.md` + a full `specs/<feature>/` folder ready for `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`. Offline. Zero dependencies. No API key.

<p align="right"><sub><code>DRAWING NO. 04.00  ·  REV. 2026.05  ·  SHEET 04 OF 05</code></sub></p>

[Problem](#the-problem) · [Install](#install) · [Quickstart](#quickstart) · [What you get](#what-you-get) · [How it works](#how-it-works) · [Two output targets](#two-output-targets) · [Claude Code Skill](#use-it-as-a-claude-code-skill) · [Comparison](#comparison) · [FAQ](#faq) · [Documentation](#documentation) · [Roadmap](#roadmap)

## The problem

`github/spec-kit` expects a populated `specs/<feature>/` tree before `/speckit.plan` will do anything useful. Authoring `spec.md`, `plan.md`, `research.md`, `data-model.md`, `quickstart.md`, `tasks.md`, and `contracts/` by hand from a raw idea is the slowest part of spec-driven development. `octalum-bdtb` writes those files for you from a single brain-dump, so spec-kit has something concrete to refine.

## Install

```bash
pipx install octalum-bdtb   # once PyPI publisher is registered; until then use the source install below
```

```bash
pip install git+https://github.com/Harery/octalum-bdtb       # current canonical install
```

## Quickstart

```bash
echo "# Cat-sitter SaaS — marketplace + Stripe billing" > dump.md   # 1. write a dump (any length)
octalum-bdtb dump.md --output-dir ./plan                            # 2. generate the spec-kit tree
tree ./plan                                                         # 3. inspect — drop into your repo
```

## What you get

```text
./plan/
├── memory/
│   └── constitution.md
└── specs/
    └── cat-sitter-saas/
        ├── spec.md           # what & why — functional requirements, user stories
        ├── plan.md           # technical strategy + OCTALUM 8-phase overlay
        ├── research.md       # stack decisions, unknowns
        ├── data-model.md     # entities, schema
        ├── quickstart.md     # how to run the feature once built
        ├── tasks.md          # ordered task list with [P] parallel markers
        └── contracts/
            └── README.md     # placeholder for OpenAPI / GraphQL / RPC
```

A fully rendered worked example lives at [`examples/saas/output-spec-kit/`](examples/saas/output-spec-kit/) — every file the spec-kit `/speckit.*` commands expect, generated from a 30-line dump.

## How it works

`octalum-bdtb` is a deterministic, template-driven parser. It tokenises the dump, classifies the project domain (SaaS / CLI / IoT / browser-ext / ML / generic), extracts features, risks, and stack hints, then renders each spec-kit artifact from a versioned Jinja-free Python template. No LLM. No network. The same input always produces the same output.

```text
brain dump ── octalum-bdtb ──▶ memory/constitution.md
                             │
                             └▶ specs/<feature>/spec.md
                                                 plan.md       (incl. OCTALUM 8-phase overlay)
                                                 research.md
                                                 data-model.md
                                                 quickstart.md
                                                 tasks.md
                                                 contracts/
                                          │
                                          └─▶ /speckit.plan ▶ /speckit.tasks ▶ /speckit.implement
```

See [ALIGNMENT.md](ALIGNMENT.md) for the full gap analysis between pre-0.2.0 output and spec-kit's filesystem convention, and the realignment shipped in v0.2.0.

## Two output targets

| `--target` | When to use | Files produced |
|:--|:--|:--|
| `spec-kit` *(default)* | You use github/spec-kit, Claude Code, or any agent that consumes spec-kit-shaped Markdown. | `memory/constitution.md` + `specs/<feature>/{spec,plan,research,data-model,quickstart,tasks}.md` + `contracts/` |
| `octalum-classic` | You want the original 5-file shape for human review or to hand off to legacy [OCTALUME](https://github.com/Harery/OCTALUME) workflows. | `STRUCTURE.md` · `STACK.md` · `PHASES.md` · `RISKS.md` · `BUILD_NOW.sh` |

```bash
octalum-bdtb dump.md --target octalum-classic --output-dir ./plan
```

Both targets are offline and use zero LLM tokens. Pass `--llm` to enrich (stubbed today; wiring tracked on the roadmap).

## Use it as a Claude Code Skill

The repo ships a Claude Code Skill manifest. Install once:

```bash
cp SKILL.md ~/.claude/skills/octalum-bdtb.md
```

Then in any Claude Code conversation, say *"I have a brain dump, turn it into a spec-kit plan"* — Claude invokes the skill, calls the CLI if installed, or emits the same artifacts inline if not. See [SKILL.md](SKILL.md) for the manifest.

## Comparison

|  | octalum-bdtb | gpt-engineer | Aider | Cookiecutter | bare spec-kit |
|:--|:--|:--|:--|:--|:--|
| Input form | Free-form brain-dump | Polished prompt | Existing repo | Pre-filled variables | Hand-authored `spec.md` |
| Output | Populated `specs/<feature>/` tree | Full app source | Diffs to a repo | Templated repo skeleton | Whatever you typed |
| LLM required | No | Yes | Yes | No | Optional |
| Offline | Yes | No | No | Yes | Yes |
| Target phase | Phase 0 — discovery | Phase 3 — build | Phase 3-4 — edit | Phase 1 — scaffold | Phase 1 — spec authoring |

`octalum-bdtb` is deliberately the *earliest* tool in the chain — it fills the gap between "I had an idea" and "I have a spec-kit folder."

## FAQ

### Does it work with github/spec-kit?

Yes — that is the entire point. `--target spec-kit` (the default) writes the exact filesystem layout `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` expect. Drop the output into a spec-kit-enabled repo and the slash commands consume it directly. See [ALIGNMENT.md](ALIGNMENT.md).

### How is this different from gpt-engineer?

gpt-engineer takes a polished prompt and writes the app. `octalum-bdtb` takes a messy idea and writes the spec. Different phase, different artifact. Use `octalum-bdtb` first; hand its `specs/<feature>/` tree to gpt-engineer, Aider, or Claude Code as the source spec.

### Do I need an API key?

No. The default path is 100% deterministic templates — no LLM, no network, no key. The optional `--llm` flag (Claude / Ollama) is opt-in and stubbed pending wire-up.

### Can I use it with Claude Code?

Yes. Copy `SKILL.md` into `~/.claude/skills/` and Claude Code invokes the skill automatically when you describe an idea. No additional subscription beyond Claude itself.

### What's the OCTALUM family connection?

`octalum-bdtb` is sheet 04 of a five-repo portfolio. The generated `plan.md` carries an "OCTALUM 8-phase mapping" section so [OCTALUME](https://github.com/Harery/OCTALUME)'s SDLC framework composes with spec-kit rather than competing with it.

### When will it hit PyPI?

The OIDC trusted-publishing pipeline is wired (see [PUBLISHING.md](PUBLISHING.md)); registration on pypi.org is the only remaining human step. Until then, `pip install git+https://github.com/Harery/octalum-bdtb` is canonical.

## Documentation

- [ALIGNMENT.md](ALIGNMENT.md) — spec-kit gap analysis and realignment notes
- [SKILL.md](SKILL.md) — Claude Code Skill manifest
- [PUBLISHING.md](PUBLISHING.md) — PyPI / OIDC release flow
- [`examples/saas/`](examples/saas/) · [`examples/cli-tool/`](examples/cli-tool/) · [`examples/iot/`](examples/iot/) — input dumps and rendered outputs
- [CHANGELOG.md](CHANGELOG.md) — release history (v0.2.0 current)

## Roadmap

- **2026-05** — v0.2.0 released: `--target spec-kit` default, 39/39 tests, 96% coverage.
- **2026-06** — Register on pypi.org and cut v0.2.1 via the OIDC pipeline.
- **2026-07** — Wire `--llm` enrichment (Anthropic + Ollama) behind the deterministic core.
- **2026-08** — `--target aider` and `--target cursor` output modes.
- **2026-09** — VS Code extension wrapping the CLI.
- **2026-Q4** — v1.0: stable artifact schema, plugin API for third-party templates.

## Contributing · License · Security

- Contributing — open an issue before non-trivial PRs; `pytest -q --cov=octalum_bdtb` must stay green at ≥80%; `ruff check` and `mypy src` must be clean.
- License — MIT, see [LICENSE](LICENSE).
- Security — report privately via [harery.com](https://harery.com); do not file public issues for vulnerabilities.

<!-- ============================================================== -->
<!-- UNIFIED OCTALUM FAMILY FOOTER — keep verbatim across every repo -->
<!-- ============================================================== -->

---

<div align="center">

### Drawn by the same hand

A working portfolio of digital infrastructure, designed and maintained by [**Mohamed Harery**](https://harery.com) — Architect of Digital Systems.

| Sheet | Repo | What it is |
|:--:|:--|:--|
| 00 | [**harery.com**](https://github.com/Harery/Mo) | The studio — portfolio, ledger, contact |
| 01 | [**OCTALUME**](https://github.com/Harery/OCTALUME) | 8-phase enterprise SDLC framework |
| 02 | [**OCTALUM-PYLAB**](https://github.com/Harery/OCTALUM-PYLAB) | Python DSA & coding-interview prep |
| 03 | [**OCTALUM-PULSE**](https://github.com/Harery/OCTALUM-PULSE) | Cross-distro Linux maintenance CLI |
| 04 | [**octalum-bdtb**](https://github.com/Harery/octalum-bdtb) | Brain-dump → spec-kit-shaped plan |

<sub>
  <a href="https://harery.com">harery.com</a> ·
  <a href="https://github.com/Harery">github.com/Harery</a> ·
  <a href="https://www.linkedin.com/in/harery/">LinkedIn</a>
</sub>

<sub>BLUEPRINT · drawn 2026 · MIT-licensed code · all drawings reserved</sub>

</div>
