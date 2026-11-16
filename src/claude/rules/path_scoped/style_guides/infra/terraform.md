---
paths:
  - "**/*.tf"
---
# 🏗️ Terraform Style Guide & Standards

**Purpose:** how to write and ship Terraform for infrastructure. This team's environments, layout, names, provider pin and pipelines are in [`team_conventions/infra/terraform.md`](../../team_conventions/infra/terraform.md), which loads with this guide.

## 🏗️ Core principles

- **Separation by environment:** each environment is an independent Terraform root module with its own state.
- **Modules for reuse:** shared resource patterns (roles, warehouses, grants) live in reusable modules, called from environment configurations.
- **Config-driven:** no credentials or environment-specific values are hardcoded, and a committed template lists the variables local setup needs.
- **Validation-first:** variable inputs are validated with `validation` blocks; naming conventions for Snowflake objects are enforced at the variable level.
- **Infrastructure only:** Terraform manages infrastructure, such as roles, warehouses, databases and grants, not application logic.
- **Formatting and hooks:** run `terraform fmt -recursive` before committing, and fix a failing pre-commit hook rather than suppress it without a documented reason.

## 📚 Read on demand

- `on_demand/style_guides/infra/terraform/_structure.md`, in your Claude config directory, when adding a module or environment, or deciding what to commit.
- `on_demand/style_guides/infra/terraform/_conventions.md`, when naming a Snowflake object, resource, module, variable or output.
- `on_demand/style_guides/infra/terraform/_declarations.md`, when declaring a variable or output, or adding a validation block.
- `on_demand/style_guides/infra/terraform/_modules.md`, when composing modules, using `for_each` or adding a `lifecycle` block.
- `on_demand/style_guides/infra/terraform/_providers.md`, when pinning, authenticating or configuring the Snowflake provider.
