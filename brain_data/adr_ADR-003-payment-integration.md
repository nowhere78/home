# ADR-003: Payment Integration — Stripe

**Status:** Accepted  
**Date:** 2026-04-22  
**Authors:** WidgetAI Architecture Team

---

## Context

WidgetAI must process payments on behalf of sellers. This introduces significant requirements:

- **Security**: raw cardholder data must never touch WidgetAI servers (PCI-DSS compliance)
- **Multi-party payments**: a buyer pays a seller; WidgetAI may take a platform fee; the seller receives the remainder
- **Global coverage**: sellers and buyers can be located in different countries and currencies
- **Webhook reliability**: payment status changes (succeeded, failed, refunded) must be reliably communicated back to WidgetAI
- **Fraud prevention**: card testing attacks and fraudulent orders must be minimised
- **Seller onboarding**: sellers must be able to connect their bank accounts without WidgetAI holding funds in escrow

We must choose a payment processor and define how it integrates into the platform.

## Options Considered

### Option A: Stripe
Full-stack payment platform with client SDKs (Stripe.js / Stripe Elements), server SDKs, Stripe Connect for marketplace payouts, Radar for fraud detection, and extensive webhook infrastructure.

**Pros:**
- Stripe.js tokenises card data in the browser; PCI-DSS scope is reduced to SAQ-A
- Stripe Connect supports three account types (Standard, Express, Custom) for flexible seller onboarding
- PaymentIntents API handles 3D Secure authentication automatically
- Stripe Radar (ML-based fraud scoring) is included at no additional cost
- Idempotency keys on all write operations prevent double-charges on retry
- Webhooks are signed (HMAC-SHA256); replay attacks are prevented
- Available in 46+ countries; supports 135+ currencies

**Cons:**
- Transaction fees (2.9% + 30¢ per successful card charge; additional fees for Connect)
- Vendor lock-in: migrating away from Stripe requires significant rework of the payment flow
- Stripe Connect Express/Custom requires accepting Stripe's terms of service on behalf of sellers

### Option B: Braintree (PayPal)
Another full-featured payment platform with Drop-in UI, vault, and Venmo/PayPal support.

**Pros:**
- Good PayPal and Venmo integration
- Competitive pricing for high-volume merchants

**Cons:**
- Marketplace / platform payouts are complex and less developer-friendly than Stripe Connect
- Smaller developer community; fewer third-party integrations
- Less mature fraud tooling compared to Stripe Radar

### Option C: Adyen
Enterprise-grade global payment platform.

**Pros:**
- Excellent global coverage and local payment methods
- Competitive interchange rates at high volume
- Unified commerce (online + in-person)

**Cons:**
- Minimum volume requirements make it unsuitable for small sellers
- Integration complexity is higher; less suitable for a self-serve platform
- Setup time is significantly longer (weeks of onboarding)

### Option D: Build custom payment processing (direct card network integration)
Integrate directly with card networks or issuing banks.

**Pros:**
- Full control; lowest per-transaction cost at extreme scale

**Cons:**
- Requires full PCI-DSS Level 1 compliance (annual audit, QSA assessment, significant infrastructure investment)
- Years of engineering effort to build fraud, dispute, and reconciliation tooling
- Entirely out of scope for the current stage of the product

## Decision

**We adopt Stripe as the exclusive payment processor, using Stripe Connect for marketplace payouts.**

### Integration Architecture

```
 Browser (Widget)
     │
     │  1. Stripe.js / Payment Element (card tokenisation in iframe)
     ▼
 Stripe Servers ──── token/PaymentMethod ────► Payment Integration Service
                                                       │
                                      2. Create PaymentIntent (server-side)
                                                       │
                                                       ▼
                                               Stripe API
                                                       │
                                      3. Confirm payment (client-side)
                                                       │
                                                       ▼
                                               Stripe Servers
                                                       │
                                      4. Webhook: payment_intent.succeeded
                                                       │
                                                       ▼
                                       Payment Integration Service
                                         (verify HMAC signature)
                                                       │
                                      5. Publish: payment.completed event
                                                       │
                                            ┌──────────┴──────────┐
                                            ▼                     ▼
                                    Checkout Service      Notification Service
                                  (fulfil order)        (send receipt email)
```

### Stripe Connect Model

- **Seller onboarding:** Express accounts (Stripe hosts the onboarding UI; sellers provide KYC details directly to Stripe)
- **Application fee:** WidgetAI charges a configurable platform fee (e.g., 2%) on each transaction using the `application_fee_amount` parameter
- **Payouts:** Stripe pays sellers directly according to their configured payout schedule; WidgetAI never holds seller funds

### Security Controls

| Control | Implementation |
|---------|---------------|
| Card data isolation | Stripe.js Payment Element; no card data enters WidgetAI infrastructure |
| Webhook authenticity | `stripe.webhooks.constructEvent` with `STRIPE_WEBHOOK_SECRET`; reject invalid signatures |
| Idempotency | All PaymentIntent creation requests include a UUID idempotency key derived from the order ID |
| Secret management | `STRIPE_SECRET_KEY` stored in AWS Secrets Manager; rotated on compromise |
| Restricted keys | Separate restricted API keys per service (webhook handler key has only `read:charges` + `write:refunds`) |

## Consequences

**Positive:**
- PCI-DSS scope is minimised to SAQ-A; no cardholder data touches WidgetAI servers
- Stripe Radar provides ML-based fraud scoring out of the box, reducing fraudulent order rates
- Stripe Connect Express dramatically simplifies seller onboarding (minutes vs. days for custom bank integrations)
- Idempotency keys and signed webhooks make the integration robust against network failures
- Global coverage enables the platform to serve international sellers from day one

**Negative / Risks:**
- Vendor lock-in: the payment flow is deeply coupled to Stripe's API model (PaymentIntents, Payment Methods, Connect accounts)
- Transaction fees reduce seller margins; large sellers may request alternative processors in the future
- Stripe's terms of service prohibit certain business categories; sellers in restricted categories will be declined

**Mitigations:**
- Encapsulate all Stripe calls behind a `PaymentGateway` interface in the Payment Integration Service; this isolates the Stripe-specific implementation and simplifies a future processor migration if required
- Monitor Stripe's operational status page; implement a circuit breaker that pauses payment processing and queues orders if Stripe's API error rate exceeds a threshold
- Document the restricted business category policy clearly in the seller onboarding flow
