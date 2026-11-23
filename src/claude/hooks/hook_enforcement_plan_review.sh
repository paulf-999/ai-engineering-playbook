#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: PreToolUse hook on ExitPlanMode that blocks a long plan until a cold reviewer scores it 10/10, for two rounds
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code reads its stdout, stderr and exit code, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# exit code 2 tells Claude Code to block the tool call and show stderr to Claude
BLOCK=2
# a plan with fewer non-blank lines than this is a small task, so it isn't reviewed
MIN_PLAN_LINES=15
# the same headings the plan sections hook checks; a plan without them is that hook's to block
INTENT_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*intent\b'
SPEC_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*spec\b'
# after this many blocks in a session, a plan passes with the findings, so review can't loop forever
MAX_BLOCKS=2
# seconds to wait for the reviewer before letting the plan through unreviewed
REVIEW_TIMEOUT=240
# the writing style rule, at the same path relative to this hook in the repo and in an install
STYLE_FILE="$(dirname "${BASH_SOURCE[0]}")/../rules/always_on/02_preferences/claude_writing_style.md"
# a verdict whose four scores are numbers, pulled from the reviewer's reply even when it's wrapped in a code fence
VERDICT_FILTER='.result | capture("(?s)(?<json>\\{.*\\})").json | fromjson
    | select([.scores.intent, .scores.spec, .scores.plan, .scores.writing_style] | all(type == "number"))'

#=======================================================================
# Functions
#=======================================================================

# Print the reviewer prompt for the plan on stdin: the rubric, the writing style rule, then the plan
review_prompt() {
    cat << 'EOF'
You review a software change plan cold. Score each theme from 0 to 10, where 10 means nothing to fix.

- intent: an Intent section with a Why bullet and a Success bullet, where Success is specific enough to check.
- spec: a Spec section with Change, Files changed, Why and Out of scope bullets, naming the actual files.
- plan: a Plan section of numbered steps, each with the check that proves it's done.
- writing_style: the plan follows every bullet of the writing style rule below.

Each section opens with a fixed first line the team's workflow requires, such as "Why this change is needed, and how
we'll know it worked.", so don't mark those lines down. Judge the plan text alone.

Reply with only this JSON, giving one short finding per point lost:
{"scores": {"intent": 0, "spec": 0, "plan": 0, "writing_style": 0}, "findings": ["..."]}

Writing style rule:
EOF
    cat "${STYLE_FILE}" 2> /dev/null || echo "None is installed, so score writing_style 10."
    printf '\nThe plan:\n\n'
    cat
}

# Print stdout JSON that passes the plan with a message added to Claude's context, leaving the user's approval in place
allow_with_context() {
    jq -n --arg context "$1" '{hookSpecificOutput: {hookEventName: "PreToolUse", additionalContext: $context}}'
    exit 0
}

#=======================================================================
# Main script logic
#=======================================================================

# without jq the plan can't be read, and the plan sections hook already blocks for that
command -v jq > /dev/null || exit 0

INPUT="$(cat)"
PLAN="$(jq -r '.tool_input.plan // empty' <<< "${INPUT}" 2> /dev/null || true)"
[[ -n "${PLAN}" ]] || exit 0
[[ "$(grep -c '[^[:space:]]' <<< "${PLAN}")" -ge "${MIN_PLAN_LINES}" ]] || exit 0
grep -Eiq "${INTENT_HEADING}" <<< "${PLAN}" && grep -Eiq "${SPEC_HEADING}" <<< "${PLAN}" || exit 0

# --safe-mode loads no config or hooks, so the reviewer is unprimed and can't trigger this hook again
# it runs from the temp folder, so the repo's git status doesn't reach the reviewer, and with no tools, so it reads only
# the prompt; perl's alarm stands in for timeout, which macOS doesn't ship; any failure lets the plan through unreviewed
RAW="$(review_prompt <<< "${PLAN}" | (cd "${TMPDIR:-/tmp}" && perl -e 'alarm shift; exec @ARGV' "${REVIEW_TIMEOUT}" \
    claude -p --safe-mode --model sonnet --tools "" --no-session-persistence --output-format json) 2> /dev/null)" \
    || allow_with_context "This plan wasn't reviewed: the reviewer failed or timed out. Tell the user."
# -e makes jq fail when the filter finds no verdict
VERDICT="$(jq -ce "${VERDICT_FILTER}" <<< "${RAW}" 2> /dev/null)" \
    || allow_with_context "This plan wasn't reviewed: the reviewer gave no scores. Tell the user."

jq -e '[.scores[]] | all(. == 10)' <<< "${VERDICT}" > /dev/null && exit 0

FINDINGS="$(jq -r '"Plan review scores: " + (.scores | to_entries | map("\(.key) \(.value)/10") | join(", ")) + ".",
    (.findings // [] | .[] | "- \(.)")' <<< "${VERDICT}")"
# the session ID names the round counter, kept to safe filename characters
SESSION="$(jq -r '.session_id // "unknown"' <<< "${INPUT}" | tr -cd '[:alnum:]_-')"
ROUNDS_FILE="${TMPDIR:-/tmp}/claude_plan_review_${SESSION}"
ROUNDS="$(cat "${ROUNDS_FILE}" 2> /dev/null || echo 0)"

if [[ "${ROUNDS}" -ge "${MAX_BLOCKS}" ]]; then
    allow_with_context "${FINDINGS}
The plan review still has these findings after ${MAX_BLOCKS} rounds. Show them to the user with the plan."
fi
echo $((ROUNDS + 1)) > "${ROUNDS_FILE}"
echo "${FINDINGS}
Fix these findings, then submit the plan again." >&2
exit "${BLOCK}"
