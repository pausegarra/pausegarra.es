---
title: Pullyt
shortDescription: Descargador de medios de escritorio multiplataforma construido con Rust, Tauri y Svelte, impulsado por yt-dlp y FFmpeg.
link: https://github.com/pausegarra/pullyt
featured: true
links:
  - title: GitHub
    url: https://github.com/pausegarra/pullyt
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
tech:
  - Rust
  - Tauri
  - Svelte
  - yt-dlp
  - FFmpeg
  - GitHub Actions
features:
  - Aplicación de escritorio multiplataforma
  - Automatización de descargas multimedia
  - Dependencias autoinstaladas
  - Arquitectura limpia
  - Actualizador integrado
---

![Pullyt](/pullyt.png)

Pullyt es una aplicación de escritorio centrada en hacer que las descargas multimedia sean fiables, rápidas y portables entre sistemas operativos. Combina un backend en Rust con una capa Tauri y un frontend en Svelte para ofrecer una experiencia con aspecto nativo sin perder ligereza. El objetivo principal del proyecto es proporcionar una interfaz amigable sobre `yt-dlp` y FFmpeg para que los usuarios puedan descargar y procesar contenido sin montar manualmente flujos complejos de línea de comandos.

El backend sigue un enfoque de Clean Architecture y se organiza alrededor de un único módulo de descarga con límites claros entre las capas de dominio, aplicación, infraestructura y presentación. Esta estructura mantiene la lógica de negocio independiente de las particularidades de la plataforma y hace que el codebase sea más fácil de probar, evolucionar y mantener a medida que se añaden nuevas funciones o proveedores de descarga.

Una de las fortalezas más prácticas de Pullyt es la gestión de dependencias. Si FFmpeg/FFprobe o `yt-dlp` no están disponibles en el sistema anfitrión, la app puede instalarlos automáticamente en `~/.pullyt/`. Esto reduce muchísimo la fricción de setup y ayuda a garantizar un comportamiento consistente en macOS, Linux y Windows sin obligar al usuario a preparar herramientas externas manualmente.

El proyecto también incluye empaquetado listo para releases y flujos de actualización. Soporta instaladores específicos por plataforma (`.dmg`, `.exe`, `.deb`), integra GitHub Actions para CI multiplataforma y habilita el updater de Tauri con artefactos firmados para una distribución segura. Todo esto convierte a Pullyt no solo en una utilidad local, sino en una aplicación de escritorio de nivel producción que puede distribuirse y mantenerse en el tiempo.

Los puntos clave del proyecto incluyen:
* Arquitectura backend con Rust + Tauri y frontend en Svelte para una UX de escritorio responsive.
* Pipeline de descarga y conversión multimedia impulsado por `yt-dlp` y FFmpeg.
* Instalación automática de binarios necesarios en `~/.pullyt/` cuando faltan en el PATH.
* Diseño de módulo con Clean Architecture que separa la lógica de dominio de los adaptadores y comandos de UI.
* CI/CD multiplataforma y proceso de release preparado para updater con artefactos de actualización firmados.

En conjunto, Pullyt es un ejemplo sólido de ingeniería moderna de escritorio: rendimiento de Rust, portabilidad de Tauri y una interfaz limpia y accesible para flujos cotidianos de trabajo con multimedia.
