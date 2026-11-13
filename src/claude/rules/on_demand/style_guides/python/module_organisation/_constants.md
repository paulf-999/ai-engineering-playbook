<!-- version: 1.0.1 -->
<!-- created: 2026-11-08 -->
<!-- updated: 2026-11-08 -->
# 🏷️ Constants

**Purpose:** How to group, name and use module-level constants.

---

## 🏷️ Constants grouping

Group related module-level constants and label the group with a comment.

```python
# Migration action states
CREATE = "CREATE"
UPDATE = "UPDATE"
DISABLE = "DISABLE"
NOOP = "NOOP"

# Default configuration values
DEFAULT_TIMEOUT = 30
DEFAULT_RETRIES = 3
DEFAULT_BATCH_SIZE = 100

# Environment variables required at startup
REQUIRED_ENV_VARS = ["AIRBYTE_API_URL", "AIRBYTE_USERNAME", "AIRBYTE_PASSWORD"]
```

**Why:** Comments make intent clear and group related constants visually.

### ✅ Naming

- 🔠 **Format:** `SCREAMING_SNAKE_CASE` (all uppercase with underscores)
- 🗂️ **Grouping:** Related constants should be grouped together
- 💬 **Comments:** Each group should have a descriptive comment above it

### ✅ When to use constants

```python
# ✅ GOOD — magic numbers and strings extracted to named constants
CREATE = "CREATE"
UPDATE = "UPDATE"
DISABLE = "DISABLE"

if action == CREATE:
    ...
elif action == UPDATE:
    ...

# ❌ BAD — magic strings in code
if action == "CREATE":
    ...
elif action == "UPDATE":
    ...
```

---

## ⚡ Quick reference

| Element | Convention | Example |
|---------|-----------|---------|
| **Public function** | No underscore | `def load_config():` |
| **Private function** | Leading underscore | `def _make_client():` |
| **Constants** | SCREAMING_SNAKE_CASE, grouped | `TIMEOUT = 30` |
| **Constant group label** | Comment above group | `# Defaults` |
