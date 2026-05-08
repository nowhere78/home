# WidgetAI — Embeddable AI-Powered E-Commerce Platform

WidgetAI is a **distributed, cloud-native e-commerce widget platform** for creators, educators, and small businesses. Sellers embed a fully-featured storefront into any website, blog, or newsletter with a single JavaScript snippet — no separate store required. An AI-powered recommendation engine personalises product discovery; Stripe handles secure payments; and a suite of microservices provides the scalability, resiliency, and security required for production workloads.

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Architecture Components](#2-architecture-components)
3. [Data Tier](#3-data-tier)
4. [Quality Attributes](#4-quality-attributes)
5. [External Integrations](#5-external-integrations)
6. [Repository Structure](#6-repository-structure)
7. [Architecture Decision Records](#7-architecture-decision-records)
8. [Getting Started](#8-getting-started)

---

## 1. System Overview

```
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  Seller's website / blog / newsletter                                   │
 │                                                                         │
 │   <script src="https://cdn.widgetai.io/embed.js"                       │
 │           data-store-id="abc123"></script>                              │
 │                                                                         │
 │              ┌──────────────────────────┐                               │
 │              │  Embeddable Widget (CDN) │                               │
 │              └────────────┬─────────────┘                               │
 └───────────────────────────┼─────────────────────────────────────────────┘
                             │ HTTPS / REST + WebSocket
                             ▼
                    ┌─────────────────┐
                    │   API Gateway   │  (rate limiting, auth, routing)
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────────┐
          ▼                  ▼                       ▼
  ┌──────────────┐  ┌────────────────┐  ┌────────────────────┐
  │  Auth Service│  │ Product Catalog│  │ Recommendation     │
  │  (JWT/OAuth) │  │    Service     │  │ Engine (ML / CF)   │
  └──────────────┘  └────────────────┘  └────────────────────┘
          │                  │                       │
          ▼                  ▼                       ▼
  ┌──────────────┐  ┌────────────────┐  ┌────────────────────┐
  │  Checkout /  │  │    Payment     │  │   Notification     │
  │ Order Service│  │ Integration    │  │      Service       │
  │              │  │   (Stripe)     │  │  (email / push)    │
  └──────────────┘  └────────────────┘  └────────────────────┘
          │                  │                       │
          └──────────────────┼───────────────────────┘
                             │  async events (Kafka / SQS)
                             ▼
                  ┌──────────────────────┐
                  │ Analytics / Event    │
                  │  Tracking Pipeline   │
                  └──────────────────────┘
                             │
          ┌──────────────────┼──────────────────────┐
          ▼                  ▼                       ▼
   ┌─────────────┐  ┌────────────────┐  ┌───────────────────┐
   │ PostgreSQL  │  │  DynamoDB /    │  │  Redis            │
   │ (ACID data) │  │  Cassandra     │  │  (cache / session)│
   └─────────────┘  └────────────────┘  └───────────────────┘
```

---

## 2. Architecture Components

| # | Component | Responsibility |
|---|-----------|---------------|
| 1 | **Embeddable Widget** | Lightweight JS/CSS bundle served from CDN; renders product grid, search, and cart inside any host page via Shadow DOM. |
| 2 | **Seller Dashboard** | Vue 3 + TypeScript single-page application for product management, order review, analytics, and Stripe Connect onboarding. |
| 3 | **API Gateway** | Single entry-point for all client traffic. Handles TLS termination, JWT validation, rate limiting, request routing, and observability hooks. |
| 4 | **Auth / Authorization Service** | Issues and validates JWTs; manages seller and buyer identities; enforces RBAC; integrates with OAuth 2.0 providers (Google, GitHub). |
| 5 | **Product Catalog Service** | CRUD for products, variants, and media assets; search powered by Elasticsearch; backed by DynamoDB/Cassandra for high read throughput. |
| 6 | **Recommendation Engine** | Collaborative-filtering + content-based hybrid model; real-time scoring served from a low-latency feature store (Redis); batch retraining pipeline on scheduled cadence. |
| 7 | **Checkout / Order Service** | Cart management, order lifecycle (created → paid → fulfilled → shipped), inventory reservation, idempotent payment initiation. |
| 8 | **Payment Integration Service** | Wraps Stripe APIs (Charges, PaymentIntents, Stripe Connect for seller payouts, Webhooks); translates Stripe events to internal domain events. |
| 9 | **Notification Service** | Consumes order/payment events; sends transactional email (SES/SendGrid), SMS, and push notifications via fan-out. |
| 10 | **Analytics / Event Tracking Pipeline** | Collects widget interaction events (impressions, clicks, conversions); streams through Kafka; materialises aggregate views in a columnar store (Redshift / BigQuery). |
| 11 | **Data Storage Tier** | PostgreSQL, DynamoDB/Cassandra, Redis — see [§3](#3-data-tier) for details. |
| 12 | **Monitoring / Logging / Resiliency Layer** | Distributed tracing (OpenTelemetry), structured logging (ELK), metrics (Prometheus + Grafana), circuit breakers (Resilience4j / Hystrix), PagerDuty alerting. |

---

## 3. Data Tier

### Storage Technologies

| Store | Use Case | Consistency Model |
|-------|----------|--------------------|
| **PostgreSQL** | Users, orders, payments, seller accounts — ACID transactions, foreign-key integrity | Strong consistency |
| **DynamoDB / Cassandra** | Product catalog, recommendation feature vectors, event counters — high-volume reads/writes, flexible schema | Eventual consistency (tunable) |
| **Redis** | Session tokens, product/recommendation cache, rate-limit counters, distributed locks | Eventual consistency (TTL-based) |
| **S3 / GCS** | Product images, widget JS bundles, export files | Eventual consistency |
| **Redshift / BigQuery** | Analytics aggregations, business intelligence queries | Eventual consistency |

### Consistency Tradeoffs

**Strong consistency required:**
- Order creation and payment capture (double-spend prevention)
- Inventory decrement during checkout (prevents overselling)
- User authentication and session management

**Eventual consistency acceptable:**
- Product catalog reads (slight staleness tolerated for performance)
- Recommendation scores (model is retrained periodically anyway)
- Analytics counters and dashboards (near-real-time is sufficient)

---

## 4. Quality Attributes

### Resiliency
- **Retries with exponential back-off** on all outbound service calls (Stripe, email, downstream services)
- **Circuit breakers** (Resilience4j) around Payment and Notification services to prevent cascade failures
- **Graceful degradation**: widget falls back to a static product list when the Recommendation Engine is unavailable
- **Idempotency keys** on all Stripe payment intents to handle duplicate webhook delivery
- **Dead-letter queues** (DLQ) on all Kafka consumers; failed messages are replayed after investigation

### Scalability
- All backend services are **stateless and horizontally scalable** behind a load balancer
- **Kafka** decouples producers (Checkout, Payment) from consumers (Notification, Analytics) for async, back-pressure-resistant messaging
- **Redis** caching reduces database read load; catalog pages cached with configurable TTL
- **CDN** (CloudFront / Fastly) distributes the widget bundle globally for sub-50 ms load times

### Security
- **TLS everywhere** — inter-service communication enforced via mTLS in Kubernetes service mesh (Istio)
- **JWT-based authentication** with short-lived access tokens (15 min) and refresh tokens stored in HttpOnly cookies
- **RBAC**: seller roles, buyer roles, admin roles enforced at API Gateway and per-service
- **Secrets management**: all credentials stored in AWS Secrets Manager / HashiCorp Vault; never in environment files or source code
- **PCI-DSS scope minimisation**: raw card data never touches WidgetAI servers; Stripe.js tokenises on the client; Stripe handles cardholder data

---

## 5. External Integrations

| Integration | Purpose | API Style |
|-------------|---------|-----------|
| **Stripe Payments** | Payment intents, refunds, webhooks | REST (Stripe SDK) |
| **Stripe Connect** | Seller onboarding, managed payouts | REST (OAuth flow) |
| **SendGrid / AWS SES** | Transactional email | REST |
| **Twilio** | SMS notifications (optional) | REST |
| **Elasticsearch** | Full-text product search | REST |

---

## 6. Repository Structure

```
WidgetAI/
├── README.md                        # This file
├── adr/                             # Architecture Decision Records
│   ├── ADR-001-architecture-style.md
│   ├── ADR-002-data-tier-design.md
│   ├── ADR-003-payment-integration.md
│   ├── ADR-004-recommendation-architecture.md
│   └── ADR-005-deployment-infrastructure.md
├── services/
│   ├── api-gateway/                 # Kong / custom Express gateway
│   ├── auth-service/                # JWT issuance, OAuth, RBAC
│   ├── product-catalog-service/     # Product CRUD + search
│   ├── recommendation-engine/       # ML scoring + feature store
│   ├── checkout-order-service/      # Cart, orders, inventory
│   ├── payment-integration-service/ # Stripe wrapper + webhooks
│   ├── notification-service/        # Email / SMS / push fan-out
│   └── analytics-pipeline/          # Event ingestion + streaming
├── widget/                          # Embeddable JS/CSS bundle
│   ├── src/
│   └── dist/
├── dashboard/                       # Seller admin SPA (Vue 3 + TypeScript)
│   └── src/
├── infra/                           # Infrastructure-as-Code
│   ├── terraform/                   # Cloud resource provisioning
│   ├── k8s/                         # Kubernetes manifests
│   └── helm/                        # Helm charts
└── docs/                            # Additional documentation
    ├── api/                         # OpenAPI specs
    └── diagrams/                    # Architecture diagrams
```

---

## 7. Architecture Decision Records

Five ADRs document the most important architectural decisions:

| ADR | Title | Status |
|-----|-------|--------|
| [ADR-001](adr/ADR-001-architecture-style.md) | Overall Architecture Style — Microservices | Accepted |
| [ADR-002](adr/ADR-002-data-tier-design.md) | Data Tier Design — Polyglot Persistence | Accepted |
| [ADR-003](adr/ADR-003-payment-integration.md) | Payment Integration — Stripe | Accepted |
| [ADR-004](adr/ADR-004-recommendation-architecture.md) | Recommendation Engine Architecture | Accepted |
| [ADR-005](adr/ADR-005-deployment-infrastructure.md) | Deployment and Infrastructure Approach | Accepted |

---

## 8. Getting Started

> **Note:** Full service implementations are scaffolded under `/services`. Refer to each service's own `README.md` for local development instructions.

### Prerequisites

- Docker & Docker Compose
- Node.js 20+
- Python 3.11+ (recommendation engine)
- Terraform 1.5+ (infrastructure)
- `kubectl` + a Kubernetes cluster (local: `kind` or `minikube`)

### Quick Start (local development)

```bash
# Clone the repo
git clone https://github.com/tousif-anwar/WidgetTech.git
cd WidgetTech

# Start all services with Docker Compose
docker compose up -d

# Seed the database
docker compose exec checkout-order-service npm run db:seed

# Open the seller dashboard
open http://localhost:3000

# Load the widget demo page
open http://localhost:8080/demo
```

### Environment Variables

Copy `.env.example` to `.env` and populate the required secrets:

```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
JWT_SECRET=...
```

Never commit `.env` to source control.

