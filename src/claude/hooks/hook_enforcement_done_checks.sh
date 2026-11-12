#!/bin/bash
# version: 1.0.0
# created: 2026-11-12
# updated: 2026-11-12
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Stop hook that sends Claude back once to run the repo's done checks when tracked files changed since its last stop
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code reads its stderr and exit code, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# exit code 2 tells Claude Code not to stop yet, and shows stderr to Claude
BLOCK=2
# one fingerprint file per session, so each session is nudged only when its changes move on
STATE_DIR="${TMPDIR:-/tmp}/claude_done_checks"

#=======================================================================
# Functions
#=======================================================================

# Print a fingerprint of the tracked changes in the repo at $1, or nothing when there are none
changes_fingerprint() {
    local repo="${1}"
    [[ -n "$(git -C "${repo}" status --porcelain --untracked-files=no)" ]] || return 0
    git -C "${repo}" diff HEAD | git hash-object --stdin
}

#=======================================================================
# Main script logic
#=======================================================================

# without jq the input can't be read, so allow the stop rather than block every one
command -v jq > /dev/null || exit 0

INPUT="$(cat)"
# while a stop hook is already keeping Claude going, blocking again would loop
[[ "$(jq -r '.stop_hook_active // false' <<< "${INPUT}" 2> /dev/null || true)" == "true" ]] && exit 0
# the session id names a file, so keep only characters safe in a path
SESSION="$(jq -r '.session_id // empty' <<< "${INPUT}" 2> /dev/null | tr -cd 'A-Za-z0-9_-' || true)"
REPO="$(jq -r '.cwd // empty' <<< "${INPUT}" 2> /dev/null || true)"
[[ -n "${SESSION}" && -n "${REPO}" ]] || exit 0
git -C "${REPO}" rev-parse --is-inside-work-tree > /dev/null 2>&1 || exit 0

FINGERPRINT="$(changes_fingerprint "${REPO}")"
[[ -n "${FINGERPRINT}" ]] || exit 0
STATE_FILE="${STATE_DIR}/${SESSION}"
[[ "$(cat "${STATE_FILE}" 2> /dev/null || true)" == "${FINGERPRINT}" ]] && exit 0
mkdir -p "${STATE_DIR}"
printf '%s\n' "${FINGERPRINT}" > "${STATE_FILE}"

echo "Tracked files changed since you last stopped." \
    "Before finishing, run the checks this repo's CLAUDE.md says define done, such as its test command," \
    "and report what they showed. If none apply, say so." >&2
exit "${BLOCK}"
