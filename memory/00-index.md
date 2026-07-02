---
title: Cultivate Web Memory Index
last_updated: 2026-05-20
---
# Cultivate Web Memory Index

## Purpose

This folder is the durable Web Agent memory layer for the Cultivate website.

## Load Order

1. `AGENTS.md`
2. This index
3. `memory/01-agent-purpose.md`
4. `memory/02-site-strategy.md`
5. `memory/03-brand-and-ui-system.md`
6. `memory/04-route-architecture.md`
7. `memory/05-owner-preview-rules.md`
8. `memory/07-owner-input-workflow.md`
9. `memory/08-owner-answer-log.md`
10. `memory/09-session-closeout-2026-05-10.md`
11. `BROOKE_AI_INTERVIEW_PACKET.md`
12. Relevant `skills/*/SKILL.md`

## Memory Files

| File | Use |
|---|---|
| `01-agent-purpose.md` | Web Agent role and boundaries |
| `02-site-strategy.md` | Preview-site strategy and current priorities |
| `03-brand-and-ui-system.md` | Brand tokens, type, colors, and UI rules |
| `04-route-architecture.md` | Route map and gated-preview structure |
| `05-owner-preview-rules.md` | Rules for private owner-facing pages |
| `06-repo-and-deploy-operations.md` | GitHub repo setup, SSH account strategy, verification, Railway readiness, and push rules |
| `07-owner-input-workflow.md` | How to run the owner input meeting and convert answers into site updates |
| `08-owner-answer-log.md` | Durable pending/approved owner answer record for public-site blockers |
| `09-session-closeout-2026-05-10.md` | Current live preview, Railway state, Brooke handoff, and next-session start notes |
| `../BROOKE_AI_INTERVIEW_PACKET.md` | Attachment-ready AI interview packet for Brooke to clarify owner decisions without overwhelm |
| `../BROOKE_EMAIL_DRAFT.md` | Simple email draft for sending Brooke the Claude-ready interview packet |
| `inbox.md` | Open web questions |

## Current Setup Status

- Git is initialized, committed, and pushed to GitHub as `Josue-Gimbernard/Cultivate_Web`.
- The local repo uses repo-specific SSH auth for `Josue-Gimbernard` so miniBIOTA global Git credentials remain untouched.
- The current private preview is Flask-based and runs locally at `http://127.0.0.1:8080/?access=cultivate-preview`.
- The current live Railway preview is `https://web-production-dcfae.up.railway.app/?access=cultivate-preview`.
- The current preview remains private/gated and is not public launch copy.
- The current owner-facing copy is written for Brooke and should stay personal, decision-oriented, and careful around unapproved public promises.
- Latest pushed web closeout commits include `09ab2b9 Prepare Railway deployment config`, `d51d250 Fix preview access gate sizing`, `90df654 Add Brooke AI interview packet`, `c89fadf Clarify Brooke Claude handoff`, and `a991b56 Add preview link to Brooke email draft`.
- Brooke's 2026-05-20 direction is now logged in `memory/08-owner-answer-log.md` and reflected in `app.py`, the approval matrix, and the private public-draft packet.
- Current approved direction: Cultivate is a community space for homeschool families where everyone belongs; immediate CTA is a warm, no-commitment interest list.
