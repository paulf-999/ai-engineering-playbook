# 📋 Templates Directory

Starting points for new rules, skills, agents and scripts. `make install` installs only the templates other rules point to, `TODO.md.template` and `utils/`; the rest stay here for authoring in this repo. Copy the template you need next to the file you're creating, then fill it in.

| Template | Starting point for |
|---|---|
| [`rule.md.template`](rule.md.template) | A new rule: H1, Purpose, sections and `Read on demand` pointers |
| [`skills/SKILL.md.template`](skills/SKILL.md.template) | A new skill's `SKILL.md`, kept for the skills coming soon |
| [`skills/skill.contract.yaml.template`](skills/skill.contract.yaml.template) | A skill's contract, filled in before its `SKILL.md` |
| [`AGENT.md.template`](AGENT.md.template) | A new agent, kept for the agents coming soon |
| [`TODO.md.template`](TODO.md.template) | The `TODO.md` in your Claude config directory |
| [`utils/template_bash_script.sh`](utils/template_bash_script.sh) | A new bash script, which sources `shell_utils.sh` from its own folder |
| [`utils/shell_utils.sh`](utils/shell_utils.sh) | The shell helpers that script uses, copied beside your scripts |

The `AGENT.md` and `TODO.md` templates keep uppercase names, since they mirror the files they produce.
