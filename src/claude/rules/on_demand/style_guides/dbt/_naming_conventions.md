# 🏷️ dbt Naming Conventions

**Purpose:** Set naming standards for models, files, keys, data types, audit fields, CTEs, and null handling across all layers of the dbt project.

## 🔑 Surrogate keys

The surrogate key's name, macro and position, and the sentinel for unknown keys, are team conventions in [`_team_conventions.md`](_team_conventions.md).

## 📋 Contents

- [🔠 General conventions](#-general-conventions)
- [📂 Model layer naming](#-model-layer-naming)
- [🔍 Audit fields](#-audit-fields)
- [📅 Data type naming](#-data-type-naming)
- [🚫 Null handling](#-null-handling)
- [🔖 CTE naming](#-cte-naming)

---

## 🔠 General conventions

- Use `snake_case` for file names and Python/Jinja identifiers.
- Source column references must use the original casing from the source system (often quoted mixed case, e.g. `"MerchantNumber"`).
  - Transformed and derived columns use `lowercase_snake_case`.
- Use names based on business terminology, not source system terminology.
- Avoid reserved words as column names.
- Be consistent — use the same field names across models wherever possible.

---

## 📂 Model layer naming

| Layer | File naming convention | Example |
|-------|------------------------|---------|
| Staging | `staging_<source>_<entity>.sql` | `staging_crm_customer_list.sql` |
| Base | `<source>_<entity>.sql` | `crm_customer_list.sql` |
| Mart | `mart_<domain>_<entity>.sql` | `mart_commerce_payouts.sql` |
| Publication | `pub_<domain>_<entity>.sql` | `pub_commerce_payouts.sql` |
| Snapshots | `dim_<entity>_history.sql` | `dim_merchant_history.sql` |
| Macros | File name must match the macro name | `my_macro.sql` |

---

## 🔍 Audit fields

Staging models include the team's audit fields, listed in [`_team_conventions.md`](_team_conventions.md).

---

## 📅 Data type naming

| Type | Convention | Example |
|------|------------|---------|
| **Timestamps** | `<event>_at`, stored in UTC | `created_at` |
| **Dates** | `<event>_date` or `<event>_KEY` for date dimension joins | `snapshot_date`, `SNAPSHOT_DATE_KEY` |
| **Booleans** | Prefixed with `is_` or `has_` | `is_active`, `has_admin_access` |
| **Amounts** | Decimal — clean currency values from source with the team's numeric-cleaning macro | `gross_volume` |

---

## 🚫 Null handling

| Column type | NULL / NOT NULL |
|-------------|-----------------|
| Surrogate key | `NOT NULL` |
| Foreign keys | `NOT NULL` — use the team's unknown-key sentinel for unknown references |
| Audit fields | `NOT NULL` |
| Measures | Nullable where source data may be absent |
| All other fields | As applicable |

---

## 🔖 CTE naming

Name CTEs as [`../sql/_cte_style_guide.md`](../sql/_cte_style_guide.md) sets out. A dbt model's final SELECT reads everything from `final`:

```sql
SELECT *
FROM final
{{ limit_rows() }}
```
