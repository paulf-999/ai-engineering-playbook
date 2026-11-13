---
paths:
  - "**/*.py"
  - "**/*.sh"
  - "**/*.sql"
---
<!-- created: 2026-08-28 -->
<!-- applies_to: Python, shell and SQL files -->
<!-- miss_cost: medium — code changes ship untested or tests fall out of step -->
# 🧪 Testing

**Purpose:** when code needs a test, and how tests stay in step with it.

- 🆕 **New code:** a new feature, function, class or script gets a test that checks what it's meant to do, not just that it runs.
- 🔄 **Same commit:** change a test in the same commit as the behaviour it covers.
- 🗑️ **Dead tests:** delete a feature's tests when the feature is removed.
- 📄 **Docs:** a README, doc or rule needs no behaviour test, since following prose can't be checked by a script.

## 📚 Read on demand

- `on_demand/testing/_testing_design_pattern.md`, in your Claude config directory, before writing a new test.
- `on_demand/testing/_testing_anti_patterns.md`, before writing or reviewing a test, for the mistakes that make tests mislead.
