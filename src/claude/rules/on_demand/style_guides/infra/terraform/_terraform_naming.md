# 🏷️ Terraform naming

**Purpose:** the naming standards any Terraform repo follows, for resources, modules, variables and outputs. This team's Snowflake object patterns are in [`terraform_team_conventions.md`](../../../../path_scoped/style_guides/infra/terraform_team_conventions.md), and declaration rules in [`_declarations.md`](_declarations.md).

## 📋 Contents

- [🧊 Snowflake object names](#-snowflake-object-names)
- [🔧 Terraform resource names](#-terraform-resource-names)
- [📦 Module names](#-module-names)
- [📥 Variable names](#-variable-names)
- [📤 Output names](#-output-names)

---

## 🧊 Snowflake object names

Snowflake object names follow the team's patterns in [`terraform_team_conventions.md`](../../../../path_scoped/style_guides/infra/terraform_team_conventions.md), enforced via `validation` blocks on the corresponding input variable.

## 🔧 Terraform resource names

| Construct | Convention | Example |
|-----------|------------|---------|
| Primary resource in a module | `this` | `resource "snowflake_account_role" "this"` |
| Non-primary resources | `snake_case` naming what the resource does, then what it acts on | `grant_ownership_snowflake_warehouse` |

Use `this` when a module manages a single primary resource. Name each resource descriptively when a module creates multiple related resources.

---

## 📦 Module names

| Convention | Example |
|------------|---------|
| Reusable module directories: `snake_case` | `snowflake_role`, `grants_db_access` |
| Module block labels in HCL: `snake_case` | `module "roles_and_grants"` |

---

## 📥 Variable names

| Category | Convention | Example |
|----------|------------|---------|
| Input variables | `snake_case`, apart from the team's provider variables | `sf_warehouse_name`, `role_name_ownership_perms` |

---

## 📤 Output names

Use `snake_case`, named to describe the value they expose — not the resource they come from.

Examples: `name`, `id`, `dq_framework_db`

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/infra/terraform.md`](../../../../path_scoped/style_guides/infra/terraform.md), when naming a Snowflake object, resource, module, variable or output.
