#!/bin/bash
# version: 1.3.0
# created: 2026-11-04
# updated: 2026-11-10
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
#              On-demand files in rules/_rules_on_demand/ go beside rules/, since Claude Code loads everything under rules/
#              A manifest records what was installed, so files the repo has since removed are backed up and removed
#              It also registers the config's hooks in settings.json, keeping every setting already there
# Usage: src/sh/claude_install_config.sh (run from the repo root, at your own terminal; make install calls it)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# mirrors the config directory's layout, so each file is copied to the same relative path, except on-demand files
SOURCE_DIR="src/claude"
LAZY_RULES_DIR="rules/_rules_on_demand"
TARGET_DIR="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
# the paths the last install wrote, one per line, so the next install can remove any the repo no longer has
MANIFEST="${TARGET_DIR}/.playbook_install_manifest"
BACKUP_DIR="${TARGET_DIR}/backups/install_$(date +%Y_%m_%d_%H%M%S)"
# the tracked files under SOURCE_DIR, set by list_source_files
SOURCE_FILES=()
# where each source file installs, one per line, set by list_source_files
TARGET_PATHS=""
# files the last install wrote that the repo no longer has, set by list_removed_files
REMOVED_FILES=()
# settings.json holds personal settings, so install merges the hook into it rather than copying a file over it
SETTINGS="${TARGET_DIR}/settings.json"
# an absolute path, since hook commands in user settings can't refer to CLAUDE_CONFIG_DIR
PLAN_HOOK_COMMAND="bash \"${TARGET_DIR}/hooks/hook_enforcement_plan_sections.sh\""

#=======================================================================
# Functions
#=======================================================================

# Print where a source file installs: on-demand files move from rules/_rules_on_demand/ to _rules_on_demand/
target_path() {
    local file="${1}"
    if [[ "${file}" == "${LAZY_RULES_DIR}/"* ]]; then
        echo "${file#rules/}"
    else
        echo "${file}"
    fi
}

