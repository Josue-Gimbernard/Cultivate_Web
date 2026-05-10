# Close Web Session

Use this skill before finishing Cultivate Web work.

## Checks

1. Read changed docs/templates/CSS where practical.
2. Run `python -m compileall app.py`.
3. Run `python -m unittest discover -s tests`.
4. Run `npm run lint:colors` when CSS changed.
5. Confirm git was not initialized unless explicitly requested.
6. Confirm no public commitments, secrets, live production records, or hosting changes were made unless explicitly scoped.

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

