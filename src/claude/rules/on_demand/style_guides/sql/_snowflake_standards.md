# ❄️ Snowflake Standards

**Purpose:** the Snowflake data types to choose, the warehouse settings that keep spend down, and the team's SQLFluff settings.

> 🏢 **Team conventions:** the warehouse sizes and `AUTO_SUSPEND = 60` under Cost guardrails, and the whole SQLFluff section. The rest is good practice for any team. Keep them, or propose a change by PR to this repo.

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

- 💤 **`AUTO_SUSPEND = 60`:** set it on every pipeline warehouse, since idle warehouses are the largest spend leak.
- 📏 **Size to the query:** XS for simple aggregations, tests and dbt runs in dev, S for standard dbt runs in CI and prod, and M or above only for rare, join-heavy transformations.
- 🔍 **Check scans:** read the query profile before merging a large refactor, and flag it in the PR if bytes scanned rise by more than 20%.

## 🔧 SQLFluff

SQL style is enforced by SQLFluff, and the canonical config is the `.sqlfluff` file in the dbt project. Resolve every violation before committing.

- 🗣️ **Settings:** dialect `snowflake`, templater `dbt` and a max line length of 120 characters.
- 🔤 **Parse errors:** a `PRS` error often means a reserved keyword, such as `ORDER`, is an unquoted column name, so rename it or quote it as `"ORDER"`.

The team config excludes these rules. Codes use SQLFluff 2.0+ names, with the legacy alias older configs may use in brackets:

| Rule | What it checks | Why it's excluded |
|---|---|---|
| `RF02` (`L027`) | Columns are qualified when a query reads from more than one table | Not enforced by lint, though `_formatting.md` still asks for table prefixes in joins |
| `RF04` (`L029`) | Unreserved keywords aren't used as identifiers | Legacy column names use them |
| `AM02` (`L033`) | `UNION` is written as `UNION ALL` or `UNION DISTINCT` | Bare `UNION` is allowed |
| `ST06` (`L034`) | Wildcards and simple columns come before calculations in `SELECT` | Not enforced by lint, though `_formatting.md` still lists plain fields before aggregates |
| `RF05` (`L057`) | Identifiers contain no special characters | Source data has them |
| `RF06` (`L059`) | Identifiers aren't quoted unnecessarily | Unnecessary quoting is allowed |
| `LT15` | No run of too many blank lines | Extra blank lines between CTEs are allowed |
| `ST09` | Join conditions list the earlier table first | Join condition order is not enforced |
