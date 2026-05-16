# RISKS — dotsync — dotfile sync across machines without git

## Known risks

- Risk: conflict resolution UX is the hardest part. Could ship and have it suck.
- Worry: people will use this as a password manager. It is not one.
- Scary: key loss = total data loss. Need a recovery story.

## Open questions / unknowns

- Rust vs Go?
- Daemon (launchd/systemd) or polling cron?
- How do I distribute the encryption key safely across machines on first setup?
- - Rust vs Go?
- - Daemon (launchd/systemd) or polling cron?
- - How do I distribute the encryption key safely across machines on first setup?

## Constraints

- Must be installable via `curl | sh` AND a homebrew tap
- Cannot pull in heavy deps; aiming for <5MB binary

## Decisions to make this week

- [ ] Confirm primary user persona
- [ ] Lock in tech stack (or commit to a 2-day spike)
- [ ] Define what's explicitly **out of scope** for v0.1
