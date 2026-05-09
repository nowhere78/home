# Product Catalog Service

CRUD for products, variants, and media assets. Powers the widget product grid.

## Responsibilities

- Create / update / delete products and variants per seller store
- Full-text search via Elasticsearch
- Image asset metadata (URLs pointing to S3)
- Cache product listings in Redis (TTL 5 minutes, invalidated on write)

## Tech Stack

- **Runtime:** Node.js 20
- **Database:** DynamoDB (product records) — see [ADR-002](../../adr/ADR-002-data-tier-design.md)
- **Search:** Elasticsearch
- **Cache:** Redis

## Local Development

```bash
npm install
npm run dev
```

Service listens on `http://localhost:4002`.
