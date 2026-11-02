<!-- version: 1.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🛠️ Current architecture: Proposed changes

For anyone shaping the target architecture: proposed changes to two core rule files, and lessons for the target design.

- **Part of:** [Current architecture](../current_architecture.md).
- 📌 **Snapshot:** everything here describes [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook) at commit `915685f`, dated 2026-10-31.
- 🔄 **SDLC:** software development lifecycle, from Anthropic's [AI-native SDLC course](../reference_material/anthropic_ai_native_sdlc.md).
- 📊 **DORA:** DevOps Research and Assessment, whose [AI Capabilities Model](../reference_material/dora_ai_capabilities.md) informs the curated-context proposal.

## 📝 Proposed changes

- 🎯 **Why these two:** they are the always-on files that set Claude's guiding principles and its naming and writing standards.
- 🧾 **Format:** keep both files' current shape, a principles table and a short index, and change only their content.

| File | Keep | Proposed change |
|---|---|---|
| 🧭 [`guiding_principles.md`](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/guiding_principles.md) | • **Principles:** load detail on demand, keep changes reversible, grow in stages, put essentials first, and prefer live sources.<br>• **Format:** its four-column table. | See [Changes to `guiding_principles.md`](#-changes-to-guiding_principlesmd) below. |
| 📐 [`claude_usage_standards.md`](https://github.com/paulf-999/claude_ai_playbook/blob/915685f/src/claude/rules/01_essentials/claude_usage_standards.md) | • **Role:** a short index of directory, naming and writing standards.<br>• **Loading:** children load on their own. | See [Changes to `claude_usage_standards.md`](#-changes-to-claude_usage_standardsmd) below. |

### 🧭 Changes to `guiding_principles.md`

- 🔗 **Merge overlaps:** combine the three rows on real need, token cost and automation payback into one principle, "Every component earns its cost".
- 🎯 **Curated context:** add DORA's finding that irrelevant context degrades answers to that merged principle.
- 🛡️ **Enforce what must hold:** add the SDLC split between advisory guidance and enforced controls.
- 📏 **Measure outcomes:** give each new component, and each one kept after the [issue #7](https://github.com/paulf-999/ai-engineering-playbook/issues/7) review, a leading (early) and a lagging (later) indicator.
- 🧑 **Human accountability:** state that humans own every judgement call.

### 📐 Changes to `claude_usage_standards.md`

- 📁 **Change files:** for multi-file or architectural tasks, write a `spec.md` (intent and acceptance criteria) and a `plan.md` in `.claude/changes/<date>_<topic>/`, committed in the repo being changed.
- 🌐 **Rule location:** the standard lives in the global config, while each change's files live with the change and its PR.
- 🧹 **Current state only:** remove the "Why this file exists" history note, which breaks the writing style's own rule.

## 🎓 Lessons for the target architecture

- 🌱 **Start minimal:** begin with `CLAUDE.md`, one test command and CI, then add a component only once a real problem recurs.
- 🔪 **Apply the halving test:** ask whether removing half the components would make outcomes materially worse.
- 💪 **Keep the strengths:** carry over everything in [What works well](02_what_works_well.md) unchanged.
