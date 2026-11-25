#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: PreToolUse hook on ExitPlanMode that blocks a long plan until a cold reviewer scores it 10/10, for two rounds
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code reads its stdout, stderr and exit code, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# a plan with fewer non-blank lines than this is a small task, so it isn't reviewed
MIN_PLAN_LINES=15
# the same headings the plan sections hook checks; a plan without them is that hook's to block
INTENT_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*intent\b'
SPEC_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*spec\b'
# after this many blocks, a plan passes with the findings, so review can't loop forever
MAX_BLOCKS=2
# seconds to wait for the reviewer before letting the plan through unreviewed
REVIEW_TIMEOUT=60
# the writing style rule, at the same path relative to this hook in the repo and in an install
STYLE_FILE="$(dirname "${BASH_SOURCE[0]}")/../../rules/always_on/02_preferences/claude_writing_style.md"
# a verdict whose five scores are numbers, pulled from the reviewer's reply even when it's wrapped in a code fence
# it keeps only those scores, since the reviewer sometimes puts its findings inside them
VERDICT_FILTER='.result | capture("(?s)(?<json>\\{.*\\})").json | fromjson
    | select([.scores.intent, .scores.spec, .scores.plan, .scores.writing_style, .scores.decisions] | all(type == "number"))
    | .findings = (.findings // .scores.findings)
    | .scores |= {intent, spec, plan, writing_style, decisions}'

#=======================================================================
# Functions
#=======================================================================

# Print the reviewer prompt for the plan on stdin: the rubric, the writing style rule, then the plan
review_prompt() {
    cat << 'EOF'
You review a software change plan cold. Score each theme from 0 to 10, where 10 means nothing to fix.

- intent: an Intent section with all six of these bullets: Problem, Proposed outcome, Success, Affected users and
  systems, Constraints and Open questions. Check for each by name, as a missing one loses 2 points, even when it would
  only say "none". Success is specific enough to check, and "none" is a fine answer for any other bullet.
- spec: a Spec section with Change, Files changed, Why and Out of scope bullets, naming the actual files.
- plan: a Plan section of numbered steps, each with the check that proves it's done. The only sections are an Executive
  summary, Intent, Spec and Plan, in that order, so any other section loses points.
- writing_style: the plan follows every bullet of the writing style rule below.
- decisions: the Executive summary gives the outcome, the decisions agreed with the user and the assumptions, where "none"
  is a fine answer for decisions or assumptions. Every material choice in the plan is listed under its decisions agreed. A
  choice is material if it changes the outcome, scope, files or published wording, or is hard to undo. A choice isn't
  material if it's a minor detail of how the work is done, so it can be an assumption or go unlisted. Flag only a choice
  the plan text makes, quoting it, and never one it leaves unsaid. Detail that carries out the stated outcome or an agreed
  decision, and an Out of scope line that only leaves out what the outcome doesn't cover, aren't separate choices. You
  can't see the user's conversation, so take the listed decisions as agreed.

Judge the plan text alone.

Reply with only this JSON, giving one short finding per point lost, each opening with its theme's name and a colon:
{"scores": {"intent": 0, "spec": 0, "plan": 0, "writing_style": 0, "decisions": 0}, "findings": ["..."]}

Writing style rule:
EOF
    cat "${STYLE_FILE}" 2> /dev/null || echo "None is installed, so score writing_style 10."
    printf '\nThe plan:\n\n'
    cat
}

# Append the outcome in $1 and the scores in $2, if any, to the review log, when the project has a memory folder
log_review() {
    [[ -n "${REVIEWS_LOG}" && -d "$(dirname "${REVIEWS_LOG}")" ]] || return 0
    echo "$(date +%Y-%m-%d) session=${SESSION} outcome=$1 ${2:-}" >> "${REVIEWS_LOG}"
}

# Pass the plan, leaving the user's approval in place, with the message in $1 for the user and any context in $2 for Claude
# each outcome prints JSON and exits 0, as Claude Code reads a hook's JSON only then
allow() {
    jq -n --arg message "$1" --arg context "${2:-}" '{systemMessage: $message}
        + if $context == "" then {}
            else {hookSpecificOutput: {hookEventName: "PreToolUse", additionalContext: $context}} end'
    exit 0
}

# Block the plan, with the message in $1 for the user and the reason in $2 for Claude
deny() {
    jq -n --arg message "$1" --arg reason "$2" '{systemMessage: $message,
        hookSpecificOutput: {hookEventName: "PreToolUse", permissionDecision: "deny", permissionDecisionReason: $reason}}'
    exit 0
}

