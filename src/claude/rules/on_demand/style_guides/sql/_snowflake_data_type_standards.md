<!-- created: 2026-04-08 -->
# ❄️ Snowflake Data Type Standards

**Purpose:** Define a simple, consistent standard for selecting Snowflake data types across all projects.

## 📋 Contents

- [⚡ Data types at a glance](#-data-types-at-a-glance)
- [📋 Why each type](#-why-each-type)
- [🔗 References](#-references)

---

## ⚡ Data types at a glance

- **Numeric:** use `NUMBER`
- **String:** use `VARCHAR`
- **Date/Time:** use `TIMESTAMP_NTZ`, converting values to UTC before storing them, since NTZ keeps no timezone
- **Date (only):** use `DATE` when time-of-day is not being captured
- **Timezone-specific Date/Time:** use `TIMESTAMP_TZ` only when the original timezone must be preserved

---

## 📋 Why each type

This section provides clarification on *why* each data type is preferred.

| Category        | Reason                                                   | Usage Notes |
|-----------------|----------------------------------------------------------|-------------|
| **NUMBER**      | `DECIMAL` and `NUMERIC` are synonyms of `NUMBER`.        | Use explicit precision/scale only when needed (e.g., financial data). |
| **VARCHAR**     | `STRING` and `TEXT` are synonyms of `VARCHAR`.           | Large max lengths are fine; choose smaller lengths only for clarity. |
| **TIMESTAMP_NTZ** | `DATETIME` is a synonym, and `TIMESTAMP` maps to NTZ by default.             | Convert to UTC before loading, since NTZ does no conversion. |
| **DATE**        | Represents a date without time-of-day.                   | Use only when time-of-day is irrelevant. |
| **TIMESTAMP_TZ** | Required only when timezone must be preserved.          | Use when original timezone is meaningful (e.g., a customer's local transaction time). |

---

## 🔗 References

- [Snowflake Data Types](https://docs.snowflake.com/en/sql-reference/intro-summary-data-types)
- [Snowflake Table Design Considerations](https://docs.snowflake.com/en/user-guide/table-considerations)
