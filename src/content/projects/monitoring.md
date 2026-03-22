---
title: Monitoring
shortDescription: Containerized observability stack built around Prometheus, Grafana, Loki, and Alloy.
link: null
featured: true
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
  - Metrics Collection
  - Log Ingestion
  - OTLP Pipeline
  - Dashboard Provisioning
  - Alerting
---

![Monitoring](/monitoring.svg)

Monitoring is a production-oriented observability stack designed to centralize metrics, logs, dashboards, and alerting in a single containerized deployment. The project combines Grafana, Prometheus, Loki, and Alloy to provide a cohesive monitoring platform that is easy to run locally and straightforward to ship in production. It is intended for teams that want a self-hosted foundation for infrastructure and application observability without having to assemble each piece from scratch.

At the center of the stack, Grafana is delivered through a custom image with datasources, dashboards, and alerting resources already provisioned. This makes the environment reproducible and removes the need for manual post-deployment configuration. Prometheus handles metric scraping through a dedicated configuration file, while Loki stores logs and exposes them for exploration inside Grafana alongside the metric dashboards.

The log ingestion path is built around Alloy acting as the OTLP collector. Services can send telemetry to Alloy over gRPC or HTTP, and the pipeline forwards logs into Loki while promoting selected attributes to labels. This allows teams to filter logs in Grafana by fields such as `service.name`, `service.namespace`, environment name, log level, or logger, making troubleshooting much faster in multi-service environments.

The stack also includes operational exporters such as Blackbox Exporter, `nginx-prometheus-exporter`, and `cadvisor`, extending visibility beyond application-level telemetry. With these components, the project can monitor endpoint availability, container metrics, and reverse proxy metrics out of the box, covering a practical baseline for real-world deployments.

The repository separates production and local workflows clearly. A production `compose.yaml` consumes versioned images published to GitHub Container Registry, while `compose.local.yaml` relies on public images for local validation and integration testing. This keeps development lightweight without losing compatibility with the production architecture.

Deployment automation is handled through GitHub Actions. When a semantic version tag is pushed, the pipeline builds and publishes the required images, connects to the target server over SSH, pulls the new versions, and recreates the stack with Docker Compose. This approach keeps releases predictable and makes the monitoring platform easy to update as the configuration evolves.

Key aspects of the project include:
* Pre-provisioned Grafana setup with datasources, dashboards, and alert definitions baked into the image.
* Prometheus-based metrics collection for infrastructure and service monitoring.
* Loki plus Alloy pipeline for OTLP log ingestion and centralized exploration in Grafana.
* Separate local and production Docker Compose flows for validation and deployment.
* CI/CD pipeline that builds, publishes, and deploys versioned images automatically.

Overall, Monitoring is a compact but complete observability foundation for containerized services. It emphasizes reproducibility, low-friction deployment, and a practical telemetry pipeline that supports both local development and production operations.
