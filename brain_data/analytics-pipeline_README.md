# Analytics Pipeline

Collects widget interaction events and materialises aggregate views for the seller dashboard.

## Responsibilities

- Ingest widget events (impressions, clicks, add-to-cart, purchase) via a Kafka topic
- Stream processing with Apache Flink or Spark Streaming
- Materialise aggregate metrics: conversion rate, revenue per product, top products by store
- Store aggregates in a columnar store (Amazon Redshift / BigQuery) for dashboard queries
- Expose a read API for the seller dashboard

## Tech Stack

- **Runtime:** Python 3.11 (stream processor), Node.js 20 (read API)
- **Streaming:** Apache Kafka → Apache Flink
- **Storage:** Amazon Redshift or BigQuery (aggregates), S3 (raw event archive)
- **Ingestion:** AWS Kinesis Data Streams → Lambda (serverless buffer)

## Local Development

```bash
# Start Kafka + Flink locally
docker compose up kafka flink

# Run stream processor
python processor.py
```
