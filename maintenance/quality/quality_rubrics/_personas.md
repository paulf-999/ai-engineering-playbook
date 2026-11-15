# 👥 Personas

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how to get blind reviews of the repo from three likely users, and rank the feedback they share, as part of the [quality rubrics](../quality_rubrics.md).

The [repo rubric](_repo.md) scores how the repo is built, while this review asks whether the people it's for would use it.

## 🧑‍💼 Readers

Each reader gets their role and the same task, and the manager gets one extra question:

| Reader | Role line |
|---|---|
| 🛠️ **Data engineer** | You are a data engineer who uses Claude Code daily. |
| 📊 **Data analyst** | You are a data analyst who writes SQL and some Python and is new to Claude Code. |
| 🧭 **Engineering manager** | You are a manager of a data engineering and analytics team. |

## 🕵️ Reader brief

Each reader is a separate `claude -p --safe-mode` process run from a fresh clone, so no CLAUDE.md, rules, hooks or memory load. An in-session subagent would inherit them. The brief describes nothing about the repo, since a primed brief goes easier on the work:

```text
<role line> A colleague pointed you at the repo in <clone path>. Review it fully, as you would
before deciding whether to use it. Report what it is and who it's for, what's valuable, what's
confusing or off-putting, how complex it looks against what it delivers, and what you'd change,
citing files. No word limit.
```

The manager's brief ends with "Also answer: would you adopt it for your team, and what would convince you?"

## ▶️ How to run

Run this from the repo root at a terminal, and it saves each review verbatim to `OUT`:

```bash
OUT="$(mktemp -d)/persona_reviews"; WORK="$(mktemp -d)"; CLONE="${WORK}/ai-engineering-playbook"
mkdir -p "${OUT}"
# full clone, not --depth 1, so readers can see the history and tags
git clone --quiet "file://${PWD}" "${CLONE}"
TASK="A colleague pointed you at the repo in ${CLONE}. Review it fully, as you would before deciding whether to use it. \
Report what it is and who it's for, what's valuable, what's confusing or off-putting, how complex it looks against what \
it delivers, and what you'd change, citing files. No word limit."
review() {
    # the prompt goes on stdin, since --allowedTools is variadic and would swallow it
    (cd "${WORK}" && echo "${2}" | claude -p --safe-mode --permission-mode default --output-format json \
        --allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(wc:*),Bash(find:*)") | jq -r '.result' > "${OUT}/${1}.md"
}
review data_engineer "You are a data engineer who uses Claude Code daily. ${TASK}" &
review data_analyst "You are a data analyst who writes SQL and some Python and is new to Claude Code. ${TASK}" &
review engineering_manager "You are a manager of a data engineering and analytics team. ${TASK} \
Also answer: would you adopt it for your team, and what would convince you?" &
wait; rm -rf "${WORK}"; echo "Reviews are in ${OUT}"
```

- 🔒 **Read-only tools:** `-p` can't answer permission prompts, and a reader never needs to write.
- 🚦 **Default mode:** `--permission-mode default` stops a configured plan mode from writing plan files.
- 🧪 **Blindness probe:** to check nothing leaks, ask one session to quote any CLAUDE.md, rules or memory it was given, and expect none.

## 🎯 Shared feedback

Write `shared_feedback.md` beside the reviews, with a table of each point two or more readers raised:

1. Rank the points by how many readers raised them, 3 before 2.
2. Break ties by impact on adoption: blocks use, then confuses, then polish.
3. Give each row its theme, who raised it, the impact, the evidence as file paths, and a suggested fix.
4. Mark any fix that clashes with a [kept-by-choice](_repo.md#-how-to-score) decision, so it isn't argued again.
5. List the strengths all readers share, and the points only one reader raised, under the table.
6. Above the table, sum up whether the readers found the repo over-engineered and, if so, where, with who raised each area, its evidence and any kept-by-choice clash.

Turn the top rows into GitHub issues or fix PRs, as with the [checklists](_repo.md#-where-findings-go).
