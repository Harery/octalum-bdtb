# ALIGNMENT — `octalum-bdtb` ↔ `github/spec-kit`

> **Mission re-statement (from the project owner):**
> *"BDTB was planned and implemented originally for Claude Code skills, as
> it's developed to give MD files and structure that match and work with
> github/spec-kit framework."*

This document is an honest gap-analysis between what `octalum-bdtb`
**emitted before v0.2.0** and what `github/spec-kit` actually expects on
disk. It documents the realignment shipped in v0.2.0.

## Side-by-side: spec-kit ↔ pre-0.2.0 bdtb

| spec-kit artifact (`.specify/…` or `specs/<feature>/…`) | Pre-0.2.0 bdtb artifact | Mapping | Gap |
|---|---|---|---|
| `memory/constitution.md` — governing principles | _(absent)_ | — | **Missing.** bdtb had no notion of project-wide principles. |
| `specs/<feature>/spec.md` — functional requirements, user stories, "what & why" | `STRUCTURE.md` (folder tree) + parts of `PHASES.md` (features) | partial | bdtb's `STRUCTURE.md` is about file layout, not functional requirements. Features were buried inside `PHASES.md`. **Needs a dedicated spec.md.** |
| `specs/<feature>/plan.md` — technical implementation strategy, stack, architecture | `STACK.md` + `STRUCTURE.md` | partial | bdtb split tech across two files; spec-kit wants one `plan.md`. **Needs merging.** |
| `specs/<feature>/research.md` — investigation of stack decisions, rapid-change areas, unknowns | `RISKS.md` (unknowns section) | partial | bdtb's unknowns lived inside RISKS; spec-kit treats research as its own first-class artifact. |
| `specs/<feature>/data-model.md` — DB schema, data structures | _(absent)_ | — | **Missing.** bdtb never emitted a data-model file. |
| `specs/<feature>/quickstart.md` — getting-started for the feature | parts of `BUILD_NOW.sh` README block | partial | bdtb's README block was minimal and lived inside a shell script. |
| `specs/<feature>/contracts/` — API specs (OpenAPI / GraphQL / RPC) | _(absent)_ | — | **Missing.** bdtb gestured at "define API contract" as a Phase-2 task only. |
| `specs/<feature>/tasks.md` — ordered, executable task breakdown with deps | `PHASES.md` (OCTALUME 8-phase task list) | strong | bdtb's PHASES.md is already a task list — just needs reshaping into spec-kit's flat ordered task format with `[P]` parallelism markers and dependency annotations. |

## Verdict

The pre-0.2.0 implementation was **conceptually aligned** with spec-kit's
mindset (deterministic generation of structured markdown from a free-form
input) but **structurally divergent** from spec-kit's filesystem
convention. Three of spec-kit's eight artifacts were entirely absent
(`constitution.md`, `data-model.md`, `contracts/`); four others were
present but split, renamed, or buried inside other files; only
`PHASES.md → tasks.md` had a strong 1:1 mapping.

**Without the v0.2.0 realignment, a user could not have piped bdtb's
output into `/speckit.plan` or `/speckit.tasks` without significant
hand-editing.** That contradicts the project's stated mission.

## What v0.2.0 ships

1. **A new `--target spec-kit` mode (now the default).** Writes to a
   spec-kit-compatible tree:

   ```
   <output-dir>/
   ├── memory/
   │   └── constitution.md
   └── specs/
       └── <feature-slug>/
           ├── spec.md
           ├── plan.md          ← also carries the OCTALUM 8-phase mapping
           ├── research.md
           ├── data-model.md
           ├── quickstart.md
           ├── contracts/
           │   └── README.md    ← placeholder explaining what to drop here
           └── tasks.md
   ```

2. **OCTALUM is preserved inside `plan.md`** as a labelled section
   ("OCTALUM 8-phase mapping"), so the two methodologies *compose*
   rather than conflict. The phase-numbered task list — bdtb's
   signature output — survives.

3. **`--target octalum-classic`** preserves the v0.1.0 five-file output
   (`STRUCTURE.md` / `STACK.md` / `PHASES.md` / `RISKS.md` /
   `BUILD_NOW.sh`) for users who liked the original shape.

4. **`examples/saas/output-spec-kit/`** ships a fully rendered
   spec-kit-shaped snapshot of the SaaS brain-dump for inspection.

## Composing with spec-kit

```bash
# 1. Brain dump → spec-kit-shaped plan
octalum-bdtb my-idea.md --output-dir .

# 2. Hand control to spec-kit
/speckit.plan      # refines specs/<feature>/plan.md
/speckit.tasks     # refines specs/<feature>/tasks.md
/speckit.implement # executes
```

The seam is clean: bdtb fills `specs/<feature>/*.md` from the brain-dump,
spec-kit takes over for refinement and execution.
