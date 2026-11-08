<!-- version: 1.0.0 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-08 -->
# ❌ Error handling anti-patterns

**Purpose:** The exception-handling patterns that lose errors or their context, and when to log or re-raise.

---

## ❌ Bad patterns to avoid

### 1. Bare except clause — catches everything, including system exceptions

```python
# ❌ WRONG — catches KeyboardInterrupt, SystemExit, etc.
try:
    do_something()
except:
    pass
```

**Problem:** Masks unexpected exceptions; hides bugs.

### 2. Generic Exception — too broad

```python
# ❌ WRONG — catches unrelated exceptions
try:
    config = load_config(path)
except Exception:
    logger.error("Failed")
    return None
```

**Problem:** Catches the wrong exceptions; makes debugging harder.

### 3. Swallowing without logging — no debugging context

```python
# ❌ WRONG — no way to know what failed
try:
    os.environ["REQUIRED_VAR"]
except KeyError:
    pass  # Silent failure
```

**Problem:** Impossible to debug why the program behaves unexpectedly.

### 4. Catching specific exception without re-raising — changes control flow silently

```python
# ❌ WRONG — caller has no idea this failed
try:
    validate_config(config)
except ValueError:
    logger.error("Invalid config")
    # No re-raise; caller thinks validation passed
```

**Problem:** Caller unaware of error; program continues with invalid state.

### 5. Logging the full traceback — too verbose and exposes internals

```python
# ❌ WRONG
try:
    process()
except Exception as e:
    logger.error(f"Error: {traceback.format_exc()}")
    raise
```

**Problem:** Full tracebacks are noisy; exception message is usually sufficient.

---

## 📋 Decision tree: When to log vs. re-raise

```text
Exception occurs
    │
    ├─ Is this expected (e.g., validation error)?
    │  ├─ YES: Log at WARNING level, maybe continue with fallback
    │  └─ NO: Log at ERROR level, re-raise (caller decides what to do)
    │
    ├─ Do I have context to add (file path, values)?
    │  ├─ YES: Log with context, then re-raise
    │  └─ NO: Just re-raise (logging won't add value)
    │
    └─ Is this the last handler (main function)?
       ├─ YES: Log and handle/exit (no re-raise)
       └─ NO: Log and re-raise (let caller handle)
```
