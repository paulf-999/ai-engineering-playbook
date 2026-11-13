<!-- created: 2026-08-28 -->
# 📐 Complexity Metrics

**Purpose:** Explain the cyclomatic and cognitive complexity scores, their thresholds and how to measure them.

---

## 🎯 Cyclomatic Complexity (McCabe)

**What:** Count of decision points (if, elif, for, while, and, or).

**Why:** Industry standard, tool-supported, proven baseline.

**Thresholds:**

- **1-5**: Simple, easy to understand
- **6-10**: Moderate, acceptable
- **11+**: Complex, refactor needed

**Tool:** `radon cc <package> -a`, or ruff's `C901` rule.

**Example (CC=3):**

```python
def process(items):
    result = []
    for item in items:  # +1
        if item.valid:  # +1
            result.append(item.transform())
    return result
```

---

## 🧠 Cognitive Complexity

**What:** Mental load — how hard is the code to understand?

**Why:** Complements cyclomatic complexity. Low CC + high nesting = still hard to follow.

**Factors:**

- **Nesting depth**: Each level increases cognitive load
- **Boolean chains**: Multiple conditions on one line
- **Conditional jumps**: Early returns, exception handling

**When to apply:** When CC passes but code still "feels" complex.

**Example (CC=6, but high cognitive load):**

```python
if a and b or c and (d or e):  # Confusing, break it down
    # ...
```

**Better:**

```python
is_valid = a and b or c and (d or e)
if is_valid:
    # ...
```
