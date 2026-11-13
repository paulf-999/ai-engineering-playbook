---
paths:
  - "**/*.py"
---
<!-- version: 1.6.4 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: Python files -->
<!-- miss_cost: low — Python drifts from the house style -->
# 🐍 Python Coding Standards

**Purpose:** Python conventions that extend PEP 8, covering only what `ruff` and `ruff format` don't already enforce.

## 🏷️ Naming

- **Constants:** `SCREAMING_SNAKE_CASE`
- **Meaningful names:** avoid abbreviations; no single-letter variables outside loop counters
- **No history in names:** change history belongs in git, not code

## ⚠️ Error handling

- **Control flow:** use `try-except-else` where appropriate; `finally` only for cleanup

## 📝 Docstrings

- **Default:** one line saying what the function does, enough for most private helpers and tests.
- **Fields:** reST only, such as `:param:`, and only when they add meaning, with no `:type:` or `:rtype:`.

## 🔖 Type hints

- **When:** add them when the type is non-obvious or specific.
- **`-> None`:** add it to typed functions that return nothing, since type checkers treat a missing annotation as unannotated.
- **No bare types:** use `dict[str, Any]` or `list[str]`, not bare `dict` or `list`.

## 📚 Read on demand

- `on_demand/style_guides/python/_python_environment.md`, in your Claude config directory, when setting up a virtual environment or dependencies.
- `on_demand/style_guides/python_testing.md`, before writing or changing pytest tests.
- `on_demand/style_guides/python_logging.md`, before adding logging or error handling.
- `on_demand/style_guides/python/_comments.md`, when deciding whether or how to comment code.
- `on_demand/style_guides/python_code_complexity.md`, when a function grows long or deeply nested.
- `on_demand/style_guides/python_module_organisation.md`, when writing docstrings or splitting public and private code.
