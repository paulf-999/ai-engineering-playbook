# 👀 Before and after: a dbt model

**Purpose:** what Claude actually wrote for the same dbt request, with and without the playbook's instructions.

Both runs got the same prompt, *"Add a dbt model that counts each customer's orders."*, in a small sample project with one staging model, `staging_shop_orders`.

> [!NOTE]
> This is one run of each, with the rules pasted into the prompt rather than installed, so it illustrates the difference rather than measuring it. [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) tracks a rerun across several tasks with a real install.

## ➖ Without the playbook

Claude already uses `ref()`, and adds a description and tests for each column:

```sql
-- models/marts/customer_order_counts.sql
SELECT
    customer_id
    , COUNT(order_id) AS order_count
FROM {{ ref('staging_shop_orders') }}
GROUP BY customer_id
```

## ➕ With the playbook

Claude follows the [dbt guide](../../src/claude/rules/path_scoped/style_guides/dbt.md) and its child files on naming, layers and CTEs:

```sql
-- models/mart/shop/mart_shop_customer_order_count.sql
{{ config(materialized='table') }}

WITH ORDERS AS (
    SELECT
        order_id
        , customer_id
    FROM {{ ref('staging_shop_orders') }}
),

FINAL AS (
    SELECT
        /* MD5 stands in for create_surrogate_key(), which this project doesn't define yet */
        MD5(CAST(customer_id AS VARCHAR)) AS "KEY"
        , customer_id
        , COUNT(order_id) AS order_count
    FROM ORDERS
    GROUP BY 1, 2
)

SELECT *
FROM FINAL
```

## 🔍 What changed

| | Without | With |
|---|---|---|
| 🏷️ **Name** | `customer_order_counts` | `mart_shop_customer_order_count`, with the mart prefix |
| 🔑 **Surrogate key** | None | `KEY` first, with `unique` and `not_null` tests |
| 🧱 **Structure** | One `SELECT` | Import and final CTEs |
| 🧊 **Materialisation** | Not set | `table`, the mart layer's default |
| ⚠️ **Gaps flagged** | None | It said the project lacks the team's `create_surrogate_key()` and `limit_rows()` macros and a base layer |

## 🧪 How it was run

Each run was a separate `claude -p --safe-mode` session, so no other instructions loaded. The "with" run added the files a real install would load for a dbt model to its system prompt: [`CLAUDE.md`](../../src/claude/CLAUDE.md), the always-on rules, and the dbt, SQL, security and testing guides. This matches an install closely but isn't the real loading, and one run of each can vary.
