---
<!-- version: 1.5.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: **/*.sql -->
<!-- miss_cost: low — SQL drifts from the house style and needs reformatting -->
<!-- loading: path-scoped — loads with SQL files -->
paths:
  - "**/*.sql"
---

# 🗄️ SQL Style Guide & Standards

**Purpose:** Define team SQL standards for consistency, readability, and cost optimization. Standards apply to all SQL written in the warehouse (dbt, Airflow, ad-hoc queries).

**dbt models:** the dbt style guide also loads for them and covers `ref()`, `source()` and YAML.

**Enforcement:** All SQL must pass SQLFluff validation before commit/merge. Violations surface in pre-commit checks.

---

## 🎯 Core Principles

- **Consistency:** All SQL follows the same style; code reviews focus on logic, not formatting
- **Readability:** SQL is read more than written; prioritize clarity (CTEs > subqueries; explicit aliases)
- **Cost control:** Write queries that minimize Snowflake warehouse spend (smallest warehouse sufficient, query scans optimized)

---

## 🛠️ Tooling

SQL style is enforced by **SQLFluff** in dialect mode `snowflake`:

- Pre-commit hook validates all `.sql` files and dbt models
- Violations block commits; fix before retry

**Common violations & fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| `CP01` (capitalisation.keywords) | Mixed-case keywords | Use UPPERCASE for keywords |
| Parse error (`PRS`) | A reserved keyword such as `ORDER` used as an unquoted column name | Rename the column, or quote it with Snowflake double quotes: `"ORDER"` |

---

## 💰 Cost guardrails

- **`AUTO_SUSPEND = 60`:** set on all pipeline warehouses (idle warehouses are the largest spend leak)
- **Match warehouse size to query complexity:**
  - XS: Simple aggregations, tests, dbt runs in dev
  - S: Standard dbt runs in CI/prod
  - M+: Complex transformations, join-heavy queries (should be rare)

- **Validate query scans:** check query profile before merging large refactors
  - Increased scans = increased cost; flag in the PR if bytes scanned rise by more than 20%

---

## ⚠️ Common Mistakes & Recovery

### Over-aliasing leading to unreadable queries

- ❌ `SELECT a.id, b.amt, c.dt FROM table_a a JOIN table_b b ON a.id = b.id ...`
- ✅ Use CTEs: `WITH customers AS (SELECT ...), orders AS (SELECT ...) SELECT customers.customer_id, orders.amount FROM customers INNER JOIN orders ON ...`
- **Recovery:** Refactor into CTEs following CTE style guide

---

## ✅ Pre-commit Validation

Before committing SQL changes:

- [ ] SQLFluff passes (no violations)
- [ ] Query scan cost validated if query complexity increased
- [ ] Aliases are meaningful (not single letters)

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/sql/_formatting.md`, in your Claude config directory, before writing or reformatting a query.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_cte_style_guide.md`, when structuring a query or model into CTEs.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md`, when choosing a column's data type.
- **Read on demand:** `_rules_on_demand/style_guides/sql/_sqlfluff.md`, when a SQLFluff rule fails or the config changes.
