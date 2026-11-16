# 🏷️ dbt Naming Conventions

**Purpose:** Set naming standards for models, files, keys, data types, audit fields, CTEs, and null handling across all layers of the dbt project.

## 🔑 Surrogate keys

The surrogate key's name, macro and position, and the sentinel for unknown keys, are team conventions in [`_macros_and_keys.md`](../../team_conventions/dbt/_macros_and_keys.md). The key's input fields must uniquely identify the row.

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

Each layer's file-name prefix, and the snapshot name pattern, are the team's, in [`team_conventions/dbt.md`](../../../path_scoped/team_conventions/dbt.md).

- **Macros:** name each macro file after its macro, such as `my_macro.sql`.

---

## 🔍 Audit fields

Staging models include the team's audit fields, listed in [`_macros_and_keys.md`](../../team_conventions/dbt/_macros_and_keys.md).

---

## 📅 Data type naming

| Type | Convention | Example |
|------|------------|---------|
| **Timestamps** | `<event>_at`, stored in UTC | `created_at` |
| **Dates** | `<event>_date`, or the team's date-key pattern for date dimension joins | `snapshot_date` |
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

Name CTEs as [`../sql/_cte_style_guide.md`](../sql/_cte_style_guide.md) sets out. A dbt model's final SELECT reads everything from `final`, then appends the team's row-limiting macro:

```sql
SELECT *
FROM final
```
