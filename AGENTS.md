# AGENTS.md

## Stack
- Astro 5.x (Vite-based, not webpack)
- Tailwind CSS 4.x via `@tailwindcss/vite` (not the old `@astrojs/tailwind`)
- Content: Astro content collections with Zod schemas in `src/content.config.ts`
- Icons: `astro-icon` with `@iconify-json/material-symbols`, `devicon`, `entypo-social`
- `skills-lock.json` tracks skill sources

## Dev commands
```sh
yarn dev      # localhost:4321
yarn build    # output to dist/
yarn preview  # preview build
yarn astro add <integration>  # add Astro integrations
yarn astro check  # type-check
```

No lint/typecheck/test scripts configured. Run `astro check` for type-checking.

## Architecture
- Pages: `src/pages/`
- Components: `src/compoents/` (note: "compoents" is intentional typo in this repo)
- Content collections: `src/content/projects/{en,es}/*.md`
- Global CSS: `src/styles/global.css`
- Layout: `src/layouts/Layout.astro` (contains all SEO meta, OG tags, JSON-LD schema)
- Shared locale data: `src/lib/i18n.ts`
- Locale redirects and browser language detection: `src/lib/browser-locale.ts`

## Content collections
Projects use a single `projects` collection with locale-prefixed slugs such as `en/...` and `es/...`. Keep the same markdown structure in each locale folder and translate the body/frontmatter copy per locale.

## Internationalization
- Supported locales: `en`, `es`
- Default locale: `en`
- Fallback locale for unsupported browser languages: `en`
- Routes are prefixed by locale, including the default locale.
- `/`, `/projects/`, and old project URLs act as browser-based redirects; localized pages live under `src/pages/en/` and `src/pages/es/`.
- Language selector lives in the header and must stay data-driven so more locales can be added without rewriting the UI.

## Tailwind
Tailwind 4 uses CSS-first config via `@import "tailwindcss"` in `global.css`. `tailwind.config.mjs` only adds the typography plugin.
