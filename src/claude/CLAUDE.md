<!-- version: 1.2.0 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-04 -->
# 🧠 Global Claude configuration

<!-- Template for ~/.claude/CLAUDE.md, which Claude loads in every session in every repo, so keep it lean. Put project facts in each repo's own CLAUDE.md, and add a line here only when Claude repeatedly gets something wrong across repos. -->

## 🧭 Behavioural Guidelines

*Adapted from [Andrej Karpathy's guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), which target the coding mistakes LLMs make most often. They favour care over speed, so use judgement on trivial tasks.*

### 1️⃣ Think Before Coding

**State assumptions. Surface confusion. Show tradeoffs.**

- 🤔 **Assumptions:** state what you're assuming before you start.
- 🔀 **Ambiguity:** when a request has more than one reading, lay out the readings and ask which is meant.
- 🛤️ **Simpler options:** say when an easier route exists, and push back when it's warranted.

### 2️⃣ Simplicity First

**Write the minimum code that solves the problem.**

- 🎯 **Scope:** build only what was asked for.
- 🧱 **Abstractions:** add one only when a second use appears.
- 🎛️ **Options:** add settings or flexibility only when requested.
- 🚧 **Errors:** handle the cases that can actually happen.
- 📏 **Size:** if 50 lines would do the job of 200, rewrite it, as a senior engineer would.

### 3️⃣ Surgical Changes

**Change only what the request needs, and clean up only your own mess.**

- 🏘️ **Neighbouring code:** keep surrounding code, comments and formatting as they are, even where you'd choose differently.
- 💀 **Dead code:** mention unrelated dead code rather than deleting it.
- 🧹 **Your leftovers:** remove the imports, variables and functions your own change left unused.
- 🧵 **Traceable:** every changed line should trace back to the request.

### 4️⃣ Goal-Driven Execution

**Define success criteria, then loop until they're verified.**

Restate each task as something you can check:

| Task | Becomes |
|---|---|
| 🛡️ Add validation | Write tests for bad inputs, then make them pass |
| 🐛 Fix a bug | Write a test that reproduces it, then make it pass |
| ♻️ Refactor | Confirm the tests pass both before and after |

For multi-step work, give a short plan with a check for each step, since clear checks let you work without constant clarification:

```text
1. <step> → verify: <check>
2. <step> → verify: <check>
```

<!-- Working if: diffs carry fewer unneeded changes, fewer rewrites come from overcomplication, and clarifying questions come before the work rather than after mistakes. -->

## ⚙️ Changing Claude's config

- **Read on demand:** `_rules_lazy_load/guiding_principles.md`, in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset), before proposing or adding a rule, skill, hook, import, setting or memory note to Claude's config.

<!-- Imports (optional): @-import files Claude needs every session; each import loads in full at startup, so add sparingly -->
