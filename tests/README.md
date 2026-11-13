# 🧪 tests

**Purpose:** how the `tests/` folder is laid out, and where a new test goes.

Tests follow these layout rules:

- 🪞 **Mirrored paths:** a test sits at the same path as the file it checks, so tests for `src/sh/git/git_validate_pr_description.sh` live in `tests/src/sh/git/test_git_validate_pr_description.py`.
  - **Docs too:** the tests that keep the doc quality audits accurate mirror `maintenance/quality/`.
- 🌐 **Repo-wide tests:** a test that checks the whole repo, such as every file's header, sits at the top of `tests/`.
- 🤝 **Shared helpers:** modules that start with `_`, such as `_paths.py`, hold code several tests share, and aren't tests themselves.
  - **Importable:** `pythonpath = ["tests"]` in `pyproject.toml` lets any test import them by name.
  - **New helper:** add it to the `name-tests-test` exclude in `.pre-commit-config.yaml`, or the hook rejects its name.
- 🏷️ **Naming:** each test file is `test_<what it checks>.py`, and a pre-commit hook enforces the prefix.

## 🏃 Running and scoring

- ▶️ **Running:** `make test` runs every test.
- ⚠️ **Not in pre-commit:** the hooks don't run tests, so `make test` is a separate part of [Done means](../CLAUDE.md).
- 📊 **Scoring:** each test gets a priority, explained in [test maintenance](../maintenance/test_maintenance.md) and recorded as a `# MoSCoW:` comment above it, and the [tests audit](../maintenance/quality/audits/quality_audit_test_files.md) scores each script's tests.
