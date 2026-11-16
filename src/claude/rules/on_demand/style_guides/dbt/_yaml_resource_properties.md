# 📄 YAML Resource Properties

**Purpose:** Set the standards for declaring dbt resource properties in YAML — covering file naming, formatting style, source definitions, tests, and sensitive data tagging.

## 🏷️ YAML file naming

- YAML files must be prefixed with an underscore (`_`) so that they sort to the top of the directory listing.
- Each layer uses a consistent file name, per the team's patterns in [`team_conventions/dbt.md`](../../../path_scoped/team_conventions/dbt.md).

## 📋 Contents

- [🎨 YAML style guide](#-yaml-style-guide)
- [🧪 Tests](#-tests)
- [📥 Source definitions](#-source-definitions)
- [🔒 Sensitive data](#-sensitive-data)

---

## 🎨 YAML style guide

- Indent with **2 spaces**.
- Keep lines within the team's maximum length, which matches the project's SQLFluff config.
- List items must be indented relative to their parent key.
- Use a blank line to separate list items that are dictionaries.

---

## 🧪 Tests

Apply at minimum `unique` and `not_null` tests to the surrogate key of every model that has one, or to an aggregate's grain columns. Declare tests in the resource property YAML co-located with the model, under `data_tests:` (named `tests:` before dbt 1.8).

```yaml
models:
  - name: staging_crm_customer_list
    columns:
      - name: <surrogate_key>
        data_tests:
          - unique
          - not_null
```

---

## 📥 Source definitions

Source YAML files select the correct database per environment, and avoid repeating the database name across tables in the same source. The team's pattern for both, and its casing for source and table names, are in [`team_conventions/dbt.md`](../../../path_scoped/team_conventions/dbt.md).

---

## 🔒 Sensitive data

Columns containing PII or data that should not be exposed must be flagged in the YAML, using the team's `meta` key in [`team_conventions/dbt.md`](../../../path_scoped/team_conventions/dbt.md).
