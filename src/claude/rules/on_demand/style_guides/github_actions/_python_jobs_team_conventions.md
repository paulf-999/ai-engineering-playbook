# 🐍 GitHub Actions team conventions: Python jobs

**Purpose:** how this team's jobs set up Python, install tools and cache, so CI runs the versions the repo pins.

## 🧰 Setup

Every Python job checks out, then sets up Python with pip's cache keyed on `requirements.txt`:

```yaml
steps:
    - uses: actions/checkout@<sha>  # vX.Y.Z
    - uses: actions/setup-python@<sha>  # vX.Y.Z
      with:
          python-version: '3.13'
          cache: pip
          cache-dependency-path: requirements.txt
```

## 📦 Installing tools

- 🎯 **Only what the job needs:** install the job's own tools, not the whole of `requirements.txt`, and say which in the step's comment.
- 📌 **Versions from the repo:** read each version from `requirements.txt` with `grep -oE '^<tool>==[^ ]+'`, so CI never drifts from local.
- 🪝 **pre-commit:** install only `pre-commit`, since each hook installs its own tools, and cache `~/.cache/pre-commit` keyed on `hashFiles('.pre-commit-config.yaml')`.
- 🧪 **Tests:** install `pytest`, `pytest-xdist` and `pyyaml` the same way, then run `pytest`.

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/github_actions_team_conventions.md`](../../../path_scoped/style_guides/github_actions_team_conventions.md), when a job sets up Python, installs a tool or caches dependencies.
