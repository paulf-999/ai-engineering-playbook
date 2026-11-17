# 👀 Before and after: a dbt model

**Purpose:** what Claude actually wrote for the same dbt request, with and without the playbook's instructions.

Both runs got the same prompt, *"Add a dbt model that counts each customer's orders."*, in a small sample project with one staging model, `staging_shop_orders`.

> [!NOTE]
> This is one run of each, on 2026-11-16 with Claude Opus 5.5, so it illustrates the difference rather than measuring it. [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) tracks a rerun across several tasks with a real install.

## ➖ Without the playbook

Claude already uses `ref()`, and adds a YAML file with `unique` and `not_null` tests on the grain:

```sql
-- models/marts/customer_order_counts.sql
SELECT
    customer_id
    , COUNT(order_id) AS order_count
FROM {{ ref('staging_shop_orders') }}
WHERE customer_id IS NOT NULL
GROUP BY customer_id
```

```yaml
# models/marts/customer_order_counts.yml
version: 2
models:
  - name: customer_order_counts
    description: One row per customer with the number of orders they have placed.
    columns:
      - name: customer_id
        tests: [unique, not_null]
      - name: order_count
        tests: [not_null]
```

## ➕ With the playbook

Claude follows the [dbt guide](../../src/claude/rules/path_scoped/01_standards/style_guides/dbt.md) and its child files on naming, layers and CTEs:

```sql
-- models/mart/shop/mart_shop_customer_order_counts.sql
{{ config(materialized='table') }}

WITH orders AS (
    SELECT
        order_id
        , customer_id
    FROM {{ ref('staging_shop_orders') }}
    WHERE customer_id IS NOT NULL
),

final AS (
    SELECT
        orders.customer_id
        , COUNT(orders.order_id) AS order_count
    FROM orders
    GROUP BY orders.customer_id
)

SELECT
    customer_id
    , order_count
FROM final
```

```yaml
# models/mart/shop/_mart_shop.yml
version: 2

models:
  - name: mart_shop_customer_order_counts
    description: One row per customer, with the number of orders they have placed. Orders with no customer are excluded.
    columns:
      - name: customer_id
        description: Identifier of the customer who placed the orders. The grain of this model.
        tests:
          - unique
          - not_null

      - name: order_count
        description: Number of orders the customer has placed, across all order statuses.
        tests:
          - not_null
```

## 🔍 What changed

| | Without | With |
|---|---|---|
| 🏷️ **Name** | `customer_order_counts` in `marts/` | `mart_shop_customer_order_counts` in `mart/shop/`, with the layer prefix |
| 🧱 **Structure** | One `SELECT` | An import CTE and a `final` CTE, with an explicit column list |
| 🧊 **Materialisation** | Not set | `table`, the mart layer's default |
| 📝 **Descriptions** | The model only | The model and every column |
| 🧪 **Tests** | `unique` and `not_null` on the grain | The same |
| ⚠️ **Gaps flagged** | The undeclared source | The undeclared source, the missing base layer and the missing `limit_rows()` macro |

- ❌ **Still breaks a rule:** the name is plural, `counts`, though the [SQL guide](../../src/claude/rules/path_scoped/01_standards/style_guides/sql.md) asks for singular names.
- 🔑 **No key column:** correctly, since the [team conventions](../../src/claude/rules/on_demand/02_team_conventions/dbt/_macros_and_keys.md) give an aggregate model none.

## 🧪 How it was run

Each run was a separate `claude -p --safe-mode` session in the same sample project, so no other instructions loaded. The "with" run added the files an install loads for a dbt model to its system prompt: [`CLAUDE.md`](../../src/claude/CLAUDE.md), the always-on rules, and the dbt, SQL and testing guides. Their `on_demand/` child files sat in a config folder for Claude to read when a rule pointed there. This matches an install closely but isn't the real loading, and one run of each can vary.
