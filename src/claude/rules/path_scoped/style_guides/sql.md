---
paths:
  - "**/*.sql"
---
# 🗄️ SQL Style Guide & Standards

**Purpose:** Define team SQL standards for consistency, readability, and cost optimization. Standards apply to all SQL written in the warehouse (dbt, Airflow, ad-hoc queries), except where a repo's own `.sqlfluff` config differs, which wins.

**dbt models:** the dbt style guide also loads for them and covers `ref()`, `source()` and YAML.

---

## ⚡ Key rules

- 🔠 **Case:** UPPERCASE keywords, functions and literals, such as `SELECT`, `COALESCE` and `NULL`.
- 🏷️ **Names:** `snake_case`, singular and unabbreviated, with descriptive keys such as `order_id` rather than a bare `id`.
- 🧱 **CTEs, not subqueries:** one CTE per logical step, grouped Import → Logical → Final → `SELECT`.
- 📋 **Columns:** list them explicitly, one per line, with leading commas, rather than `SELECT *` from a table.
- 🔗 **Joins:** name the join type, such as `LEFT JOIN`, use meaningful aliases and prefix every column with its table's alias.

---

## 📚 Read on demand

- `on_demand/style_guides/sql/_formatting.md`, in your Claude config directory, before writing or reformatting a query.
- `on_demand/style_guides/sql/_cte_style_guide.md`, when structuring a query or model into CTEs.
- `on_demand/style_guides/sql/_snowflake_standards.md`, when choosing a column's data type, creating or resizing a warehouse, refactoring a large query, or when a SQLFluff rule fails.
