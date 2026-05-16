# Changelog

All notable changes follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
