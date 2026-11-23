# 🌳 dbt team conventions: layout

**Purpose:** where this team's dbt project keeps its models, YAML and macros.

## 📁 Additional directories

| Directory | Purpose |
|-----------|---------|
| `warehouse/` | Dimensional and fact table models (e.g. `dim_merchant`) |
| `intermediate/` | Intermediate transformation models where needed between layers |
| `operations/` | Operational and admin models |
| `dq_framework/` | Data quality framework models |

---

## 🌳 Folder structure

```text
<dbt_project>/
└── models/
    ├── staging/
    │   └── <source_system>/
    │       ├── _staging_src.yml         # source definitions
    │       └── staging_<source>_<entity>.sql
    ├── base/
    │   └── <source_system>/
    │       ├── _src_base.yml
    │       └── <source>_<entity>.sql
    ├── mart/
    │   └── <domain>/
    │       └── mart_<domain>_<entity>.sql
    ├── publication/
    │   └── <domain>/
    │       └── pub_<domain>_<entity>.sql
    ├── warehouse/
    ├── intermediate/
    ├── operations/
    └── dq_framework/
```

Source systems each have a corresponding folder under both `staging/` and `base/`. Marts and publications are organised by **business domain**, not by source system.

## 🧩 Macro folders

Macros are grouped by category under `macros/`:

```text
macros/
├── audit_field_macros/         # DA_* audit field generation
├── data_processing_macros/     # Numeric cleaning, surrogate key, string normalisation
├── environment_macros/         # limit_rows(), environment-conditional logic
└── helper_macros/
    ├── dbt_test_helper_macros/
    ├── jinja_function_wrapper_macros/
    └── validation_macros/
```

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/dbt_team_conventions.md`](../../../path_scoped/style_guides/dbt_team_conventions.md), when adding a folder or placing a model or YAML file.
