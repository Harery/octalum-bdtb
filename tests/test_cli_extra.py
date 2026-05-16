"""Extra CLI tests targeting argparse edge cases, modes, stdin, --llm,
Unicode handling, path-traversal safety, and large input handling."""

from __future__ import annotations

import io
import subprocess
import sys
from pathlib import Path

import pytest

from brain_dump_to_build.cli import _ask_interactive, _read_input, main

SAMPLE = """# Sample App

A small SaaS for testing. Users can log in.

- feature: login with magic link
- risk: spam signups
- unclear: should we use Stripe or Paddle?
"""


def test_stdin_input(tmp_path: Path, monkeypatch):
    """When no positional arg and stdin is not a TTY, read from stdin."""
    monkeypatch.setattr("sys.stdin", io.StringIO(SAMPLE))
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)
    out = tmp_path / "plan"
    rc = main(["--output-dir", str(out)])
    assert rc == 0
    assert (out / "STACK.md").exists()


def test_dash_means_stdin(tmp_path: Path, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(SAMPLE))
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)
    out = tmp_path / "plan"
    rc = main(["-", "--output-dir", str(out)])
    assert rc == 0


def test_bootstrap_mode_prints_next(tmp_path: Path, capsys):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    rc = main([str(src), "--output-dir", str(out), "--mode", "bootstrap"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "BUILD_NOW.sh" in captured.out
    assert "Next:" in captured.out


def test_llm_stub_prints_notice(tmp_path: Path, capsys):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    rc = main([str(src), "--output-dir", str(out), "--llm", "claude-sonnet"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "claude-sonnet" in captured.err
    assert "enrichment" in captured.err.lower()


def test_invalid_mode_rejected():
    """argparse should reject an invalid --mode value."""
    with pytest.raises(SystemExit):
        main(["x.md", "--mode", "nonsense"])


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "brain-dump-to-build" in captured.out


def test_empty_input_rejected(tmp_path: Path):
    src = tmp_path / "empty.md"
    src.write_text("   \n  ", encoding="utf-8")
    out = tmp_path / "plan"
    with pytest.raises(ValueError):
        main([str(src), "--output-dir", str(out)])


def test_unicode_input(tmp_path: Path):
    """Brain-dumps with emoji, RTL, and CJK characters should round-trip."""
    src = tmp_path / "dump.md"
    src.write_text(
        "# 项目 — Café résumé app 🚀\n\n"
        "An app for مطاعم with Stripe.\n\n"
        "- feature: تسجيل الدخول 🔐\n"
        "- risk: الترميز Unicode 中文\n",
        encoding="utf-8",
    )
    out = tmp_path / "plan"
    rc = main([str(src), "--output-dir", str(out)])
    assert rc == 0
    text = (out / "PHASES.md").read_text(encoding="utf-8")
    assert "🚀" in text or "Café" in text


def test_large_input_handled(tmp_path: Path):
    """A multi-MB brain-dump should not crash or take forever."""
    src = tmp_path / "big.md"
    with src.open("w", encoding="utf-8") as fh:
        fh.write("# Big dump\n\n")
        for i in range(50_000):
            fh.write(f"- feature: do thing number {i}\n")
    assert src.stat().st_size > 1_000_000  # > 1 MB
    out = tmp_path / "plan"
    rc = main([str(src), "--output-dir", str(out)])
    assert rc == 0
    assert (out / "STRUCTURE.md").exists()


def test_output_dir_created_recursively(tmp_path: Path):
    """--output-dir with nested non-existent parents should be created."""
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "deeply" / "nested" / "plan"
    rc = main([str(src), "--output-dir", str(out)])
    assert rc == 0
    assert out.is_dir()


def test_output_writes_stay_inside_output_dir(tmp_path: Path):
    """Generated filenames should never escape the chosen output directory."""
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    main([str(src), "--output-dir", str(out)])
    out_resolved = out.resolve()
    for f in out.iterdir():
        assert out_resolved in f.resolve().parents or f.resolve().parent == out_resolved


def test_read_input_nonexistent_path_treated_as_literal():
    """A non-path string with markdown-like content is the dump itself."""
    text = _read_input("# Inline\n\nLiteral dump string here.")
    assert "Literal dump" in text


def test_interactive_mode_assembles_dump(tmp_path: Path, monkeypatch, capsys):
    """Simulate keystroke-by-keystroke answers to the interactive wizard."""
    inputs = iter([
        "A note-taking CLI", "", "",        # Q1
        "Indie hackers", "", "",            # Q2
        "- markdown notes", "- tags", "", "",  # Q3
        "deadline: 2026-Q3", "", "",        # Q4
        "Risk: data loss on crash", "", "", # Q5
        "Should we sync to git", "", "",    # Q6
    ])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    text = _ask_interactive()
    assert "note-taking CLI" in text
    assert "markdown notes" in text
    assert "risk:" in text
    assert "git?" in text


def test_interactive_mode_full_run(tmp_path: Path, monkeypatch):
    inputs = iter([
        "A tiny CLI", "", "",
        "Devs", "", "",
        "- arg parsing", "", "",
        "", "",
        "", "",
        "", "",
    ])

    def _input():
        try:
            return next(inputs)
        except StopIteration as exc:
            raise EOFError from exc

    monkeypatch.setattr("builtins.input", _input)
    out = tmp_path / "plan"
    rc = main(["--mode", "interactive", "--output-dir", str(out)])
    assert rc == 0
    assert (out / "STACK.md").exists()


def test_module_entrypoint_runs():
    """`python -m brain_dump_to_build --version` should exit 0."""
    proc = subprocess.run(
        [sys.executable, "-m", "brain_dump_to_build", "--version"],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 0
    assert "brain-dump-to-build" in proc.stdout
