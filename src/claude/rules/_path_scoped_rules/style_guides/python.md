---
<!-- version: 1.5.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — Python drifts from the house style -->
<!-- loading: path-scoped — loads with Python files -->
paths:
  - "**/*.py"
---

# 🐍 Python Coding Standards

**Purpose:** Establish Python coding conventions extending PEP 8, ensuring consistent, readable, and maintainable code across the team.

PEP 8 is the baseline. One override: maximum line length is **120 characters** (enforced by `ruff`).

## 🗂️ Code layout

- **Indentation:** 4 spaces — no tabs
- **Between top-level:** two blank lines between functions and classes
- **Between methods:** one blank line between methods within a class
- **Within functions:** space logically to maintain readability

## 🏷️ Naming conventions

- **Modules/packages:** `snake_case`
- **Functions/methods:** `snake_case`
- **Variables:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `SCREAMING_SNAKE_CASE`
  - **Meaningful names:** avoid abbreviations; no single-letter variables outside loop counters
  - **No history in names:** change history belongs in git, not code

## 📥 Imports

- **One per line:** one module per import statement
- **Absolute imports:** no wildcard imports (`from module import *`)
- **Group and order:** standard library → third-party → local, separated by blank lines

## 💬 String formatting

- **Use f-strings:** exclusively; do not use `str.format()` or `%` formatting

## ⚠️ Error handling

- **Specific exceptions:** never bare `except:` or `except Exception:`
- **Control flow:** use `try-except-else` where appropriate; `finally` only for cleanup

## 📝 Docstrings

All functions, classes, and modules must have a docstring, and a one-line summary is the default:

```python
def build_hook(header: str = VALID_HEADER, shebang: str = "#!/bin/bash") -> str:
    """Build a minimal hook script from a shebang, header and body."""
```

Add reST fields only for public or complex functions, and only the ones a reader needs:

```python
def get_secret_by_name(secret_name: str) -> str:
    """Retrieve a secret value by name from the configured secret manager.

    :param secret_name: The name the secret is stored under, not its path.
    :raises KeyError: If the secret name does not exist.
    :return: The secret value, never logged.
    """
```

- **Default:** one line saying what the function does — enough for most private helpers and tests.
- **Fields when they add meaning:** `:param:` for an argument its name doesn't explain, `:raises:` for exceptions callers must handle, `:return:` when the value isn't obvious.
- **No `:type:` or `:rtype:`:** the type hints already say this, and only the hints are checked by tools.
- **Format:** reST only — no Google-style or NumPy-style docstrings.
- **Existing code:** trim long docstrings when a file is next edited, not in bulk sweeps.

## 🔧 Functions and methods

- **Defaults at end:** default arguments go at the end of the argument list
- **Keyword arguments:** no spaces around `=` (e.g., `func(name="foo")`)
- **Spacing:** single space after commas in calls and definitions

## 🔖 Type hints

Add type hints when they add value — i.e., when the type is non-obvious or specific.

- **`-> None`:** add it to typed functions that return nothing, since type checkers treat a missing return annotation as unannotated, not as `None`
- **Avoid bare types:** `dict`, `list`, `tuple` without parameterization are not informative — use specific forms (`dict[str, Any]`, `list[str]`) or omit entirely

## 💬 Inline comments

Err on the side of over-commenting: explain non-obvious logic and purpose, put comments above the code they describe, and keep them accurate.

## 📌 General

- **File paths:** use `pathlib.Path` over `os.path`
- **Mutable defaults:** avoid — use `None` and assign inside function

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/python/_python_environment.md`, in your Claude config directory, when setting up a virtual environment or dependencies.
- **Read on demand:** `_rules_on_demand/style_guides/python/testing.md`, before writing or changing pytest tests.
- **Read on demand:** `_rules_on_demand/style_guides/python/logging.md`, before adding logging or error handling.
- **Read on demand:** `_rules_on_demand/style_guides/python/_comments.md`, when deciding whether or how to comment code.
- **Read on demand:** `_rules_on_demand/style_guides/python/code_complexity.md`, when a function grows long or deeply nested.
- **Read on demand:** `_rules_on_demand/style_guides/python/module_organisation.md`, when writing module docstrings or splitting public and private code.
