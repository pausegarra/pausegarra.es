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
- Content collections: `src/content/projects/*.md`
- Global CSS: `src/styles/global.css`
- Layout: `src/layouts/Layout.astro` (contains all SEO meta, OG tags, JSON-LD schema)

## Content collections
Projects use a `projects` collection with schema: `title`, `shortDescription`, `tech[]`, `features[]`, `link`, `featured`, `links[]`.

## Tailwind
Tailwind 4 uses CSS-first config via `@import "tailwindcss"` in `global.css`. `tailwind.config.mjs` only adds the typography plugin.