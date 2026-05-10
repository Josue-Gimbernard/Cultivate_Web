---
title: Site Strategy
last_updated: 2026-05-10
---
# Site Strategy

## Current Mode

Private owner preview.

## Current Repo State

The web repo is initialized and pushed to `git@github.com:Josue-Gimbernard/Cultivate_Web.git`. Use `memory/06-repo-and-deploy-operations.md` before changing Git remotes, SSH auth, Railway setup, or deployment behavior.

## Current Navigation Strategy

The site now uses a tight primary tab set for the owner review:

- Preview
- Command
- Brief
- Actions
- Drafts
- Walkthrough

All other workrooms live behind the grouped `All rooms` directory and inside `/review-command-center`. The command center is the preferred hub for owner meetings because it provides the recommended review path before exposing the full route inventory.

Navigation is now data-driven from `app.py` through `PRIMARY_NAV` and `DIRECTORY_NAV`, so future route changes should update those structures instead of hand-editing header links.

The command center no longer repeats the primary start pages as ordinary cards. It now leads with the recommended owner review flow, then meeting modes, then supporting rooms.

Command-center content is also data-driven from `app.py`:

- `COMMAND_FLOW` controls the recommended owner meeting path.
- `MEETING_TRACKS` controls the short meeting-mode cards.
- `REVIEW_SURFACES` controls the supporting rooms, including the build-system workrooms.

## Guided Review Path

The main owner-review pages now include a reusable guided-review band:

1. Preview
2. Command
3. Walkthrough
4. Brief
5. Approvals
6. Actions

This is registered in `app.py` as `GUIDED_REVIEW_STEPS` and rendered through `templates/_guided_review.html`. Use this path when preparing a first owner review so the site feels like a composed sequence rather than a route catalog.

The preview homepage has been reduced to a compact hero and curated review suite. Detailed route browsing belongs in the header `All rooms` directory and `/review-command-center`.

## Public Draft Packet

The gated public-draft pages now behave as one private packet:

- Public Draft Hub
- Draft Home
- Draft About
- Draft Founding Cohort
- Draft FAQ
- Founding Family Interest

The packet is registered in `app.py` as `DRAFT_NAV` and rendered through `templates/_draft_nav.html`. The hub cards link directly to their draft pages, while every draft page shows the packet navigation and remains clearly marked private/unapproved.

Every draft packet page also includes a reusable publishing gate from `templates/_publish_gate.html`. The gate is driven by `PUBLISH_GATES` in `app.py` and tracks the items that must be resolved before public launch:

- Category language
- First offer scope
- Claim boundaries
- Operational validation
- Intake and privacy

## Approval Matrix

The approval matrix now starts with a status snapshot so owner review can begin with the big picture before reading every claim. The snapshot is built from `APPROVAL_ITEMS` through `build_approval_summaries()` in `app.py`.

Current status categories:

- Ready for owner review
- Needs confirmation
- Validate first
- Internal only
- Blocked for public

## Next Actions Board

The next-actions board now starts with an action-lane snapshot and then groups the queue by lane. The snapshot is built from `NEXT_ACTIONS` through `build_action_lane_summaries()` in `app.py`.

Current action lanes:

- Owner approval
- Validation
- Web build
- Evidence

## Owner Decisions

The owner decision dashboard now starts with a risk snapshot before the individual decision cards. The snapshot is built from `DECISIONS` through `build_decision_risk_summaries()` in `app.py`.

Current risk levels:

- Low
- Medium
- High

## Owner Input Packet

`/owner-input-packet` turns the remaining owner-dependent blockers into a meeting packet. It asks for the founder story, public category line, first-cohort audience, schedule, pricing stance, day-one space availability, high-risk future-vision handling, teen contribution boundaries, intake/privacy process, proof assets, and public CTA.

