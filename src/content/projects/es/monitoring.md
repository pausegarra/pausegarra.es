---
title: Monitoring
shortDescription: Stack de observabilidad contenedorizado construido alrededor de Prometheus, Grafana, Loki y Alloy.
link: null
featured: false
links:
  - title: GitHub
    url: https://github.com/pausegarra/monitoring
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
tech:
  - Docker
  - Prometheus
  - Grafana
  - Loki
  - Alloy
  - GitHub Actions
features:
  - Recolección de métricas
  - Ingesta de logs
  - Pipeline OTLP
  - Provisionamiento de dashboards
  - Alertas
---

![Monitoring](/monitoring.png)

Monitoring es un stack de observabilidad orientado a producción, diseñado para centralizar métricas, logs, dashboards y alertas en un único despliegue contenedorizado. El proyecto combina Grafana, Prometheus, Loki y Alloy para ofrecer una plataforma de monitorización coherente, fácil de ejecutar en local y sencilla de llevar a producción. Está pensado para equipos que quieren una base autoalojada para la observabilidad de infraestructura y aplicaciones sin tener que montar cada pieza desde cero.

En el centro del stack, Grafana se entrega mediante una imagen personalizada con datasources, dashboards y recursos de alertado ya provisionados. Esto hace que el entorno sea reproducible y elimina la configuración manual después del despliegue. Prometheus se encarga del scraping de métricas a través de un archivo de configuración dedicado, mientras que Loki almacena los logs y los expone dentro de Grafana junto a los dashboards de métricas.

La ruta de ingesta de logs está construida alrededor de Alloy como colector OTLP. Los servicios pueden enviar telemetría a Alloy por gRPC o HTTP, y el pipeline reenvía los logs a Loki mientras promueve atributos seleccionados a labels. Esto permite filtrar logs en Grafana por campos como `service.name`, `service.namespace`, el entorno, el nivel de log o el logger, acelerando mucho el troubleshooting en entornos con varios servicios.

El stack también incluye exporters operativos como Blackbox Exporter, `nginx-prometheus-exporter` y `cadvisor`, ampliando la visibilidad más allá de la telemetría a nivel de aplicación. Con estos componentes, el proyecto puede monitorizar la disponibilidad de endpoints, las métricas de contenedores y las métricas del reverse proxy desde el primer momento, cubriendo una base práctica para despliegues reales.

El repositorio separa claramente los flujos de producción y local. Un `compose.yaml` de producción consume imágenes versionadas publicadas en GitHub Container Registry, mientras que `compose.local.yaml` utiliza imágenes públicas para validación local y pruebas de integración. Esto mantiene el desarrollo ligero sin perder compatibilidad con la arquitectura de producción.

La automatización del despliegue se gestiona con GitHub Actions. Cuando se publica una etiqueta de versión semántica, el pipeline construye y publica las imágenes necesarias, se conecta al servidor destino por SSH, descarga las nuevas versiones y recrea el stack con Docker Compose. Este enfoque mantiene los lanzamientos predecibles y hace que la plataforma sea fácil de actualizar a medida que evoluciona la configuración.

Los puntos clave del proyecto incluyen:
* Configuración de Grafana preprovisionada con datasources, dashboards y alertas integradas en la imagen.
* Recolección de métricas basada en Prometheus para monitorizar infraestructura y servicios.
* Pipeline Loki + Alloy para ingesta de logs OTLP y exploración centralizada en Grafana.
* Flujos de Docker Compose separados para validación local y despliegue en producción.
* Pipeline CI/CD que construye, publica y despliega imágenes versionadas automáticamente.

En conjunto, Monitoring es una base de observabilidad compacta pero completa para servicios contenedorizados. Prioriza la reproducibilidad, el despliegue con poca fricción y un pipeline de telemetría práctico que funciona tanto en desarrollo local como en operación real.
