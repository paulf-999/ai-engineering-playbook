<!-- version: 1.0.1 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🛠️ Claude Code docs: Extend Claude with skills

**Purpose:** what Anthropic's Claude Code docs say about how skills are named, described and loaded, and where Claude Code goes beyond the Agent Skills standard.

It's one of the summaries listed in this repo's [reference material](../README.md).

## 📋 Executive Summary

- 📘 **What it is:** the official page on skills in Claude Code, the folders of instructions Claude loads when a task needs them.
- 💡 **Core idea:** Claude Code follows the [Agent Skills standard](agent_skills_spec.md) and adds fields of its own.
- 📦 **Portability:** a skill with only the standard's six fields loads in Claude Code, claude.ai and the Skills API alike.
- 🎯 **For this repo:** its extra frontmatter works in Claude Code but would block uploading a skill to claude.ai.

## 🔗 Source

- 📘 **Page:** [Extend Claude with skills](https://code.claude.com/docs/en/skills), Claude Code docs, Anthropic.
- 📅 **Version:** the page shows no date or version, so cite the section heading and the capture date.
- 🗓️ **Captured:** 2026-11-09, after reading the sections on configuring and naming skills.

## 📋 The docs say

The page makes these points, by section:

- 📐 **Standard:** Claude Code skills "follow the Agent Skills open standard", and extend it with features such as invocation control (introduction).
- 🏷️ **`name` is optional:** it sets the `/` command, and defaults to the folder name ("Frontmatter reference").
- 🗣️ **Description cap:** `description` and `when_to_use` together are cut off at 1,536 characters in the skill listing, so put the key use case first (same section).
- 🚫 **Unknown fields:** Claude Code ignores a field it doesn't recognise, but claude.ai uploads and the Skills API fail with a hard error on any field outside the standard's six ("Using skill frontmatter outside Claude Code").

### ➕ Also on the page

- ✋ **Manual only:** `disable-model-invocation: true` stops Claude running a skill on its own, which suits actions such as deploys ("Types of skill content").
- 🔤 **Refused names:** Claude Code refuses names with control characters, `<` or `>`, or odd spacing, and the skill then drops out of the `/` menu ("Characters a skill name can't hold").

## 🎯 What it means for this repo

This section is this repo's reading, not the page's:

- 🏷️ **Naming:** Claude Code itself accepts snake_case, so this repo's hyphenated names are for the standard and portability, not for making skills load.
- 🧾 **House fields:** the `maturity` and `tags` fields in this repo's [skill template](../../../../src/claude/_templates/skills/SKILL.md.template) are fine locally, but would have to go before a skill is uploaded to claude.ai.
