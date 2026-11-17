# 👥 Personas

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how to get blind reviews of the repo from three likely users, and rank the feedback they share, as part of the [quality rubrics](../quality_rubrics.md).

The [repo rubric](_repo.md) scores how the repo is built, while this review asks whether the people it's for would use it.

## 🧑‍💼 Readers

Each reader gets their role and goal, then the same task, and the manager gets one extra question. The goal gives the review a job to judge the repo against, and the skill levels keep readers from tolerating more than the team would:

| Reader | Role and goal |
|---|---|
| 🛠️ **Data engineer** | You are a data engineer who writes Python, SQL and simple bash commands, and has tried Claude Code but isn't an expert. You want help building dbt models and Airflow DAGs. |
| 📊 **Data analyst** | You are a data analyst who writes SQL, builds Looker and Omni dashboards and works with the business. You can write basic dbt models and follow your team's steps to put one into production, but you aren't technical beyond that and are new to Claude Code. You want help turning business requests into SQL and dbt models. |
| 🧭 **Engineering manager** | You are a manager of a data engineering and analytics team, who knows Claude Code, data engineering and business needs at a high level but doesn't work in the detail. You're deciding whether to roll it out to your team. |

## 🕵️ Reader brief

Each reader is a separate `claude -p --safe-mode` process run from a fresh clone, so no CLAUDE.md, rules, hooks or memory load. An in-session subagent would inherit them. The brief describes nothing about the repo, since a primed brief goes easier on the work:

```text
<role and goal> A colleague pointed you at your team's repo in <clone path>. You'd install and
use it, not maintain it. Explore it as you naturally would, starting where you'd start, and say
where you'd stop, get stuck or give up. Skip material meant for its maintainers, unless it gets
in your way.
Report what it is and who it's for, what's valuable, what's confusing or off-putting, how complex
it looks against what it delivers, and what you'd change, citing files. No word limit.
```

The task asks where each reader would stop rather than for a full review, since a model reads everything whatever its role, and the stopping point shows what the role's skill level can manage.

The manager's brief ends with "Also answer: would you adopt it for your team, and what would convince you?"

## ▶️ How to run

Run this from the repo root at a terminal, and it saves each review verbatim to `OUT`:

```bash
OUT="$(mktemp -d)/persona_reviews"; WORK="$(mktemp -d)"; CLONE="${WORK}/ai-engineering-playbook"
mkdir -p "${OUT}"
# full clone, not --depth 1, so readers can see the history and tags
git clone --quiet "file://${PWD}" "${CLONE}"
TASK="A colleague pointed you at your team's repo in ${CLONE}. You'd install and use it, not maintain it. \
Explore it as you naturally would, starting where you'd start, and say where you'd stop, get stuck or give up. \
Skip material meant for its maintainers, unless it gets in your way. Report what it is and who it's for, what's valuable, what's confusing or \
off-putting, how complex it looks against what it delivers, and what you'd change, citing files. No word limit."
DE="You are a data engineer who writes Python, SQL and simple bash commands, and has tried Claude Code but isn't an expert. You want help building dbt models and Airflow DAGs."
DA="You are a data analyst who writes SQL, builds Looker and Omni dashboards and works with the business. You can write basic dbt models and follow your team's steps to put one into production, but you aren't technical beyond that and are new to Claude Code. You want help turning business requests into SQL and dbt models."
EM="You are a manager of a data engineering and analytics team, who knows Claude Code, data engineering and business needs at a high level but doesn't work in the detail. You're deciding whether to roll it out to your team."
review() {
    # the prompt goes on stdin, since --allowedTools is variadic and would swallow it
    (cd "${WORK}" && echo "${2}" | claude -p --safe-mode --model sonnet --permission-mode default --output-format json \
        --allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(wc:*),Bash(find:*)") | jq -r '.result' > "${OUT}/${1}.md"
}
review data_engineer "${DE} ${TASK}" &
review data_analyst "${DA} ${TASK}" &
review engineering_manager "${EM} ${TASK} Also answer: would you adopt it for your team, and what would convince you?" &
wait; rm -rf "${WORK}"; echo "Reviews are in ${OUT}"
```

- 🤖 **A script, not agents:** an in-session agent loads CLAUDE.md, rules and the session's context, which breaks blindness, and one in `src/claude/agents/` would install for every user.
- 🔒 **Read-only tools:** `-p` can't answer permission prompts, and a reader never needs to write.
- 🚦 **Default mode:** `--permission-mode default` stops a configured plan mode from writing plan files.
- ⚡ **Quick rounds:** readers run in parallel on Sonnet, so a round takes minutes, not a quarter of an hour. Fix what a round finds in one pass, and stop after 2 rounds to ship the fixes rather than polish towards a perfect verdict.
- 🧪 **Blindness probe:** to check nothing leaks, ask one session to quote any CLAUDE.md, rules or memory it was given, and expect none.

## 🎯 Shared feedback

Record the shared feedback in the [audit's persona review](../quality_audit.md#-persona-review) section, replacing the last run, with a table of each point two or more readers raised:

1. Rank the points by how many readers raised them, 3 before 2.
2. Break ties by impact on adoption: blocks use, then confuses, then polish.
3. Give each row its theme, who raised it, the impact, and a status: its issue or fix PR, or why it stays open.
4. Mark any fix that clashes with a [kept-by-choice](_repo.md#-how-to-score) decision, so it isn't argued again.
5. List the strengths all readers share, and the points only one reader raised, under the table.
6. Above the table, sum up whether the readers found the repo over-engineered and, if so, where, with who raised each area, its evidence and any kept-by-choice clash.

Turn the top rows into GitHub issues or fix PRs, as with the [checklists](_repo.md#-where-findings-go), with the evidence and suggested fix in each. The verbatim reviews stay out of the repo.
