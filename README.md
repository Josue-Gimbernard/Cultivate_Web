# Cultivate Web

Private preview website and Railway-ready Flask app for Cultivate.

This repo owns the web experience, UI system, owner preview, UI kitchen sink, UX lab, and web-specific agent memory for the Cultivate brand.

Repo, GitHub, SSH account, verification, and Railway-readiness rules live in `memory/06-repo-and-deploy-operations.md`.

## Start

```powershell
python app.py
```

Then open:

- `http://127.0.0.1:8080/?access=cultivate-preview`
- `http://127.0.0.1:8080/review-command-center?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-brief?access=cultivate-preview`
- `http://127.0.0.1:8080/next-actions?access=cultivate-preview`
- `http://127.0.0.1:8080/public-draft-hub?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-walkthrough?access=cultivate-preview`

The header keeps those primary review tabs visible. Deeper rooms are grouped under `All rooms` and organized through the command center.

The guided owner-review path is:

`Preview -> Command -> Walkthrough -> Brief -> Approvals -> Actions`

The gated public-draft packet is:

`Draft Hub -> Home -> About -> Cohort -> FAQ -> Interest`

Each draft packet page includes a publishing gate for category language, first offer scope, claim boundaries, operational validation, and intake/privacy.

The approval matrix includes a status snapshot before the full claim table so owner review can start with what is ready, blocked, internal, or validation-first.

The next-actions board includes lane summaries for owner approval, validation, web build, and evidence work before the grouped action queues.

The owner decisions dashboard includes a risk snapshot before the individual decision cards.

The owner input packet turns the remaining owner-dependent blockers into meeting questions:

- `http://127.0.0.1:8080/owner-input-packet?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-review-worksheet?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-answer-log?access=cultivate-preview`
- `http://127.0.0.1:8080/post-meeting-update-plan?access=cultivate-preview`

The safe-without-owner informational layer is complete:

- `http://127.0.0.1:8080/why-cultivate?access=cultivate-preview`
- `http://127.0.0.1:8080/glossary?access=cultivate-preview`
- `http://127.0.0.1:8080/what-cultivate-is?access=cultivate-preview`
- `http://127.0.0.1:8080/assumptions-review?access=cultivate-preview`

Additional private rooms:

- `http://127.0.0.1:8080/day-at-cultivate?access=cultivate-preview`
- `http://127.0.0.1:8080/spaces?access=cultivate-preview`
- `http://127.0.0.1:8080/brand-voice?access=cultivate-preview`
- `http://127.0.0.1:8080/membership-model?access=cultivate-preview`
- `http://127.0.0.1:8080/family-journey?access=cultivate-preview`
- `http://127.0.0.1:8080/launch-roadmap?access=cultivate-preview`
- `http://127.0.0.1:8080/faq-lab?access=cultivate-preview`
- `http://127.0.0.1:8080/source-evidence?access=cultivate-preview`
- `http://127.0.0.1:8080/draft-home?access=cultivate-preview`
- `http://127.0.0.1:8080/draft-about?access=cultivate-preview`
- `http://127.0.0.1:8080/draft-cohort?access=cultivate-preview`
- `http://127.0.0.1:8080/draft-faq?access=cultivate-preview`
- `http://127.0.0.1:8080/approval-matrix?access=cultivate-preview`
- `http://127.0.0.1:8080/founding-family-interest?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-decisions?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-input-packet?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-review-worksheet?access=cultivate-preview`
- `http://127.0.0.1:8080/owner-answer-log?access=cultivate-preview`
- `http://127.0.0.1:8080/post-meeting-update-plan?access=cultivate-preview`
- `http://127.0.0.1:8080/ecosystem-map?access=cultivate-preview`
- `http://127.0.0.1:8080/founding-cohort?access=cultivate-preview`
- `http://127.0.0.1:8080/cohort-blueprint?access=cultivate-preview`
- `http://127.0.0.1:8080/impact-signals?access=cultivate-preview`
- `http://127.0.0.1:8080/launch-readiness?access=cultivate-preview`
- `http://127.0.0.1:8080/ui-kitchen-sink?access=cultivate-preview`
- `http://127.0.0.1:8080/ux-lab?access=cultivate-preview`

## Current Mode

This is a private owner-preview site. It is not public launch copy.

The first job is to make the concept feel real, coherent, and impressive while keeping regulated or unapproved claims clearly out of public commitment territory.

## Brand Reference

Brand cues come from the Cultivate source docs in `M:\Cultivate\docs\source`:

- Display type: Georgia
- Body/system type: Calibri fallback stack
- Deep teal: `#2A7D6F`
- Clay: `#C4622D`
- Soft mint: `#E8F5F2`
- Warm cream: `#FDF6F0`
- Garden green: `#E8F5E9`
