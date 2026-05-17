# Marketing drafts

> Drafts only. **Nothing here is published.** Owner reviews + posts when ready.

---

## 1-paragraph pitch

You opened your inbox and there it is — a 2,000-word voice-memo transcript from a non-technical client describing the app they want. They don't know their stack. They don't know their stages. They don't even know all their features yet. **`octalum-bdtb`** is a Claude Code Skill that takes that exact mess and drives it through 12 stage-gated steps — intake, BRD, MVP, business plan, tech stack, spec-kit constitution, logic, diagrams, build, monitoring, maintenance — with the AI owning 90-95% of the work and approval gates at every hand-off. Install: `cp -r skill ~/.claude/skills/brain-dump-to-build`. Repo ships the full skill manifest, all 12 stage sub-skills, 5 reference docs, and an offline Python CLI fallback for non-interactive runs.

---

## Twitter / X thread (12 tweets)

**1/12** Every consulting engagement I run starts the same way: a non-technical client sends a 2000-word voice-memo transcript describing their dream product. The hard part isn't the idea. It's the 90 minutes of "OK but what about…" that has to happen next. (thread)

**2/12** I built a Claude Code Skill that runs those 90 minutes for me. It's called `octalum-bdtb`. You paste the customer's dump. Claude takes over — 12 stages, gated at every hand-off, with the AI owning 90-95% of the work.

**3/12** Stage 1 isn't "ask 30 questions." It's "read the dump first, then generate exactly 9 questions targeting the *real* gaps." Pyramid questioning — Macro → Meso → Micro → Nano → Atomic. Each stage gets a smaller question budget than the last.

**4/12** Stage 2: BRD. Stage 3: MVP. Stage 4: Business analysis (live competitor search). Stage 5: Business plan. Stage 6: Tech stack with version-pinning and a cost ledger. Stage 7: spec-kit constitution + CLAUDE.md + MEMORY.md.

**5/12** Stage 8: logic blocks. Stage 9: Mermaid diagrams. Stage 10: actually build the codebase. Stage 11: observability + monitoring. Stage 12: maintenance + upgrade cycle. You're not hand-typing anything in 1–9 except yes/revise/skip at the gates.

**6/12** The skill is **opinionated** about who does what. The operator (you) translates the customer's intent and approves at gates. Claude does the rest. No "let me know your preferred database." Claude knows.

**7/12** Token discipline is built in. Only the active stage sub-skill loads at a time. CLAUDE.md caps at 100 lines (uses @imports). MEMORY.md caps at 200. A mandatory compaction checkpoint runs after Stage 5.

