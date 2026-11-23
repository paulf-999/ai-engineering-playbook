# 🧩 dbt team conventions: macros and keys

**Purpose:** the team's macros, packages, key column and audit fields, which the dbt guides refer to by role, such as "the team's surrogate key macro", so a change here applies everywhere.

## 🔑 Surrogate key

Staging, base and dimension models have a surrogate key named `KEY`, built with the `create_surrogate_key` macro, a wrapper around `dbt_utils.generate_surrogate_key`:

```sql
{{ create_surrogate_key(['FIELD1', 'FIELD2']) }} AS "KEY"
```

- **First column:** `KEY` is always the first column in the SELECT list.
- **Unknown references:** `unknown_key()` returns the sentinel for an unknown or missing key, in place of `-1` or `NULL`.
- **Aggregates:** an aggregate model needs no `KEY`.

## 🛠️ Team macros

Use these in preference to writing equivalent logic inline.

| Macro | Description |
|-------|-------------|
| `create_surrogate_key(field_list)` | Generates a surrogate key from a list of fields. Use it instead of calling `dbt_utils` directly. |
| `clean_and_cast_numeric(field_expr, precision, scale, default_value)` | Cleans currency strings (strips symbols, handles parentheses as negatives) and casts to the given precision and scale. |
| `clean_string_for_join(field_expr)` | Normalises a string for safe use in join conditions (trims whitespace, uppercases). |
| `unknown_key()` | Returns the sentinel value for unknown or missing surrogate key references. |
| `limit_rows()` | Returns `LIMIT {{ var('limit_rows') }}` on `dev` and `cicd` targets, and nothing in `prod`. |
| `dbt_last_modified_field()` | Appends the `DA_FILE_LAST_MODIFIED` audit column. |

- **Row limiting:** append `{{ limit_rows() }}` to the final SELECT, to major intermediate CTEs and to snapshots.
- **Documented:** every macro is documented in a `macros.yml` file.

## 📦 dbt packages

| Package | Version | Purpose |
|---------|---------|---------|
| `dbt-labs/dbt_utils` | 1.3.3 | General utility macros (surrogate keys, date spine, etc.) |
| `godatadriven/dbt_date` | 0.14.2 | Date dimension and date utility macros |
| `dbt-labs/audit_helper` | 0.12.2 | Helpers for comparing model outputs during refactoring |
| `brooklyn-data/dbt_artifacts` | 2.9.3 | Captures dbt run metadata to Snowflake for observability |
| `get-select/dbt_snowflake_monitoring` | 5.5.1 | Snowflake query cost and performance monitoring |
| `dbt-labs/dbt_external_tables` | 0.12.0 | Manages Snowflake external table definitions |
| `dbt-labs/dbt_project_evaluator` | 1.0.2 | Enforces dbt project structure best practices |

## 🔍 Audit fields

Staging models include these `NOT NULL` fields, added by `dbt_last_modified_field()` and the related audit macros:

| Field | Description |
|-------|-------------|
| `DA_FILE_YEARMONTH` | Year-month of the source file |
| `DA_PROCESS_ID` | ID of the process that loaded the record |
| `DA_FILE_NAME` | Name of the source file |
| `DA_FILE_ROW_NUMBER` | Row number within the source file |
| `DA_UNIQUE_KEY` | Unique key from the source system |
| `DA_FILE_LAST_MODIFIED` | Last modified timestamp of the source file |
| `DA_START_SCAN_TIME` | Timestamp when the scan or load started |

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/dbt_team_conventions.md`](../../../path_scoped/style_guides/dbt_team_conventions.md), before writing logic a team macro or package may already cover, or using the team's key column or audit fields.
