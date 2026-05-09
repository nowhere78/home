# Seller Dashboard

Vue 3 + TypeScript single-page application for seller product management, order review, analytics, and Stripe Connect onboarding.

## Features

- **Product management:** Create, edit, and delete products; upload images; manage variants
- **Order management:** View order list, order detail, and fulfillment status updates
- **Analytics:** Revenue time-series chart, top products, conversion funnel
- **Stripe Connect onboarding:** Connect seller bank account for payouts
- **Settings:** Store name, widget appearance, notification preferences

## Tech Stack

| Concern | Library |
|---------|---------|
| Framework | **Vue 3** (Composition API + `<script setup>`) + **TypeScript** |
| State management | **Pinia** |
| Routing | **Vue Router 4** |
| HTTP client | **Axios** (with JWT refresh interceptor) |
| Styling | **Tailwind CSS 3** |
| Charts | **Chart.js 4** + **vue-chartjs** |
| Build | **Vite 5** |
| Tests | **Vitest** + **@vue/test-utils** |

## Project Structure

```
src/
├── api/            # Axios API modules (auth, products, orders, analytics, settings)
├── assets/         # Global CSS (Tailwind entry-point)
├── components/
│   ├── charts/     # RevenueChart, ConversionChart
│   ├── layout/     # AppLayout, Sidebar, TopBar
│   └── ui/         # BaseButton, BaseInput, BaseTextarea, BaseModal, BaseCard, BaseTable
├── router/         # Vue Router config + navigation guards
├── stores/         # Pinia stores (auth, products, orders, analytics, settings)
├── types/          # Shared TypeScript interfaces
└── views/          # Route-level page components
    ├── auth/       # LoginView, RegisterView
    ├── orders/     # OrderListView, OrderDetailView
    ├── products/   # ProductListView, ProductFormView
    ├── AnalyticsView.vue
    ├── DashboardView.vue
    ├── SettingsView.vue
    └── StripeConnectView.vue
```

## Local Development

```bash
# Install dependencies
npm install

# Start Vite dev server (http://localhost:3000)
npm run dev

# Type-check
npm run type-check

# Build for production
npm run build

# Run unit tests
npm run test
```

## Environment Variables

Copy `.env.example` to `.env` and adjust:

```
VITE_API_BASE_URL=http://localhost:3001/api
```

> **Note:** The Vite dev server proxies `/api` → `http://localhost:3001` by default (see `vite.config.ts`).
> Set `VITE_API_BASE_URL` to override the base URL when deploying.
