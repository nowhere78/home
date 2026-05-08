# API Gateway

Single entry-point for all external client traffic. Responsibilities:

- TLS termination
- JWT validation (delegates to Auth Service)
- Rate limiting (token-bucket per API key / IP)
- Request routing to downstream microservices
- Observability: request logging, tracing header injection

## Tech Stack

- **Runtime:** Node.js 20 (Express + http-proxy-middleware) or Kong Gateway
- **Auth:** Validates `Authorization: Bearer <JWT>` header; forwards decoded claims downstream
- **Rate limiting:** Redis-backed sliding window counter

## Local Development

```bash
npm install
npm run dev
```

Service listens on `http://localhost:4000`.
