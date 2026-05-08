# D1 — FAQ Document: WidgetAI Working Backwards

## External FAQs
*Questions a potential customer or member of the media might ask about WidgetAI.*

---

### Q1. How is WidgetAI different from simply signing up for Shopify or Gumroad?

**A:** Shopify and Gumroad are destination platforms — they require your customers to leave your site, visit a separate storefront URL, and complete a purchase in a foreign environment. That context switch increases abandon rates and weakens your brand. WidgetAI is an *embedded* experience: the entire product catalogue, recommendation engine, and checkout live inside your existing webpage. There is no redirect, no separate domain to maintain, and no monthly platform fee that scales with your revenue. You keep your audience where you already have their attention, and you keep more of every dollar you earn.

---

### Q2. Is my customers' payment data secure? Who handles it?

**A:** WidgetAI never touches raw card data. All payment processing is delegated to **Stripe**, which operates under PCI DSS Level 1 compliance — the highest certification available in the payments industry. The widget communicates with Stripe's JavaScript SDK directly in the buyer's browser, so sensitive financial information is never transmitted through WidgetTech's servers. Additionally, all widget-to-backend communication is encrypted in transit (TLS 1.3), and WidgetAI undergoes regular third-party penetration testing. Sellers can review WidgetTech's security posture at any time via the Trust Centre in the dashboard.

---

### Q3. My website already loads slowly — will adding WidgetAI make things worse?

**A:** No. WidgetAI is engineered for minimal host-page impact. The embed snippet loads asynchronously, so it never blocks your page's critical rendering path. The widget core (JavaScript + styles) is served from a globally distributed CDN with aggressive edge caching, keeping the initial payload under 40 KB gzipped. The recommendation engine and product catalogue data are fetched lazily — only after the widget enters the visitor's viewport — so pages with the widget consistently score within 5 points of their pre-widget Lighthouse performance score in our benchmark testing. We also publish real-world Core Web Vitals results on our status page so you can verify this independently.

---

## Internal FAQs
*Questions that internal stakeholders — CIO, CEO, and other executives — might raise about WidgetAI.*

---

### Q4 (Internal). How does WidgetAI generate revenue, and what does the unit economics model look like at scale?

**A:** WidgetAI operates a SaaS subscription model with three tiers: a free tier (capped at 50 transactions/month to drive top-of-funnel adoption), a Pro tier at $19/month (unlimited transactions, advanced analytics), and a Business tier at $79/month (multi-product catalogues, A/B testing, priority SLA). We do not take a percentage of gross merchandise volume — a deliberate positioning decision that makes our pricing dramatically more attractive to high-volume sellers compared to revenue-share platforms. Our target payback period for a Pro subscriber is under six months given current infrastructure cost per tenant. At 10,000 paying subscribers the projected gross margin is approximately 74%, rising to 81% at 50,000 subscribers as CDN and ML inference costs are amortised across a larger base.

---

### Q5 (Internal). What is our vendor lock-in exposure, particularly around Stripe, and what is the contingency plan?

**A:** Stripe is our sole external payment processor at launch, which is intentional — Stripe's developer experience and fraud tooling significantly accelerates time-to-market. However, the payment integration is architected behind an internal `PaymentProvider` interface within the Payment Integration Service. Swapping in an alternate provider (e.g., Adyen, Braintree, PayPal) requires implementing that interface and updating configuration — no changes to the checkout widget or order service are needed. We have documented this as a formal Architectural Decision Record (ADR-003). The contingency trigger for adding a second provider is if Stripe's uptime SLA falls below 99.9% over any rolling 90-day period, or if regulatory requirements in a target market preclude Stripe's use.

---

### Q6 (Internal). How does the architecture scale to support projected growth, and where are the most likely bottlenecks?

**A:** The system is designed around independently deployable microservices (API Gateway, Auth, Product Catalogue, Recommendation Engine, Checkout/Order, Payment Integration, and supporting infrastructure). Each service is containerised (Docker) and deployed on Kubernetes with horizontal pod autoscaling, allowing individual components to scale under load independently. The most load-sensitive path is widget initialisation — the sequence that fetches product data and recommendation scores on page load for every visitor to every embedded page. This path is protected by a multi-layer caching strategy: Redis in-process at the Recommendation Engine, CDN-level caching for static product data, and read replicas on the PostgreSQL product catalogue. Our load-test baseline is 10,000 simultaneous widget loads with p99 latency under 300 ms. The anticipated first bottleneck at extreme scale (>1M active widgets) is the real-time ML inference layer; the mitigation roadmap includes asynchronous pre-computation of recommendation vectors and potential migration to a dedicated ML serving platform (e.g., AWS SageMaker Inference).
