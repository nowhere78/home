# ADR-004: Recommendation Engine Architecture

**Status:** Accepted  
**Date:** 2026-04-22  
**Authors:** WidgetAI Architecture Team

---

## Context

One of WidgetAI's key differentiators is the AI-powered recommendation engine that personalises the product grid shown in each seller's embedded widget. The engine must:

- Serve personalised product recommendations in **under 100 ms** (the widget renders inline on the seller's page; latency directly impacts conversion rates)
- Handle **cold-start scenarios** where there is no interaction history for a new buyer or a newly listed product
- Support **multi-tenant isolation**: recommendations for Store A must not leak product data from Store B
- Scale to serve **millions of recommendation requests per day** across potentially thousands of seller storefronts
- Improve over time as more interaction data is collected (clicks, purchases, time-on-page)
- Be **cost-effective** for a platform with many small sellers who individually generate low traffic volumes

We must decide on a recommendation algorithm, training pipeline, serving architecture, and feature storage strategy.

## Options Considered

### Option A: Pure Collaborative Filtering (Matrix Factorisation)
Learn latent factors for users and items from the interaction matrix (e.g., Alternating Least Squares, SVD++).

**Pros:**
- Strong accuracy when sufficient interaction data exists
- Captures subtle user preference signals

**Cons:**
- Severe cold-start problem: new sellers with no purchase history get no recommendations
- Requires periodic full retraining as the interaction matrix grows; expensive at scale
- Does not incorporate product content features (title, category, price) which are available from day one

### Option B: Content-Based Filtering
Recommend products similar to those a buyer has previously viewed, based on product features (title embeddings, category, price range).

**Pros:**
- No cold-start problem for products (recommendations available immediately on listing)
- Explainable ("Recommended because you viewed X")

**Cons:**
- Over-specialisation: recommends items too similar to what was already seen; misses serendipity
- Does not incorporate collective wisdom of other buyers
- Limited effectiveness in discovery use cases

### Option C: Hybrid Model (Collaborative Filtering + Content-Based + Popularity Fallback)
Combine collaborative filtering, content-based signals, and a popularity-based fallback in a weighted ensemble, with a retrieval + ranking two-stage pipeline.

**Pros:**
- Addresses cold-start via content features and popularity signals
- Improves accuracy over any single approach
- Two-stage retrieval + ranking is the industry-standard architecture (used by Netflix, Spotify, Amazon)

**Cons:**
- More complex to build and maintain (multiple models, feature pipelines, serving infrastructure)
- Requires careful A/B testing framework to evaluate model variants

### Option D: Third-Party Recommendation API (e.g., AWS Personalize, Google Recommendations AI)
Delegate recommendation logic entirely to a managed ML service.

**Pros:**
- No ML engineering required; fast time to market
- Managed infrastructure; no model serving complexity

**Cons:**
- Significant cost at scale (per-event and per-recommendation pricing)
- Data must be exported to the cloud provider; raises data privacy/portability concerns
- Less control over model behaviour; cannot customise for WidgetAI-specific business rules (e.g., boost newly listed products, suppress out-of-stock items)

## Decision

**We adopt a Hybrid Two-Stage Retrieval + Ranking architecture (Option C)** with a popularity-based cold-start fallback.

### Architecture Overview

```
Buyer request (store_id, visitor_id, context)
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  Recommendation Engine Service  (Python / FastAPI)          │
  │                                                             │
  │  1. RETRIEVAL — Candidate Generation                        │
  │     ├── Collaborative Filtering retrieval                   │
  │     │   (pre-computed user–item scores from ALS model)      │
  │     │   stored in Redis as sorted sets (ZRANGEBYSCORE)      │
  │     │                                                       │
  │     ├── Content-Based retrieval                             │
  │     │   (product embedding similarity via HNSW index)       │
  │     │   stored in a vector store (Pinecone / pgvector)      │
  │     │                                                       │
  │     └── Popularity fallback                                 │
  │         (top-N by sales rank per store, cached in Redis)   │
  │                                                             │
  │  2. MERGING — Candidate deduplication + union               │
  │     (typically 100–500 candidates)                          │
  │                                                             │
  │  3. RANKING — Lightweight LightGBM re-ranker                │
  │     (features: CTR history, recency, price affinity,        │
  │      stock level, seller boost rules)                       │
  │                                                             │
  │  4. FILTERING — Business rules post-filter                  │
  │     (remove out-of-stock, enforce category exclusions)      │
  │                                                             │
  │  5. RETURN top-K products (default K = 8)                   │
  └─────────────────────────────────────────────────────────────┘
        │
        ▼
   Widget renders personalised product grid
```

### Training Pipeline

```
Raw Events (Kafka)
    │  (click, purchase, impression, add-to-cart)
    ▼
Analytics Pipeline (Spark / Flink)
    │  feature engineering: user–item interaction matrix,
    │  product embeddings (sentence-transformers on title+description)
    ▼
Feature Store (Redis — online store; S3 — offline store)
    │
    ▼
Model Training (SageMaker / Vertex AI — scheduled nightly)
    │  ├── ALS matrix factorisation (collaborative filtering)
    │  └── LightGBM ranker (ranking)
    ▼
Model Registry (MLflow)
    │
    ▼
Model Serving (deployed to Recommendation Engine Service on promotion)
```

### Cold-Start Strategy

| Scenario | Strategy |
|----------|----------|
| New visitor (no history) | Return store's top-K products by sales rank (popularity fallback) |
| New product (no interactions) | Content-based retrieval only (embedding similarity to buyer's viewed items) |
| New store (no sales history) | Return products from seller's manually curated "featured" list; fall back to newest listings |

### Serving Latency Budget

| Step | Target Latency |
|------|---------------|
| Redis retrieval (collaborative) | < 5 ms |
| Vector similarity search (content) | < 20 ms |
| LightGBM ranking (100 candidates) | < 10 ms |
| Total (p99) | < 100 ms |

## Consequences

**Positive:**
- The hybrid approach handles cold-start gracefully, ensuring new stores and new products receive recommendations immediately
- Pre-computed collaborative filtering scores in Redis deliver sub-5 ms retrieval; total p99 latency target of 100 ms is achievable
- The two-stage design allows the retrieval step to run cheaply at scale while concentrating ML compute in the lighter ranking step
- Multi-tenant isolation is enforced at the retrieval stage: each store's candidate pool is scoped to `store_id` as the partition key

**Negative / Risks:**
- Two models (ALS + LightGBM) require ongoing maintenance, retraining, monitoring for model drift, and A/B evaluation infrastructure
- The vector index for content-based retrieval adds operational complexity (Pinecone managed service recommended to reduce this)
- Nightly batch retraining means the model does not reflect very recent interactions; a streaming update mechanism may be needed as the platform matures

**Mitigations:**
- Adopt MLflow for model versioning and experiment tracking; require model performance regression tests before promotion to production
- Implement a shadow-mode A/B testing framework: route 5% of traffic to a new model variant; compare CTR and conversion rate before full rollout
- Use Pinecone or `pgvector` (PostgreSQL extension) for the vector index to avoid self-managing a vector database
- The popularity fallback guarantees the widget always renders something useful, even if both ML models are unavailable (graceful degradation)