# Collect the files git tracks under SOURCE_DIR, so untracked drafts and caches are never installed
list_source_files() {
    local file
    while IFS= read -r -d '' file; do
        SOURCE_FILES+=("${file#"${SOURCE_DIR}"/}")
        TARGET_PATHS+="$(target_path "${file#"${SOURCE_DIR}"/}")"$'\n'
    done < <(git ls-files -z -- "${SOURCE_DIR}")
    if [[ "${#SOURCE_FILES[@]}" -eq 0 ]]; then
        log_message "${ERROR}" "No tracked files found under ${SOURCE_DIR} - nothing to install."
        exit 1
    fi
}

# Collect the manifest's paths that are no longer installed, skipping any path that could point outside the target
list_removed_files() {
    local path
    file_exists "${MANIFEST}" || return 0
    while IFS= read -r path; do
        [[ -n "${path}" && "${path}" != /* && "${path}" != *..* ]] || continue
        if ! grep -Fxq -- "${path}" <<< "${TARGET_PATHS}" && file_exists "${TARGET_DIR}/${path}"; then
            REMOVED_FILES+=("${path}")
        fi
    done < "${MANIFEST}"
}

# Show what will change and require 'install' typed at a real terminal, so Claude's Bash tool can't run it unattended
confirm_install() {
    local answer file
    if [[ ! -t 0 ]]; then
        log_message "${ERROR}" "Run make install from your own terminal - nothing changed."
        exit 1
    fi
    log_message "${INFO}" "Installing ${#SOURCE_FILES[@]} file(s) into ${TARGET_DIR}:"
    for file in "${SOURCE_FILES[@]}"; do
        echo "  $(target_path "${file}")"
    done
    if [[ "${#REMOVED_FILES[@]}" -gt 0 ]]; then
        log_message "${WARNING}" "Removing ${#REMOVED_FILES[@]} file(s) an earlier install added that the repo no longer has:"
        for file in "${REMOVED_FILES[@]}"; do
            echo "  ${file}"
        done
    fi
    echo "It also adds the plan sections hook to ${SETTINGS}, if it isn't there yet."
    echo "Each file it overwrites or removes is backed up to ${BACKUP_DIR} first."
    read -r -p "Type 'install' to continue: " answer || true
    if [[ "${answer}" != "install" ]]; then
        log_message "${WARNING}" "Install cancelled - nothing changed."
        exit 1
    fi
}

# Copy each file over the target, backing up any existing copy that differs, and skipping identical ones
install_files() {
    local file relative target copied=0 backed_up=0
    for file in "${SOURCE_FILES[@]}"; do
        relative="$(target_path "${file}")"
        target="${TARGET_DIR}/${relative}"
        if file_exists "${target}" && cmp -s "${SOURCE_DIR}/${file}" "${target}"; then
            continue
        fi
        if file_exists "${target}"; then
            mkdir -p "$(dirname "${BACKUP_DIR}/${relative}")"
            cp -p "${target}" "${BACKUP_DIR}/${relative}"
            backed_up=$((backed_up + 1))
        fi
        mkdir -p "$(dirname "${target}")"
        cp "${SOURCE_DIR}/${file}" "${target}"
        copied=$((copied + 1))
    done
    log_message "${INFO}" "Installed ${copied} changed file(s), backing up ${backed_up}, into ${TARGET_DIR}."
}

# Back up and remove each file the repo no longer has, then record what this install wrote
remove_old_files() {
    local file
    for file in "${REMOVED_FILES[@]+"${REMOVED_FILES[@]}"}"; do
        mkdir -p "$(dirname "${BACKUP_DIR}/${file}")"
        cp -p "${TARGET_DIR}/${file}" "${BACKUP_DIR}/${file}"
        rm "${TARGET_DIR}/${file}"
    done
    log_message "${INFO}" "Removed ${#REMOVED_FILES[@]} file(s) the repo no longer has." false
    printf '%s' "${TARGET_PATHS}" > "${MANIFEST}"
}

# Add the plan sections hook to settings.json, backing up the old file, unless it's already registered
register_hooks() {
    local current updated
    if ! command -v jq > /dev/null; then
        log_message "${WARNING}" "jq isn't installed, so the plan sections hook wasn't added to ${SETTINGS}."
        return 0
    fi
    current="{}"
    if file_exists "${SETTINGS}"; then
        # a settings file jq can't read is left alone, rather than replaced
        if ! current="$(jq '.' "${SETTINGS}" 2> /dev/null)"; then
            log_message "${WARNING}" "${SETTINGS} isn't valid JSON, so the plan sections hook wasn't added."
            return 0
        fi
        if jq -e --arg command "${PLAN_HOOK_COMMAND}" \
            '[.hooks.PreToolUse[]?.hooks[]?.command] | index($command)' <<< "${current}" > /dev/null; then
            return 0
        fi
        mkdir -p "${BACKUP_DIR}"
        cp -p "${SETTINGS}" "${BACKUP_DIR}/settings.json"
    fi
    # a PreToolUse value that isn't a list can't take the hook, so it's reported rather than aborting the install
    if ! updated="$(jq --arg command "${PLAN_HOOK_COMMAND}" \
        '.hooks.PreToolUse += [{matcher: "ExitPlanMode", hooks: [{type: "command", command: $command}]}]' \
        <<< "${current}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} has a hooks.PreToolUse that isn't a list, so the hook wasn't added."
        return 0
    fi
    # write a temporary file, then move it, so a failed write can't leave settings.json half written
    printf '%s\n' "${updated}" > "${SETTINGS}.tmp"
    mv "${SETTINGS}.tmp" "${SETTINGS}"
    log_message "${INFO}" "Added the plan sections hook to ${SETTINGS}."
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

list_source_files
list_removed_files
confirm_install
install_files
remove_old_files
register_hooks

print_section_header "${DEBUG}" "Script execution completed." && echo
