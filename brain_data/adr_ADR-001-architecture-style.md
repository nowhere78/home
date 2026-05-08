# ADR-001: Overall Architecture Style — Microservices

**Status:** Accepted  
**Date:** 2026-04-22  
**Authors:** WidgetAI Architecture Team

---

## Context

WidgetAI must support a diverse set of capabilities under one platform: embeddable widget delivery, seller administration, product catalog management, AI-driven recommendations, payment processing, order management, notifications, and analytics. Each of these domains has different:

- **Scalability requirements** (e.g., the recommendation engine and product catalog must sustain high read traffic; the checkout service requires strict transactional integrity)
- **Technology choices** (e.g., ML scoring best served by Python; API services best served by Node.js or Go)
- **Release cadences** (e.g., the widget JS bundle may ship multiple times per day; the analytics pipeline may ship weekly)
- **Team ownership boundaries** (each service area can be owned by a separate squad)

We must choose a primary architectural style that governs how these capabilities are decomposed, deployed, and communicated.

## Options Considered

### Option A: Monolithic Architecture
Deploy all capabilities as a single application and database.

**Pros:**
- Simple to develop initially
- No distributed systems complexity (no network calls between services, no eventual consistency)
- Single deployment artifact

**Cons:**
- Scaling the entire application to serve peak widget traffic is wasteful for components with lower demand
- Technology lock-in: cannot use Python for ML inside a Node.js monolith without significant overhead
- Large blast radius: a bug in notifications can bring down checkout
- Slow release cycles: any change requires a full application re-deployment
- Difficult to isolate PCI-DSS scope for payment processing

### Option B: Microservices Architecture
Decompose the platform into independently deployable services, each owning its own data store, communicating over lightweight protocols (REST/gRPC/Kafka).

**Pros:**
- Each service can be scaled independently (e.g., Product Catalog can scale to 100 replicas while Notification Service stays at 2)
- Technology heterogeneity: Python for the recommendation engine, Node.js for the API gateway, Go for high-throughput services
- Isolated fault domains: circuit breakers prevent failures from cascading
- Independent deployments enable continuous delivery at the service level
- PCI-DSS scope can be tightly bounded to the Payment Integration Service

**Cons:**
- Distributed systems complexity: network latency, partial failures, eventual consistency
- Operational overhead: more containers, more deployments, more observability tooling needed
- Data consistency across services requires careful design (Saga pattern, outbox pattern)

### Option C: Modular Monolith
A single deployment unit with strictly enforced internal module boundaries, later extractable to services.

**Pros:**
- Lower operational complexity than microservices
- Easier to refactor boundaries early on

**Cons:**
- Does not address the fundamental scaling and technology heterogeneity problems
- Technology lock-in remains
- Deferred extraction rarely happens in practice; the codebase tends to drift toward a big ball of mud

## Decision

**We adopt Microservices Architecture (Option B).**

The platform's requirements for polyglot technology (ML in Python, APIs in Node.js/Go), independent scaling of heterogeneous workloads, and PCI-DSS scope isolation directly justify the added operational complexity. The 12 logical components map cleanly to the following deployable services:

1. `api-gateway`
2. `auth-service`
3. `product-catalog-service`
4. `recommendation-engine`
5. `checkout-order-service`
6. `payment-integration-service`
7. `notification-service`
8. `analytics-pipeline`

The embeddable widget and seller dashboard are frontend artefacts deployed to CDN / static hosting and are not backend services.

Inter-service communication follows these conventions:
- **Synchronous (REST/gRPC):** used when the caller requires an immediate response (e.g., product lookup during widget render, payment intent creation)
- **Asynchronous (Kafka events):** used for decoupled workflows where the caller does not need to wait (e.g., order-placed → notification, order-paid → analytics)

## Consequences

**Positive:**
- Each service can be iterated, deployed, and scaled independently
- The recommendation engine can use specialised ML libraries (scikit-learn, PyTorch) without impacting other services
- Payment processing is isolated, limiting PCI-DSS compliance scope
- Individual service failures do not propagate platform-wide if circuit breakers are in place

**Negative / Risks:**
- Teams must invest in shared observability tooling (distributed tracing, centralised logging) from day one
- Distributed transactions (e.g., reducing inventory and capturing payment atomically) require the Saga / outbox pattern; developers must understand these patterns
- Service discovery, load balancing, and mTLS are handled by a service mesh (Istio on Kubernetes), which adds infrastructure complexity
- Integration testing across service boundaries requires a robust contract-testing strategy (Pact)

**Mitigations:**
- Adopt OpenTelemetry as the tracing standard across all services from day one
- Use the Transactional Outbox Pattern for all event emissions from services that also write to a database
- Provide shared libraries (SDK packages) for common cross-cutting concerns: logging format, JWT validation, retry/circuit-breaker configuration
