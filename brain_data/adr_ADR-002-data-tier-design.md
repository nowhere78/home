# ADR-002: Data Tier Design — Polyglot Persistence

**Status:** Accepted  
**Date:** 2026-04-22  
**Authors:** WidgetAI Architecture Team

---

## Context

WidgetAI handles fundamentally different data access patterns across its services:

- **Transactional data** (users, orders, payments): requires ACID guarantees, foreign-key relationships, complex queries, and auditability
- **High-volume catalogue and recommendation data** (product listings, feature vectors, event counters): demands high throughput reads/writes, flexible schema evolution, and geographic distribution
- **Low-latency ephemeral data** (sessions, rate-limit counters, recommendation cache): needs sub-millisecond reads and TTL-based expiry
- **Analytical data** (aggregated events, conversion funnels): requires efficient columnar scans over large datasets

Using a single database technology across all these patterns would force compromises: either sacrificing the transactional guarantees needed for payments or limiting read throughput for the catalog.

We must decide on a data storage strategy that matches each service's access pattern while keeping operational complexity manageable.

## Options Considered

### Option A: Single Relational Database (PostgreSQL Only)
Use PostgreSQL for every service.

**Pros:**
- Operational simplicity: one database technology to operate and monitor
- ACID transactions across all entities
- Mature ecosystem, strong tooling

**Cons:**
- Relational schemas do not model product catalog data well (variable attributes per product category require EAV anti-patterns or JSONB sprawl)
- Horizontal write scaling is complex (requires Citus or sharding)
- Full-text search and recommendation vector similarity queries are not PostgreSQL's strengths at high scale
- A single shared database across services violates the microservices "database per service" principle, creating tight coupling

### Option B: Single NoSQL Database (DynamoDB or Cassandra Only)
Use a wide-column or document store for every service.

**Pros:**
- Excellent horizontal scalability
- Flexible schema ideal for catalog data

**Cons:**
- No multi-row ACID transactions (critical for order + inventory updates)
- Ad-hoc querying is limited, making order management and reporting difficult
- Not suitable for complex relational queries needed by the seller dashboard

### Option C: Polyglot Persistence (PostgreSQL + DynamoDB/Cassandra + Redis)
Assign each data store to the workload it is best suited for.

**Pros:**
- Each store is used for the problem it solves best
- Services are decoupled at the data layer
- Scales each tier independently

**Cons:**
- Operational complexity: three storage technologies to provision, monitor, back up, and secure
- Engineers must understand multiple consistency models
- Cross-service queries (e.g., joining order history with product details) require application-level aggregation or a read model (CQRS)

## Decision

**We adopt Polyglot Persistence (Option C)** with the following assignment:

### PostgreSQL — Transactional Data (Strong Consistency)
**Services:** `auth-service`, `checkout-order-service`, `payment-integration-service`  
**Data stored:** user accounts, seller profiles, orders, payment records, audit logs

Rationale:
- ACID transactions are mandatory: capturing a payment and decrementing inventory must be atomic
- Foreign-key constraints enforce referential integrity between orders and line items
- Row-level security (RLS) enables multi-tenancy isolation at the database level
- Point-in-time recovery (PITR) supports auditability and compliance

### DynamoDB (or Cassandra) — High-Volume Catalog and Recommendation Data (Eventual Consistency)
**Services:** `product-catalog-service`, `recommendation-engine`  
**Data stored:** product listings, variants, media metadata, recommendation feature vectors, click/impression counters

Rationale:
- Products per seller can number in the thousands; variant attributes differ by category (electronics vs. apparel); a wide-column / document model is more natural than a rigid relational schema
- Single-digit millisecond reads at any scale without sharding complexity
- DynamoDB Global Tables enable multi-region active-active replication for low-latency reads
- Cassandra's tunable consistency (ONE / QUORUM) allows the team to trade consistency for availability on less critical paths

**DynamoDB vs. Cassandra choice:**  
We default to **DynamoDB** on AWS deployments for its fully managed operations. Self-hosted or multi-cloud deployments may substitute **Apache Cassandra**. Both are modelled identically in the service layer via an abstraction interface.

### Redis — Caching and Low-Latency Ephemeral Data
**Services:** all services (shared cluster, logically separated by key namespace)  
**Data stored:** JWT refresh token blocklist, seller session data, product/recommendation response cache, rate-limit counters, distributed locks (Redlock)

Rationale:
- Sub-millisecond reads required for recommendation serving (the widget renders inline on the seller's page)
- TTL-based expiry naturally models session lifetimes and cache invalidation
- Redis Pub/Sub used for real-time cart synchronisation across widget tabs
- Redis Cluster provides horizontal scaling; Redis Sentinel provides high availability

### Consistency Model Summary

| Data Domain | Store | Consistency | Justification |
|-------------|-------|-------------|---------------|
| User accounts / auth | PostgreSQL | Strong | Prevents duplicate registrations, auth bypass |
| Orders | PostgreSQL | Strong | Double-spend prevention, inventory integrity |
| Payment records | PostgreSQL | Strong | Financial audit trail |
| Product catalog reads | DynamoDB + Redis | Eventual | Stale by seconds is acceptable; throughput matters |
| Recommendation scores | Redis (cache) | Eventual | Model is retrained periodically; slight staleness is fine |
| Analytics counters | DynamoDB / Kafka | Eventual | Approximate counts are acceptable for dashboards |
| Cart state | Redis | Eventual | Lost cart is recoverable; low-latency matters more |

## Consequences

**Positive:**
- Each service's data layer is tuned to its access pattern, eliminating performance bottlenecks
- The payment and order services meet ACID requirements without compromise
- The catalog and recommendation services can scale reads to millions of requests per second
- Redis caching reduces PostgreSQL and DynamoDB load by an estimated 80–90% for read-heavy paths

**Negative / Risks:**
- Three storage systems increase the operational surface area (backups, monitoring, failover procedures for each)
- Developers must be aware that reading a product after writing it through DynamoDB may return stale data for a brief window (eventual consistency lag)
- Cross-entity queries (e.g., "orders containing product X") cannot be executed with a single SQL JOIN; require a CQRS read model or application-side aggregation

**Mitigations:**
- Use Terraform modules to provision all three stores consistently across environments
- Implement a shared cache invalidation strategy: services publish `product.updated` events; the catalog service's cache layer subscribes and evicts affected keys
- Document explicit consistency guarantees in each service's API contract; use optimistic locking (version columns in PostgreSQL) for high-contention entities
