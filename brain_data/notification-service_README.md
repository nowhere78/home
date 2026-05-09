# Notification Service

Sends transactional email, SMS, and push notifications triggered by platform events.

## Responsibilities

- Consume `order.paid`, `order.shipped`, `payment.failed` events from Kafka
- Send transactional email via AWS SES / SendGrid
- Send SMS notifications via Twilio (optional, configurable per seller)
- Render notification templates (Handlebars / Jinja2)
- Dead-letter queue handling for failed notification deliveries

## Tech Stack

- **Runtime:** Node.js 20
- **Messaging:** Kafka consumer
- **Email:** AWS SES or SendGrid
- **SMS:** Twilio (optional)
- **Templates:** Handlebars

## Local Development

```bash
npm install
npm run dev
```

Service runs as a Kafka consumer; no HTTP server.
