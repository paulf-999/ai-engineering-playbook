<!-- version: 1.2.6 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-10 -->
# 📋 Templates Directory

Centralized templates for skills and other Claude configuration artifacts. `make install` copies this directory to `_templates/` in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset).

## Directory Structure

```text
_templates/
├── skills/                  # Skill-related templates
│   ├── SKILL.md.template
│   └── skill.contract.yaml.template
├── AGENT.md.template        # Starting point for a new agent
├── rule.md.template         # Starting point for a new rule
├── rules/                   # Lean rule shapes, chosen by bullet count
│   ├── short_rule.md.template
│   └── sectioned_rule.md.template
├── TODO.md.template         # Starting point for a project TODO list
├── utils/
│   ├── shell_utils.sh           # Shared shell helpers: log colours and common variables
│   └── template_bash_script.sh  # Starting point for a new bash script
└── README.md                # This file
```

## Templates

### Skills

**`skills/SKILL.md.template`**

- Standard skill documentation template: frontmatter, metadata header and 5 sections (Instructions for Claude, Purpose, Example Usage, Best For, References)
- Used by: `_rules_on_demand/claude_config/authoring_guidelines.md`

**`skills/skill.contract.yaml.template`**

- Contract definition for skills (name, version, triggers, requirements)
- Enforces contract-first design pattern
- Used by: `_rules_on_demand/claude_config/authoring_guidelines.md`, filled in before `SKILL.md`

### Agents, rules and TODOs

**`AGENT.md.template`**

- Starting point for a new agent at `agents/<group>/<name>/AGENT.md`: frontmatter, metadata header and the standard sections
- Keeps its uppercase name because it mirrors the `AGENT.md` file it produces
- Used by: `_rules_on_demand/claude_config/authoring_guidelines.md`

**`rule.md.template`**

- Decision tree for a new rule: picks the short or sectioned shape below by bullet count
- Ends with a quality checklist that applies to both shapes
- Used by: `_rules_on_demand/claude_config/authoring_guidelines.md`

**`rules/short_rule.md.template`**

- Lean rule of 5 labelled bullets or fewer: metadata and usage header, H1, Purpose, bullets and optional `Read on demand` pointers

**`rules/sectioned_rule.md.template`**

- Lean rule of more than 5 labelled bullets: the same opening, then 2 to 4 emoji `##` sections of up to 5 bullets each

**`TODO.md.template`**

- Table layout for a project's `TODO.md`, with pending and completed items
- Keeps its uppercase name because it mirrors the `TODO.md` file it produces

### Scripts

**`utils/template_bash_script.sh`**

- Starting point for a new bash script: shebang, safety flags, `shell_utils.sh` source, section headers, trap and logging

**`utils/shell_utils.sh`**

- Shared shell helpers the script template sources: log colours, `log_message`, `print_section_header` and `handle_interruption`
- Copy it into the repo beside your scripts, since the template sources it from the script's own folder
- Used by: `rules/_path_scoped_rules/style_guides/bash.md`, when the repo has no script template of its own

## Usage

Copy the template you need next to the file you're creating, fill it in, and follow `_rules_on_demand/claude_config/authoring_guidelines.md`, in your Claude config directory.

## Maintenance

- **Sync with global:** After updating templates here, run `make install` to copy them to your Claude config directory
- **Keep in sync:** The playbook repo is the source of truth. Updates to the installed `_templates/` should be backported here.
