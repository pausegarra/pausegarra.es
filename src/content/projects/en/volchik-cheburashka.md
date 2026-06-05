---
title: Volchik & Cheburashka
shortDescription: A bilingual Spanish/Russian illustrated story website built with Astro and content collections.
link: https://volchikcheburashka.com/
featured: true
links:
  - title: GitHub
    url: https://github.com/pausegarra/volchik-cheburashka
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
  - title: Website
    url: https://volchikcheburashka.com/
    className: "bg-gradient-to-r from-green-500 to-purple-500"
tech:
  - Astro 6
  - Tailwind CSS 4
  - TypeScript
  - Content Collections
  - Node.js
features:
  - Localized home pages for Spanish and Russian
  - Browser-language redirect from the root route
  - Story pages rendered from Markdown content
  - Localized SEO metadata and hreflang support
  - Sitemap generation with `@astrojs/sitemap`
---

![Volchik & Cheburashka](/volchik-cheburashka.png)

Volchik & Cheburashka is a bilingual illustrated story website designed to deliver short emotional stories in Spanish and Russian through a clean static publishing pipeline. The project focuses on content delivery first: each story is written in Markdown, rendered through Astro content collections, and exposed through localized routes so the same editorial workflow can support two languages without duplicating the application logic.

The site serves dedicated home pages for `/es` and `/ru`, with the root path automatically redirecting visitors based on browser language. That keeps the entry experience simple for readers while preserving explicit locale routes for search engines and sharing. The result is a small but well-structured internationalized site that behaves predictably in both languages.

From a technical standpoint, the stack is intentionally lean. Astro handles the rendering and routing, Tailwind CSS 4 provides styling, and TypeScript keeps the implementation explicit and maintainable. Content collections drive the story pages, which makes the content model easy to extend as new illustrated posts are added. The site also includes localized SEO metadata, canonical URLs, hreflang tags, Open Graph data, Twitter cards, and a generated sitemap to support discoverability.

The visual identity of the project is driven by warm, storybook-style illustrations and a soft editorial layout. That combination gives the site a strong emotional tone while keeping navigation straightforward: the content is the focus, the language switcher is always visible, and the story index stays lightweight enough to work well on mobile and desktop.

This project is a good example of how a static site can still feel dynamic when the content model, localization, and SEO are designed together from the start. It is built to be easy to maintain, easy to extend, and easy to index.
