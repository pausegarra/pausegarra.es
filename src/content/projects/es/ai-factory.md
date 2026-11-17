---
title: AI Factory
shortDescription: Automatización local de GitHub mediante flujos visuales y agentes CLI, construida con Tauri 2, Rust y React.
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
  - Ejecución local de agentes CLI
  - Edición visual de flujos
  - Cuatro disparadores de GitHub
  - Tokens de GitHub por cuenta
  - Historial y artefactos persistentes
---

![Ilustración conceptual de automatización local de GitHub con flujos conectados y agentes de IA](/ai-factory.png)

AI Factory es una aplicación de escritorio para coordinar la automatización de GitHub mediante flujos visuales y agentes CLI que se ejecutan en el equipo local. Reúne los eventos de los repositorios, las dependencias entre tareas y el historial de ejecución en un mismo lugar, con interfaz en inglés y tema oscuro.

El editor de flujos utiliza React Flow para conectar pasos y definir sus dependencias. Cada paso permite seleccionar un agente instalado, como Codex u OpenCode, configurar su modelo y prompt, y describir el resultado esperado. Los flujos responden a cuatro disparadores de GitHub: nuevas issues, pull requests aprobadas, solicitudes de revisión e issues de publicación de releases.

La integración con GitHub utiliza la API REST con tokens configurados por cuenta. Los perfiles definen los propietarios, autores y revisores con los que puede trabajar cada cuenta. Los procesos de los agentes CLI se ejecutan localmente y las operaciones de GitHub utilizan el token de la cuenta correspondiente. La aplicación de escritorio no necesita la CLI de GitHub ni Python.

Tauri 2 y Rust proporcionan la aplicación de escritorio y el motor de ejecución, mientras que React, React Flow y Tailwind CSS componen la interfaz. El historial conserva los estados de los pasos, los logs y los resultados estructurados, y los artefactos declarados permanecen en la memoria persistente del proyecto tras limpiar los espacios de trabajo temporales.

El proyecto combina una forma visual de organizar tareas de desarrollo con dependencias explícitas y ejecución local trazable. Su repositorio de GitHub reúne las instrucciones completas de puesta en marcha y los detalles de funcionamiento.
