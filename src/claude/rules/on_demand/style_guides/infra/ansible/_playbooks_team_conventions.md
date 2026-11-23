# 📋 Ansible team conventions: playbooks

**Purpose:** how this team names, folders, links and tags its playbooks.

## 🏷️ Naming convention

Playbook files follow the pattern: `[app]_[asset_role]_[descriptor].yml`

| Segment | Meaning | Example values |
|---------|---------|----------------|
| `app` | Application or department code | `acme`, `data`, `webapp` |
| `asset_role` | Functional role of the target asset | `ilb`, `web`, `db`, `agent` |
| `descriptor` | Short description of what the playbook does | `setup`, `configure`, `upgrade` |

Examples: `acme_ilb_setup.yml`, `acme_web_configure.yml`

## 📋 Contents

- [🌳 Folder structure](#-folder-structure)
- [🔖 CODEOWNERS](#-codeowners)
- [🏷 Tags](#-tags)
- [🔧 Play standards](#-play-standards)

---

## 🌳 Folder structure

Playbooks live under `playbooks/` organised by owner or application, with optional team nesting:

```text
playbooks/
  <dept_or_app>/            # e.g. acme/, dev_ops/, obs/
    [<team>/]               # optional — e.g. dpe/, dba/
      <playbook>.yml
      group_vars -> ../../group_vars   # symlink — required
      roles -> ../../roles             # symlink — required
```

Each playbook directory must contain symlinks to the root `group_vars/` and `roles/` directories so Ansible resolves variables and roles correctly regardless of where the playbook is invoked. Adjust the relative path to match the actual directory depth — see [_variables_team_conventions.md](_variables_team_conventions.md) for the full symlink guidance.

---

## 🔖 CODEOWNERS

When adding a new playbook directory, update `.github/CODEOWNERS` with the appropriate owner. Ownership follows the directory structure — the team or individual responsible for that application or domain owns the subdirectory.

---

## 🏷 Tags

The team's standard operational tags:

| Tag | When to use |
|-----|-------------|
| `install` | Package or software installation |
| `configure` | Configuration file management |
| `restart` | Service restarts |
| `uninstall` | Package or software removal |
| `upgrade` | Version upgrades |

```bash
# Run only configuration tasks
ansible-playbook playbooks/acme/acme_ilb_setup.yml --tags configure

# Skip installation tasks
ansible-playbook playbooks/acme/acme_ilb_setup.yml --skip-tags install
```

---

## 🔧 Play standards

- Reference roles by their full path: `role: systems/azure_devops_agent`, not `role: azure_devops_agent`.

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/infra/ansible_team_conventions.md`](../../../../path_scoped/style_guides/infra/ansible_team_conventions.md), when adding a playbook or its folder or tags.
