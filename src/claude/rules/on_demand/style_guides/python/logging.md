<!-- created: 2026-08-28 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: medium — logs leak secrets or miss what's needed to debug -->
# 📝 Python Logging Conventions

**Purpose:** the house rules for logging and error handling in Python, so logs are useful, safe and free of duplicates.

## 🔧 Setup

- 🧭 **One logger per module:** create it at module level with `logger = logging.getLogger(__name__)`, never inside a function.
- 💬 **Lazy formatting:** pass values as arguments, such as `logger.info("Loaded %s rows", count)`, so a disabled level costs nothing.

## 📊 Levels

| Level | Use it for | Example |
|---|---|---|
| **DEBUG** | Detail for development, off in production | `logger.debug("Using timeout %s", timeout)` |
| **INFO** | Milestones, counts and results a user can follow | `logger.info("Migrated %s of %s connections", done, total)` |
| **WARNING** | Something unexpected that the code recovers from | `logger.warning("Config %s not found, using defaults", path)` |
| **ERROR** | A failure the program can't recover from, in the top-level handler | `logger.exception("Migration failed")` |

## 🔁 Log each error once

Log an error where the most context is known, and let it travel up from there:

| Situation | What to do |
|---|---|
| 🟡 **Expected and recoverable**, such as a missing optional file | Log at WARNING with context, use the fallback, and don't re-raise |
| 🔴 **Unexpected, and you can add context**, such as the file path | Raise a clearer error `from` it, with that context in its message, and don't log it |
| ⏭️ **Unexpected, and you have nothing to add** | Don't catch it, and let it propagate |
| 🏁 **Top-level handler**, such as `main()` | Call `logger.exception()` once, which attaches the traceback, then exit |

```python
try:
    config = yaml.safe_load(path.read_text())
except yaml.YAMLError as e:
    raise ConfigError(f"Invalid YAML in {path}") from e
```

- 🎯 **Specific exceptions:** catch the narrowest type, never a bare `except:` or a broad `except Exception` outside the top-level handler.
- 🔇 **No silent failures:** never catch an error and carry on without logging it or re-raising it.

## 🚫 What never to log

- 🔑 **Secrets:** API keys, passwords, tokens or connection strings, so log the host or "using configured credentials" instead.
- 🪪 **Personal data:** names, emails or phone numbers, so log the record's ID instead.
- 🔊 **Per-item noise:** a line for every item in a large loop, so log every N items or a summary at the end.
