# Marketing drafts

> Drafts only. **Nothing here is published.** Owner reviews + posts when ready.

---

## 1-paragraph pitch

You had the idea in the shower. You opened a text file. Twenty minutes later you have a wall of words and no plan. **brain-dump-to-build** reads that wall and hands you back five files — a folder structure, a stack recommendation, a phased task list mapped onto the OCTALUME SDLC framework, a risks register, and a ready-to-run bootstrap script. Deterministic, offline, no API keys required. Install with `pipx install brain-dump-to-build` and turn an idea into a buildable Phase-0 in under sixty seconds.

---

## Twitter / X thread (12 tweets)

**1/12** I keep meeting builders who have great ideas trapped in 2000-word voice-memo transcripts. The bottleneck isn't the idea — it's the leap from prose to plan. So I built a tool for that leap. (thread)

**2/12** It's called `brain-dump-to-build`. You give it your messy idea-dump. It gives you back a folder structure, a stack, a phased task list, a risks register, and a bootstrap script. Five files. Sixty seconds.

**3/12** It is **deterministic**. No API keys. No "we'll call OpenAI behind your back." It uses keyword detection + structural templates. The smart-feeling output comes from templates that were already smart.

**4/12** That means it works on a plane. On a corporate laptop with egress rules. In a SCIF (probably).

**5/12** It detects six domains today: SaaS, CLI, IoT, data, mobile, ML. Each domain gets a tailored tree + stack table. Open a PR to add yours.

**6/12** It maps your tasks onto an 8-phase SDLC framework (OCTALUME). So instead of "do everything at once," you get Phase 0 → Phase 7 with concrete checkboxes per phase.

**7/12** It also ships as a **Claude Code Skill**. `cp SKILL.md ~/.claude/skills/`. Now Claude knows when to run it and when not to.

**8/12** What it is NOT: a code generator. It's the step BEFORE you call gpt-engineer or Aider. The plan is for humans (and downstream LLMs) to execute.

**9/12** Compared to Cookiecutter: Cookiecutter needs you to know variables. b2b needs you to know nothing — it figures out which template to apply.

**10/12** Built it because every consulting engagement I do starts with a 90-minute meeting that should have been a markdown file. Now it can be.

**11/12** Roadmap: real `--llm` enrichment in v0.2 (Anthropic + Ollama). OCTALUME workspace exporter in v0.4. Custom template plugins in v1.0.

**12/12** Install: `pipx install brain-dump-to-build`. Repo: github.com/Harery/brain-dump-to-build. License: MIT. Boost if you like the shape of it.

---

## LinkedIn post

I shipped a tool today called **brain-dump-to-build**.

It solves a problem I see in nearly every digital-transformation engagement: clients come with great ideas trapped in unstructured text — voice memos, slack threads, two-page emails. The bottleneck isn't the idea, it's the leap from prose to plan.

`brain-dump-to-build` reads that unstructured text and produces five artifacts in under a minute:

• STRUCTURE.md — a proposed folder tree
• STACK.md — a recommended technology stack
• PHASES.md — a task list mapped onto an 8-phase SDLC framework
• RISKS.md — risks, unknowns, and open decisions
• BUILD_NOW.sh — a runnable bootstrap script

It is deterministic and offline by default — no API keys, no LLM call required — which matters for regulated industries where data egress is a hard line. Optional LLM enrichment is gated behind an explicit flag.

It also ships as a Claude Code Skill, so it integrates naturally into AI-assisted workflows.

This is Phase 0 / Pre-Phase for OCTALUME, the SDLC framework I use with clients. The two compose: brain-dump-to-build hands a structured Phase 0 to OCTALUME, OCTALUME drives it to production.

Install: `pipx install brain-dump-to-build`
Repo: github.com/Harery/brain-dump-to-build
MIT licensed.

Curious for feedback from anyone who runs Phase-0 workshops for a living.

---

## Show HN post

**Title:** Show HN: brain-dump-to-build – turn unstructured idea text into a project plan, offline

Hi HN — I built `brain-dump-to-build`, a small Python CLI that reads a raw brain-dump (a markdown file, a transcript, anything) and emits five files: STRUCTURE.md, STACK.md, PHASES.md, RISKS.md, BUILD_NOW.sh.

Three things that might be interesting:

1. **Deterministic by default.** No LLM in the hot path. Keyword detection + structural templates. Works offline. The `--llm` flag exists but is opt-in and currently a stub (v0.2 will wire it up).

2. **OCTALUME-aware.** The generated PHASES.md is structured around an 8-phase SDLC framework, so the output is meant to feed *into* a downstream methodology rather than stand alone.

3. **Ships as a Claude Code Skill too.** Same logic, but invokable from any Claude Code session via `SKILL.md`.

It's not trying to compete with gpt-engineer / Aider — those are Phase 3 (build). This is Phase 0 (figure out what to build). Comparison table in the README.

Install: `pipx install brain-dump-to-build`
Repo: https://github.com/Harery/brain-dump-to-build

Happy to answer questions about why I went deterministic-first instead of LLM-first, or about the 8-phase framework it slots into.
