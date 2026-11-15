# 🧪 Test Maintenance

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tests to write, which ones earn their place, and when to delete one.

Size the suite by test functions, not pytest cases, since one parametrised function can produce dozens of cases.

## 🏷️ Which tests earn their place

Keep a test only if it protects one of these:

| Kind | Use it for | If the test breaks |
|---|---|---|
| 🔴 **Core** | A core promise of a hook or CI check, such as blocking a bad commit | A bad change gets through, or a good one is blocked |
| 🟠 **Common path** | Main options, common edge cases and clear error messages | A common path misbehaves, but the core check still works |

A test that's neither, such as a rare edge case, a duplicate or a cosmetic check, doesn't earn its upkeep, so delete it.

## 📏 How many tests

Size each script's tests by these rules:

- 🔴 **Core:** cover the happy path, each failure that blocks, and both sides of any limit, such as exactly at a cap and one over it.
- 🧱 **Shared helpers:** test them once in `tests/src/sh/test_shell_utils.py`, and give each script that uses them one test that it calls them correctly.
- 🔀 **Variants:** use parametrised cases rather than near-duplicate functions.
- 🐛 **Bug fixes:** add one regression test.
- 👯 **Duplicates:** if two tests always fail together for the same reason, delete one.

## 🍂 Keeping tests current

A stale test checks behaviour the code no longer has, so it passes but protects nothing. A PR that changes a script also:

- 🔗 **Updates its tests:** and deletes those for behaviour it removes.
- 🔄 **Re-checks them:** since a change can turn a test into a duplicate.
- 📛 **Keeps names current:** names and docstrings describe what the code does now, never what's "new" or "old".

## 🔍 Periodic review

At each [regular review](../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests), run the [tests checklist](quality/quality_rubrics/_repo.md#-rules-and-tests-checklists) on every script whose tests changed since the last review, and open an issue for each finding not fixed in that PR.
