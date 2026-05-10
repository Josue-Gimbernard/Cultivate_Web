---
title: Repo And Deploy Operations
last_updated: 2026-05-10
---
# Repo And Deploy Operations

## Repo Identity

This repo is the deployable web app for Cultivate:

- Local path: `M:\Cultivate_Web`
- Remote: `git@github.com:Josue-Gimbernard/Cultivate_Web.git`
- Branch: `main`
- Initial commit: `3d3c7dc Initial Cultivate web preview`

The company/source framework lives separately:

- Local path: `M:\Cultivate`
- Remote: `git@github.com:Josue-Gimbernard/Cultivate.git`

Keep source docs, company domains, and broad strategy in `M:\Cultivate`. Keep website code, UI system, route memory, tests, and Railway files here.

## GitHub Account Strategy

Global Git on this machine still belongs to miniBIOTA. Do not change global Git identity for Cultivate web work.

This repo uses repo-local Git identity:

- Name: `Josue-Gimbernard`
- Email: `Josue-Gimbernard@users.noreply.github.com`

This repo uses repo-local SSH configuration:

- SSH key path: `C:/Users/gimbo/.ssh/id_ed25519_josue_github`
- `core.sshCommand`: `ssh -i C:/Users/gimbo/.ssh/id_ed25519_josue_github -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new`

This keeps Cultivate pushes on the `Josue-Gimbernard` GitHub account while leaving miniBIOTA credentials alone.

## Verification Before Commit

Run these checks before committing web changes:

```powershell
python -m compileall app.py
python -m unittest discover -s tests
npm.cmd run lint:colors
node --check static\js\main.js
```

Use `npm.cmd`, not bare `npm`, because PowerShell script execution may block `npm`.

## Local Preview

The private local preview runs on:

`http://127.0.0.1:8080/?access=cultivate-preview`

Access code:

`cultivate-preview`

Preview pages remain private and should not be treated as public launch copy.

## Railway Readiness

Railway files exist:

- `Procfile`
- `railway.toml`
- `requirements.txt`
- `.env.example`

Do not deploy, change secrets, or make hosting changes unless the founder explicitly asks.

## Current Commit Status

Initial web preview was committed and pushed on 2026-05-10.

The first pushed commit includes:

- Flask app and gated preview routes
- Owner preview and owner-review flow
- Public draft packet and publishing gate
- Approval, decision, and action dashboards
- UI kitchen sink and UX lab
- Route tests and color-token lint
- Web memory and skills

