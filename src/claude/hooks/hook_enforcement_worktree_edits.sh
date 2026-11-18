#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: PreToolUse hook on file edits that blocks a session's first edit in a repo's main folder once,
#              so Claude moves into its own git worktree before another session's changes mix with its own
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code reads its stderr and exit code, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# exit code 2 tells Claude Code to block the tool call and show stderr to Claude
BLOCK=2
# one marker file per session and repo, so each session is warned once per repo
STATE_DIR="${TMPDIR:-/tmp}/claude_worktree_edits"

#=======================================================================
# Functions
#=======================================================================

# Print the nearest existing folder holding the path $1, since a new file's folder may not exist yet
existing_folder() {
    local folder
    folder="$(dirname "${1}")"
    while [[ ! -d "${folder}" ]]; do
        folder="$(dirname "${folder}")"
    done
    echo "${folder}"
}

# Succeed if the repo at $1 is a linked worktree rather than the repo's main folder
is_linked_worktree() {
    local repo="${1}"
    [[ "$(git -C "${repo}" rev-parse --absolute-git-dir)" \
        != "$(git -C "${repo}" rev-parse --path-format=absolute --git-common-dir)" ]]
}

#=======================================================================
# Main script logic
#=======================================================================

# without jq the input can't be read, so allow the edit rather than block every one
command -v jq > /dev/null || exit 0

INPUT="$(cat)"
# the session id names a file, so keep only characters safe in a path
SESSION="$(jq -r '.session_id // empty' <<< "${INPUT}" 2> /dev/null | tr -cd 'A-Za-z0-9_-' || true)"
FILE="$(jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' <<< "${INPUT}" 2> /dev/null || true)"
[[ -n "${SESSION}" && "${FILE}" == /* ]] || exit 0

ROOT="$(git -C "$(existing_folder "${FILE}")" rev-parse --show-toplevel 2> /dev/null)" || exit 0
is_linked_worktree "${ROOT}" && exit 0

STATE_FILE="${STATE_DIR}/${SESSION}_$(git hash-object --stdin <<< "${ROOT}")"
[[ -f "${STATE_FILE}" ]] && exit 0
mkdir -p "${STATE_DIR}"
touch "${STATE_FILE}"

echo "This is your first edit in ${ROOT}, the repo's main folder, not a worktree." \
    "If another session or sub-agent may work in this repo, move into your own git worktree first," \
    "per rules/on_demand/01_standards/git.md, and make the edit there. Otherwise, make the edit again." >&2
# this session hasn't edited the repo yet, so changes already there are most likely another session's
if [[ -n "$(git -C "${ROOT}" status --porcelain --untracked-files=no)" ]]; then
    echo "Tracked files here already have changes from before this edit, so another session is likely working here." >&2
fi
exit "${BLOCK}"
