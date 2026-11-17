# pausegarra.com

Personal portfolio of [Pau Segarra](https://pausegarra.com), Backend Software Engineer specializing in scalable microservices, APIs, and cloud infrastructure.

## Stack

- **Framework**: [Astro](https://astro.build) 5.x with View Transitions
- **Styling**: [Tailwind CSS](https://tailwindcss.com) 4.x via `@tailwindcss/vite`
- **Icons**: [astro-icon](https://github.com/nicoBretz/astro-icon) with [Iconify](https://iconify.design/)
- **Content**: Astro content collections with Zod schema validation

## Project Structure

```
/
├── src/
│   ├── compoents/          # Astro components (atoms, molecules, organisms)
│   ├── content/
│   │   └── projects/       # Project markdown files with Zod schema
│   ├── content.config.ts   # Content collection definitions
│   ├── layouts/
│   │   └── Layout.astro    # Base layout with SEO, OG tags, JSON-LD
│   ├── lib/
│   │   └── swiper.js       # Swiper carousel initialization
│   ├── pages/
│   │   └── index.astro     # Homepage
│   └── styles/
│       └── global.css      # Tailwind imports and global styles
├── public/                 # Static assets
├── astro.config.mjs
└── package.json
```

## Commands

| Command          | Action                                    |
| :--------------- | :---------------------------------------- |
| `yarn dev`       | Start dev server at `localhost:4321`      |
| `yarn build`     | Build production site to `./dist/`       |
| `yarn preview`   | Preview build locally                     |
| `yarn astro add` | Add Astro integrations                    |
| `yarn astro check`| Run TypeScript type checking             |

## Development

```sh
yarn install
yarn dev
```

## Content Collections

Projects are defined in `src/content/projects/*.md` with the schema:

```ts
{
  title: string;
  shortDescription: string;
  tech: string[];
  features: string[];
  link: string | null;
  featured: boolean;
  links: { title, url, className }[];
}
```

## SEO

The site includes:
- Sitemap generation (`@astrojs/sitemap`)
- Open Graph and Twitter meta tags
- JSON-LD structured data (WebSite + Person schema)
- Canonical URLs and hreflang tags

## Headless verification

Run from the repository root with dependencies installed:

    yarn astro check
    yarn build
    python3 tests/project_images_contract_test.py -v
    python3 tests/restyling_contract_test.py -v
    python3 tests/ai_factory_contract_test.py -v

The fixture records the pre-restyling semantic baseline. Do not regenerate it after presentation changes. The suite checks localized routes, content, links, metadata, images, navigation and transition wiring. It does not measure rendered layout or execute browser navigation. No dev server is required.

The project image suite checks nine local PNG assets and their eighteen localized detail references. The eight historical illustrations must still differ from their original hashes. All nine images must decode, remain opaque, have distinct pixels, preserve a 3:2 aspect ratio with a minimum resolution of 960 × 640, and stay within a 128 KiB transfer budget.

The original pre-restyling fixture remains unchanged. Preservation permits only the eight historical image replacements, the two localized AI Factory entries, its shared PNG and the exact featured-flag change in both Pullyt entries. The build must contain the thirty historical HTML routes plus AI Factory's two localized details and language redirect. Homepages replace the Pullyt card with AI Factory while preserving the other featured projects, content, metadata and portrait images. Catalogues retain both projects. Project illustrations remain restricted to detail pages.

The AI Factory contract checks localized metadata and copy, the featured swap, catalogue membership, GitHub links, shared image, language links and the generated redirect. Build before running all three suites. These are code-level checks; they do not launch a server, execute browser navigation or measure rendered layout.

Project illustrations are optimized derivatives of archived ImageGen originals. Generation originals, prompts and optimization provenance belong in delivery evidence outside public/. Production build assets must match the optimized files in public/.
