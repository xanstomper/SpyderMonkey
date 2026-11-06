# PLAYBOOK C — SAAS / MULTI-TENANT — chain composition

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-c-saas-multi-te.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

**Objective**: validate tenant isolation, subscription enforcement, and admin boundaries.

**Phase 1 — Recon**
- Tenant enumeration: subdomain (`tenant.target.com`) vs path (`target.com/tenant`) vs
  header (`X-Tenant-ID`). Map isolation model.
- CT logs + DNS for forgotten tenant subdomains (dangling CNAME takeover).

**Phase 2 — Tenant Isolation**
- **IDOR across tenants**: `GET /api/tenant-a/resource/123` with tenant-b token.
- **Shared infrastructure**: Redis, DB, queue — can you leak across via cache keys,
  pub/sub channels, job queues?
- **Feature flags**: can tenant-a enable enterprise features by guessing flag names?
- **Subdomain takeover**: tenant churn leaves orphaned DNS → cloud service takeover.

**Phase 3 — Subscription & Billing**
- Downgrade-with-features: cancel subscription, verify enterprise features revoke immediately.
- Trial re-spam: email tricks (`+tag`, dots, unicode) to farm infinite trials.
- Usage metering: can you reset/rollback usage counters via API or race conditions?
- Webhook integrity: unsigned subscription events → free upgrades (replay test).

**Phase 4 — Admin & Superuser**
- Admin panel discovery: `/admin`, `/internal`, `/ops` — 405-matrix verify.
- Impersonation endpoints: `POST /admin/impersonate` with tenant-admin token — BFLA test.
- Audit logs: are admin actions logged? Can admins wipe their own logs?

**Phase 5 — API & Integration**
- OAuth app validation: third-party integrations with over-scoped permissions.
- API key scoping: read-only keys that can write? Write keys that can delete?
- Webhook payload validation: SSRF in webhook URLs, blind payload injection.

**Deliverable**: tenant-isolation map, subscription-bypass findings, admin-boundary
violations, integration-trust model, dangling-takeover candidates.

---

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
