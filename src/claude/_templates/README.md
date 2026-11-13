<!-- version: 1.2.12 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-13 -->
# 📋 Templates Directory

Centralized templates for skills and other Claude configuration artifacts. `make install` installs it to `_templates/` in your Claude config directory, as the [config README](../README.md) describes.

- 🗓️ **Planned:** the skill and agent templates are kept for the skills and agents coming soon, since none exist yet.

## Directory Structure

```text
_templates/
├── skills/                  # Skill-related templates
│   ├── SKILL.md.template
│   └── skill.contract.yaml.template
├── AGENT.md.template        # Starting point for a new agent
├── rule.md.template         # Starting point for a new rule
├── TODO.md.template         # Starting point for your TODO list
├── utils/
│   ├── shell_utils.sh           # Shared shell helpers: log colours and common variables
│   └── template_bash_script.sh  # Starting point for a new bash script
└── README.md                # This file
```

## Templates

### Skills (planned)

**`skills/SKILL.md.template`**

- Standard skill documentation template: frontmatter, metadata header and 5 sections (Instructions for Claude, Purpose, Example Usage, Best For, References)
- Used by: `on_demand/claude_config/authoring_guidelines.md`

**`skills/skill.contract.yaml.template`**

- Contract definition for skills (name, version, triggers, requirements)
- Enforces contract-first design pattern
- Used by: `on_demand/claude_config/authoring_guidelines.md`, filled in before `SKILL.md`

### Agents, rules and TODOs

**`AGENT.md.template`** (planned)

- Starting point for a new agent at `agents/<group>/<name>/AGENT.md`: frontmatter, metadata header and the standard sections
- Keeps its uppercase name because it mirrors the `AGENT.md` file it produces
- Used by: `on_demand/claude_config/authoring_guidelines.md`

**`rule.md.template`**

- Starting point for a new rule: metadata and usage header, H1, Purpose, emoji `##` sections and `Read on demand` pointers
- Its closing comments say when to drop the sections, when to split, and the checks the tests don't cover
- Used by: `on_demand/claude_config/authoring_guidelines.md`

**`TODO.md.template`**

- Table layout for the `TODO.md` in your Claude config directory, with pending and completed items
- Keeps its uppercase name because it mirrors the `TODO.md` file it produces

### Scripts

**`utils/template_bash_script.sh`**

- Starting point for a new bash script: shebang, safety flags, `shell_utils.sh` source, section headers, trap and logging

**`utils/shell_utils.sh`**

- Shared shell helpers the script template sources: log colours, `log_message`, `print_section_header` and `handle_interruption`
- Copy it into the repo beside your scripts, since the template sources it from the script's own folder
- Used by: `rules/path_scoped/style_guides/bash.md`, when the repo has no script template of its own

## Usage

Copy the template you need next to the file you're creating, fill it in, and follow `on_demand/claude_config/authoring_guidelines.md`, in your Claude config directory.

## Maintenance

- **Sync with global:** After updating templates here, run `make install` to copy them to your Claude config directory
