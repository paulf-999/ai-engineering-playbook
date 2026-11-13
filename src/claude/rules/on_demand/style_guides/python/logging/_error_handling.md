<!-- created: 2026-08-28 -->
# 🚨 Logging in Error Handling

**Purpose:** Establish logging patterns for exception handling — ensuring errors are logged with context before being raised or handled.

---

## ✅ Always log before re-raising

Log errors with context before re-raising exceptions — provides debugging information without silencing the error.

```python
try:
    with open(config_path) as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logger.error(f"Config file not found: {config_path}")
    raise
except yaml.YAMLError as e:
    logger.error(f"Invalid YAML in {config_path}: {e}")
    raise
```

**Why:**

- Logs provide debugging context (which file, why it failed)
- Re-raising preserves the stack trace for the caller
- Caller can decide how to handle the error (retry, fallback, fail)

---

## ✅ Specific exception types

Catch specific exceptions, not generic `Exception`:

```python
# ✅ GOOD — catches specific error, logs context
try:
    os.environ["REQUIRED_VAR"]
except KeyError:
    logger.error("Required environment variable not set: REQUIRED_VAR")
    raise EnvironmentError("REQUIRED_VAR is not set")
```

**Why:** Specific exception types help isolate the problem and prevent masking unrelated errors.

---

## ✅ Use appropriate log level for error context

| Scenario | Level | Example |
|----------|-------|---------|
| **Expected validation error** | WARNING | `logger.warning(f"Skipping invalid connection: {e}")` |
| **Unexpected system error** | ERROR | `logger.error(f"System error during migration: {e}")` |
| **Critical failure** | CRITICAL | `logger.critical(f"Cannot start: {e}")` |

### Expected errors (WARNING level)

```python
# Validation errors expected from user input
try:
    validate_config(user_config)
except ValueError as e:
    logger.warning(f"Invalid user config: {e}")
    # Maybe retry or use fallback
```

### Unexpected errors (ERROR level)

```python
# System errors not expected to happen
try:
    client = AirbyteClient()
except ConnectionError as e:
    logger.error(f"Failed to connect to Airbyte server: {e}")
    raise
```

---

## ✅ Use `finally` for guaranteed cleanup with logging

```python
client = None
try:
    client = AirbyteClient()
    result = client.migrate(connections)
except ConnectionError as e:
    logger.error(f"Migration failed: {e}")
    raise
finally:
    if client is not None:
        try:
            client.close()
            logger.debug("Client closed successfully")
        except ConnectionError as e:
            logger.warning(f"Error closing client: {e}")
```

**Why:** `finally` runs regardless of success or exception. Ensure critical cleanup happens and log any cleanup errors.
