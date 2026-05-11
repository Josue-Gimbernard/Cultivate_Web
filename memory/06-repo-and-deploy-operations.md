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

## Railway Deployment

Railway files exist and the app has been deployed:

- `Procfile`
- `railway.toml`
- `requirements.txt`
- `.env.example`

Current live private preview:

`https://web-production-dcfae.up.railway.app/?access=cultivate-preview`

Current deploy details:

- Builder: `RAILPACK`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Healthcheck: `/healthz`
- App is still private/gated and not public launch copy.

Do not change Railway variables, domains, secrets, public preview behavior, or hosting settings unless explicitly asked.

Railway account lesson:

- Railway GitHub repo visibility comes from the Railway GitHub App connection, not local SSH keys.
- If the repo picker only shows miniBIOTA repos, the Railway/GitHub App session is still seeing miniBIOTA.
- Do not disturb miniBIOTA Railway/GitHub settings when connecting Cultivate. Prefer separate browser profiles or carefully selected GitHub App repository access.

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

Documentation updates were also pushed on 2026-05-10:

- `1b9b5ff Document web repo operations and deployment rules`

Current owner-preview completion commits pushed on 2026-05-10:

- `32953df Add owner review packet`
- `756b08b Personalize owner preview copy for Brooke`
- `fcd44f0 Refine Brooke owner preview copy`
- `09ab2b9 Prepare Railway deployment config`
- `d51d250 Fix preview access gate sizing`
- `90df654 Add Brooke AI interview packet`
- `c89fadf Clarify Brooke Claude handoff`
- `a991b56 Add preview link to Brooke email draft`

The latest pushed state is a Brooke-facing private owner preview with live Railway access, the owner-review packet, meeting prep, script, worksheet, recap, answer log, post-meeting update plan, approval matrix, public draft packet, safe-without-owner support pages, and a Claude-ready Brooke decision packet. It remains gated and not public launch copy.

## Known Local Git Warning

`git status` may print:

```text
warning: unable to access 'C:\Users\gimbo/.config/git/ignore': Permission denied
```

This warning comes from a global Git ignore path and has not blocked commits or pushes. Do not change global Git configuration casually because miniBIOTA also uses this machine. Prefer repo-local configuration for Cultivate.
