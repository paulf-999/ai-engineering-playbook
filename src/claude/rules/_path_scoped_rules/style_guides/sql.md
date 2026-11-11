---
paths:
  - "**/*.sql"
---
<!-- version: 1.7.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: SQL files -->
<!-- miss_cost: low — SQL drifts from the house style and needs reformatting -->
# 🗄️ SQL Style Guide & Standards

**Purpose:** Define team SQL standards for consistency, readability, and cost optimization. Standards apply to all SQL written in the warehouse (dbt, Airflow, ad-hoc queries).

**dbt models:** the dbt style guide also loads for them and covers `ref()`, `source()` and YAML.

---

## 🎯 Core Principles

- **Consistency:** All SQL follows the same style; code reviews focus on logic, not formatting
- **Readability:** SQL is read more than written; prioritize clarity (CTEs > subqueries; explicit aliases)
- **Cost control:** Write queries that minimize Snowflake warehouse spend (smallest warehouse sufficient, query scans optimized)

---

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/sql/_formatting.md`, in your Claude config directory, before writing or reformatting a query.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_cte_style_guide.md`, when structuring a query or model into CTEs.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md`, when choosing a column's data type.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_sqlfluff.md`, when a SQLFluff rule fails or the config changes.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_cost_guardrails.md`, when creating or resizing a warehouse, or refactoring a large query.
