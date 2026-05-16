# Publishing `octalum-bdtb` to PyPI

This repo uses **PyPI Trusted Publishing (OIDC)** via GitHub Actions — no
long-lived API tokens are stored anywhere. The release workflow lives at
`.github/workflows/release.yml` and is triggered by pushing a `v*` git tag.

## One-time setup (human follow-up)

1. **Create the PyPI project** (placeholder reservation):
   - Go to https://pypi.org/manage/account/publishing/
   - Click "Add a new pending publisher"
   - Fill in:
     - PyPI project name: `octalum-bdtb`
     - Owner: `Harery`
     - Repository name: `octalum-bdtb`
     - Workflow name: `release.yml`
     - Environment name: `pypi`
2. **Create the `pypi` environment in GitHub**:
   - https://github.com/Harery/octalum-bdtb/settings/environments
   - New environment → name it `pypi`
   - (Optional but recommended) Require a reviewer for deployments.
3. **Optional TestPyPI dry-run**: repeat steps 1-2 on https://test.pypi.org and
   add a parallel `publish-testpypi` job, or use a `test-pypi` environment.

No `PYPI_API_TOKEN` secret is needed — OIDC handles auth at publish time.

## Cutting a release

```bash
# 1. Bump version in pyproject.toml and src/octalum_bdtb/__init__.py
# 2. Update CHANGELOG.md
git commit -am "release: v0.1.1"
git tag -a v0.1.1 -m "v0.1.1"
git push origin main --tags
```

The `Release` workflow will:

1. Build sdist + wheel with `python -m build`.
2. Upload to PyPI via `pypa/gh-action-pypi-publish@release/v1` using OIDC.
3. Create a GitHub Release with auto-generated notes and attached artifacts.

## Verifying

```bash
pipx install octalum-bdtb==0.1.1
octalum-bdtb --version
```

## Troubleshooting

- **`invalid-publisher` error**: the GitHub environment name in
  `release.yml` (`pypi`) must match the trusted-publisher config on PyPI.
- **Tag pushed but workflow didn't run**: confirm the tag matches `v*` and was
  pushed to `Harery/octalum-bdtb` (`git push origin v0.1.1`).
