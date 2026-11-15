# 👀 Before and after: a dbt model

**Purpose:** an illustrative example of what changes once the playbook is installed. You ask Claude to *"add a dbt model that counts each customer's orders"*.

**Without the playbook**, Claude might hard-code `FROM raw.shop.orders` and add no tests.

**With it**, the [dbt guide](../../src/claude/rules/path_scoped/style_guides/dbt.md) loads as soon as Claude opens a model, so it follows your team's style:

```sql
WITH orders AS (
    SELECT * FROM {{ ref('staging_shop_orders') }}
)

, final_cte AS (
    SELECT
        {{ create_surrogate_key(['customer_id']) }} AS "KEY"
        , customer_id
        , COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
)

SELECT * FROM final_cte
```

It also adds a YAML description for each column, with `unique` and `not_null` tests on `KEY`.
