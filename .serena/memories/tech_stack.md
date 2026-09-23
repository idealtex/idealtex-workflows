# Architecture
- idealtex-mono is the .NET/EF backend; MySQL, Redis and Meilisearch are dependencies. Both frontend repositories use Next.js/React; consult package.json and locks for versions.
- idealtex-management owns Swarm platform setup: Dokploy with its PostgreSQL/Redis, Caddy TLS, internal Traefik routing, Grafana/Loki/VictoriaMetrics/Alloy. Version pins live in configs/versions.env.
- Initial manager hosts ingress/control/monitoring; worker hosts applications and local state. WireGuard carries inter-host traffic because provider private networking is unavailable.
- Backend images and keys remain local and pinned to the data-owning worker. No initial shared storage or HA guarantee. Scaling backend replicas requires reviewing storage and queue safety.
- Application DEV/PROD are environments, never server roles. Production migration, backups, dependency remediation and acceptance gates are documented separately.
