---
paths:
  - "**/Dockerfile*"
---
# 🐳 Docker & Dockerfile Style Guide & Standards

**Purpose:** how to write Dockerfiles and work with Docker images. This team's image and container names are in [`docker_team_conventions.md`](docker_team_conventions.md), which loads with this guide.

## ⚡ Key rules

- 📦 **Base image:** an official or verified-publisher image, as minimal as the job allows, such as `slim` or distroless, with its tag pinned and never `:latest` outside local work.
- 🧱 **Order:** base image, `WORKDIR`, OS packages, dependency files, then source and runtime config, so changing the source doesn't rebuild the dependency layers.
- 🏷️ **Names:** image and container names that say what the image is for, cased as the team's conventions set, with semantic-version tags such as `1.0.0`.

## 📚 Read on demand

- [`on_demand/style_guides/infra/docker/_fundamentals.md`](../../../on_demand/style_guides/infra/docker/_fundamentals.md), in your Claude config directory, when choosing a base image or ordering a Dockerfile's sections.
- [`on_demand/style_guides/infra/docker/_advanced.md`](../../../on_demand/style_guides/infra/docker/_advanced.md), when optimising layers, hardening an image, writing `.dockerignore` or using a multi-stage build.
