# Payment Integration Service

Wraps the Stripe API and translates Stripe events to internal domain events.

## Responsibilities

- Create and confirm Stripe PaymentIntents
- Manage Stripe Connect Express accounts for seller onboarding
- Calculate and apply platform application fees
- Process and verify incoming Stripe webhooks (HMAC-SHA256 signature verification)
- Publish `payment.completed`, `payment.failed`, `payment.refunded` events

## Tech Stack

- **Runtime:** Node.js 20
- **External API:** Stripe (see [ADR-003](../../adr/ADR-003-payment-integration.md))
- **Database:** PostgreSQL (payment records, idempotency keys)
- **Messaging:** Kafka (payment domain events)

## Environment Variables

| Variable | Description |
|----------|-------------|
| `STRIPE_SECRET_KEY` | Stripe secret API key (stored in AWS Secrets Manager) |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook endpoint signing secret |
| `STRIPE_CONNECT_CLIENT_ID` | OAuth client ID for Stripe Connect |

## Local Development

```bash
npm install
npm run dev
```

Service listens on `http://localhost:4005`.

Use `stripe listen --forward-to localhost:4005/webhooks/stripe` for local webhook testing.
