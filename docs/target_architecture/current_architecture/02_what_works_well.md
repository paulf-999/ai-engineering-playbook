<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# ✅ Current architecture: What works well

**Purpose:** the strengths of the old Claude configuration that the new design keeps.

This page is part of the [current architecture](../current_architecture.md) review.

## 🛡️ Safety and verification

- 🔐 **Safe installer:** `make install` previews every step, needs a typed confirmation, and backs up the old config first.
- 🌍 **Portability:** scripts find the config folder from a setting or their own location, rather than a fixed path, and tests check this.
- 🧪 **Checks that can fail:** tests, pre-commit hooks and CI can each block a bad change.

## 🧩 Design and review

- 💤 **Loading on demand:** rules for certain files, or rarely needed detail, stay out of most sessions.
- 👀 **Independent review:** a reviewer agent can score work in a fresh context, so the author doesn't mark its own work.
- 📜 **Recorded decisions:** a `docs/decisions/` folder in that repo explains why key choices were made.
