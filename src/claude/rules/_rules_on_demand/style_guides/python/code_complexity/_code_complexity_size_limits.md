<!-- version: 1.0.0 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-08 -->
# 📏 Complexity size limits

**Purpose:** The limits on function length, nesting depth, parameter count and line length, and how to measure each.

---

## 📏 Lines of Code (LOC)

**What:** Number of lines in a function.

**Why:** CC doesn't capture length. Long linear functions are hard to understand.

**Threshold:** < 30-40 lines

- Exceeds 40? Consider extracting helper functions
- Exception: Data processing, setup code, linear sequences

**Tool:** `radon raw src/ -s`

---

## 📍 Nesting Depth

**What:** How many levels deep code is nested (if/for/while/def inside each other).

**Why:** Each level exponentially increases cognitive load.

**Threshold:** < 3 levels

**How to reduce:**

- **Early returns**: Exit function early instead of deep nesting
- **Extract functions**: Move nested logic into helpers
- **Use guard clauses**: Invert conditionals to reduce nesting

**Example (depth=4, bad):**

```python
if x:
    if y:
        for item in items:
            if item.valid:
                # Deep nesting!
```

**Better (depth=2):**

```python
if not x or not y:
    return
for item in items:
    if not item.valid:
        continue
    # Process item
```

---

## 🔧 Parameter Count

**What:** Number of function parameters.

**Why:** Many parameters = complex interface and high cognitive load.

**Threshold:** < 5 parameters

**How to reduce:**

- **Group related params**: Use dataclasses or dicts for related options
- **Use kwargs**: Accept `**options` for flexible configuration
- **Partial application**: Pre-fill common parameter values

---

## 📏 Line Length

**What:** Characters per line (from your style guide).

**Threshold:** < 120 characters

**Why:** Long lines hide complexity or indicate poor naming.

**Exception:** Long strings, URLs, unavoidable literals.

**Tool:** `ruff check` (already configured)
