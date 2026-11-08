<!-- version: 1.1.3 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-08 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — functions grow harder to read and change -->
<!-- loading: on demand — read when python.md's complexity pointer sends Claude here -->
# 📊 Code Complexity

**Purpose:** Establish metrics to identify and prevent overly complex Python code. Reduces mental load and improves maintainability.

---

## 📋 Contents

- [Overview](#-overview)
- [Single responsibility](#-single-responsibility-principle)
- [Quick reference](#-quick-reference)
- [Detailed metrics](#-detailed-metrics) — See `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md`
- [Escape hatches](#-escape-hatches) — See `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md`

---

## 🎯 Overview

**Why it matters:** Complex code is hard to understand, maintain, and test. Mental load increases risk of bugs.

**Two types of complexity:**

1. **Structural** — decision points, nesting, parameters (measured by metrics)
2. **Cognitive** — how hard it is for humans to understand (measured by readability)

**Approach:** Use metrics as early warning signs. When metrics exceed thresholds, refactor or document why.

---

## 🎯 Single Responsibility Principle

**Each function should do one thing and do it well.**

**Indicators that a function does too much:**

- **High LOC:** > 30-40 lines suggests multiple responsibilities
- **High CC:** > 10 suggests multiple decision paths
- **Hard to name:** Can't explain in one sentence = too many responsibilities
- **Multiple reasons to change:** Each reason suggests a separate responsibility

**How to split:**

- Extract helpers for distinct concerns (e.g., setup logic separate from main logic)
- Use descriptive function names to clarify purpose
- Group related parameters together

**Example (too much responsibility):**

```python
def process_data(items, config, output_dir):
    # Validate items
    for item in items:
        if not validate(item):
            raise ValueError(...)

    # Transform items
    transformed = [transform(item) for item in items]

    # Write output
    write_results(transformed, output_dir)
```

**Better (split into helpers):**

```python
def process_data(items, config, output_dir):
    validate_items(items)
    transformed = transform_items(items)
    write_results(transformed, output_dir)
```

---

## ⚡ Quick Reference

| Metric | Target | Tool |
|--------|--------|------|
| **Cyclomatic Complexity** | < 10 | `radon cc` |
| **Lines of Code** | < 30-40 | `radon raw` |
| **Nesting Depth** | < 3 | Manual review |
| **Parameters** | < 5 | Manual review |
| **Line Length** | < 120 chars | `ruff check` |

**Readability test:** Can you explain the function in one sentence?

---

## 📐 Detailed Metrics

Full explanation of each metric, thresholds, and examples:

- **Read on demand:** `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md`, in your Claude config directory, for cyclomatic and cognitive complexity.
- **Read on demand:** `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_size_limits.md`, in your Claude config directory, for the length, nesting, parameter and line-length limits.

---

## 🚪 Escape Hatches

When complex code is acceptable and how to document it:

- **Read on demand:** `_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md`, in your Claude config directory, for the detail of this section.

---

## 🛠️ Workflow

1. **Before submitting:** Run `radon cc` and `ruff check`
2. **If metrics exceed thresholds:** Refactor or document exception
3. **If documented:** Add comments explaining why complexity is necessary
4. **Review checklist:** Use scorecard in exceptions doc
