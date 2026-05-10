---
name: review-owner-preview
description: Review and change the Cultivate private owner preview, especially Brooke-facing copy, owner-review routes, approval boundaries, and public-promise safety. Use when working on owner preview pages, owner review packet, owner input workflow, approval matrix, or copy that could imply launch, pricing, childcare, cafe, Foxtail, paid teen work, rentals, or Wilds commitments.
---
# Review Owner Preview

Use this skill when changing the private owner preview.

## Required Context

- `memory/02-site-strategy.md`
- `memory/05-owner-preview-rules.md`
- `memory/07-owner-input-workflow.md`
- `memory/08-owner-answer-log.md`
- `M:\Cultivate\domains\company\current_recommendations.md`
- `M:\Cultivate\domains\product\founding_cohort_launch_plan.md`

## Rules

- Make the page feel polished and real.
- Keep full vision visible.
- Keep first-launch recommendation grounded.
- Write for Brooke directly enough that the review feels made for her, but do not repeat her name so often that the copy feels mechanical.
- Make owner-facing copy decision-oriented: what Brooke should feel, approve, revise, hold, validate, or answer next.
- Do not imply unvalidated childcare, cafe, Foxtail, paid teen work, public rental, pricing, or launch-date commitments.
- Do not invent Brooke's founder story, pricing, schedule, proof assets, operating commitments, or public claims.
- Keep route gated unless the user explicitly asks for public mode.

## Current Owner Review Flow

Use `/owner-review-packet` as the entry point for a full session:

1. `/owner-review-prep`
2. `/owner-meeting-script`
3. `/owner-walkthrough`
4. `/owner-input-packet`
5. `/owner-review-worksheet`
6. `/owner-meeting-recap`
7. `/owner-answer-log`
8. `/post-meeting-update-plan`
9. `/approval-matrix`
10. `/next-actions`

## Verification

- For copy-only preview changes, run `python -m unittest discover -s tests`.
- For app data or route changes, also run `python -m compileall app.py`, `node --check static\js\main.js`, and `npm.cmd run lint:colors`.
- Live-check the changed route at `http://127.0.0.1:8080/<route>?access=cultivate-preview` when the local server is running.
