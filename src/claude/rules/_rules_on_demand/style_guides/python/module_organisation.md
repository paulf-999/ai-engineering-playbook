<!-- version: 1.2.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-10 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — modules lose their docstrings and clear interfaces -->
# 📦 Python Module Organisation

**Purpose:** Establish conventions for module docstrings, metadata, and public/private function organisation — ensuring modules are self-documenting and their interfaces are clear.

---

## 📋 Contents

- [Module docstrings & metadata](#-module-docstrings--metadata) — `_rules_on_demand/style_guides/python/module_organisation/_docstrings.md`
- [Public vs private functions](#-public-vs-private-functions) — `_rules_on_demand/style_guides/python/module_organisation/_public_private.md`
- [Quick reference](#-quick-reference)

---

## 📝 Module docstrings & metadata

- **Read on demand:** `_rules_on_demand/style_guides/python/module_organisation/_docstrings.md`, in your Claude config directory, for module docstrings.
- **Read on demand:** `_rules_on_demand/style_guides/python/module_organisation/_metadata_and_ordering.md`, in your Claude config directory, for module metadata and function ordering.

---

## 🔒 Public vs private functions

- **Read on demand:** `_rules_on_demand/style_guides/python/module_organisation/_public_private.md`, in your Claude config directory, for public and private functions.
- **Read on demand:** `_rules_on_demand/style_guides/python/module_organisation/_constants.md`, in your Claude config directory, for module-level constants.

---

## ⚡ Quick reference

| Element | Convention | Example |
|---------|-----------|---------|
| **Module docstring** | One sentence at top, before imports | `"""YAML config loader with ${ENV_VAR} interpolation."""` |
| **Date created** | Git history | `git log --follow <file>` |
| **`__author__`** | String, after docstring | `__author__ = "Your Name"` |
| **`__version__`** | String, after docstring | `__version__ = "0.1"` |
| **Public function** | No underscore | `def load_config():` |
| **Private function** | Leading underscore | `def _make_client():` |
| **Constants** | SCREAMING_SNAKE_CASE, grouped | `TIMEOUT = 30` |
| **Constant group label** | Comment above group | `# Defaults` |
