<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# ⚠️ Current architecture: Where complexity outran evidence

**Purpose:** where the old Claude configuration grew heavier than the evidence for it justified.

This page is part of the [current architecture](../current_architecture.md) review. It found five problems:

- 🏋️ **Always-on weight:** about 30,000 tokens of rules load into every session, whatever the task, and nothing measures how many a task uses.
- 🔁 **Per-turn overhead:** a hook adds the response-format rules to every prompt, including trivial ones.
- 📐 **Rules about rules:** standards for writing rules, scoring them and dating them add upkeep without changing engineering results.
- 🗣️ **Advisory controls:** most safeguards, such as "ask before acting", are written rules that rely on Claude checking itself.
- 📉 **No outcome data:** nothing records delivery time, rework or human effort, so nobody can tell which components help.
