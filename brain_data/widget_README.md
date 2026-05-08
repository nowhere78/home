# WidgetAI Embeddable Widget

Lightweight JavaScript/CSS bundle that sellers embed into any website, blog, or newsletter.

## Usage

Add the following snippet to any HTML page:

```html
<script
  src="https://cdn.widgetai.io/embed.js"
  data-store-id="YOUR_STORE_ID"
  data-theme="light"
  data-products="8"
></script>
```

The widget renders a responsive product grid with personalized recommendations, an add-to-cart button, and a hosted checkout flow. It uses a Shadow DOM to prevent host-page CSS from affecting the widget's appearance.

## Architecture

- **Rendering:** Vanilla JS + Shadow DOM (no framework dependency, ~20 KB gzipped)
- **API calls:** Fetches product and recommendation data from the API Gateway
- **Checkout:** Opens a hosted Stripe checkout page (no card data handled by the widget)
- **Events:** Fires impression, click, and purchase events to the Analytics Pipeline

## Local Development

```bash
npm install
npm run dev       # webpack-dev-server on http://localhost:8080
npm run build     # produces dist/embed.js
```

The `demo/index.html` file demonstrates the widget embedded in a sample page.

## Configuration Options

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `data-store-id` | string | required | Seller store identifier |
| `data-theme` | `light` \| `dark` | `light` | Widget color theme |
| `data-products` | number | `8` | Number of products to display |
| `data-locale` | string | `en-US` | Display language and currency formatting |
