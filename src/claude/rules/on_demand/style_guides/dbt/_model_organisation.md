# 🗂️ dbt Model Organisation

**Purpose:** Define the four-layer model architecture, folder structure, and the minimum requirements that every dbt model in the project must satisfy.

## 🏛️ Model layers

The project's layers, with what each selects from and materialises as, are the team's, in [`team_conventions/dbt.md`](../../../path_scoped/team_conventions/dbt.md).

## 📋 Contents

- [✅ Minimum requirements for dbt models](#-minimum-requirements-for-dbt-models)
- [📁 Folders](#-folders)
- [⚡ Incremental model configuration](#-incremental-model-configuration)

---

## ✅ Minimum requirements for dbt models

| Requirement | Detail |
|-------------|--------|
| **Surrogate key** | Staging, base and dimension models have a surrogate key, built as [`_macros_and_keys.md`](../../team_conventions/dbt/_macros_and_keys.md) sets out. An aggregate model tests its grain columns instead. |
| **dbt tests** | At minimum, apply `unique` and `not_null` tests to the surrogate key, or to an aggregate's grain columns. |
| **Source selection** | Only `staging` models select from `source()`. All downstream models use `ref()`. |
| **CTEs over subqueries** | Use CTEs — never subqueries. See [`../sql/_cte_style_guide.md`](../sql/_cte_style_guide.md). |
| **Row limiting** | Append the team's row-limiting macro, per [`_macros_and_keys.md`](../../team_conventions/dbt/_macros_and_keys.md), so dev and CI runs read fewer rows. |
| **Audit fields** | Staging models include the team's audit fields, per [`_macros_and_keys.md`](../../team_conventions/dbt/_macros_and_keys.md). |

---

## 📁 Folders

The project's folders, and where each layer's models and YAML go, are the team's, in [`_layout.md`](../../team_conventions/dbt/_layout.md).

---

## ⚡ Incremental model configuration

When a model uses `materialized='incremental'`, configure these properties explicitly — never leave them at implicit defaults:

**`unique_key`** — the column(s) that uniquely identify a row. dbt uses this to match incoming records against existing ones. Use the model's surrogate key unless the source has a reliable natural key.

**Partition filter (`is_incremental()` block)** — always include a filter that bounds the incremental run to a time window. Align the filter column with the table's clustering key:

```sql
{% if is_incremental() %}
  WHERE event_date >= DATEADD('day', -3, CURRENT_DATE)
{% endif %}
```

The lookback window (3 days above) must accommodate late-arriving data. Document the chosen window in a model comment if it deviates from the team default.
