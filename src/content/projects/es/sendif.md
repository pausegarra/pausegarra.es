---
title: SendIf
shortDescription: Aplicación web que permite calcular la dificultad de una ruta de montaña concreta.
link: https://github.com/pausegarra/sendif
featured: false
links:
  - title: GitHub
    url: https://github.com/pausegarra/sendif
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
  - title: Website
    url: https://sendif.pausegarra.es
    className: "bg-gradient-to-r from-green-500 to-purple-500"
tech:
  - NodeJS
  - NextJS
  - Docker
features:
  - Renderizado en servidor
  - Server Actions
---

![SendIf](/sendif.png)

SendIf es una aplicación web full-stack pensada para ayudar a escaladores, senderistas y aficionados al aire libre a evaluar la dificultad de una ruta de montaña antes de salir a la aventura. La aplicación ofrece una interfaz moderna y responsive donde el usuario introduce las características de la ruta y recibe una valoración calculada a partir de varios parámetros técnicos y ambientales. Esto convierte a SendIf en una herramienta útil para planificar, valorar la seguridad y progresar en el entrenamiento, tanto en actividades recreativas como profesionales.

La plataforma está construida con foco en usabilidad, rendimiento y precisión. Desarrollada con Next.js y Node.js, aprovecha capacidades modernas del stack web, incluyendo server-side rendering (SSR) para mejorar el SEO y el tiempo de carga, así como React Server Actions para gestionar datos de forma fluida entre cliente y servidor.

Los usuarios pueden definir rutas de montaña personalizadas especificando variables como el desnivel y la longitud total. La aplicación aplica una serie de algoritmos internos para calcular un grado de dificultad coherente, similar en espíritu al grado alpino francés o a la escala UIAA, ofreciendo una estimación fiable y transparente del nivel de exigencia.

La aplicación está contenedorizada con Docker, lo que simplifica el despliegue en distintos entornos, desde desarrollo local hasta infraestructuras de producción escalables. Esta arquitectura garantiza una alta portabilidad y facilidad de mantenimiento, tanto si el servicio se autoalojó como si se despliega en la nube.

SendIf es open source y está disponible en GitHub, lo que permite a la comunidad de montaña y de desarrollo contribuir a sus algoritmos, diseño o localización. El proyecto está pensado para crecer, con posibilidad de integrar en el futuro herramientas de GPS, bases de datos de rutas o funciones colaborativas de planificación.

Los puntos clave del proyecto incluyen:
* Evaluación dinámica de rutas con un algoritmo detallado de puntuación de dificultad.
* Interfaz responsive apta para escritorio y móvil, incluso en uso de campo.
* Renderizado en servidor para mejorar rendimiento y SEO.
* Arquitectura segura y escalable basada en tecnologías modernas como Docker y Node.js.
* Modelo abierto de contribución en GitHub para fomentar feedback y mejoras de la comunidad.

Tanto si estás planificando una ascensión en solitario, coordinando una escalada en grupo o registrando ascensos completados, SendIf ayuda a aportar objetividad y estructura al análisis de rutas. Permite tomar decisiones informadas en la montaña, donde la preparación suele marcar la diferencia entre el éxito y el riesgo.
