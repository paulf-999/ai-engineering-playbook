# ❄️ SQL team conventions: Snowflake and SQLFluff

**Purpose:** this team's Snowflake warehouse settings and SQLFluff config. Another team can replace them with its own, while the standards stay beside it in `_snowflake_standards.md`. It has no `_team_conventions` suffix, so a fork replaces it by name.

## 💰 Warehouses

- 💤 **`AUTO_SUSPEND = 60`:** on every pipeline warehouse.
- 📏 **Sizes:** XS for simple aggregations, tests and dbt runs in dev, S for standard dbt runs in CI and prod, and M or above only for rare, join-heavy transformations.

## 🔧 SQLFluff

The canonical config is the `.sqlfluff` file in the dbt project.

- 🗣️ **Settings:** dialect `snowflake`, templater `dbt` and a max line length of 120 characters.

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

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/sql_team_conventions.md`](../../../path_scoped/style_guides/sql_team_conventions.md), when sizing a warehouse, setting `AUTO_SUSPEND`, or when a SQLFluff rule fails.
