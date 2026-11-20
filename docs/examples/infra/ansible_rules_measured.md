# 📏 Measured: do the Ansible rules change Claude's output?

**Purpose:** what 24 scripted runs showed about whether the Ansible rules make Claude follow them, on 4 common tasks in a sparse sample repo.

> [!NOTE]
> Run on 2026-11-20 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks taken from the rules as written, not whether the playbooks work, which needs a real run against hosts. It's 3 runs per task, on one model and one sample, so treat the figures as a signal, not a precise rate. The variables task edits `group_vars/` and `inventory/`, which sit outside the rules' `paths:`, so an install loads the rules there only once Claude touches a playbook or role.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sparse sample: one plain `playbooks/web.yml` with short module names, lowercase task names and no tags, a static inventory and a root `group_vars/all.yml`. Nothing in it shows the team's layout, so the conventions come only from the rules. A script checked each output against the rules.

| Task | Without | With |
|---|---|---|
| 📦 **Playbook:** install Redis on the db servers and keep it running | 11% | 90% |
| 🧩 **Role:** install the Prometheus node exporter from its tarball, with a playbook for all servers | 25% | 100% |
| 📊 **Variable:** set the nginx port to 8080 for production web servers only | 33% | 75% |
| ✏️ **Edit:** add ufw firewall tasks to the existing web playbook | 25% | 77% |
| **All checks**, the mean of the 4 task figures | **24%** | **85%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Without | With |
|---|---|---|
| 🧰 **Standards:** FQCN modules, named tasks, `changed_when` on commands, tags applied, `gather_facts` and `become` on every play, a role's `tasks/` and `defaults/`, prefixed and commented defaults, an `assert` of required variables, variables in `group_vars` rather than `host_vars` | 40% | 96% |
| 🏢 **Team conventions:** the `[app]_[asset_role]_[descriptor].yml` name in `playbooks/<app>/`, the `group_vars` and `roles` symlinks, CODEOWNERS entries, roles by full path in a capability folder, sentence-case task names, the team's tags, an `l<n>_` level file, `acme__` variable names | 6% | 88% |

## 🔍 What changed

- 📁 **The team's layout came only with the rules:** without them, no run named a playbook to the pattern, used a `playbooks/<app>/` folder, made symlinks or touched CODEOWNERS. With them, every new playbook and role did, apart from the symlinks below.
- 🧩 **Roles without the rules sat under `playbooks/roles/`:** none used a capability folder, asserted required variables or commented its defaults. With them, all 3 used `roles/observability/node_exporter/` and met every check.
- 📊 **Production variables:** without the rules, 2 runs wrote `group_vars/production.yml` and 1 wrote a `host_vars` file. With them, all 3 added an `l4_prd_acme_web` group to the inventory and its `group_vars` file.
- ✏️ **Edits copied the file without the rules:** all 3 used the short `ufw` module name and lowercase task names. With them, all 3 used `community.general.ufw` and sentence case.
- ❌ **Still missed:**
  - 🏷️ **Tags:** 2 of 3 edits left the new tasks untagged, matching the existing file, and the third tagged them `firewall`, outside the team's list.
  - 📊 **Variable names:** all 3 variable runs kept `nginx_port`, since the template reads it, rather than an `acme__` name.
  - 🔗 **Symlinks:** all 3 Redis playbooks skipped the `roles` symlink, saying no `roles/` folder existed yet.

## 🧪 How it was run

- 🗂️ **Sample project:** the sparse repo above, with a `.github/CODEOWNERS` holding one catch-all owner.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with the same prompt in both conditions, ending "Go ahead without asking me questions." It had read and write tools, plus `ln` and `mkdir`, so it could make the symlinks the rules ask for.
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a file under `playbooks/` or `roles/`: `CLAUDE.md`, the always-on rules, and the Ansible rule with its team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script read each run's new or changed files and checked them, after a self-test on a hand-made good and bad output per task. It can tell whether a rule was followed, but not whether the playbook runs.
- 🔧 **Scorer fixes after the runs:** three checks were loosened after reading the outputs, to accept Ansible's `always` and `never` tags, untagged handlers and one comment covering a pair of keys. They lifted the role task from 86% to 100%, and team conventions from 83% to 88%.
- 💰 **Cost:** $5.12 for the 24 runs, with runs that had the rules costing $3.24 against $1.89, since they wrote more files.
