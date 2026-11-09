<!-- version: 1.2.0 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-09 -->
# ❌ Error handling anti-patterns

**Purpose:** The exception-handling patterns that lose errors or their context, and when to log or re-raise.

---

## ❌ Bad patterns to avoid

### 🚫 1. Bare except clause — catches everything, including system exceptions

```python
# ❌ WRONG — catches KeyboardInterrupt, SystemExit, etc.
try:
    do_something()
except:
    pass
```

**Problem:** Masks unexpected exceptions; hides bugs.

### 🚫 2. Generic Exception — too broad

```python
# ❌ WRONG — catches unrelated exceptions
try:
    config = load_config(path)
except Exception:
    logger.error("Failed")
    return None
```

**Problem:** Catches the wrong exceptions; makes debugging harder.

### 🚫 3. Swallowing without logging — no debugging context

```python
# ❌ WRONG — no way to know what failed
try:
    os.environ["REQUIRED_VAR"]
except KeyError:
    pass  # Silent failure
```

**Problem:** Impossible to debug why the program behaves unexpectedly.

### 🚫 4. Catching specific exception without re-raising — changes control flow silently

```python
# ❌ WRONG — caller has no idea this failed
try:
    validate_config(config)
except ValueError:
    logger.error("Invalid config")
    # No re-raise; caller thinks validation passed
```

**Problem:** Caller unaware of error; program continues with invalid state.

### 🚫 5. Formatting the traceback into the message — hard to read and search

```python
# ❌ WRONG
try:
    process()
except ProcessingError:
    logger.error(f"Error: {traceback.format_exc()}")
    raise
```

**Problem:** the traceback lands inside the message string, so log tools can't parse it.

- ✅ **Instead:** call `logger.exception("Processing failed")` once, in the top-level handler, which attaches the traceback properly.

---

## 📋 When to log vs. re-raise

Log each error once, where the most context is known, and let it travel up from there.

| Situation | What to do |
|---|---|
| 🟡 **Expected and recoverable**, such as a missing optional file | Log at WARNING with context, use the fallback, and don't re-raise |
| 🔴 **Unexpected, and you can add context**, such as the file path | Raise a clearer error `from` it, with that context in its message, and leave the logging to the top-level handler |
| ⏭️ **Unexpected, and you have nothing to add** | Don't catch it, and let it propagate |
| 🏁 **Top-level handler**, such as `main()` | Call `logger.exception()` and exit, since nothing above can handle it |

Pattern 4 is wrong because a validation failure is not recoverable there: the caller carries on with an invalid config.
