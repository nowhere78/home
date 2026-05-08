# Recommendation Engine

AI-powered product recommendation service. Serves personalized product rankings for the widget.

## Responsibilities

- Two-stage retrieval + ranking pipeline (see [ADR-004](../../adr/ADR-004-recommendation-architecture.md))
- Collaborative filtering retrieval (pre-computed ALS scores in Redis)
- Content-based retrieval (product embedding similarity via vector index)
- Popularity fallback for cold-start scenarios
- LightGBM re-ranker

## Tech Stack

- **Runtime:** Python 3.11, FastAPI
- **Models:** ALS (implicit library), LightGBM
- **Feature store:** Redis (online), S3 (offline)
- **Vector index:** Pinecone or pgvector

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 4003
```

Service listens on `http://localhost:4003`.
