---
title: Route Architecture
last_updated: 2026-05-10
---
# Route Architecture

## Routes

| Route | Purpose | Access |
|---|---|---|
| `/` | Owner preview home | gated |
| `/owner-preview` | Same as home | gated |
| `/review-command-center` | Front-door dashboard for owner-review navigation | gated |
| `/owner-brief` | Compact owner-facing private summary | gated |
| `/next-actions` | Private approvals, validation, web build, and evidence work queue | gated |
| `/day-at-cultivate` | Narrative day-in-the-life owner preview | gated |
| `/spaces` | Detailed space panels with launch stance and dependencies | gated |
| `/brand-voice` | Brand voice, phrase guardrails, and copy safety lab | gated |
| `/membership-model` | Internal offer bucket and revenue model visualizer | gated |
| `/family-journey` | Private family journey map from discovery to belonging and growth | gated |
| `/launch-roadmap` | Private phase-based roadmap from owner review to expansion decisions | gated |
| `/faq-lab` | Private FAQ and concern-response safety lab | gated |
| `/source-evidence` | Private source traceability and owner-check room | gated |
| `/why-cultivate` | Source-safe family pain point and credibility layer | gated |
| `/glossary` | Shared private-preview terminology and naming guardrails | gated |
| `/what-cultivate-is` | Safe category comparison for what Cultivate is and is not | gated |
| `/assumptions-review` | Working assumptions, source basis, current use, and owner approval needs | gated |
| `/public-draft-hub` | Private hub for future public page drafts and hold conditions | gated |
| `/draft-home` | Private unapproved public-homepage draft | gated |
| `/draft-about` | Private unapproved public About page draft | gated |
| `/draft-cohort` | Private unapproved public Founding Cohort page draft | gated |
| `/draft-faq` | Private unapproved public FAQ draft | gated |
| `/approval-matrix` | Private publishing-approval gate for sensitive claims | gated |
| `/founding-family-interest` | Disabled private draft of a family interest page | gated |
| `/owner-decisions` | Owner decision dashboard for next approvals | gated |
| `/owner-review-prep` | Pre-meeting checklist for owner review readiness | gated |
| `/owner-input-packet` | Owner-only question packet for public-copy blockers | gated |
| `/owner-review-worksheet` | Printable owner answer tracker for review meetings | gated |
| `/owner-answer-log` | Pending/approved owner answer ledger for public-site blockers | gated |
| `/post-meeting-update-plan` | Ordered plan for converting owner answers into repo updates | gated |
| `/owner-walkthrough` | Guided private presentation flow with focus mode and speaker notes | gated |
| `/ecosystem-map` | Interactive source-derived ecosystem map | gated |
| `/founding-cohort` | Recommended first-launch package | gated |
| `/cohort-blueprint` | Private operational first-term blueprint | gated |
| `/impact-signals` | Private first-cohort evidence and measurement dashboard | gated |
| `/launch-readiness` | Validation and promise-boundary dashboard | gated |
| `/ui-kitchen-sink` | Design system surface | gated |
| `/ux-lab` | Interaction and experience lab | gated |
| `/healthz` | Railway health check | public |

## Access

Routes are private by default. Use `?access=cultivate-preview` locally, or set `CULTIVATE_PREVIEW_ACCESS_CODE`.

## Navigation

The global header intentionally shows only the primary review tabs: Preview, Command, Brief, Actions, Drafts, and Walkthrough. Detailed experience, planning, safety, and build-system routes remain available through the `All rooms` directory and the `/review-command-center` route.

Header navigation is registered in `app.py`:

- `PRIMARY_NAV` controls the visible review tabs.
- `DIRECTORY_NAV` controls the grouped `All rooms` panel.
- `COMMAND_FLOW` controls the recommended owner meeting path on `/review-command-center`.
- `MEETING_TRACKS` controls the owner meeting-mode cards.
- `GUIDED_REVIEW_STEPS` controls the reusable bottom-of-page review path.
- `DRAFT_NAV` controls the reusable public-draft packet navigation.
- `PUBLISH_GATES` controls the reusable publishing-gate cards shown on draft packet pages.
- `APPROVAL_ITEMS` controls the approval matrix, and `build_approval_summaries()` derives the status snapshot shown above the full matrix.
- `NEXT_ACTIONS` controls the next-actions board, and `build_action_lane_summaries()` derives the lane snapshot shown above the grouped queues.
- `DECISIONS` controls the owner decision dashboard, and `build_decision_risk_summaries()` derives the risk snapshot shown above the individual decision cards.
- `PAIN_POINTS`, `GLOSSARY_TERMS`, `COMPARISON_ITEMS`, and `ASSUMPTION_ITEMS` control the safe-without-owner informational support pages.
- `OWNER_INPUT_ITEMS` controls the owner input packet questions and their supporting routes.
- `POST_MEETING_UPDATES` controls the ordered post-meeting update plan.
- `OWNER_REVIEW_PREP_ITEMS` controls the pre-meeting readiness checklist.
- `REVIEW_SURFACES` controls supporting owner-review rooms, while the start pages are handled by the curated review flow instead of duplicated as cards.

`templates/_guided_review.html` appears on the primary owner-review sequence: `/owner-preview`, `/review-command-center`, `/owner-walkthrough`, `/owner-brief`, `/approval-matrix`, and `/next-actions`.

`templates/_draft_nav.html` appears on `/public-draft-hub`, `/draft-home`, `/draft-about`, `/draft-cohort`, `/draft-faq`, and `/founding-family-interest`.

`templates/_publish_gate.html` appears on the same draft packet routes and should remain the final public-readiness reminder until publishing is approved.
