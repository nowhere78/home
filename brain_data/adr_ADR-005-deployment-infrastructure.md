# ADR-005: Deployment and Infrastructure Approach

**Status:** Accepted  
**Date:** 2026-04-22  
**Authors:** WidgetAI Architecture Team

---

## Context

WidgetAI is a distributed system with 8+ independently deployable services, 3 storage technologies, a CDN-distributed widget bundle, and a seller dashboard SPA. The infrastructure decisions made here will directly impact:

- **Developer velocity**: how quickly engineers can deploy, test, and roll back changes
- **Operational cost**: idle resource cost, per-unit compute cost, infrastructure management overhead
- **Reliability**: uptime SLAs, recovery time objectives (RTO), and recovery point objectives (RPO)
- **Security posture**: network isolation, secrets management, patch cadence
- **Scalability**: ability to handle traffic spikes (e.g., a seller's product goes viral)

We must decide on the container orchestration platform, cloud provider strategy, infrastructure-as-code approach, CI/CD pipeline, and environment strategy.

## Options Considered

### Option A: Kubernetes (EKS / GKE) with Helm + Terraform
Deploy all services as containerised workloads on managed Kubernetes, provisioned with Terraform, packaged with Helm charts, with Istio as the service mesh.

**Pros:**
- Industry-standard container orchestration; large ecosystem of operators, tooling, and community support
- Declarative infrastructure: every service's resource requirements, scaling rules, and networking are version-controlled
- Istio service mesh provides mTLS, traffic management, circuit breaking, and observability without application code changes
- Horizontal Pod Autoscaler (HPA) reacts to CPU/RPS metrics; Cluster Autoscaler provisions new nodes on demand
- Works identically across AWS (EKS), GCP (GKE), Azure (AKS), enabling multi-cloud or cloud-neutral operation
- Helm packages each service's Kubernetes manifests as versioned, configurable charts

**Cons:**
- Kubernetes has a steep learning curve; operational complexity is significant
- Running a managed Kubernetes cluster has a minimum cost floor even with no traffic
- Istio adds another layer of complexity (control plane, sidecar injection, certificate management)

### Option B: AWS ECS (Elastic Container Service) with Fargate
Serverless container execution on AWS-native infrastructure without Kubernetes.

**Pros:**
- Simpler operational model than Kubernetes (no node management)
- Deep AWS integration (IAM roles per task, native ALB integration, CloudWatch logging)
- Lower minimum cost: Fargate charges per vCPU-second of task execution

**Cons:**
- AWS-only: strong vendor lock-in
- Less portable than Kubernetes; migrating to another cloud requires significant rework
- Service mesh capabilities are more limited (App Mesh is less mature than Istio)
- Smaller community and ecosystem compared to Kubernetes

### Option C: Serverless Functions (AWS Lambda / Google Cloud Run)
Deploy each service as serverless functions triggered by HTTP or queue events.

**Pros:**
- Zero infrastructure management; automatic scaling to zero
- Pay-per-execution pricing is very cost-effective at low traffic

**Cons:**
- Cold-start latency is unacceptable for the recommendation engine (target p99 < 100 ms)
- Stateful services (Redis connections, ML model loading) do not fit the stateless function model well
- Vendor lock-in is even stronger than ECS
- Debugging and local development are more complex

### Option D: Kubernetes (Option A) + Serverless hybrid
Use Kubernetes for latency-sensitive and stateful services; serverless functions for event-driven, bursty workloads.

**Pros:**
- Best of both worlds: Kubernetes for the core platform; Lambda/Cloud Functions for analytics ingestion, email sending, webhook processing

**Cons:**
- Operational complexity of managing two deployment paradigms
- Adds cognitive overhead for developers working across both styles

## Decision

**We adopt Kubernetes on AWS EKS as the primary deployment platform (Option A), with a targeted Serverless hybrid (Option D) for event-driven ancillary workloads.**

### Primary Platform: AWS EKS + Istio + Terraform + Helm

**Compute:**
- All 8 backend services deployed as Kubernetes Deployments with HPA
- Recommendation Engine runs on GPU-enabled node pools (g4dn.xlarge) for model inference; separate node pool from CPU-only services
- Cluster Autoscaler provisions additional nodes during traffic spikes; scales down during off-peak

**Service Mesh:**
- Istio for mTLS between all services, traffic management (canary deployments, traffic mirroring), and distributed tracing export to Jaeger/Tempo
- `PeerAuthentication` policy set to `STRICT` across all namespaces — no plaintext inter-service traffic allowed

**Ingress & CDN:**
- AWS ALB Ingress Controller for external HTTPS traffic to the API Gateway
- CloudFront CDN distributes the widget JS bundle globally (edge locations in NA, EU, APAC)
- CloudFront Origin Shield reduces origin load; widget bundle cache TTL = 24 hours (versioned by content hash, so deploys are instant)

**Infrastructure-as-Code:**
- Terraform manages all cloud resources: EKS cluster, RDS PostgreSQL, DynamoDB tables, ElastiCache Redis, S3 buckets, IAM roles, CloudFront distributions, Secrets Manager
- Terraform state stored in S3 with DynamoDB state locking; remote state shared across teams via Terraform Cloud
- Separate Terraform workspaces per environment (`dev`, `staging`, `production`)

**Secrets Management:**
- AWS Secrets Manager stores all application secrets (Stripe keys, database credentials, JWT signing keys)
- External Secrets Operator synchronises secrets from Secrets Manager into Kubernetes Secrets automatically; no secrets stored in Helm values or source control

### Serverless Hybrid: AWS Lambda for Event-Driven Workloads
- **Analytics event ingestion**: Kinesis Data Streams → Lambda → DynamoDB / S3 (Firehose) — handles bursty widget event traffic without provisioning dedicated capacity
- **Stripe webhook processor**: API Gateway → Lambda → SQS FIFO → Payment Integration Service — provides a decoupled, scalable webhook ingestion layer
- **Scheduled jobs**: EventBridge Scheduler → Lambda for nightly recommendation model retraining triggers, daily report generation

### CI/CD Pipeline

```
Developer pushes to feature branch
        │
        ▼
GitHub Actions — CI Pipeline
  ├── Lint + Unit tests
  ├── Integration tests (Testcontainers)
  ├── Docker image build + push (ECR)
  ├── Helm chart lint + template validation
  └── Pact contract tests (consumer + provider)
        │
        ▼ (merge to main)
GitHub Actions — CD Pipeline
  ├── Deploy to 'dev' namespace (automatic)
  ├── Smoke tests against dev
  ├── Deploy to 'staging' namespace (automatic)
  ├── Integration + load tests against staging
  └── Deploy to 'production' (manual approval gate)
        │  (uses Argo Rollouts for canary deployment)
        ▼
Production — Canary Release
  ├── 5% traffic → new version
  ├── Monitor error rate + p99 latency (Prometheus)
  └── Auto-promote or rollback based on metrics
```

### Environment Strategy

| Environment | Purpose | Infrastructure |
|-------------|---------|---------------|
| `dev` | Active development | Shared EKS cluster, namespace-isolated; scaled-down resources |
| `staging` | Pre-production validation, load testing | Isolated EKS cluster; production-equivalent config |
| `production` | Live traffic | Isolated EKS cluster; multi-AZ, autoscaling, full observability |

### Observability Stack

| Concern | Tool |
|---------|------|
| Distributed tracing | OpenTelemetry → Grafana Tempo |
| Metrics | Prometheus + Grafana dashboards |
| Structured logging | Fluent Bit → OpenSearch (ELK) |
| Alerting | Prometheus AlertManager → PagerDuty |
| Uptime monitoring | Synthetic checks (Grafana Synthetic Monitoring) |
| Error tracking | Sentry (SDK in each service) |

### Resiliency Mechanisms

- **Pod Disruption Budgets (PDB):** minimum 2 replicas always running for critical services during node drains
- **Liveness + Readiness probes:** services report unhealthy if downstream dependencies are unavailable; Kubernetes stops routing traffic to unhealthy pods
- **Argo Rollouts canary:** automatic rollback if error rate > 1% or p99 latency > 500 ms during canary phase
- **Multi-AZ deployment:** EKS node groups spread across 3 availability zones; RDS PostgreSQL configured with Multi-AZ standby

## Consequences

**Positive:**
- Kubernetes provides a vendor-neutral, portable deployment target; migrating from EKS to GKE or self-hosted Kubernetes requires only changing the cloud provider integration (load balancer, storage class)
- Istio mTLS enforces zero-trust networking automatically without application code changes
- Terraform + Helm enables reproducible, version-controlled infrastructure; environment parity between staging and production
- Argo Rollouts canary deployments reduce deployment risk; automatic rollback limits blast radius

**Negative / Risks:**
- Kubernetes has a steep operational learning curve; teams must invest in Kubernetes expertise
- The EKS control plane and node groups have a minimum cost floor (~$150–200/month) regardless of traffic; this is higher than a pure serverless baseline
- Istio adds operational complexity (control plane upgrade cadence, sidecar injection, certificate rotation)

**Mitigations:**
- Invest in internal platform engineering: a Platform Team owns the EKS cluster, Istio, and shared Helm library charts; product teams consume abstractions rather than raw Kubernetes manifests
- Use AWS Savings Plans and Spot Instances for non-critical node groups (analytics pipeline, recommendation batch jobs) to reduce compute costs by up to 70%
- Automate Istio upgrades using the Sail Operator; document the upgrade runbook and test in staging before production
- Provide a local development environment using `kind` (Kubernetes in Docker) with a reduced-resource configuration so engineers can test Kubernetes manifests without cloud costs
