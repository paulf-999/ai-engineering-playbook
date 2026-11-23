# 📋 Declarations

**Purpose:** Set what every variable and output must declare, and how to validate inputs, split from [`_terraform_naming.md`](_terraform_naming.md).

## 📋 Contents

- [📋 Variable declaration requirements](#-variable-declaration-requirements)
- [✅ Validation blocks](#-validation-blocks)
- [📤 Output declarations](#-output-declarations)

---

## 📋 Variable declaration requirements

Every variable must declare `description` and `type`, and declares `default` only when a safe one exists:

| Field | Requirement |
|-------|-------------|
| `description` | Always required — explain what the variable controls and any constraints |
| `type` | Always explicit — use `string`, `number`, `bool`, `list(...)`, `map(...)` as appropriate |
| `default` | Omit unless a safe default exists — prefer requiring callers to be explicit |

Mark variables that contain credentials or sensitive values with `sensitive = true`.

---

## ✅ Validation blocks

Use `validation` blocks to enforce naming conventions and format constraints at the variable level, so a bad value fails at plan time with a clear message rather than as a Snowflake error at apply time.

```terraform
variable "name" {
  description = <<-EOT
    Snowflake warehouse name. Must be uppercase letters and
    underscores only, and 255 characters or fewer.
  EOT
  type = string

  validation {
    condition = can(regex(
      "^[A-Z_]+$",
      var.name
    ))
    error_message = "Warehouse name must be uppercase letters and underscores only."
  }

  validation {
    condition     = length(var.name) <= 255
    error_message = "Warehouse name must be 255 characters or fewer."
  }
}
```

- Write one `validation` block per constraint — do not combine unrelated conditions.
- `error_message` must describe what a valid value looks like.
- Use `<<-EOT` heredoc syntax for multi-line descriptions.

---

## 📤 Output declarations

Every output must include a `description`. Reference the resource attribute directly — do not compute values in output blocks.

```terraform
output "name" {
  description = "The Snowflake role name."
  value       = snowflake_account_role.this.name
}
```

Expose only the attributes that callers are expected to consume.

## 📞 Called by

This rule is invoked by [`rules/path_scoped/style_guides/infra/terraform.md`](../../../../path_scoped/style_guides/infra/terraform.md), when declaring a variable or output, or adding a validation block.
