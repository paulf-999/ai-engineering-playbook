#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Stop hook that sends Claude back once to run the repo's done checks when tracked files it edited changed since its last stop,
#              unless it already ran a command CLAUDE.md names after its last edit
#              It stays quiet in a repo with no CLAUDE.md, since only a CLAUDE.md says which checks define done
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

# Succeed when the transcript at $2 shows this session editing a changed tracked file in the repo at $1
# With no readable transcript it succeeds, so the hook falls back to firing on any change
session_edited_changes() {
    local root="${1}" transcript="${2}"
    [[ -r "${transcript}" ]] || return 0
    jq -r 'select(.type == "assistant") | .message.content[]? | select(.type == "tool_use")
        | select(.name | test("^(Edit|MultiEdit|Write|NotebookEdit)$"))
        | .input.file_path // .input.notebook_path // empty' "${transcript}" 2> /dev/null \
        | grep -Fxq -f <(git -C "${root}" diff HEAD --name-only | sed "s#^#${root}/#")
}

# Succeed when the transcript at $2 shows a Bash call, after this session's last edit, that runs a command the
# CLAUDE.md in the repo at $1 names in backticks, such as `make test`, so checks already run aren't asked for again
checks_ran_since_last_edit() {
    local root="${1}" transcript="${2}" commands
    [[ -r "${transcript}" ]] || return 1
    # shellcheck disable=SC2016  # the backticks are literal, matching CLAUDE.md's inline code
    commands="$(cat "${root}/CLAUDE.md" "${root}/.claude/CLAUDE.md" 2> /dev/null | grep -o '`[^`]* [^`]*`' | tr -d '`' || true)"
    [[ -n "${commands}" ]] || return 1
    jq -r 'select(.type == "assistant") | .message.content[]? | select(.type == "tool_use")
        | if (.name | test("^(Edit|MultiEdit|Write|NotebookEdit)$")) then "EDIT"
          elif .name == "Bash" then "BASH " + ((.input.command // "") | gsub("\n"; " "))
          else empty end' "${transcript}" 2> /dev/null \
        | awk '/^EDIT$/ { after = ""; next } { after = after $0 "\n" } END { printf "%s", after }' \
        | grep -Fq -f <(printf '%s\n' "${commands}")
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
ROOT="$(git -C "${REPO}" rev-parse --show-toplevel 2> /dev/null)" || exit 0
# a repo with no CLAUDE.md names no done checks, so sending Claude back would only ask it to guess
[[ -f "${ROOT}/CLAUDE.md" || -f "${ROOT}/.claude/CLAUDE.md" ]] || exit 0

FINGERPRINT="$(changes_fingerprint "${REPO}")"
[[ -n "${FINGERPRINT}" ]] || exit 0
# changes another session made aren't this session's to check
TRANSCRIPT="$(jq -r '.transcript_path // empty' <<< "${INPUT}" 2> /dev/null || true)"
session_edited_changes "${ROOT}" "${TRANSCRIPT}" || exit 0
checks_ran_since_last_edit "${ROOT}" "${TRANSCRIPT}" && exit 0
STATE_FILE="${STATE_DIR}/${SESSION}"
[[ "$(cat "${STATE_FILE}" 2> /dev/null || true)" == "${FINGERPRINT}" ]] && exit 0
mkdir -p "${STATE_DIR}"
printf '%s\n' "${FINGERPRINT}" > "${STATE_FILE}"

echo "Tracked files changed since you last stopped." \
    "Before finishing, run the checks this repo's CLAUDE.md says define done, such as its test command," \
    "and report what they showed. If none apply, say so." >&2
exit "${BLOCK}"
