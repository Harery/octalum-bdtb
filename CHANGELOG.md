# Changelog

All notable changes follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] — 2026-05-17

### Changed — major repositioning
- **Repo is now the public mirror of the BDTB 12-stage orchestrator skill.**
  Previous releases positioned the repo as a Python CLI that emitted a
  spec-kit feature folder on a single pass; that's only a sliver of what
  the real skill does. The repo now ships the full skill verbatim.
- New top-level `skill/` directory contains the authoritative manifest:
  - `skill/SKILL.md` — orchestrator with frontmatter for Claude Code
  - `skill/stages/s01-intake.md` … `skill/stages/s12-maintenance.md`
  - `skill/references/{operating-constraints,voice-guide,enhancements,build-handoff,architecture}.md`
- README rewritten to lead with the 12-stage pipeline; the Python CLI is
  reframed as the **offline Stage-7-only fallback** for non-interactive
  use and CI smoke-tests, not the primary product.
- Install changed from `cp SKILL.md ~/.claude/skills/octalum-bdtb.md`
  (single file) to `cp -r skill ~/.claude/skills/brain-dump-to-build`
  (full multi-file skill). The legacy single-file install no longer works
  — the skill is now multi-file with per-stage sub-skills.

### Added
- 18-file skill content: 1 manifest + 12 stage sub-skills + 5 reference docs.
- `Pipeline` and `What gets produced` sections in README documenting all
  15 expected output files of a real BDTB run.
- Comparison table now includes "Dynamic questioning" (yes/no) and
  "Approval gates" (yes/no) columns — the differentiators vs gpt-engineer
  / Aider / Cookiecutter / bare spec-kit.

### Preserved
- The deterministic Python CLI (`src/octalum_bdtb/`) still works
  unchanged — useful for non-interactive Stage-7 templating.
- 39/39 tests still pass, 96% coverage maintained.
- All three worked examples (`saas/`, `cli-tool/`, `iot/`) render correctly.
- `--target spec-kit` (default) and `--target octalum-classic` both work.
- v0.2.0 git tag and release notes remain available.

### Migration notes
If you installed v0.2.0 via `cp SKILL.md ~/.claude/skills/octalum-bdtb.md`,
remove that file and reinstall:
```bash
rm ~/.claude/skills/octalum-bdtb.md
git clone https://github.com/Harery/octalum-bdtb ~/octalum-bdtb
cp -r ~/octalum-bdtb/skill ~/.claude/skills/brain-dump-to-build
```

## [0.2.0] — 2026-05-16

### Added
- `--target spec-kit` (default) writes `memory/constitution.md` +
  `specs/<feature>/{spec,plan,research,data-model,quickstart,tasks}.md`
  + `contracts/` — the exact layout `/speckit.plan`, `/speckit.tasks`,
  and `/speckit.implement` expect.
- `--target octalum-classic` preserves the original 5-file output.
- Worked spec-kit example at `examples/saas/output-spec-kit/`.
- `ALIGNMENT.md` documenting the gap-closure vs github/spec-kit.

### Changed
- Repo renamed from `brain-dump-to-build` → `octalum-bdtb` (OCTALUM family
  alignment). GitHub auto-redirects the old URL.
- Python module: `brain_dump_to_build` → `octalum_bdtb`.
- README adopts the OCTALUM family unified pattern + footer.

## [0.1.0] — 2026-05-16

### Added
- Initial public release.
- Deterministic brain-dump parser with 6 domain detectors
  (saas, cli, iot, data, mobile, ml).
- CLI with three modes: `quick`, `bootstrap`, `interactive`.
- Generates `STRUCTURE.md`, `STACK.md`, `PHASES.md`, `RISKS.md`,
  `BUILD_NOW.sh`.
- PHASES mapped onto OCTALUME's 8-phase SDLC framework.
- Claude Code Skill (`SKILL.md`) with inline-fallback instructions.
- Three worked examples under `examples/` (saas, cli-tool, iot) with
  pre-generated output.
- Test suite (pytest) covering parser, CLI, file generation.
- GitHub Actions CI matrix (Linux + macOS, Python 3.9–3.12).
- Issue templates, PR template, SECURITY policy, dependabot config.

### Known limitations
- `--llm` flag is a stub; LLM enrichment lands in v0.2.
- No Windows-native testing yet (WSL works).
