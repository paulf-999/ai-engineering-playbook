#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: SessionStart hook that stays silent until 5 or more feedback notes have been saved since the last
#              /claude-kaizen run, then has Claude draft rules once a day, and logs the nudge for the trial's review
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code adds its stdout to the session, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# new feedback notes needed before a nudge
THRESHOLD=5

#=======================================================================
# Main script logic
#=======================================================================

# without jq the input can't be read, so stay silent
command -v jq > /dev/null || exit 0

INPUT="$(cat)"
TRANSCRIPT="$(jq -r '.transcript_path // empty' <<< "${INPUT}" 2> /dev/null || true)"
[[ "${TRANSCRIPT}" == /* ]] || exit 0

# a resumed, compacted or forked session carries on with earlier work, so only a fresh one nudges
SOURCE="$(jq -r '.source // "startup"' <<< "${INPUT}")"
[[ "${SOURCE}" == startup || "${SOURCE}" == clear ]] || exit 0

# the skill needs a repo with rule evals, so stay silent anywhere else
CWD="$(jq -r '.cwd // empty' <<< "${INPUT}")"
REPO_DIR="$(git -C "${CWD:-.}" rev-parse --show-toplevel 2> /dev/null || true)"
[[ -f "${REPO_DIR}/src/claude/rules/evals.yaml" ]] || exit 0

# auto-memory keeps a project's notes in memory/ beside its session transcripts
MEMORY_DIR="$(dirname "${TRANSCRIPT}")/memory"
[[ -d "${MEMORY_DIR}" ]] || exit 0
# /claude-kaizen appends a line here after each run, so a note newer than this file is new since that run
RUNS_LOG="${MEMORY_DIR}/kaizen_runs.log"
NUDGES_LOG="${MEMORY_DIR}/kaizen_nudges.log"
TODAY="$(date +%Y-%m-%d)"

# one nudge a day is enough
grep -q "^${TODAY} " "${NUDGES_LOG}" 2> /dev/null && exit 0

if [[ -f "${RUNS_LOG}" ]]; then
    NEW_NOTES="$(find "${MEMORY_DIR}" -maxdepth 1 -name 'feedback_*.md' -newer "${RUNS_LOG}" | wc -l | tr -d ' ')"
else
    NEW_NOTES="$(find "${MEMORY_DIR}" -maxdepth 1 -name 'feedback_*.md' | wc -l | tr -d ' ')"
fi
(( NEW_NOTES >= THRESHOLD )) || exit 0

echo "${TODAY} new_notes=${NEW_NOTES}" >> "${NUDGES_LOG}"
echo "${NEW_NOTES} feedback notes have been saved since the last /claude-kaizen run." \
    "Once the user's first task in this session is done, read skills/claude-kaizen/reference/_draft.md in your Claude" \
    "config directory (\$CLAUDE_CONFIG_DIR, or ~/.claude when unset) and follow it. Don't interrupt the task for it."
