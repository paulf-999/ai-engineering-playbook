# 📁 Structure

**Purpose:** the files every module and environment needs, and what stays out of version control; provider configuration lives in [`_providers.md`](_providers.md). This team's folder layout is in [`02_team_conventions/infra/terraform.md`](../../../../../path_scoped/02_team_conventions/infra/terraform.md).

## 📋 Contents

- [📄 Standard files per module or environment](#-standard-files-per-module-or-environment)
- [🔒 What must not be committed](#-what-must-not-be-committed)

---

## 📄 Standard files per module or environment

Every module and every environment root contains at least these, plus the team's required files in [`02_team_conventions/infra/terraform.md`](../../../../../path_scoped/02_team_conventions/infra/terraform.md):

| File | Purpose |
|------|---------|
| `main.tf` | Resource definitions or module calls |
| `variables.tf` | Input variable declarations with types, descriptions, and validation |
| `outputs.tf` | Output value declarations |
| `README.md` | Module documentation — purpose, inputs, outputs, example usage |

---

## 🔒 What must not be committed

- `.env` files — document required variables in a committed template instead
- `terraform.tfstate` and `terraform.tfstate.backup` — state must be stored remotely
- Private keys or credentials of any kind
- The `detect-private-key` pre-commit hook blocks private keys, so list the other files in `.gitignore`
