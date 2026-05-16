"""Command-line interface for brain-dump-to-build."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from . import __version__
from .parser import parse_brain_dump
from .templates import render_all


def _read_input(arg: str | None) -> str:
    """Read the brain-dump from a file path or stdin."""
    if arg and arg != "-":
        p = Path(arg)
        if p.exists():
            return p.read_text(encoding="utf-8")
        # If it's not an existing path, treat the literal string as the dump.
        return arg
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit(
        "error: no brain-dump provided. Pass a file path, a quoted string, "
        "or pipe text on stdin."
    )


def _ask_interactive() -> str:
    """Lightweight Q&A to assemble a dump for users who don't have one."""
    print("Interactive mode. Press Enter twice to finish each answer.\n")
    questions = [
        "1) In one sentence, what are you building?",
        "2) Who is it for?",
        "3) Top 3-5 features (one per line):",
        "4) Hard constraints (deadline, budget, regulatory)?",
        "5) What scares you / what could go wrong?",
        "6) Any open questions you don't know the answer to?",
    ]
    chunks: list[str] = []
    for q in questions:
        print(q)
        lines: list[str] = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
        chunks.append("\n".join(lines).strip())
        print()

    title = chunks[0].splitlines()[0] if chunks[0] else "Untitled Project"
    body = []
    body.append(f"# {title}")
    body.append("")
    body.append(chunks[0])
    body.append("")
    if chunks[1]:
        body.append(f"Target users: {chunks[1]}")
    if chunks[2]:
        body.append("\n## Features\n")
        for line in chunks[2].splitlines():
            line = line.strip("-* \t")
            if line:
                body.append(f"- {line}")
    if chunks[3]:
        body.append("\n## Constraints\n")
        for line in chunks[3].splitlines():
            if line.strip():
                body.append(f"- {line.strip()}")
    if chunks[4]:
        body.append("\n## Risks\n")
        for line in chunks[4].splitlines():
            if line.strip():
                body.append(f"- risk: {line.strip()}")
    if chunks[5]:
        body.append("\n## Unknowns\n")
        for line in chunks[5].splitlines():
            if line.strip():
                q = line.strip()
                if not q.endswith("?"):
                    q += "?"
                body.append(f"- {q}")
    return "\n".join(body)


def _maybe_llm_enrich(project, model: str) -> None:
    """Stub for --llm enrichment. Documents the wiring without requiring keys.

    To enable, set ANTHROPIC_API_KEY (or OPENAI_API_KEY, or OLLAMA_HOST) and
    install the corresponding SDK. See README.md > "LLM enrichment".
    """
    print(f"[--llm {model}] enrichment not invoked: no SDK wired in v0.1.0. "
          "See README > LLM enrichment.", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brain-dump-to-build",
        description="From brain to build in 60 seconds. "
                    "Turn a raw idea-dump into a structured project plan.",
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Path to a text/markdown file containing the brain-dump, "
             "a literal string, or '-' for stdin.",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="./plan",
        help="Directory to write generated artifacts (default: ./plan).",
    )
    parser.add_argument(
        "--mode",
        choices=("quick", "bootstrap", "interactive"),
        default="quick",
        help="quick = plan only; bootstrap = plan + runnable BUILD_NOW.sh; "
             "interactive = Q&A wizard to assemble the dump.",
    )
    parser.add_argument(
        "--llm",
        metavar="MODEL",
        default=None,
        help="Optional: name of an LLM to use for enrichment "
             "(e.g. claude-sonnet, gpt-4o, ollama:llama3). "
             "Requires API key env vars — see README.",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing files in --output-dir.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: list | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.mode == "interactive":
        text = _ask_interactive()
    else:
        text = _read_input(args.input)

    project = parse_brain_dump(text)

    if args.llm:
        _maybe_llm_enrich(project, args.llm)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    artifacts = render_all(project)

    if args.mode != "bootstrap":
        # Still write BUILD_NOW.sh for reference, but mark it as a template.
        pass

    written = []
    for name, content in artifacts.items():
        target = out_dir / name
        if target.exists() and not args.force:
            print(f"skip: {target} (exists; use --force to overwrite)", file=sys.stderr)
            continue
        target.write_text(content, encoding="utf-8")
        if name.endswith(".sh"):
            os.chmod(target, 0o755)
        written.append(str(target))

    print(f"\nProject: {project.title}")
    print(f"Domain : {project.primary_domain}")
    print(f"Wrote  : {len(written)} file(s) → {out_dir}")
    for w in written:
        print(f"  - {w}")

    if args.mode == "bootstrap":
        print(f"\nNext: bash {out_dir / 'BUILD_NOW.sh'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
