---
title: Session Closeout 2026-05-10
last_updated: 2026-05-10
---
# Session Closeout 2026-05-10

## What Changed

The Cultivate website moved from local private preview to live Railway-hosted private preview.

Current live preview:

`https://web-production-dcfae.up.railway.app/?access=cultivate-preview`

The live app is still a private owner-review surface, not public launch copy.

## Deployment State

- Railway is connected to the `Josue-Gimbernard/Cultivate_Web` GitHub repo.
- The deployed app is reachable at `web-production-dcfae.up.railway.app`.
- The access gate is working.
- `railway.toml` uses `RAILPACK`.
- Gunicorn binds to `0.0.0.0:$PORT` through both `railway.toml` and `Procfile`.
- `/healthz` remains the healthcheck route.

## Brooke Handoff

Brooke does not need repo access.

Files created for the Brooke handoff:

- `BROOKE_AI_INTERVIEW_PACKET.md`: attachment-ready Claude packet that interviews Brooke one section at a time.
- `BROOKE_EMAIL_DRAFT.md`: email draft that includes the live private preview link and instructions for uploading the packet to Claude.

Expected Brooke workflow:

1. Brooke opens the live preview link.
2. Brooke reviews what feels right, too big, not like her, or not ready for others.
3. Brooke uploads `BROOKE_AI_INTERVIEW_PACKET.md` into Claude.
4. Claude interviews Brooke one section at a time.
5. Brooke sends back Claude's final summary.
6. Future site work updates `memory/08-owner-answer-log.md` before changing public-facing drafts.

## Current Commit Trail

Important pushed commits after the owner-preview copy pass:

- `09ab2b9 Prepare Railway deployment config`
- `d51d250 Fix preview access gate sizing`
- `90df654 Add Brooke AI interview packet`
- `c89fadf Clarify Brooke Claude handoff`
- `a991b56 Add preview link to Brooke email draft`

## Lessons Learned

- Keep website build work in `M:\Cultivate_Web`. Keep company strategy, source extraction, and domain planning in `M:\Cultivate`.
- Railway GitHub repo visibility is controlled by the GitHub App connection, not local SSH keys.
- Do not disturb the miniBIOTA GitHub/Railway setup when configuring Cultivate. Use separate browser sessions, a separate browser profile, or careful GitHub App repository selection when accounts overlap.
- Brooke-facing handoffs should not assume GitHub or repo access. Prefer plain Markdown attachments and simple AI-app instructions.
- The private preview access screen needs responsive sizing because it may be the first thing the owner sees from the live URL.

## Next Session Start

For website work, start in `M:\Cultivate_Web` and read:

1. `AGENTS.md`
2. `memory/00-index.md`
3. `memory/09-session-closeout-2026-05-10.md`
4. `memory/06-repo-and-deploy-operations.md`
5. `memory/07-owner-input-workflow.md`
6. `BROOKE_AI_INTERVIEW_PACKET.md` if Brooke has answered or is about to answer

## Next Work

- Wait for Brooke's Claude summary or direct notes.
- Update `memory/08-owner-answer-log.md` first when Brooke answers.
- Then update the approval matrix, assumptions review, and draft public pages.
- Do not turn the private preview into public launch copy until Brooke's answers are logged and claim boundaries are updated.
