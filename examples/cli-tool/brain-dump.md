# dotsync — dotfile sync across machines without git

I'm tired of dotfile repos. Every time I switch laptops I forget to push,
or I commit a secret by accident. I want a CLI tool that syncs dotfiles
via an encrypted blob stored on S3-compatible storage (R2, B2, whatever).

Features:
- `dotsync add ~/.zshrc` registers a file
- `dotsync push` encrypts and uploads diff
- `dotsync pull` fetches and merges, prompting on conflict
- `dotsync watch` runs in background and pushes on save
- Secrets detected via gitleaks-style rules before upload (bail loudly)
- Single binary, no python runtime required on target machines

Stack thoughts: probably Rust for the single-binary thing? Or Go?
I keep going back and forth. Unix-only is fine, no Windows.

Constraints:
- Must be installable via `curl | sh` AND a homebrew tap
- Encryption: age (https://age-encryption.org) — battle-tested
- Cannot pull in heavy deps; aiming for <5MB binary

Risks:
- Risk: conflict resolution UX is the hardest part. Could ship and have it suck.
- Worry: people will use this as a password manager. It is not one.
- Scary: key loss = total data loss. Need a recovery story.

Decisions to make:
- Rust vs Go?
- Daemon (launchd/systemd) or polling cron?
- How do I distribute the encryption key safely across machines on first setup?
