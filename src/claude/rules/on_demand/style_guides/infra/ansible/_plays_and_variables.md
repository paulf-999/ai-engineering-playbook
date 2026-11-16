# 🎭 Ansible plays and variables

**Purpose:** the play settings and variable rules any Ansible repo follows. This team's playbook layout, tags and `group_vars` hierarchy are in [`team_conventions/infra/ansible.md`](../../../../path_scoped/team_conventions/infra/ansible.md).

## 🔧 Plays

- Set `gather_facts` and `become` explicitly on every play — do not rely on defaults.
- Comment each role reference briefly where its purpose is not obvious from the name.

## 📝 Variables

- **Role defaults:** prefix every variable in `roles/<role>/defaults/main.yml` with the role name, such as `nginx_port`.
- **host_vars:** put host-specific variables in `host_vars/<inventory_hostname>.yml`, with the filename exactly matching the hostname in the inventory output. Use them only when a value genuinely differs per host, and prefer `group_vars` otherwise.
- **Precedence:** `host_vars` always overrides `group_vars`, at any level.
