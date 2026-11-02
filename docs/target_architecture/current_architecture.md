<!-- version: 2.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 🏛️ Current architecture

For anyone shaping the target architecture: what the current Claude configuration repo contains, what works well, and which lessons the next design must carry forward so complexity stays in proportion to evidence.

## 📋 Executive Summary

- **What it is:** [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook), a personal Claude Code configuration installed onto each machine with `make install`.
- **Strengths:** a safe installer, a real test suite and automated checks make it reproducible and portable.
- **Main risk:** 36 always-on rule files load about 30,000 tokens into every session, whatever the task.
- **Reference fit:** measured against Anthropic's [AI-native SDLC (software development lifecycle) course](reference_material/anthropic_ai_native_sdlc.md) and the [AI Capabilities Model by DORA (DevOps Research and Assessment)](reference_material/dora_ai_capabilities.md), it has a strong feedback loop but no intent-first step or outcome measures.
- **For the target:** keep the current format, and reshape the core rule files around those sources' findings.

## 📸 Snapshot

- **Read:** [Snapshot](current_architecture/01_snapshot.md), each component of the repo at commit `915685f`, its count, how it loads and what it's for.

## ✅ What works well

- **Read:** [What works well](current_architecture/02_what_works_well.md), the strengths the target architecture should keep.

## ⚠️ Where complexity outran evidence

- **Read:** [Where complexity outran evidence](current_architecture/03_complexity_without_evidence.md), where the repo grew heavier than the evidence justifies.

## 🔍 Alignment with the reference material

- **Read:** [Alignment with the reference material](current_architecture/04_reference_alignment.md), how far the repo follows the SDLC course and DORA findings.

## 🛠️ Proposed changes to the core rule files

- **Read:** [Proposed changes](current_architecture/05_proposed_changes.md), changes to two core rule files that are proposed but not yet adopted.

## 🧭 Lessons for the target architecture

- **Read:** [Lessons](current_architecture/05_proposed_changes.md), on the proposed changes page: start minimal, apply the halving test, and keep the strengths.
