<!-- version: 1.0.1 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🤖 Claude Code docs: Create custom subagents

**Purpose:** what Anthropic's Claude Code docs say about defining subagents, the helper agents Claude hands tasks to, and what that means for this repo's agent template.

It's one of the summaries listed in this repo's [reference material](../README.md).

## 📋 Executive Summary

- 📘 **What it is:** the official page on subagents, each a Markdown file with YAML frontmatter that runs in its own context window.
- 💡 **Core idea:** Claude decides when to delegate from each subagent's `description` alone.
- 🏷️ **Names:** a `name` can be up to 256 characters and needn't match its file, so no open standard fixes the format the way the [Agent Skills standard](agent_skills_spec.md) does for skills.
- 🎯 **For this repo:** it's the source for the fields in the [agent template](../../../../src/claude/_templates/AGENT.md.template).

## 🔗 Source

- 📘 **Page:** [Create custom subagents](https://code.claude.com/docs/en/sub-agents), Claude Code docs, Anthropic.
- 📅 **Version:** the page shows no date or version, so cite the section heading and the capture date.
- 🗓️ **Captured:** 2026-11-09, after reading the configuration and delegation sections.

## 📋 The docs say

The page makes these points, by section:

- 🏷️ **`name`:** a "unique identifier of at most 256 characters, such as `code-reviewer`", with no `:`, which plugins reserve, and "the filename doesn't have to match" ("Frontmatter reference").
- 🗣️ **`description`:** Claude delegates based on it, and "use proactively" in it encourages delegation ("Understand automatic delegation").
- 📏 **Description budget:** Claude Code warns at startup when all custom subagents' descriptions together pass 15,000 tokens (same section).
- 🔧 **`tools`:** an allowlist, and leaving it out grants every tool a subagent can use ("Frontmatter reference").
- 🗂️ **Scopes:** when two subagents share a name, the higher-priority location wins, in the order managed settings, `--agents` flag, project, user, then plugin ("Choose the subagent scope").

### ➕ Also on the page

- 🙈 **Unknown fields:** fields Claude Code doesn't recognise are ignored without an error ("Frontmatter reference").
- 🧩 **Plugin limits:** plugin subagents ignore `hooks`, `mcpServers` and `permissionMode` "for security reasons" (same section).

## 🎯 What it means for this repo

This section is this repo's reading, not the page's:

- 🏷️ **Naming:** this repo's hyphenated agent names follow the page's examples and match the skills, but the page doesn't require them.
- 🧾 **House fields:** the template's `maturity` field is safe, since unknown fields are ignored.
- 🔒 **Least privilege:** the template's advice to list `tools` follows from the default that grants every tool.
