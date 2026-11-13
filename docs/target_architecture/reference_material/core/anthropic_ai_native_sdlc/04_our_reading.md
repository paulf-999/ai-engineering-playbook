<!-- version: 1.1.4 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-13 -->
# 🔍 AI-native SDLC course: Our reading

**Purpose:** what Anthropic's SDLC course means for the design of this repo's Claude configuration.

This page is part of the [summary of Anthropic's SDLC course](../anthropic_ai_native_sdlc.md), and gives this repo's view rather than the course's.

## 🔑 Key points

These ideas carry over:

- 🦴 **Core sequence:** specify, plan, then check the work against versioned files, which needs none of the admin-run features that some plays assume.
- ⚖️ **Advice versus enforcement:** the course calls skills advisory, and this repo treats `CLAUDE.md` the same way, while hooks and required CI checks enforce.
  - **Use here:** the [review of the old configuration](../../../current_architecture.md#-where-complexity-outran-evidence) applies this split to its safeguards.
- 📏 **Measurement:** each play's early signal and later result are ready candidates for checking whether a change helped.
  - **Use here:** the [target architecture's workflow](../../../target_architecture.md#-workflow) names the signal each regular review reads for every play it adopts.
