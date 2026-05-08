# Auth Service

Issues and validates JWTs; manages seller and buyer identities; enforces RBAC.

## Responsibilities

- User registration and login (email/password with bcrypt hashing)
- OAuth 2.0 social login (Google, GitHub)
- JWT access token issuance (15-minute TTL) and refresh token rotation
- Role-based access control: `seller`, `buyer`, `admin`
- Refresh token blocklist (Redis) for logout / token revocation

## Tech Stack

- **Runtime:** Node.js 20
- **Database:** PostgreSQL (users, refresh tokens, roles)
- **Cache:** Redis (token blocklist)
- **JWT:** `jsonwebtoken` library; RS256 signing (asymmetric keys)

## Local Development

```bash
npm install
npm run dev
```

Service listens on `http://localhost:4001`.
