<!-- created: 2026-11-08 -->
# 📏 Complexity size limits

**Purpose:** why each size limit in `code_complexity.md` exists and how to get under it, with the limits and ruff checks themselves kept in that file's table.

---

## 📏 Lines of Code (LOC)

**What:** Number of lines in a function.

**Why:** Cyclomatic complexity (CC), the count of decision points, doesn't capture length, and long linear functions are hard to follow too.

- 🪚 **Over 40:** extract helper functions.
- 🧾 **Exception:** data processing, setup code and other linear sequences.

---

## 📍 Nesting Depth

**What:** How many levels deep code is nested (if/for/while/def inside each other).

**Why:** Each level adds a condition the reader must hold in mind to follow the innermost line.

**Setup:** `PLR1702` is a preview rule, so it needs `preview = true` and `max-nested-blocks = 3`.

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

**How to reduce:**

- 📦 **Group related params**: Use a dataclass for options that travel together
- 🧷 **Partial application**: Pre-fill common parameter values

---

## 📏 Line Length

**What:** Characters per line (from your style guide).

**Why:** Long lines hide complexity or indicate poor naming.

**Exception:** Long strings, URLs, unavoidable literals.
