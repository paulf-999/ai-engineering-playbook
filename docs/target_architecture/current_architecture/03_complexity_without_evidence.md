<!-- version: 1.0.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# ⚠️ Current architecture: Where complexity outran evidence

For anyone shaping the target architecture: where the repo grew heavier than the evidence justifies.

- **Part of:** [Current architecture](../current_architecture.md).
- **Snapshot:** everything here describes [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook) at commit `915685f`, dated 2026-10-31.

- **Always-on weight:** most tasks need only a fraction of the guidance that loads every session.
- **Per-turn overhead:** a prompt hook injects the response format and timing rules into every turn, including trivial ones.
- **Rules about rules:** authoring, scorecard and metadata standards add upkeep that doesn't change engineering outcomes directly.
- **Advisory controls:** most safeguards, including "ask before acting", are prose rules that rely on Claude checking itself.
- **No outcome data:** there's no record of delivery time, rework or human effort to show which components help.
