# 🐍 Azure DevOps team conventions: Python jobs

**Purpose:** how this team's jobs set up Python and install packages, so CI runs the versions the repo pins.

## 🧰 Setup

Every Python job checks out, then builds a fresh venv with the shared preparation script:

```yaml
steps:
    - checkout: self
      clean: true
      displayName: Git checkout

    - task: Bash@3
      inputs:
          filePath: $(CICD_SCRIPTS_DIR)/common/venv_preparation.sh
          arguments: requirements.txt  # the repo's central requirements file
      displayName: 'Prep step: set up the venv with the required Python packages'
      env:
          PACKAGE_FEED_TOKEN: $(<feed-token-secret>)  # from Key Vault, passed through env since secrets aren't mapped
```

## 📦 Installing packages

- 🗂️ **One script:** the venv preparation script removes any old `venv`, creates a new one with the agent's supported Python and activates it.
- 📌 **Central requirements:** every job installs from the repo's `requirements.txt`, so CI never drifts from local.
- 🔐 **Private feed:** packages come from the team's private feed, whose read-only token reaches the script only through `env:`.
- 🙈 **Token redaction:** the script turns off `set -x` before installing, and pipes pip's output through `sed` to redact the token.

## 📞 Called by

- [`rules/path_scoped/style_guides/azure_devops_team_conventions.md`](../../../path_scoped/style_guides/azure_devops_team_conventions.md), when a job sets up Python or installs packages.
