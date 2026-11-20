# 📚 Reference Material

**Purpose:** the outside sources behind this repo's target architecture, and what the design uses each one for.

You don't need these to use the Claude Code instructions: they're the sources the design pages cite.

## 🥇 Core

The design is built on these, so each has a summary in this repo:

- 🔄 **[The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)** ([summary](core/anthropic_ai_native_sdlc.md)): lifecycle and workflow guidance, from Anthropic.
- 📊 **[DORA AI Capabilities Model report](https://dora.dev/ai/capabilities-model/report/)** ([summary](core/dora_ai_capabilities.md)): the seven capabilities and how to build them, from DORA.
- 🧑‍💼 **[Handover review](core/handover_review.md)**, sections 4 and 6: an outside reviewer's view of the [old Claude configuration](../README.md#️-the-old-setup), which sets the design's stance and priorities.
- 🧩 **[Agent Skills specification](https://agentskills.io/specification)** ([summary](core/agent_skills_spec.md)): the required format and naming of a skill.

## 🥈 Supporting

These back specific limits and naming rules, so recheck the live page before relying on them:

- 🧠 **[How Claude remembers your project](https://code.claude.com/docs/en/memory):** the always-on budget's 200-line basis, and that imports still load while path-scoped rules load only for matching files.
- 🛠️ **[Extend Claude with skills](https://code.claude.com/docs/en/skills):** where Claude Code's skills go beyond the standard.
- 🤖 **[Create custom subagents](https://code.claude.com/docs/en/sub-agents):** the agent template's fields, and listing `tools`, since leaving it out grants every tool.
- 🧪 **[Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents):** how to design the rule, trigger and behaviour evals that check the config does what it says.

## 🧭 Weighing them

- 🛠️ **Guidance and standards:** the SDLC course, the Claude Code docs, the handover review and the Agent Skills specification say what to do, but none shows that a practice works.
- 🔬 **Evidence:** DORA's surveys show correlation rather than cause, so weigh them as signals, not proof.
- 📝 **Citing:** record the page or section, and the version or access date, for every claim taken from a source.
