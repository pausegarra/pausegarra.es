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

The fixture records the pre-restyling semantic baseline. Do not regenerate it after presentation changes. The suite checks localized routes, content, links, metadata, images, navigation and transition wiring. It does not measure rendered layout or execute browser navigation. No dev server is required.

The project image suite checks all eight local PNG assets, their replacement against the original hashes, full image decoding, and their references in the sixteen localized detail pages. The original fixture stays unchanged: the preservation suite permits only these eight image replacements and still protects every other recorded file and page contract. Outside project details, image src/alt pairs must match the unchanged fixture, preserving the existing home portraits and rejecting added images, including all eight project assets. Build before running both suites. These checks do not start a server or measure browser layout.

Project illustrations are optimized derivatives of archived ImageGen originals. Each locally served PNG has a transfer budget of 128 KiB, a minimum resolution of 960 × 640, an opaque background and the original 3:2 aspect ratio. The suite rejects oversized downloads, invalid images and duplicate pixels. Generation originals and optimization provenance belong in delivery evidence, outside `public/`; production build assets must match the optimized files in `public/`.
