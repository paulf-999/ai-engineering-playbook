<!-- version: 2.0.2 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — functions grow harder to read and change -->
# 📊 Code Complexity

**Purpose:** the limits that keep a Python function easy to read and change, and the ruff and radon checks that measure each.

## ⚡ Limits

| Metric | Limit | Check |
|---|---|---|
| **Cyclomatic complexity** | 10 or fewer | ruff `C901`, whose default `max-complexity` is 10, or `radon cc` |
| **Function length** | Aim for 30 lines, and split past 40 | ruff `PLR0915`, which counts statements rather than lines, so set `max-statements` to match |
| **Nesting depth** | 3 levels or fewer | ruff `PLR1702`, a preview rule |
| **Parameters** | 4 or fewer | ruff `PLR0913`, with `max-args = 4` |
| **Line length** | 120 characters or fewer | ruff `E501` |

- 🗣️ **One-sentence test:** if you can't say what a function does in one sentence, split it.
- 🔧 **Check, don't eyeball:** where a repo's ruff config lacks these rules, add them rather than checking by hand.
- 🚪 **Over a limit:** refactor, or say why in the docstring, as the exceptions file shows.

## 📚 Read on demand

- `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md`, in your Claude config directory, for what cyclomatic and cognitive complexity measure.
- `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_size_limits.md`, in your Claude config directory, for why each size limit exists and how to get under it.
- `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md`, in your Claude config directory, before accepting code over a limit.
