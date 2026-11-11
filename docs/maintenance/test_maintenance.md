<!-- version: 1.3.2 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-11 -->
# 🧪 Test Maintenance

**Purpose:** how many tests to write, how to rate each one's importance, and when to delete one.

Size the suite by test functions, not pytest cases, since one parametrised function can produce dozens of cases.

## 🏷️ Priority scores

Each test function gets a priority on the MoSCoW scale (Must, Should, Could, Won't):

| Score | Use it for | If the test breaks |
|---|---|---|
| 🔴 **Must** | A core promise of a hook or CI check, such as blocking a bad commit | A bad change gets through, or a good one is blocked |
| 🟠 **Should** | Main options, common edge cases and clear error messages | A common path misbehaves, but the core check still works |
| 🟡 **Could** | Rare edge cases and template helpers | Something unusual misbehaves |
| ⚪ **Won't** | A duplicate or cosmetic check | Nothing is lost, so delete the test |

- 📝 **Format:** put `# MoSCoW: <score> — <reason>` on the line above the test's decorators, or above `def` when it has none.
- 💬 **Reason:** about 12 words on what the test protects, not how it works.
- 🎯 **Tests only:** score `test_` functions, not helpers or fixtures.

For example:

```python
# MoSCoW: Must — security: a PR title must never run as code
def test_title_with_shell_characters_is_not_executed():
```

## 📏 How many tests

Size each script's tests by these rules:

- 🔴 **Musts:** cover the happy path, each failure that blocks, and both sides of any limit, such as exactly at a cap and one over it.
- 🧱 **Shared helpers:** test them once in `tests/src/sh/test_shell_utils.py`, and give each script that uses them one test that it calls them correctly.
- 🔀 **Variants:** use parametrised cases rather than near-duplicate functions.
- 🐛 **Bug fixes:** add one regression test, scored by the bug's impact.
- 👯 **Duplicates:** if two tests always fail together for the same reason, delete one.

## 🍂 Keeping tests current

A stale test checks behaviour the code no longer has, so it passes but protects nothing. A PR that changes a script also:

- 🔗 **Updates its tests:** and deletes those for behaviour it removes.
- 🔄 **Re-rates them:** since a change can turn a `Could` into a `Must`, or a test into a duplicate.
- 📛 **Keeps names current:** names and docstrings describe what the code does now, never what's "new" or "old".

## 🔍 Periodic review

At each [regular review](../target_architecture/design_principles/01_principles.md#-numbers-and-tests), count the tests by score:

```bash
grep -rh --include='*.py' '^# MoSCoW:' tests | awk '{print $3}' | sort | uniq -c
```

- 📉 **Balance:** more `Could` than `Must` tests means upkeep goes on rare cases rather than what matters.
- ✂️ **Cut:** delete slow `Could` tests that no longer earn their run time.
