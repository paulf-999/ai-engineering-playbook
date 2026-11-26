# 🧩 tests/plugins

**Purpose:** what each test of the plugins in `plugins/` checks.

| Test | What it checks |
|---|---|
| 🔁 [test_claude_kaizen_plugin.py](claude-kaizen/test_claude_kaizen_plugin.py) | The claude-kaizen plugin's copied skill and runner files match the repo's, its manifests agree with the skill's version, and its setup hook builds the venv once, rebuilds on new requirements, removes a half-built venv and stays silent without Python |
