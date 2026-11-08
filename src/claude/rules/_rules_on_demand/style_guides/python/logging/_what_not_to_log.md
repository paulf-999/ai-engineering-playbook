<!-- version: 1.0.1 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-08 -->
# 🚫 What not to log

**Purpose:** What logs must leave out, such as secrets, personal data and full tracebacks, and a security checklist.

---

## 🚫 What NOT to log

### ❌ Never log secrets, credentials, or PII

```python
# ❌ WRONG — exposes credentials
logger.debug(f"Connecting to Airbyte: username={username}, password={password}")

# ❌ WRONG — exposes API key
logger.debug(f"Using API key: {api_key}")

# ❌ WRONG — exposes connection string with credentials
logger.debug(f"Database connection: {db_connection_string}")

# ✅ GOOD — no sensitive data
logger.debug(f"Connecting to Airbyte server at {base_url}")
logger.debug("Using configured API credentials")
logger.debug(f"Connecting to database at {db_host}")
```

**Why:** Logs are often stored, aggregated, or reviewed by non-security teams. Credentials in logs can be leaked.

### ❌ Never log full stack traces in production logs

```python
# ❌ WRONG — too noisy, includes implementation details
except Exception as e:
    logger.error(f"Error: {traceback.format_exc()}")

# ✅ GOOD — summarize for production
except ValueError as e:
    logger.error(f"Invalid configuration: {e}")
```

**Why:** Full tracebacks are verbose and exposes internal structure. The exception message is usually sufficient.

### ❌ Avoid excessive DEBUG logs in production

```python
# ❌ WRONG — logs every iteration (100K log lines!)
for item in large_list:
    logger.debug(f"Processing item: {item}")

# ✅ GOOD — log periodically or at summary
for i, item in enumerate(large_list, 1):
    if i % 1000 == 0:
        logger.debug(f"Processed {i} items...")
```

**Why:** Excessive logs consume disk space and make it hard to find real issues.

### ❌ Don't log obvious/expected outcomes

```python
# ❌ WRONG — this happens hundreds of times, not useful
logger.debug(f"Returned result: {result}")

# ✅ GOOD — log unexpected or important outcomes only
logger.warning(f"Expected 100 connections but found {len(connections)}")
```

**Why:** Logging every routine operation creates noise that obscures real problems.

### ❌ Never log personal data or customer information

```python
# ❌ WRONG
logger.info(f"Processing customer: {customer_name}, email: {email}, phone: {phone}")

# ✅ GOOD — reference by ID only
logger.info(f"Processing customer ID: {customer_id}")
```

**Why:** Personal data in logs is a privacy and compliance risk.

---

## 🔒 Security checklist

Before logging, ask:

- 🔑 **Is this a secret?** (API key, password, token, connection string) → Don't log
- 🪪 **Is this PII?** (name, email, phone, SSN) → Don't log
- 💼 **Is this sensitive business data?** (customer data, financial data) → Don't log
- 🔊 **Will this create noise?** (logged on every loop iteration?) → Log only periodically
- 🐛 **Is this useful for debugging?** (variable values, state changes) → Log it
