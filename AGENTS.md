# Cultivate Web - Codex Agent Entry Point

## What This Repo Is

`Cultivate_Web` is the private preview website and future Railway-hosted web app for Cultivate. It owns the owner-facing preview, UI system, UX lab, route structure, brand consistency, and web-specific memory.

This is not the Company repo. Company strategy and source docs live at `M:\Cultivate`. Web uses that repo for source truth and turns approved material into a coherent website experience.

## Architecture

| Surface | Purpose |
|---|---|
| `AGENTS.md` | Hard Web Agent rules |
| `memory/` | Durable web memory |
| `skills/` | Repo-local task playbooks |
| `templates/` | Flask/Jinja pages |
| `static/css/` | Design tokens, components, page styles |
| `static/js/` | Small interaction scripts |
| `tests/` | Route and preview contract checks |
| `_system/` | Local helper notes/scripts |
| `archive/` | Superseded historical material |
| `memory/06-repo-and-deploy-operations.md` | GitHub repo setup, SSH account strategy, verification, Railway readiness, and push rules |

## Startup Sequence

1. Read `AGENTS.md`.
2. Read `memory/00-index.md`.
3. Read `M:\Cultivate\memory\00-index.md` when source/company context matters.
4. Read `M:\Cultivate\docs\normalized\cultivate_source_digest.md` for source-derived concept facts.
5. Read `memory/03-brand-and-ui-system.md` before UI work.
6. Read `skills/update-ui-system/SKILL.md` before changing tokens/components.
7. Read `skills/review-owner-preview/SKILL.md` before owner-preview changes.

## Source Of Truth

Use this hierarchy:

1. User direction in the current session.
2. This `AGENTS.md`.
3. Current code and tests.
4. Local `memory/`.
5. Local `skills/`.
6. Company source digest and memory at `M:\Cultivate`.
7. Original source docs under `M:\Cultivate\docs\source`.

Chat history is not durable source of truth.

## Web Rules

- This is private preview first. Do not treat any page as public launch copy unless explicitly approved.
- Keep unvalidated claims out of public-feeling language: launch date, pricing, licensed childcare, Foxtail partnership, paid teen jobs, cafe operation, facility capacity, or public rentals.
- Use brand tokens from the source docs: Georgia display, Calibri/system body, deep teal, clay, soft mint, warm cream, and garden green.
- UI kitchen sink and UX lab are required development surfaces.
- The rich private-preview routes are `/review-command-center`, `/owner-brief`, `/next-actions`, `/day-at-cultivate`, `/spaces`, `/brand-voice`, `/membership-model`, `/family-journey`, `/launch-roadmap`, `/faq-lab`, `/source-evidence`, `/public-draft-hub`, `/draft-home`, `/draft-about`, `/draft-cohort`, `/draft-faq`, `/approval-matrix`, `/founding-family-interest`, `/owner-decisions`, `/owner-walkthrough`, `/ecosystem-map`, `/founding-cohort`, `/cohort-blueprint`, `/impact-signals`, and `/launch-readiness`.
- Keep CSS tokenized. Add component styles before one-off page patches when a pattern repeats.
- Railway config may be edited for deploy readiness, but do not add real secrets.
- Git is initialized and pushed to `git@github.com:Josue-Gimbernard/Cultivate_Web.git`.
- Use `memory/06-repo-and-deploy-operations.md` before changing remotes, SSH auth, deploy behavior, commits, or pushes.

## Verification

For docs-only changes:

- Read changed docs end to end.

For app changes:

- Run `python -m compileall app.py`.
- Run `python -m unittest discover -s tests`.
- Run `npm.cmd run lint:colors`.
- Run `node --check static\js\main.js`.

## Closeout

Report changed files, verification, what was not changed, and unresolved questions.
