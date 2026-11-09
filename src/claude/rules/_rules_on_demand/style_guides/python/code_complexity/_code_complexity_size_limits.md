<!-- version: 1.2.0 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-09 -->
# 📏 Complexity size limits

**Purpose:** The limits on function length, nesting depth, parameter count and line length, and how to measure each.

---

## 📏 Lines of Code (LOC)

**What:** Number of lines in a function.

**Why:** Cyclomatic complexity (CC), the count of decision points, doesn't capture length, and long linear functions are hard to follow too.

**Threshold:** aim for 30 lines, and split a function past 40.

- 🪚 **Over 40:** extract helper functions.
- 🧾 **Exception:** data processing, setup code and other linear sequences.

**Tool:** ruff's `PLR0915` rule (too-many-statements), which counts statements per function, a close proxy for length.

---

## 📍 Nesting Depth

**What:** How many levels deep code is nested (if/for/while/def inside each other).

**Why:** Each level adds a condition the reader must hold in mind to follow the innermost line.

**Threshold:** 3 levels or fewer.

**Tool:** ruff's `PLR1702` rule (too-many-nested-blocks), a preview rule, so it needs `preview = true` and `max-nested-blocks = 3`.

**How to reduce:**

- ↩️ **Early returns**: Exit function early instead of deep nesting
- 🧩 **Extract functions**: Move nested logic into helpers
- 🛡️ **Use guard clauses**: Invert conditionals to reduce nesting

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

**Threshold:** 4 parameters or fewer.

**Tool:** ruff's `PLR0913` rule (too-many-arguments), with `max-args = 4`.

**How to reduce:**

- 📦 **Group related params**: Use a dataclass for options that travel together
- 🧷 **Partial application**: Pre-fill common parameter values

---

## 📏 Line Length

**What:** Characters per line (from your style guide).

**Threshold:** 120 characters or fewer, matching ruff's `line-length = 120`.

**Why:** Long lines hide complexity or indicate poor naming.

**Exception:** Long strings, URLs, unavoidable literals.

**Tool:** `ruff check`, which reports long lines as `E501`.
