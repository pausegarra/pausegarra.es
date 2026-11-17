---
title: AI Factory
shortDescription: Local GitHub automation through visual workflows and CLI agents, built with Tauri 2, Rust and React.
link: https://github.com/pausegarra/ai-factory
featured: true
links:
  - title: GitHub
    url: https://github.com/pausegarra/ai-factory
    className: "button-secondary"
tech:
  - Tauri 2
  - Rust
  - React
  - React Flow
  - Tailwind CSS
features:
  - Local CLI agent execution
  - Visual workflow editing
  - Four GitHub triggers
  - GitHub tokens per account
  - Run history and persistent artifacts
---

![Conceptual illustration of local GitHub automation with connected workflows and AI agents](/ai-factory.png)

AI Factory is a desktop application for coordinating GitHub automation through visual workflows and CLI agents running on the local computer. It brings repository events, task dependencies and execution history into one place, with an English interface and a dark theme.

The workflow editor uses React Flow to connect steps and define their dependencies. Each step can select an installed agent such as Codex or OpenCode, configure its model and prompt, and describe the expected result. Workflows respond to four GitHub triggers: new issues, approved pull requests, review requests and release issues.

GitHub integration uses the REST API with tokens configured per account. Profiles define which owners, authors and reviewers each account can work with. Agent CLI processes execute locally, while GitHub operations use the corresponding account token. The desktop application does not require the GitHub CLI or Python.

Tauri 2 and Rust provide the desktop shell and execution engine, while React, React Flow and Tailwind CSS power the interface. Run history keeps step states, logs and structured results available, and declared artifacts remain in persistent project memory after temporary workspaces are cleaned up.

The project combines a visual way to organize development tasks with explicit dependencies and traceable local execution. Its GitHub repository contains the full setup instructions and operational details.
