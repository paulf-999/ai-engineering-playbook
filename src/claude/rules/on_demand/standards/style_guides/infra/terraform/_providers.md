# 🔌 Providers

**Purpose:** Set provider version pinning, authentication and preview features, split from [`_structure.md`](_structure.md).

## 📋 Contents

- [🔒 Version pinning](#-version-pinning)
- [🔑 Provider authentication](#-provider-authentication)
- [🔬 Preview features](#-preview-features)

---

## 🔒 Version pinning

Pin provider versions as the team's policy in [`team_conventions/infra/terraform.md`](../../../../../path_scoped/team_conventions/infra/terraform.md) sets.

- Commit `.terraform.lock.hcl` to version control — it records the exact provider version resolved and must be consistent across the team.
- Upgrading a provider version requires a deliberate change, not an implicit one.

---

## 🔑 Provider authentication

Authentication uses JWT via a private key file — not username/password.

```terraform
provider "snowflake" {
  organization_name = var.organization_name
  account_name      = var.account_name
  user              = var.user
  private_key       = file(var.private_key_path)
  authenticator     = "SNOWFLAKE_JWT"
  role              = var.role
  warehouse         = var.warehouse
}
```

- All authentication values are passed in as variables — never hardcoded. The team's variable names replace the generic ones above.
- The key's path comes from an environment variable set in each developer's environment, and the key file itself is never committed. The team's variable names are in its conventions.

---

## 🔬 Preview features

When a resource type requires preview feature enablement, declare it explicitly in the provider block and document it in `README.md` — preview features may affect provider upgrade compatibility.

```terraform
provider "snowflake" {
  preview_features_enabled = [
    "snowflake_table_resource",
  ]
}
```

Only enable the specific preview features required — do not enable all.
