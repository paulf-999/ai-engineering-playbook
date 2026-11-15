# 🧪 Test Maintenance

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how many tests to write, how to rate each one's importance, and when to delete one.

Size the suite by test functions, not pytest cases, since one parametrised function can produce dozens of cases.

## 🏷️ Priority scores

Each test function has a priority on the MoSCoW scale (Must, Should, Could, Won't), but only a Must is tagged, so an untagged test is a Should:

| Score | Use it for | If the test breaks |
|---|---|---|
| 🔴 **Must** | A core promise of a hook or CI check, such as blocking a bad commit | A bad change gets through, or a good one is blocked |
| 🟠 **Should** | Main options, common edge cases and clear error messages | A common path misbehaves, but the core check still works |
| 🟡 **Could** | Rare edge cases and template helpers | Something unusual misbehaves, so don't keep the test |
| ⚪ **Won't** | A duplicate or cosmetic check | Nothing is lost, so delete the test |

A `Could` test isn't kept either, since a test for a rare case doesn't earn its upkeep, and [`test_moscow_tags.py`](../tests/test_moscow_tags.py) fails on any tag but `Must`.

- 📝 **Format:** put `# MoSCoW: Must — <reason>` on the line above a Must test's decorators, or above `def` when it has none.
- 💬 **Reason:** about 12 words on what the test protects, not how it works.
- 🎯 **Tests only:** tag `test_` functions, not helpers or fixtures.

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
- 🔄 **Re-rates them:** since a change can turn a `Should` into a `Must`, or a test into a duplicate.
- 📛 **Keeps names current:** names and docstrings describe what the code does now, never what's "new" or "old".

## 🔍 Periodic review

At each [regular review](../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests), count the Must tests and all test functions:

```bash
grep -rh --include='*.py' '^# MoSCoW: Must' tests | wc -l
grep -rh --include='*.py' '^def test_' tests | wc -l
```

- 📉 **Balance:** if under half the test functions are Musts, upkeep goes on side paths rather than what matters.
- ✂️ **Cut:** delete any untagged test that turns out to be a `Could` or `Won't`.
- 🏅 **Re-score:** refresh the [test audit](quality/quality_audit/_tests.md) row of every script whose tests changed since the last review, in one PR, using the [reviewer brief](quality/quality_rubrics/_tests.md).
