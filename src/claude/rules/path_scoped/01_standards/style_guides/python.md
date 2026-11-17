---
paths:
  - "**/*.py"
---
# 🐍 Python Coding Standards

**Purpose:** Python standards that extend PEP 8, covering only what `ruff` and `ruff format` don't already enforce. This team's own choices are in [`02_team_conventions/python.md`](../../02_team_conventions/python.md), which loads with this guide.

## 🏷️ Naming

- **Constants:** `SCREAMING_SNAKE_CASE`
- **Meaningful names:** avoid abbreviations
- **No history in names:** change history belongs in git, not code

## ⚠️ Error handling

- **Control flow:** use `try-except-else` where appropriate; `finally` only for cleanup

## 📝 Docstrings

- **Default:** one line saying what the function does, enough for most private helpers and tests.
- **Fields:** only when they add meaning, in the team's docstring style, with no `:type:` or `:rtype:`.

## 💬 Comments

- **When:** comment anything a reader would pause on: non-obvious logic, the purpose of a non-trivial conditional, fallback behaviour, the phases of a function over about 10 lines, and every `TODO` or `FIXME`, with what and why.
- **How:** keep each comment accurate and never restate the code, such as `i += 1  # increment i`.

## 🧪 Tests and environments

- **Tests:** every script gets a `pytest` test file, and coverage is run and reviewed before committing.
- **Virtual environments:** never commit one.

## 🔖 Type hints

- **When:** add them when the type is non-obvious or specific.
- **`-> None`:** add it to typed functions that return nothing, since type checkers treat a missing annotation as unannotated.
- **No bare types:** use `dict[str, Any]` or `list[str]`, not bare `dict` or `list`.

## 📚 Read on demand

- `on_demand/01_standards/style_guides/python/testing.md`, in your Claude config directory, before writing or changing pytest tests.
- `on_demand/01_standards/style_guides/python/logging.md`, before adding logging or error handling.
- `on_demand/01_standards/style_guides/python/code_complexity.md`, when a function grows long or deeply nested.
- `on_demand/01_standards/style_guides/python/module_organisation.md`, when writing docstrings or splitting public and private code.
