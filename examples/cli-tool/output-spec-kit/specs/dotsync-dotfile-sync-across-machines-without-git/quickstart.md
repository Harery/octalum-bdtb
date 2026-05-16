# Quickstart — dotsync — dotfile sync across machines without git

> How a new contributor (or future you) gets the feature running locally
> in under 10 minutes.

## Prerequisites

- A recent runtime for the chosen stack (see `plan.md` → "Tech stack").
- Credentials for any third-party service flagged in `plan.md`.
- The repo cloned and the constitution (`../../memory/constitution.md`) skimmed.

## Setup

```bash
# 1. Clone
git clone <repo-url>
cd dotsync-dotfile-sync-across-machines-without-git

# 2. Install
# (fill in based on stack — `npm i` / `pip install -e .` / `uv sync` / etc.)

# 3. Configure
cp .env.example .env
# edit .env with secrets
```

## Run locally

```bash
# (fill in — `npm run dev` / `python -m dotsync_dotfile_sync_across_machines_without_git` / etc.)
```

## Verify

- [ ] Health check returns 200.
- [ ] The first user story from `spec.md` works end-to-end.
- [ ] `pytest` (or the project's test runner) is green.

## Troubleshooting

- _(Common gotchas land here as the project matures.)_

---

_If a step here is wrong, fix it — out-of-date setup docs are a top-3 reason
contributors give up._
