---
paths:
  - "**/playbooks/**/*.yml"
  - "**/roles/**/*.yml"
---
# 📦 Ansible team conventions

**Purpose:** this team's Ansible names, folders, lint settings and processes. Another team can replace them with its own, while the standards stay in `ansible.md`.

## 🏷️ Names

| Construct | Convention | Example |
|-----------|------------|---------|
| Playbook files | `[app]_[asset_role]_[descriptor].yml` | `acme_ilb_setup.yml` |
| Role directories | `roles/[capability]/[role_name]` | `roles/systems/azure_devops_agent` |
| Inventory scope dirs | `[org]-[env]-[qualifier]` | `acme-prd-cde`, `acme-stg-dct` |
| Dynamic plugin files | `[provider]_[account/site]_[plugin].yml` | `aws_28122221233_aws_ec2.yml` |
| Variables in vars files | `[app/dept]__[role]_[variable_name]_[descriptor]` | `acme__nginx_port_http` |
| Task names | Sentence case, descriptive | `Install nginx package` |

## 🔩 Linting

- `ansible-lint` runs at the production profile, through a pre-commit hook.
- The only skip is `role-name[path]`, which nested capability directories need.

## 🗂️ Role capabilities

| Capability | Covers |
|------------|--------|
| `application` | Application-specific installation and configuration |
| `backups` | Backup agents and configuration |
| `database` | Database engines and clients |
| `networks` | Networking, load balancers, firewall rules |
| `observability` | Monitoring agents, logging, alerting |
| `provisioning` | VM bootstrapping and base configuration |
| `security` | Hardening, certificates, secret agents |
| `systems` | OS-level configuration, system utilities, CI/CD agents |
| `www` | Web servers and reverse proxies |

## 🔀 Process

- 📌 **Breaking role changes:** stage them on a short-lived branch with a `_BREAKINGCHANGE` suffix, such as `feature/my_role_BREAKINGCHANGE`, and don't leave it open.
- 🔖 **CODEOWNERS:** when adding a playbook or role directory, add its path to `.github/CODEOWNERS` with the owning team or person, such as `/roles/database` — `@acme/database-administration`.

## 📚 Read on demand

- [`_on_demand/style_guides/infra/ansible/_repo_structure_team_conventions.md`](../../../on_demand/style_guides/infra/ansible/_repo_structure_team_conventions.md), in your Claude config directory, before adding a file or folder to the repo.
- [`_on_demand/style_guides/infra/ansible/_playbooks_team_conventions.md`](../../../on_demand/style_guides/infra/ansible/_playbooks_team_conventions.md), when adding a playbook or its folder or tags.
- [`_on_demand/style_guides/infra/ansible/_variables_team_conventions.md`](../../../on_demand/style_guides/infra/ansible/_variables_team_conventions.md), when adding variables to `group_vars`.
