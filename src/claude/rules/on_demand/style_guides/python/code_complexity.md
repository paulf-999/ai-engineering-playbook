<!-- created: 2026-08-28 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — functions grow harder to read and change -->
# 📊 Code Complexity

**Purpose:** the limits that keep a Python function easy to read and change, the ruff checks that measure each, and when going over one is acceptable.

## ⚡ Limits

| Metric | Limit | Check |
|---|---|---|
| **Cyclomatic complexity** | 10 or fewer | ruff `C901`, whose default `max-complexity` is 10, or `radon cc` |
| **Function length** | Aim for 30 lines, and split past 40 | ruff `PLR0915`, which counts statements rather than lines, so set `max-statements` to match |
| **Nesting depth** | 3 levels or fewer | ruff `PLR1702`, a preview rule, so it needs `preview = true` and `max-nested-blocks = 3` |
| **Parameters** | 4 or fewer | ruff `PLR0913`, with `max-args = 4` |
| **Line length** | 120 characters or fewer | ruff `E501` |

- 🗣️ **One-sentence test:** if you can't say what a function does in one sentence, split it.
- 🔧 **Check, don't eyeball:** where a repo's ruff config lacks these rules, add them rather than checking by hand.

## 🚪 Going over a limit

Refactor first. A function may stay over a limit only when its shape comes from the problem, such as a state machine, a long linear pipeline or setup code with many options. Then say why in its docstring:

```python
def complex_operation():
    """Brief description of what it does.

    NOTE: Cyclomatic complexity is X due to [reason].
    This is acceptable because [justification].

    Phases:
    1. [Phase A]: what happens here
    2. [Phase B]: what happens here
    """
```
