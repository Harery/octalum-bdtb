import os
from pathlib import Path

import pytest

from brain_dump_to_build.cli import main, build_parser


SAMPLE = """# Sample App

A small SaaS for testing. Users can log in.

- feature: login with magic link
- risk: spam signups
- unclear: should we use Stripe or Paddle?
"""


def test_argparse_defaults():
    args = build_parser().parse_args(["input.md"])
    assert args.mode == "quick"
    assert args.output_dir == "./plan"


def test_generates_all_files(tmp_path: Path):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    rc = main([str(src), "--output-dir", str(out)])
    assert rc == 0
    for name in ("STRUCTURE.md", "STACK.md", "PHASES.md", "RISKS.md", "BUILD_NOW.sh"):
        assert (out / name).exists(), f"missing {name}"


def test_build_now_is_executable(tmp_path: Path):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    main([str(src), "--output-dir", str(out)])
    mode = (out / "BUILD_NOW.sh").stat().st_mode
    assert mode & 0o111, "BUILD_NOW.sh should be executable"


def test_no_overwrite_without_force(tmp_path: Path, capsys):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    main([str(src), "--output-dir", str(out)])
    # Tamper.
    (out / "STACK.md").write_text("MINE", encoding="utf-8")
    main([str(src), "--output-dir", str(out)])
    assert (out / "STACK.md").read_text() == "MINE"


def test_force_overwrites(tmp_path: Path):
    src = tmp_path / "dump.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    main([str(src), "--output-dir", str(out)])
    (out / "STACK.md").write_text("MINE", encoding="utf-8")
    main([str(src), "--output-dir", str(out), "--force"])
    assert (out / "STACK.md").read_text() != "MINE"


def test_literal_string_input(tmp_path: Path):
    out = tmp_path / "plan"
    rc = main(["# Tiny\n\nA tiny CLI tool with stdin.", "--output-dir", str(out)])
    assert rc == 0
    assert (out / "STACK.md").exists()


def test_missing_input_errors(tmp_path: Path, monkeypatch):
    # No stdin, no arg → SystemExit.
    monkeypatch.setattr("sys.stdin.isatty", lambda: True)
    with pytest.raises(SystemExit):
        main(["--output-dir", str(tmp_path / "x")])


def test_phases_contains_octalume(tmp_path: Path):
    src = tmp_path / "d.md"
    src.write_text(SAMPLE, encoding="utf-8")
    out = tmp_path / "plan"
    main([str(src), "--output-dir", str(out)])
    text = (out / "PHASES.md").read_text()
    assert "OCTALUME" in text
    assert "Phase 0" in text
    assert "Phase 7" in text
