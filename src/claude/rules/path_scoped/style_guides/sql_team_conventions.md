---
paths:
  - "**/*.sql"
---
# 🗄️ SQL team conventions

**Purpose:** this team's own SQL style choices. Another team can replace them with its own, while the standards stay in `sql.md`.

- 🔠 **Case:** UPPERCASE keywords, functions and literals, such as `SELECT`, `COALESCE` and `NULL`.
- 🏷️ **Singular names:** `employee` over `employees`.
- 📋 **Leading commas:** with one column per line, each comma starts its line:

```sql
SELECT
    order_id
    , customer_id
FROM orders
```

## 📚 Read on demand

- `on_demand/style_guides/sql/snowflake.md`, in your Claude config directory, when sizing a warehouse, setting `AUTO_SUSPEND`, or when a SQLFluff rule fails.
