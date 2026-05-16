# Security Policy

## Supported versions

Only the latest minor release receives security fixes. v0.1.x is the current line.

| Version | Supported |
|---------|-----------|
| 0.1.x   | yes       |
| < 0.1   | no        |

## Reporting a vulnerability

**Please do not open public issues for security problems.**

Email **mohamed@harery.com** with:

- A description of the issue
- Steps to reproduce (a minimal brain-dump that triggers the issue is gold)
- The version of `octalum-bdtb` and Python you're using
- Any suggested fix, if you have one

You'll get an acknowledgement within **72 hours**. We aim to ship a fix
within **14 days** for high-severity issues and disclose coordinated where
appropriate.

## Scope

In scope:

- Code execution via crafted brain-dump input
- Path traversal / arbitrary file write via `--output-dir`
- Secret leakage in generated artifacts
- Supply chain (dependency confusion, typo-squat protection)

Out of scope:

- Bugs in the generated `BUILD_NOW.sh` itself (it's a starter template — review before running)
- LLM provider issues when using `--llm`
