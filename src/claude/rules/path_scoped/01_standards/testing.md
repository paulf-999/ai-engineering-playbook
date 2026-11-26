---
paths:
  - "**/*.py"
  - "**/*.sh"
  - "**/models/**/*.sql"
---
# 🧪 Testing

**Purpose:** when code needs a test, and how tests stay in step with it.

- 🆕 **New code:** a new feature, function, class or script gets a test that checks what it's meant to do, not just that it runs.
- ⏱️ **Fast tests:** keep each test under about 1s by sharing expensive setup, such as one install or repo per module, rather than repeating it.
- 🔄 **Same commit:** change a test in the same commit as the behaviour it covers.
- 🗑️ **Dead tests:** delete a feature's tests when the feature is removed.
- 📄 **Docs:** a README, doc or rule needs no behaviour test, since following prose can't be checked by a script.

## 📚 Read on demand

[`_on_demand/01_standards/testing.md`](../../on_demand/01_standards/testing.md), in your Claude config directory, before writing or reviewing a test.
