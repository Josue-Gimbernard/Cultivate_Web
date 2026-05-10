---
title: Cultivate Web Memory Index
last_updated: 2026-05-10
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
10. `BROOKE_AI_INTERVIEW_PACKET.md`
11. Relevant `skills/*/SKILL.md`

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
| `../BROOKE_AI_INTERVIEW_PACKET.md` | Attachment-ready AI interview packet for Brooke to clarify owner decisions without overwhelm |
| `inbox.md` | Open web questions |

## Current Setup Status

- Git is initialized, committed, and pushed to GitHub as `Josue-Gimbernard/Cultivate_Web`.
- The local repo uses repo-specific SSH auth for `Josue-Gimbernard` so miniBIOTA global Git credentials remain untouched.
- The current private preview is Flask-based and runs locally at `http://127.0.0.1:8080/?access=cultivate-preview`.
- The current preview remains private/gated and is not public launch copy.
- The current owner-facing copy is written for Brooke and should stay personal, decision-oriented, and careful around unapproved public promises.
- Latest pushed web closeout commits: `756b08b Personalize owner preview copy for Brooke` and `fcd44f0 Refine Brooke owner preview copy`.
