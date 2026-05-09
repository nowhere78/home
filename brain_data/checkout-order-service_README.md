# Checkout / Order Service

Manages the buyer cart, order lifecycle, and inventory reservation.

## Responsibilities

- Cart creation and management (guest + authenticated carts)
- Order lifecycle: `PENDING` → `PAYMENT_INITIATED` → `PAID` → `FULFILLED` → `SHIPPED` → `DELIVERED`
- Inventory reservation (optimistic lock on product variant stock)
- Publishes `order.created`, `order.paid`, `order.fulfilled` events to Kafka

## Tech Stack

- **Runtime:** Node.js 20
- **Database:** PostgreSQL (orders, line items, inventory) — see [ADR-002](../../adr/ADR-002-data-tier-design.md)
- **Cache:** Redis (cart state)
- **Messaging:** Kafka (order lifecycle events)

## Local Development

```bash
npm install
npm run dev
```

Service listens on `http://localhost:4004`.
