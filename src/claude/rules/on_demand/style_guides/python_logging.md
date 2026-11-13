<!-- version: 1.1.9 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: medium — logs leak secrets or miss what's needed to debug -->
# 📝 Python Logging Conventions

**Purpose:** Establish logging standards for debugging, monitoring, and auditing — ensuring logs are useful, secure, and structured.

---

## ⚡ Quick reference

| Scenario | Level | Example |
|---|---|---|
| **Function starts/ends** | DEBUG | `logger.debug("Starting migration process")` |
| **Important decision** | INFO | `logger.info("Using fallback config")` |
| **State change** | INFO | `logger.info("Connection disabled")` |
| **Unexpected but recoverable** | WARNING | `logger.warning("File not found, using default")` |
| **Error before re-raise** | ERROR | `logger.error(f"Config invalid: {e}")` |
| **Development debug info** | DEBUG | `logger.debug(f"Variable x = {x}")` |

## 📚 Read on demand

- `on_demand/style_guides/python_logging/_setup_and_levels.md`, in your Claude config directory, for logger setup and levels.
- `on_demand/style_guides/python_logging/_what_to_log.md`, in your Claude config directory, for what to log.
- `on_demand/style_guides/python_logging/_what_not_to_log.md`, in your Claude config directory, for what to leave out of logs.
- `on_demand/style_guides/python_logging/_error_handling.md`, in your Claude config directory, for the patterns to follow.
- `on_demand/style_guides/python_logging/_error_anti_patterns.md`, in your Claude config directory, for the patterns to avoid.