**8/12** Stage 7 produces a `.specify/memory/constitution.md` that drops straight into [github/spec-kit](https://github.com/github/spec-kit). `/speckit.plan` and `/speckit.tasks` consume it natively. The two methodologies compose.

**9/12** A 34-check silent firewall runs before every delivery — jargon, hallucinated versions, spec-kit conformance, file-output completeness, Ubuntu compatibility, SEO. Failures fix silently. The customer never sees the firewall.

**10/12** What it is NOT: another "AI builds the app" demo. The skill is opinionated about phasing — discovery before strategy before architecture before code. The build is Stage 10, not Stage 1.

**11/12** What's also in the repo: an offline Python CLI fallback that templates Stage-7 outputs without firing up Claude Code. Useful for CI smoke tests, air-gapped envs, and "I just need the spec-kit folder" runs. 96% test coverage.

**12/12** Install: `git clone github.com/Harery/octalum-bdtb && cp -r octalum-bdtb/skill ~/.claude/skills/brain-dump-to-build`. License: MIT for code + skill content. Tell me what you'd run it on first.

---

## LinkedIn post

A pattern I see in every digital-transformation engagement: a non-technical client sends a 2,000-word voice-memo transcript describing the product they want. The bottleneck isn't the idea — it's the 90-minute structured conversation that has to happen *next* before any engineer can begin work.

I just open-sourced **octalum-bdtb**, a Claude Code Skill that runs those 90 minutes for you.

**The pipeline:** 12 stage-gated steps — intake, BRD, MVP, business analysis, business plan, tech stack with cost ledger, spec-kit constitution, logic blocks, Mermaid diagrams, build, monitoring, maintenance. The AI owns 90-95% of the technical work; the operator translates the customer's intent and approves at each hand-off.

**The discipline:** pyramid questioning narrows from Macro to Atomic across stages. Stage 1 generates *exactly 9 dynamic questions* based on what the dump actually leaves unclear — not a template. Each subsequent stage gets a smaller budget. Stage 9 onward asks zero. A 34-check silent firewall runs before every delivery; failures fix silently.

**The integration:** Stage 7 produces a [github/spec-kit](https://github.com/github/spec-kit)-conformant constitution that hands off cleanly to `/speckit.plan` and `/speckit.tasks`. The two methodologies compose — BDTB does the discovery and strategy, spec-kit handles refinement and execution.

**The fallback:** an offline Python CLI ships in the repo for non-interactive runs (CI smoke tests, air-gapped environments). 96% test coverage, zero runtime deps, deterministic templating.

This is **Phase 0** for the broader **OCTALUM** family of digital-infrastructure tools — sibling to OCTALUME (8-phase enterprise SDLC), OCTALUM-PYLAB (Python DSA pedagogy), and OCTALUM-PULSE (cross-distro Linux maintenance).

Install:
```
git clone https://github.com/Harery/octalum-bdtb
cp -r octalum-bdtb/skill ~/.claude/skills/brain-dump-to-build
```

MIT licensed. Curious for feedback from anyone running Phase-0 workshops for non-technical clients.

---

## Show HN post

**Title:** Show HN: A 12-stage Claude Code Skill that turns a customer brain-dump into a product

Hi HN — I open-sourced `octalum-bdtb`, a Claude Code Skill that runs a 12-stage pipeline from customer brain-dump to delivered codebase, with the AI doing 90-95% of the work and stage-gates at every hand-off.

Three things that might be interesting on a technical level:

1. **Pyramid questioning, not 30-question forms.** Stage 1 reads the dump first, then generates *exactly 9* dynamic questions targeting the real gaps. Each question has 4 choices + a recommended pick + a custom open answer. Subsequent stages get progressively smaller question budgets — Macro to Meso to Micro to Nano to Atomic — with Stage 9+ asking zero.

2. **Token-conservation by design.** Only one stage sub-skill loads at a time. CLAUDE.md is capped at 100 lines (uses `@import` syntax for sub-files). MEMORY.md at 200. A mandatory compaction checkpoint runs after Stage 5 with a HANDOFF.md snapshot before context reset.

3. **A 34-check silent firewall** runs before every delivery — questionnaire integrity, jargon, hallucinated versions, spec-kit conformance, Ubuntu compatibility, SEO. Failures fix silently. The customer never sees the checks.

It's NOT another "AI builds the app" demo. The build is Stage 10. Stages 1-9 are discovery, strategy, architecture, contracts. The skill is opinionated about phasing.

Stage 7 generates a [github/spec-kit](https://github.com/github/spec-kit)-conformant constitution + CLAUDE.md that hands off cleanly to `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` — so the skill composes with spec-kit rather than competing with it.

Also in the repo: an offline Python CLI fallback for non-interactive runs (CI smoke checks, air-gapped envs). 96% test coverage, zero runtime deps.

Install:
```
git clone https://github.com/Harery/octalum-bdtb
cp -r octalum-bdtb/skill ~/.claude/skills/brain-dump-to-build
```

Repo: https://github.com/Harery/octalum-bdtb
License: MIT

Happy to discuss why I went stage-gated instead of one-shot, the pyramid-questioning rationale, or the architectural choice to make spec-kit the bridge between discovery and build rather than a competing methodology.

---

## Reddit r/ClaudeAI post

**Title:** I built a 12-stage Claude Code Skill that turns customer brain-dumps into delivered products

Sharing a Claude Code Skill I open-sourced today — `octalum-bdtb` (Brain-Dump To Build).

**What it does:** runs a 12-stage pipeline from a non-technical customer's raw idea-dump to a delivered codebase, with stage-gates between each step.

**The stages:**
1. Intake (dynamic 9-question pyramid)
2. BRD
3. MVP
4. Business analysis (with live competitor search)
5. Business plan
6. Tech stack + cost ledger
7. spec-kit constitution + CLAUDE.md + MEMORY.md
8. Logic blocks
9. Mermaid diagrams
10. Build (codebase)
11. Monitoring
12. Maintenance

The AI does 90-95% of the work; the operator approves at gates.

**What's interesting about it as a skill:**
- One stage sub-skill loads at a time (token conservation)
- 34 silent quality checks before each delivery
- CLAUDE.md uses `@import` syntax to stay ≤ 100 lines
- Stage 7 output is github/spec-kit compatible — hands off to `/speckit.*` commands

Repo: https://github.com/Harery/octalum-bdtb — install via `cp -r skill ~/.claude/skills/brain-dump-to-build`.

Looking for feedback from people who run Phase-0 sessions or use spec-kit.

---

## Hashtags / mentions for X+LinkedIn

`#ClaudeCode #ClaudeCodeSkills #AICoding #SpecDrivenDevelopment #AIAgents #OpenSource #AIProductManagement #SDLC #DigitalTransformation #PromptEngineering`
