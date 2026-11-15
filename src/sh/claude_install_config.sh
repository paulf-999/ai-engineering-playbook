#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
#              On-demand files in rules/on_demand/ go beside rules/, since Claude Code loads everything under rules/
#              A manifest records what was installed, so files the repo has since removed are backed up and removed
#              It also keeps the config's hooks and deny rules in settings.json in step, keeping every other setting
#              With PROJECT set, it installs into that repo's .claude/ folder instead, leaving the hooks out unless HOOKS=1
# Usage: [PROJECT=<repo> [HOOKS=1]] src/sh/claude_install_config.sh (run from the repo root, at your own terminal;
#        make install calls it)

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
LAZY_RULES_DIR="rules/on_demand"
CONFIG_DIR="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
# a repo to install into instead of your Claude config directory, and whether its install includes the hooks
PROJECT="${PROJECT:-}"
WITH_HOOKS="${HOOKS:-}"
if [[ -n "${PROJECT}" ]]; then
    if [[ ! -d "${PROJECT}" ]]; then
        echo "PROJECT=${PROJECT} isn't a folder - nothing changed." >&2
        exit 1
    fi
    PROJECT="$(cd "${PROJECT}" && pwd)"
    TARGET_DIR="${PROJECT}/.claude"
    # backups go in your own config directory, so they're never committed with the repo
    BACKUP_DIR="${CONFIG_DIR}/backups/project_$(basename "${PROJECT}")_$(date +%Y_%m_%d_%H%M%S)"
else
    TARGET_DIR="${CONFIG_DIR}"
    BACKUP_DIR="${TARGET_DIR}/backups/install_$(date +%Y_%m_%d_%H%M%S)"
fi
# the paths the last install wrote, one per line, so the next install can remove any the repo no longer has
MANIFEST="${TARGET_DIR}/.playbook_install_manifest"
# the tracked files under SOURCE_DIR, set by list_source_files
SOURCE_FILES=()
# where each source file installs, one per line, set by list_source_files
TARGET_PATHS=""
# files the last install wrote that the repo no longer has, set by list_removed_files
REMOVED_FILES=()
# settings.json holds personal settings, so install merges the hooks into it rather than copying a file over it
SETTINGS="${TARGET_DIR}/settings.json"
# each hook the config ships, as event|matcher|path, with an empty matcher for events that take none
SHIPPED_HOOKS=(
    "PreToolUse|ExitPlanMode|hooks/hook_enforcement_plan_sections.sh"
    "Stop||hooks/hook_enforcement_done_checks.sh"
)
# deny rules that keep Claude's file tools out of .env files, kept last in this order so the carve-out follows its rule
DENY_RULES=("Read(.env)" "Read(.env.*)" "Read(!.env.example)")
# the deny rules the last install added, as a JSON list, so the next install can remove any the config has since dropped
DENY_MANIFEST="${TARGET_DIR}/.playbook_install_deny_rules"

#=======================================================================
# Functions
#=======================================================================

# Print where a source file installs: on-demand files move from rules/on_demand/ to on_demand/
target_path() {
    local file="${1}"
    if [[ "${file}" == "${LAZY_RULES_DIR}/"* ]]; then
        echo "${file#rules/}"
    else
        echo "${file}"
    fi
}

# Print a source file as it installs: in a project, pointers name the project's .claude/ folder, not your config directory
render() {
    local file="${1}"
    if [[ -n "${PROJECT}" ]]; then
        # shellcheck disable=SC2016  # the backticks and \$CLAUDE_CONFIG_DIR are literal text in the rules, not expansions
        sed -e 's/in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~\/.claude` when unset)/in this project'"'"'s `.claude\/` folder/' \
            -e 's/in your Claude config directory/in this project'"'"'s `.claude\/` folder/' "${SOURCE_DIR}/${file}"
    else
        cat "${SOURCE_DIR}/${file}"
    fi
}

