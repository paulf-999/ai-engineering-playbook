#!/bin/bash

# Description: Keep the config's hooks and deny rules in settings.json in step, keeping every other setting
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_settings.sh",
#        from claude_install_config.sh, which sets the paths and inputs these functions read

#=======================================================================
# Variables
#=======================================================================

# the hooks and deny rules to merge, as JSON, which an uninstall leaves empty, set by render_settings
RENDERED_SETTINGS="{}"
# settings.json's content, set by read_settings and changed by the merges
SETTINGS_JSON=""
# jq helpers: strip removes the hooks that match f, and any entry that leaves empty, and hook_path is the path under $dir
# of the hook_*.sh file a hook's command runs, or null if it doesn't run one
# shellcheck disable=SC2016  # these are jq variables, not shell ones
JQ_STRIP='
    def command_text: (.command? // "") | if type == "string" then . else "" end;
    def hook_path($dir): command_text
        | split($dir + "/")[1:] | join($dir + "/")
        | capture("^(?<path>[^\"]*hook_[^/\"]*\\.sh)([\"\u0027\\s]|$)").path? // null;
    def strip(f): map(if (.hooks? | type) == "array" and any(.hooks[]; f)
        then .hooks |= map(select(f | not)) | select(.hooks != []) else . end);
'

#=======================================================================
# Functions
#=======================================================================

# Set RENDERED_SETTINGS from the settings template, or stop if a hook isn't in it, before anything has changed
render_settings() {
    local options=()
    if [[ -z "${PROJECT}" || "${WITH_HOOKS}" == 1 ]]; then options=(--all-hooks); fi
    if ! RENDERED_SETTINGS="$("${RENDER_PYTHON}" "${RENDERER}" "${HOOKS_DIR}" ${options[@]+"${options[@]}"})"; then
        log_message "${ERROR}" "The hooks and deny rules couldn't be rendered, as shown above - nothing changed."
        echo "If Python or Jinja is missing, run make install, which sets both up in .venv."
        exit 1
    fi
}

# Keep one entry per rendered hook in settings.json, then the deny rules, and none for a hook whose file is gone
register_settings() {
    local current
    # bash ignores set -e inside these three, so each returns 1 itself once it has said why it can't go on
    read_settings || return 0
    current="${SETTINGS_JSON}"
    merge_hooks || return 0
    merge_deny_rules || return 0
    strip_dead_hooks
    jq -c '.permissions.deny // []' <<< "${RENDERED_SETTINGS}" > "${DENY_MANIFEST}"
    [[ "${SETTINGS_JSON}" == "${current}" ]] && return 0
    if file_exists "${SETTINGS}"; then back_up_file "${BACKUP_DIR}" settings.json; fi
    write_settings
    log_message "${INFO}" "Updated the config's hooks and deny rules in ${SETTINGS}."
}

# Set SETTINGS_JSON to what settings.json holds, failing if jq is missing or can't read it, so it's left alone
read_settings() {
    SETTINGS_JSON="{}"
    if ! command -v jq > /dev/null; then
        log_message "${WARNING}" "jq isn't installed, so the config's hooks weren't added to ${SETTINGS}."
        return 1
    fi
    if file_exists "${SETTINGS}" && ! SETTINGS_JSON="$(jq '.' "${SETTINGS}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} isn't valid JSON, so the config's hooks weren't added."
        return 1
    fi
}

# Merge the rendered hooks into SETTINGS_JSON: strip each wherever its event has it, matched by file name so an old path
# counts, then add the current entries, failing if an event's value isn't a list, so can't take the hook
merge_hooks() {
    local event
    event="$(jq -r --argjson rendered "${RENDERED_SETTINGS}" '. as $settings | first($rendered.hooks // {} | keys_unsorted[]
        | select(. as $event | try ($settings.hooks[$event] // [] | type != "array") catch true)) // empty' \
        <<< "${SETTINGS_JSON}")"
    if [[ -n "${event}" ]]; then
        log_message "${WARNING}" "${SETTINGS} has a hooks.${event} that isn't a list, so the hooks weren't added."
        return 1
    fi
    SETTINGS_JSON="$(jq --argjson rendered "${RENDERED_SETTINGS}" "${JQ_STRIP}"'
        reduce ($rendered.hooks // {} | to_entries[]) as {key: $event, value: $entries} (.;
            [$entries[].hooks[].command | "/" + (split("/") | last)] as $suffixes
            | (.hooks[$event] // []) as $old
            | (($old | strip(command_text as $c | any($suffixes[]; . as $s | $c | endswith($s)))) + $entries) as $new
            | if $new == $old then . else .hooks[$event] = $new end
        )' <<< "${SETTINGS_JSON}")"
}

# Strip from SETTINGS_JSON each hook under the target's hooks/ folder whose hook_*.sh file is gone, such as one the config
# has dropped, or all of them once an uninstall has removed the files
strip_dead_hooks() {
    local path dead=()
    while IFS= read -r path; do
        if [[ -n "${path}" ]] && ! file_exists "${TARGET_DIR}/hooks/${path}"; then dead+=("${path}"); fi
    done < <(jq -r --arg dir "${HOOKS_DIR}" "${JQ_STRIP}"'.hooks[]?[]?.hooks?[]? | hook_path($dir) // empty' \
        <<< "${SETTINGS_JSON}" 2> /dev/null || true)
    [[ "${#dead[@]}" -gt 0 ]] || return 0
    SETTINGS_JSON="$(jq --arg dir "${HOOKS_DIR}" "${JQ_STRIP}"'
        .hooks |= map_values(if type == "array"
            then strip(hook_path($dir) as $path | $path != null and any($ARGS.positional[]; . == $path))
            else . end)' --args "${dead[@]}" <<< "${SETTINGS_JSON}")"
}

# Drop the deny rules the last install added from SETTINGS_JSON, then put the config's at the end, in order, keeping
# every other rule
merge_deny_rules() {
    local previous
    # an unreadable deny manifest counts as empty, so install still adds the current rules
    previous="$(jq -c 'if type == "array" then . else [] end' "${DENY_MANIFEST}" 2> /dev/null || echo "[]")"
    if ! SETTINGS_JSON="$(jq --argjson previous "${previous}" --argjson rendered "${RENDERED_SETTINGS}" '
        (.permissions.deny // []) as $old
        | if ($old | type) != "array" then error("permissions.deny is not a list") else . end
        | ($rendered.permissions.deny // []) as $current
        | ($previous + $current) as $ours
        | ($old | map(select(. as $rule | $ours | index($rule) | not)) + $current) as $new
        | if $new == $old then . else .permissions.deny = $new end' <<< "${SETTINGS_JSON}" 2> /dev/null)"; then
        log_message "${WARNING}" "${SETTINGS} has a permissions.deny that isn't a list, so the settings weren't added."
        return 1
    fi
}

# Write SETTINGS_JSON to settings.json, keeping its mode and any symlink, through a temporary file that's then moved, so
# a failed write can't leave it half written
write_settings() {
    local path="${SETTINGS}" mode
    if [[ -L "${path}" ]]; then path="$(readlink -f "${path}")"; fi
    if file_exists "${path}"; then
        # GNU stat, then macOS's
        mode="$(stat -c %a "${path}" 2> /dev/null || stat -f %Lp "${path}")"
        # settings can hold secrets, so the temporary file starts out private
        (umask 077 && printf '%s\n' "${SETTINGS_JSON}" > "${path}.tmp")
        chmod "${mode}" "${path}.tmp"
    else
        printf '%s\n' "${SETTINGS_JSON}" > "${path}.tmp"
    fi
    mv "${path}.tmp" "${path}"
}
