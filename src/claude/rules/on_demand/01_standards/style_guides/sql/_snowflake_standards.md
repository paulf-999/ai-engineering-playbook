# ❄️ Snowflake Standards

**Purpose:** the Snowflake data types to choose, the warehouse settings that keep spend down, and how SQLFluff is used.

## ⚡ Data types

| Use | Type | Notes |
|---|---|---|
| **Numbers** | `NUMBER` | `DECIMAL` and `NUMERIC` are synonyms. Set precision and scale only when needed, such as for financial data |
| **Strings** | `VARCHAR` | `STRING` and `TEXT` are synonyms. Large max lengths are fine, so choose smaller ones only for clarity |
| **Date and time** | `TIMESTAMP_NTZ` | Convert values to UTC before storing, since NTZ keeps no timezone. `DATETIME` is a synonym, and `TIMESTAMP` maps to NTZ by default |
| **Date only** | `DATE` | When time of day isn't captured |
| **Local date and time** | `TIMESTAMP_TZ` | Only when the original timezone matters, such as a customer's local transaction time |

See the [Snowflake data types](https://docs.snowflake.com/en/sql-reference/intro-summary-data-types) and [table design considerations](https://docs.snowflake.com/en/user-guide/table-considerations).

## 💰 Cost guardrails

The team's `AUTO_SUSPEND` value and warehouse sizes are in [`sql_snowflake.md`](../../../02_team_conventions/sql_snowflake.md).

- 💤 **Auto-suspend:** set the team's `AUTO_SUSPEND` value on every pipeline warehouse, since idle warehouses are the largest spend leak.
- 📏 **Size to the query:** start small and size up only for join-heavy transformations, using the team's sizes per environment.
- 🔍 **Check scans:** read the query profile before merging a large refactor, and flag it in the PR if bytes scanned rise by more than 20%.

## 🔧 SQLFluff

SQL style is enforced by SQLFluff, and the canonical config is the `.sqlfluff` file in the dbt project. Resolve every violation before committing.

- 🔤 **Parse errors:** a `PRS` error often means a reserved keyword, such as `ORDER`, is an unquoted column name, so rename it or quote it as `"ORDER"`.

The team's SQLFluff settings and excluded rules are in [`sql_snowflake.md`](../../../02_team_conventions/sql_snowflake.md).