# Log that the plan wasn't reviewed for the reason in $1, then pass it
allow_unreviewed() {
    log_review unreviewed
    allow "⚠️ This plan wasn't reviewed: $1." "This plan wasn't reviewed: $1. Tell the user."
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

# the session ID names the round counter, kept to safe filename characters
SESSION="$(jq -r '.session_id // "unknown"' <<< "${INPUT}" | tr -cd '[:alnum:]_-')"
# auto-memory keeps a project's notes in memory/ beside its session transcripts, so the log sits with them
TRANSCRIPT="$(jq -r '.transcript_path // empty' <<< "${INPUT}")"
REVIEWS_LOG=""
[[ -n "${TRANSCRIPT}" ]] && REVIEWS_LOG="$(dirname "${TRANSCRIPT}")/memory/plan_reviews.log"

# --safe-mode loads no config or hooks, so the reviewer is unprimed and can't trigger this hook again
# it runs from the temp folder, so the repo's git status doesn't reach the reviewer, and with no tools, so it reads only
# the prompt; perl's alarm stands in for timeout, which macOS doesn't ship; any failure lets the plan through unreviewed
RAW="$(review_prompt <<< "${PLAN}" | (cd "${TMPDIR:-/tmp}" && perl -e 'alarm shift; exec @ARGV' "${REVIEW_TIMEOUT}" \
    claude -p --safe-mode --model sonnet --tools "" --no-session-persistence --output-format json) 2> /dev/null)" \
    || allow_unreviewed "the reviewer failed or timed out"
# -e makes jq fail when the filter finds no verdict
VERDICT="$(jq -ce "${VERDICT_FILTER}" <<< "${RAW}" 2> /dev/null)" \
    || allow_unreviewed "the reviewer gave no scores"

SCORES="$(jq -r '.scores | to_entries | map("\(.key)=\(.value)") | join(" ")' <<< "${VERDICT}")"
SHOWN_SCORES="$(jq -r '.scores | to_entries | map("\(.key) \(.value)/10") | join(", ")' <<< "${VERDICT}")"
ROUNDS_FILE="${TMPDIR:-/tmp}/claude_plan_review_${SESSION}"
# a plan that passes or is capped ends its rounds, so the session's next plan starts at none
if jq -e '[.scores[]] | all(. == 10)' <<< "${VERDICT}" > /dev/null; then
    rm -f "${ROUNDS_FILE}"
    log_review passed "${SCORES}"
    allow "✅ Plan review passed: ${SHOWN_SCORES}."
fi

FINDINGS="Plan review scores: ${SHOWN_SCORES}.
$(jq -r '.findings // [] | .[] | "- \(.)"' <<< "${VERDICT}")"
ROUNDS="$(cat "${ROUNDS_FILE}" 2> /dev/null || echo 0)"

if [[ "${ROUNDS}" -ge "${MAX_BLOCKS}" ]]; then
    rm -f "${ROUNDS_FILE}"
    log_review capped "${SCORES}"
    allow "⚠️ Plan review still has findings after ${MAX_BLOCKS} rounds, so the plan goes through: ${SHOWN_SCORES}." "${FINDINGS}
The plan review still has these findings after ${MAX_BLOCKS} rounds. Show them to the user with the plan."
fi
ROUNDS=$((ROUNDS + 1))
echo "${ROUNDS}" > "${ROUNDS_FILE}"
log_review blocked "${SCORES}"
deny "🔁 Plan review sent the plan back to Claude, round ${ROUNDS} of ${MAX_BLOCKS}: ${SHOWN_SCORES}." "${FINDINGS}
Ask the user about each decisions finding, fix the others yourself, then submit the plan again."
