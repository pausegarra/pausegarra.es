---
title: Volchik & Cheburashka
shortDescription: Web bilingüe de relatos ilustrados en español y ruso, construida con Astro y content collections.
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
  - Home pages localizadas para español y ruso
  - Redirección desde la raíz según el idioma del navegador
  - Páginas de relatos renderizadas desde Markdown
  - Metadatos SEO localizados y soporte `hreflang`
  - Generación de sitemap con `@astrojs/sitemap`
---

![Volchik & Cheburashka](/volchik-cheburashka.png)

Volchik & Cheburashka es una web bilingüe de relatos ilustrados pensada para publicar historias breves y emocionales en español y ruso mediante un pipeline estático y limpio. El proyecto prioriza la entrega de contenido: cada relato se escribe en Markdown, se renderiza con Astro content collections y se expone mediante rutas localizadas, de forma que el mismo flujo editorial pueda soportar dos idiomas sin duplicar la lógica de la aplicación.

El sitio sirve home pages dedicadas para `/es` y `/ru`, y la ruta raíz redirige automáticamente a los visitantes según el idioma del navegador. Eso mantiene la experiencia de entrada sencilla para los lectores y al mismo tiempo preserva rutas explícitas por locale para buscadores y compartición. El resultado es un sitio internacionalizado pequeño pero bien estructurado, que se comporta de forma predecible en ambos idiomas.

Desde el punto de vista técnico, el stack es intencionalmente ligero. Astro se encarga del renderizado y el routing, Tailwind CSS 4 aporta el styling y TypeScript mantiene la implementación explícita y mantenible. Las content collections alimentan las páginas de historias, lo que hace que el modelo de contenido sea fácil de extender a medida que se añadan nuevos relatos ilustrados. El sitio también incluye metadatos SEO localizados, URLs canónicas, tags `hreflang`, datos de Open Graph, Twitter cards y un sitemap generado para mejorar la descubribilidad.

La identidad visual del proyecto se apoya en ilustraciones cálidas de estilo cuento y en un layout editorial suave. Esa combinación le da al sitio un tono emocional fuerte sin complicar la navegación: el contenido es el protagonista, el selector de idioma siempre está visible y el índice de relatos se mantiene lo bastante ligero como para funcionar bien en móvil y escritorio.

Este proyecto es un buen ejemplo de cómo un sitio estático puede seguir sintiéndose dinámico cuando el modelo de contenido, la localización y el SEO se diseñan juntos desde el principio. Está construido para ser fácil de mantener, fácil de ampliar y fácil de indexar.
