---
paths:
  - "**/*.tf"
---
# 🏗️ Terraform team conventions

**Purpose:** this team's Terraform environments, layout, names, provider settings and pipelines. Another team can replace them with its own, while the standards stay in `style_guides/infra/terraform.md`.

## 🌍 Environments and tools

- 🧊 **Target:** Terraform manages Snowflake only, and deploys through Azure Pipelines, with secrets from Azure Key Vault.
- 🗂️ **Roots:** `dev`, `uat`, `cicd`, `prod` and `global`, each under `terraform/environments/`, with shared modules in `terraform/modules/`.
- 📄 **Files:** every module and environment root also has `provider.tf`. `.env_template` lists local variables, and `local_terraform_dev.sh` sets up local runs.

## 🔒 Provider

Pin the Snowflake provider to an **exact version** in all environment root modules. Do not use range constraints (`~>`, `>=`) in environments — only in module `provider.tf` files where caller flexibility is needed.

```terraform
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    snowflake = {
      source  = "snowflakedb/snowflake"
      version = "2.5.0"
    }
  }
}
```

- 🔑 **Variables:** provider and authentication variables are `SCREAMING_SNAKE_CASE`, such as `SNOWFLAKE_ORGANIZATION_NAME`, with the key path in `SNOWFLAKE_PRIVATE_KEY_PATH` and the names listed in each environment's `.env_template`.
- ➡️ **Passing:** always pass providers to modules explicitly with the `providers` argument, rather than relying on inheritance.

## 🧊 Snowflake object names

Snowflake objects are UPPER_CASE. Naming patterns are enforced via `validation` blocks on the corresponding input variable.

### Roles

```text
<PREFIX>_<NAME>_<SUFFIX>
```

| Component | Allowed values |
|-----------|---------------|
| Prefix | `ACCESS`, `PRIV`, `FUNC`, `PRD`, `CICD`, `UAT`, `DTE`, `OWNER` |
| Name | Uppercase letters and underscores only — no numbers |
| Suffix | `ALL_ROLE`, `SEL_ROLE`, `ROLE` |

Examples: `FUNC_CREATE_MODIFY_DATABASE_ROLE`, `ACCESS_READ_ONLY_ROLE`

### Warehouses

Pattern: `<NAME>_WH` — e.g. `DEV_WH`, `APP_DB_FILE_SUBMITTER_WH`

## 🔁 Layered resource pattern

Within a module, follow the create → ownership → usage pattern for Snowflake resources:

```terraform
# 1. Create the resource
resource "snowflake_warehouse" "this" { ... }

# 2. Grant OWNERSHIP to the owning role
resource "snowflake_grant_ownership" "grant_ownership_snowflake_warehouse" { ... }

# 3. Grant USAGE to consumer roles
resource "snowflake_grant_privileges_to_account_role" "grant_usage_snowflake_warehouse" { ... }
```

This pattern keeps permission management co-located with the resource it governs.

## 📚 Read on demand

- `on_demand/02_team_conventions/infra/terraform/_layout.md`, in your Claude config directory, when adding a module or environment.
- `on_demand/02_team_conventions/infra/terraform/_ci_and_tooling.md`, when a pre-commit hook or pipeline stage fails.
