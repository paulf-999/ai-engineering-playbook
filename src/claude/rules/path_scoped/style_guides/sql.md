---
paths:
  - "**/*.sql"
---
# 🗄️ SQL Style Guide & Standards

**Purpose:** how to write readable, cost-aware SQL in the warehouse, in dbt, Airflow and ad-hoc queries, except where a repo's own `.sqlfluff` config differs, which wins. This team's casing, naming and comma style are in [`sql_team_conventions.md`](sql_team_conventions.md), which loads with this guide.

**dbt models:** the dbt style guide also loads for them and covers `ref()`, `source()` and YAML.

---

## ⚡ Key rules

- 🔠 **Case:** use one case for keywords, functions and literals throughout, the team's in its conventions.
- 🏷️ **Names:** `snake_case` and unabbreviated, with descriptive keys such as `order_id` rather than a bare `id`.
- 🧱 **CTEs, not subqueries:** one CTE per logical step, grouped Import → Logical → Final → `SELECT`.
- 📋 **Columns:** list them explicitly, one per line, rather than `SELECT *` from a table.
- 🔗 **Joins:** name the join type, such as `LEFT JOIN`, use meaningful aliases and prefix every column with its table's alias.

---

## 📚 Read on demand

- [`_on_demand/style_guides/sql/_formatting.md`](../../on_demand/style_guides/sql/_formatting.md), in your Claude config directory, before writing or reformatting a query.
- [`_on_demand/style_guides/sql/_cte_style_guide.md`](../../on_demand/style_guides/sql/_cte_style_guide.md), when structuring a query or model into CTEs.
- [`_on_demand/style_guides/sql/_snowflake_standards.md`](../../on_demand/style_guides/sql/_snowflake_standards.md), when choosing a column's data type, creating or resizing a warehouse, refactoring a large query, or when a SQLFluff rule fails.
