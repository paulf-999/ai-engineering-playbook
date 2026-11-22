# 🌳 Terraform team conventions: layout

**Purpose:** where this team's Terraform keeps its environments and modules, and how environment sub-modules are ordered.

## 🌳 Top-level layout

```text
terraform/
├── environments/         # Environment-specific root modules
│   ├── dev/
│   ├── uat/
│   ├── cicd/
│   ├── prod/
│   └── global/
├── modules/              # Reusable module definitions
│   ├── account_level_objects/
│   │   ├── snowflake_role/
│   │   ├── snowflake_service_user/
│   │   └── warehouse/
│   └── grants/
│       ├── default_grants_new_role_v1/
│       └── grants_db_access/
│           ├── grant_ownership_all_db_objects/
│           ├── grant_read_only_db_access/
│           └── grant_write_db_access/
└── examples/             # Standalone usage examples for modules
```

## 🔢 Numbered subdirectory convention

Within an environment, sub-modules are numbered to make dependency order explicit:

```text
environments/prod/
├── 1_roles_and_grants/
├── 2_account_level_objects/
└── ...
```

Lower numbers must be applied before higher numbers — do not rely on implicit ordering.

## 📞 Called by

- [`rules/path_scoped/style_guides/infra/terraform_team_conventions.md`](../../../../path_scoped/style_guides/infra/terraform_team_conventions.md), when adding a module or environment.
