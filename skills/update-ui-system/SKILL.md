# Update UI System

Use this skill when changing Cultivate Web brand tokens, components, UI kitchen sink, or repeated visual patterns.

## Required Context

- `memory/03-brand-and-ui-system.md`
- `templates/ui_kitchen_sink.html`
- `static/css/design-tokens.css`
- relevant files under `static/css/components/`

## Rules

- Use source-derived colors and type unless the founder approves a change.
- Put reusable styles in components before page-specific CSS.
- Keep cards to repeated items, modals, or framed tools.
- Do not make the page feel like generic SaaS or generic daycare branding.
- Run `npm run lint:colors` after CSS color changes.

