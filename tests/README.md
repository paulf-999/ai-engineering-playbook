# 🧪 tests

**Purpose:** how the `tests/` folder is laid out, where a new test goes, and which tests earn their place.

Tests follow these layout rules:

- 🪞 **Mirrored paths:** a test sits at the same path as the file it checks, so tests for `src/sh/git/git_validate_pr_description.sh` live in `tests/src/sh/git/test_git_validate_pr_description.py`.
- 🌐 **Repo-wide tests:** a test that checks the whole repo, such as every file's header, sits at the top of `tests/`.
- 🤝 **Shared helpers:** modules that start with `_`, such as `_paths.py`, hold code several tests share, and aren't tests themselves.
  - **Importable:** `pythonpath = ["tests"]` in `pyproject.toml` lets any test import them by name.
  - **New helper:** add it to the `name-tests-test` exclude in `.pre-commit-config.yaml`, or the hook rejects its name.
- 🏷️ **Naming:** each test file is `test_<what it checks>.py`, and a pre-commit hook enforces the prefix.

## 🏃 Running and scoring

- ▶️ **Running:** `make test` runs every test.
- ⚠️ **Not in pre-commit:** the hooks don't run tests, so `make test` is a separate part of [Done means](../CLAUDE.md).

## 🏷️ Which tests to keep

Keep a test only if it protects a **core** promise of a hook or CI check, such as blocking a bad commit, or a **common path**: main options, common edge cases and clear error messages. Delete one that's neither, such as a rare edge case or a cosmetic check. Size the suite by test functions, not pytest cases.

- 🔴 **Core:** cover the happy path, each failure that blocks, and both sides of any limit, such as exactly at a cap and one over it.
- 🧱 **Shared helpers:** test them once in `tests/src/sh/test_shell_utils.py`, and give each script that uses them one test that it calls them correctly.
- 🔀 **Variants:** use parametrised cases rather than near-duplicate functions.
- 🐛 **Bug fixes:** add one regression test.
- 🍂 **Same PR:** a PR that changes a script updates its tests, deletes those for removed behaviour, and keeps names describing what the code does now.

The [tests checklist](../maintenance/quality/quality_rubrics/_repo.md#-rules-and-tests-checklists) catches duplicates and layout-only tests at each regular review.
