# PLAYBOOK C — SAAS / MULTI-TENANT — aws / root

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-c-saas-multi-te.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **aws** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

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

## Probe adjustment (aws × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
