#!/bin/bash
# version: 1.2.2
# created: 2026-11-04
# updated: 2026-11-05
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
#              On-demand files in rules/_rules_on_demand/ go beside rules/, since Claude Code loads everything under rules/
#              A manifest records what was installed, so files the repo has since removed are backed up and removed
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

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

list_source_files
list_removed_files
confirm_install
install_files
remove_old_files

print_section_header "${DEBUG}" "Script execution completed." && echo