# Collect the files git tracks under SOURCE_DIR, so untracked drafts and caches are never installed,
# leaving the hooks out of a project install unless HOOKS=1
list_source_files() {
    local file
    while IFS= read -r -d '' file; do
        file="${file#"${SOURCE_DIR}"/}"
        [[ -n "${PROJECT}" && "${WITH_HOOKS}" != 1 && "${file}" == hooks/* ]] && continue
        SOURCE_FILES+=("${file}")
        TARGET_PATHS+="$(target_path "${file}")"$'\n'
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
    echo "It also updates the config's hooks and deny rules in ${SETTINGS} to match the install."
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
        if file_exists "${target}" && cmp -s <(render "${file}") "${target}"; then
            continue
        fi
        if file_exists "${target}"; then
            mkdir -p "$(dirname "${BACKUP_DIR}/${relative}")"
            cp -p "${target}" "${BACKUP_DIR}/${relative}"
            backed_up=$((backed_up + 1))
        fi
        mkdir -p "$(dirname "${target}")"
        render "${file}" > "${target}"
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

# Keep one entry per hook in settings.json at the current path, or none if it isn't shipped, then the deny rules,
# backing up the old file
register_settings() {
    local current updated entry event matcher hook ship previous command
    if ! command -v jq > /dev/null; then
        log_message "${WARNING}" "jq isn't installed, so the config's hooks weren't added to ${SETTINGS}."
        return 0
    fi
    current="{}"
    # a settings file jq can't read is left alone, rather than replaced
    if file_exists "${SETTINGS}" && ! current="$(jq '.' "${SETTINGS}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} isn't valid JSON, so the config's hooks weren't added."
        return 0
    fi
    updated="${current}"
    for entry in "${SHIPPED_HOOKS[@]}"; do
        IFS='|' read -r event matcher hook <<< "${entry}"
        ship=false
        grep -Fxq -- "${hook}" <<< "${TARGET_PATHS}" && ship=true
        # a project's settings are shared, so its hook command names the project through Claude Code's own variable
        command="bash \"${TARGET_DIR}/${hook}\""
        [[ -n "${PROJECT}" ]] && command="bash \"\$CLAUDE_PROJECT_DIR/.claude/${hook}\""
        # strip the hook wherever it's registered, matched by file name so an old path counts, then re-add it if shipped
        # an event value that isn't a list can't take the hook, so it's reported rather than aborting the install
        # the command is an absolute path, since hook commands in user settings can't refer to CLAUDE_CONFIG_DIR
        if ! updated="$(jq --arg event "${event}" --arg matcher "${matcher}" \
            --arg command "${command}" --arg suffix "/${hook}\"" --argjson ship "${ship}" '
            def ours: (.command? // "") as $c | ($c | type) == "string" and ($c | endswith($suffix));
            (.hooks[$event] // []) as $old
            | if ($old | type) != "array" then error("hooks.\($event) is not a list") else . end
            | ($old
                | map(if (.hooks? | type) == "array" and any(.hooks[]; ours)
                    then .hooks |= map(select(ours | not)) | select(.hooks != [])
                    else . end)
                | . + (if $ship
                    then [(if $matcher == "" then {} else {matcher: $matcher} end)
                        + {hooks: [{type: "command", command: $command}]}]
                    else [] end)
              ) as $new
            | if $new == $old then . else .hooks[$event] = $new end' <<< "${updated}" 2> /dev/null)"; then
            log_message "${WARNING}" "${SETTINGS} has a hooks.${event} that isn't a list, so the hooks weren't added."
            return 0
        fi
    done
    # an unreadable deny manifest counts as empty, so install still adds the current rules
    previous="$(jq -c 'if type == "array" then . else [] end' "${DENY_MANIFEST}" 2> /dev/null || echo "[]")"
    # drop the rules the last install added, then put the config's rules at the end, in order, keeping every other rule
    if ! updated="$(jq --argjson previous "${previous}" --args '
        (.permissions.deny // []) as $old
        | if ($old | type) != "array" then error("permissions.deny is not a list") else . end
        | ($previous + $ARGS.positional) as $ours
        | ($old | map(select(. as $rule | $ours | index($rule) | not)) + $ARGS.positional) as $new
        | if $new == $old then . else .permissions.deny = $new end' "${DENY_RULES[@]}" <<< "${updated}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} has a permissions.deny that isn't a list, so the settings weren't added."
        return 0
    fi
    jq -cn '$ARGS.positional' --args "${DENY_RULES[@]}" > "${DENY_MANIFEST}"
    [[ "${updated}" == "${current}" ]] && return 0
    if file_exists "${SETTINGS}"; then
        mkdir -p "${BACKUP_DIR}"
        cp -p "${SETTINGS}" "${BACKUP_DIR}/settings.json"
    fi
    # write a temporary file, then move it, so a failed write can't leave settings.json half written
    printf '%s\n' "${updated}" > "${SETTINGS}.tmp"
    mv "${SETTINGS}.tmp" "${SETTINGS}"
    log_message "${INFO}" "Updated the config's hooks and deny rules in ${SETTINGS}."
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
register_settings

print_section_header "${DEBUG}" "Script execution completed." && echo