`/owner-review-prep` should be used before the owner sees the site. `/owner-meeting-script` gives facilitator language for the review itself. `/owner-review-worksheet` is the printable companion for capturing answers during the meeting. `/owner-answer-log` is the pending ledger that should be updated after the meeting. `/post-meeting-update-plan` gives the safe order for turning answers into repo changes. Use these pages after the owner walkthrough and before editing draft public pages. Owner answers should update the answer log, approval matrix, and assumptions review first.

## Safe Without Owner Completion

The remaining source-safe informational pages have been added:

- `/why-cultivate`: parent/kid/owner pain points, Cultivate response, and explicit promise boundaries.
- `/glossary`: shared definitions for brand, spaces, founding cohort, and validation-first terms.
- `/what-cultivate-is`: safe category comparison for what Cultivate is and is not.
- `/assumptions-review`: working assumptions, safe basis, current site use, and owner approval needed.

These pages do not replace owner approval. They complete the informational layer that can responsibly be filled without inventing founder story, pricing, schedule, final naming, intake rules, or operating commitments.

## Goal

Show Cultivate as a complete, warm, professional ecosystem:

- full vision visible
- first launch path grounded
- brand consistent
- no unapproved public commitments

## Current Recommendation

Lead with the ecosystem and founding cohort direction. Keep childcare, cafe, Foxtail, paid teen work, public rentals, and full outdoor campus as vision/validation items unless approved.

## Current Rich Preview Surfaces

- `/review-command-center`: front-door dashboard for choosing the right owner-review surface.
- `/owner-brief`: compact owner-facing summary of the concept, first move, holdbacks, and next approval.
- `/next-actions`: practical work queue for approvals, validation, web drafts, and evidence artifacts.
- `/day-at-cultivate`: narrative day-in-the-life page that makes the experience tangible.
- `/spaces`: deep panels for each named component, including feeling, first version, future version, and dependencies.
- `/brand-voice`: approved/avoid phrase guidance and voice samples for safe, warm copy.
- `/membership-model`: internal offer-bucket visualizer with pricing caveats.
- `/family-journey`: private journey map from discovery to belonging and growth.
- `/launch-roadmap`: phase-based build sequence from owner review through validation, cohort, and expansion.
- `/faq-lab`: private concern-response patterns for sensitive public questions.
- `/source-evidence`: traceability room connecting site claims to source docs and owner checks.
- `/public-draft-hub`: private planning hub for future public pages and hold conditions.
- `/draft-home`: private unapproved homepage draft showing possible public direction.
- `/draft-about`: private unapproved About page draft for origin story and village model.
- `/draft-cohort`: private unapproved Founding Cohort page draft for first-offer framing.
- `/draft-faq`: private unapproved FAQ draft derived from concern-response patterns.
- `/approval-matrix`: approval gate for deciding which claims are ready, internal, validation-first, or blocked for public.
- `/founding-family-interest`: private draft of an interest page with disabled form fields and no data collection.
- `/owner-decisions`: meeting-ready dashboard of key decisions, recommendations, risk, and unlocks.
- `/owner-review-prep`: pre-meeting checklist for access, flow, decision tools, and promise boundaries.
- `/owner-meeting-script`: facilitator script for what to say, show, capture, and avoid during owner review.
- `/owner-input-packet`: meeting packet for collecting owner-only answers before public copy changes.
- `/owner-review-worksheet`: printable answer tracker for marking approved, revise, hold, or validate during owner review.
- `/owner-answer-log`: pending/approved answer ledger that bridges owner notes to site updates.
- `/post-meeting-update-plan`: ordered update plan for turning owner answers into safe repo changes.
- `/owner-walkthrough`: guided presentation flow with focus mode and speaker notes for reviewing the concept with the owner.
- `/ecosystem-map`: click-through map of spaces, dependencies, and phases.
- `/founding-cohort`: recommended first safe launch shape.
- `/cohort-blueprint`: operational first-term rhythm across teens, middle kids, parents, and evidence.
- `/impact-signals`: dashboard of what to measure during the first cohort to guide next decisions.
- `/launch-readiness`: dashboard separating ready-to-show, ready-to-shape, validate-first, and future-build items.
