---
name: close-web-session
description: Close a Cultivate Web session by updating durable docs, checking repo status, running verification, confirming no public commitments or deploy changes, and reporting changed files, verification, unchanged systems, unresolved questions, and pushed commit hashes.
---
# Close Web Session

Use this skill before finishing Cultivate Web work.

## Checks

1. Read changed docs/templates/CSS where practical.
2. Run `python -m compileall app.py`.
3. Run `python -m unittest discover -s tests`.
4. Run `npm.cmd run lint:colors`.
5. Run `node --check static\js\main.js`.
6. Confirm git status and do not change remotes, SSH identity, or deploy settings unless explicitly requested.
7. Confirm no public commitments, secrets, live production records, or hosting changes were made unless explicitly scoped.
8. If owner-facing copy changed, confirm it stays Brooke-centered without inventing owner story, pricing, launch dates, childcare/cafe/Foxtail commitments, paid teen work, rentals, or Wilds availability.
9. If work was pushed, record the commit hash in the final response and update durable memory when the change affects future sessions.
10. If Railway/live preview behavior changed, update `memory/06-repo-and-deploy-operations.md`, `memory/02-site-strategy.md`, and the company repo web domain docs.
11. If Brooke handoff materials changed, update `BROOKE_AI_INTERVIEW_PACKET.md`, `BROOKE_EMAIL_DRAFT.md`, and `memory/07-owner-input-workflow.md` as needed.
12. If the session produced a durable lesson, add or update a dated closeout note under `memory/`.

## Closeout Format

```markdown
Changed files:
- path

Verification:
- command/check

Not changed:
- item

Unresolved questions:
- item or "None"
```
