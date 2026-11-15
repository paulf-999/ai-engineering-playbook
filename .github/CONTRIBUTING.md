# 🤝 Contributing

**Purpose:** the branch, commit and PR conventions every contribution to this repo follows.

Before your first commit, activate a virtualenv (see the [virtualenv setup guide](../docs/guides/virtualenv_setup.md)) and run `make deps`, which installs the pre-commit hooks these conventions rely on.

## 🌱 Branching

- 📖 **Strategy:** follow the [Git branching strategy](../docs/guides/git_branching_strategy.md).
- 🛂 **Checked:** a pre-commit hook rejects branch names that break it.

## 📝 Commits

- 📐 **Format:** write `type(scope): imperative description`, following [Conventional Commits](https://www.conventionalcommits.org/).
  - **Type:** the kind of change, such as `feat`, `fix` or `docs`.
  - **Scope:** the area of the repo affected, such as `makefile` or `ci`.
- 🛂 **Checked:** a commit-message hook rejects any message that doesn't match the format.

Two valid messages:

- `feat(pre-commit): add ruff`
- `fix(makefile): run pytest from make test`

## 🔀 Pull Requests

- 📄 **Template:** fill in the [PR template](pull_request_template.md).
- 🔤 **Title:** use the commit format, because a squash merge makes the title the commit message on `main`.
- 📏 **Size:** keep each PR within the file limit CI checks, or use a [`release/` branch](../docs/guides/git_branching_strategy.md#-exceptions-for-large-changes--use-the-release-prefix) for one bulk change.
- ⚖️ **Evaluation criteria:** when the PR changes an always-on or enforcing file, such as `src/claude/CLAUDE.md`, a rule in `rules/always/` or a hook, have a fresh-context reviewer agent fill the template's Evaluation criteria section, which CI checks is answered.
- 💥 **Breaking change:** tick it if it applies, and describe the rollout impact.

### ✅ Before raising a PR

- 🪝 **Pre-commit hooks:** fix what they flag, rather than skipping them with `--no-verify`.
- 🧪 **Done:** meet [Done means](../CLAUDE.md) in `CLAUDE.md` before raising the PR.
- 📊 **Scores:** leave the [quality audit](../maintenance/quality/quality_audit.md) as it is, since each regular review re-scores every test and rule changed since the last one, in one PR.

## 🚀 Releases

A release tags `main` once merged PRs are worth installing together.

- 🔢 **Version:** tag `vMAJOR.MINOR.PATCH`, per [Semantic Versioning](https://semver.org/). Below `1.0.0`, bump MINOR for features or breaking changes and PATCH for fixes only.
- 📝 **Notes:** open with one line on what the release delivers, then up to 5 emoji bullets, with file links pinned to the tag.
- 🛠️ **Publish:** run `gh release create vX.Y.Z --target main --title vX.Y.Z --notes-file <notes.md>`.
- 🔀 **Not a `release/` branch:** that prefix is for one bulk change over the PR file limit, not for versions.

## 🏷️ File naming

- 🔡 **Rule:** follow the [naming standards](../src/claude/rules/always/standards/naming_standards.md), which the Claude config also loads in every session.
- 📌 **Exceptions:** conventional names such as `README.md`, `CLAUDE.md` and `Makefile`.

## 🛠️ Authoring rules, skills and agents

How to build a new rule, skill or agent for `src/claude/`, once the installed [guiding principles](../src/claude/rules/on_demand/claude_config/guiding_principles.md) say it's worth adding.

### ✅ Every file

- 🔁 **No duplicate:** search the rules, skills and agents for one that already covers the need, and extend it rather than adding another.
- 📋 **Start from a template:** copy the matching file from [`src/claude/_templates/`](../src/claude/_templates/README.md), rather than starting from a blank page.
- 🎯 **Opening:** an H1 with an emoji, then a one-line **Purpose:** saying what the file does.
- 1️⃣ **One concept:** keep each file to one concept, and split anything broader into a parent and 2 or more `<parent>/_<aspect>.md` children.
- 🔑 **Bullets:** open each with a bold keyword and keep it to one sentence.

### 🌍 Portable paths

Hooks, scripts and tests for the config must work on any machine:

- 🚫 **No hard-coded paths:** never hard-code a home folder, username or `~/.claude` path, since the config directory varies between machines.
- 🐍 **Python:** read the config directory from `CLAUDE_CONFIG_DIR`, using `~/.claude` only as the fallback when it's unset.
- 🐚 **Shell:** resolve paths from the script's own location, using `"$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"`.
- 🛡️ **Guard clauses too:** compare against the resolved directory, never a substring such as `*".claude/"*`.
- 📅 **Why:** hard-coded paths pass on the machine that wrote them and fail silently elsewhere, as the old config's hooks and tests did.

### 📝 Rules

- 🚪 **Pick the tier:** `always/` only for a rule every task needs while the always-on budget holds, `path_scoped/` with a `paths:` setting for a rule tied to one kind of file, and `on_demand/` for everything else, and whenever you're unsure.
- 👉 **Pointers:** reach an on-demand file with a bullet in a `## 📚 Read on demand` section at the end of the file, naming its path, in your Claude config directory, and when to read it, or name it in a hook's block message.
- 🆕 **New-file gap:** a path-scoped rule loads only once a matching file is open, so point to it on demand too, for the first file of its kind.
- 🧩 **Children:** name each child in its parent, and keep links to other files in those pointer lines rather than a Related section.
- 🧪 **Test the pointer:** run a lean session on a matching task, and check Claude reads the file before acting.
- 🧾 **Usage lines:** give each entry-point rule `applies_to` and `miss_cost` lines straight after its header, since its folder already sets how it loads, and its children inherit them.
- 🛡️ **Before merging:** a rule backed by a hook, test or CI check gets a test in `tests/`, and an always-on rule has a fresh-context reviewer fill the PR template's Evaluation criteria section.
- 🔁 **Trial:** remove it at the next regular review if the session transcripts show it hasn't paid its way.

### 🛠️ Skills

- 📄 **SKILL.md:** about 60 lines from `_templates/skills/SKILL.md.template`, leaving longer detail to `reference/`.
- 📜 **Contract:** a `skill.contract.yaml` from its template, written before `SKILL.md`, since it sets the scope.
- 📚 **Folders:** `reference/` for the files Claude reads while running the skill, starting with `_implementation.md`, and `tests/` for `evals.yaml` and a plain-language `README.md`, with nothing else apart from one script at the root if it runs code.
- 🏷️ **Name:** `<domain>-<action>`, a domain then an imperative verb, such as `git-create-pr`, matching the folder name, per the [Agent Skills spec](https://agentskills.io/specification).
- 🚧 **Not for:** list in the contract's `not_for` what the skill doesn't do, since that boundary matters most.
- 🗣️ **Description:** use the phrases people type to ask for it, and keep it short, since every description loads in every session.
- ✋ **Confirm first:** set `confirmation_required: true` for anything irreversible or visible to others, such as a push.
- 🔐 **Safety:** read secrets from the environment, validate input before it reaches a shell or API, and hard-code no paths.

### 🤖 Agents

- 👥 **When:** build one only when the work needs a separate context or an independent view, such as a blind review, and otherwise use a skill for a procedure or a rule for guidance.
- 🏷️ **Name and place:** `agents/<group>/<name>/AGENT.md`, with a `<domain>-<purpose>` name, such as `technical-writer`, hyphenated to match skills, though the [Claude Code subagent docs](https://code.claude.com/docs/en/sub-agents) allow any name without a `:`.
- 📄 **Template:** start from `_templates/AGENT.md.template`, and keep the result to about 40 to 60 lines.
- 🗣️ **Description:** say when Claude should delegate to it, since Claude Code decides from the description alone, and keep it short, since it loads in every session.
- 🔐 **Tools:** list only what the job needs, since leaving `tools:` out grants every tool, and set `isolation: worktree` only for an agent that changes files.
- 🚧 **Constraints:** say what it doesn't do, and why.

### 🏁 Before merging a skill or agent

- 🧪 **Evals:** add evals that cover its main triggers and one case where it shouldn't fire.
- 📋 **Evaluation criteria:** answer the PR template's Evaluation criteria section.
- 🏅 **Review:** have a fresh-context reviewer score it against a rubric for its type, modelled on the Rules rubric in [`quality_rubrics.md`](../maintenance/quality/quality_rubrics.md#-rules).
