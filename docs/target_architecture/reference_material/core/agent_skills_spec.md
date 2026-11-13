# 🧩 Agent Skills: the open skill format

**Purpose:** what the Agent Skills standard, the open format for skill folders that Claude Code and other agents load, requires of a skill, and what it means for this repo's skills.

It's one of the summaries listed in this repo's [reference material](../README.md).

## 📋 Executive Summary

- 📐 **What it is:** an open standard for packaging a skill as a folder with a `SKILL.md` file, first developed by Anthropic.
- 💡 **Core idea:** agents load only each skill's name and description at startup, and read the rest when a task needs it.
- 🏷️ **Names:** a skill's `name` uses lowercase letters, digits and hyphens, and matches its folder.
- 🎯 **For this repo:** it's why skill names here use hyphens, and it caps what a `SKILL.md` should hold.

## 🔗 Source

- 🏠 **Overview:** [Agent Skills overview](https://agentskills.io/home), agentskills.io.
- 📄 **Specification:** [Specification](https://agentskills.io/specification), agentskills.io.
- 📅 **Version:** neither page shows a date or version, so cite the section heading and the capture date.
- 🗓️ **Captured:** 2026-11-09, after reading both pages in full.

## 📋 The pages say

The pages make these points, by section:

- 🏛️ **Origin:** the format "was originally developed by Anthropic, released as an open standard", and is open to contributions (overview, "Open development").
- 🏷️ **`name`:** 1–64 characters, only `a-z`, `0-9` and hyphens, with no leading, trailing or doubled hyphen, and it "must match the parent directory name" (spec, "`name` field").
- 🗣️ **`description`:** up to 1,024 characters, saying what the skill does and when to use it, with keywords that help agents spot the task (spec, "`description` field").
- 🧾 **Six fields:** `name` and `description` are required, and `license`, `compatibility`, `metadata` and `allowed-tools` are optional (spec, "Frontmatter").
- 🪜 **Progressive disclosure:** about 100 tokens of metadata load at startup, a body under 5,000 tokens loads on use, and other files load only when needed (spec, "Progressive disclosure").

### ➕ Also on the pages

- 📏 **Size:** keep `SKILL.md` under 500 lines, and keep file references one level deep (spec, "Progressive disclosure" and "File references").
- ✅ **Validation:** the `skills-ref validate` tool checks the frontmatter and naming rules (spec, "Validation").

## 🎯 What it means for this repo

This section is this repo's reading, not the pages':

- 🏷️ **Naming:** the [naming standards](../../../../src/claude/rules/always/standards/naming_standards.md) make skills an exception to snake_case because of the `name` rule.
- 🧾 **House fields:** this repo's [skill template](../../../../src/claude/_templates/skills/SKILL.md.template) adds `maturity` and `tags`, which aren't among the spec's six, so a strict validator would reject them.
- ⚠️ **Limit:** the standard covers skills only, and says nothing about agents.
