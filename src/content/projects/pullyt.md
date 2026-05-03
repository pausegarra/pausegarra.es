---
title: Pullyt
shortDescription: Cross-platform desktop media downloader built with Rust, Tauri, and Svelte, powered by yt-dlp and FFmpeg.
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
  - Cross-platform Desktop App
  - Media Download Automation
  - Auto-installed Dependencies
  - Clean Architecture
  - In-app Updater
---

![Pullyt](/pullyt.png)

Pullyt is a desktop application focused on making media downloads reliable, fast, and portable across operating systems. It combines a Rust backend with a Tauri shell and a Svelte frontend to deliver a native-feeling experience while keeping the application lightweight. The core goal of the project is to provide a user-friendly interface over `yt-dlp` and FFmpeg so users can download and process media without manually wiring complex command-line workflows.

The backend follows a Clean Architecture approach and is organized around a single downloader module with clear boundaries between domain, application, infrastructure, and presentation layers. This structure keeps business logic independent from platform-specific concerns and makes the codebase easier to test, evolve, and maintain as new download features or providers are added.

One of Pullyt's most practical strengths is dependency handling. If FFmpeg/FFprobe or `yt-dlp` are not available on the host system, the app can bootstrap them automatically under `~/.pullyt/`. This reduces setup friction significantly and helps ensure consistent behavior across macOS, Linux, and Windows without requiring users to prepare external tooling manually.

The project also includes release-ready packaging and update flows. It supports platform-specific installers (`.dmg`, `.exe`, `.deb`), integrates GitHub Actions for multi-OS CI, and enables the Tauri updater with signed artifacts for safe distribution. These pieces make Pullyt suitable not only as a local utility but as a production-grade desktop application that can be shipped and maintained over time.

Key aspects of the project include:
* Rust + Tauri backend architecture with a Svelte frontend for a responsive desktop UX.
* Media download and conversion pipeline powered by `yt-dlp` and FFmpeg.
* Automatic installation of required binaries under `~/.pullyt/` when missing from PATH.
* Clean Architecture module design that separates domain logic from adapters and UI commands.
* Cross-platform CI/CD and updater-ready release process with signed update artifacts.

Overall, Pullyt is a robust example of modern desktop engineering: performance from Rust, portability from Tauri, and a clean, approachable interface for everyday media workflows.
