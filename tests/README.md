# 🧪 tests

**Purpose:** how the `tests/` folder is laid out, where a new test goes, and which tests earn their place.

## 📁 Layout

Tests follow these layout rules:

- 🪞 **Mirrored paths:** a test sits at the same path as the file it checks, so tests for `src/sh/git/git_validate_pr_description.sh` live in `tests/src/sh/git/test_git_validate_pr_description.py`.
- 🤝 **Shared helpers:** modules that start with `_`, such as `_paths.py`, hold code several tests share, and aren't tests themselves.
  - **Importable:** `pythonpath = ["tests"]` in `pyproject.toml` lets any test import them by name.
  - **New helper:** add it to the `name-tests-test` exclude in `.pre-commit-config.yaml`, or the hook rejects its name.
- 🏷️ **Naming:** each test file is `test_<what it checks>.py`, and a pre-commit hook enforces the prefix.

## ▶️ Running

- ▶️ **Running:** `make test` runs every test, in parallel across CPU cores.
- ⚠️ **Not in pre-commit:** the hooks don't run tests, so `make test` is a separate part of [Done means](../CLAUDE.md).

## 🏷️ Which tests to keep

| Keep or delete | When | Examples |
|---|---|---|
| ✅ Keep | It protects a core promise of a hook or CI check, or a common path | Blocking a bad commit; main options, common edge cases, clear error messages |
| 🗑️ Delete | It's neither | A rare edge case, a cosmetic check |

- 🔴 **Core:** cover the happy path, each failure that blocks, and both sides of any limit, such as exactly at a cap and one over it.
- 🧱 **Shared helpers:** test them once in `tests/src/sh/test_shell_utils.py`, and give each script that uses them one test that it calls them correctly.
- 🔀 **Variants:** use parametrised cases rather than near-duplicate functions, and size the suite by test functions, not pytest cases.
- 🐛 **Bug fixes:** add one regression test.
- 🍂 **Same PR:** a PR that changes a script updates its tests, deletes those for removed behaviour, keeps names describing what the code does now, and updates the folder's README row.

The [tests checklist](../maintenance/quality/quality_rubrics/_repo.md#-rules-and-tests-checklists) catches duplicates and layout-only tests at each regular review.
