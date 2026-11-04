# T2 — Web-app tenant takeover — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t2-web-app-tenant-takeover.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Cross-tenant IDOR on tenant-scoped resources; tenant-selection confusion
  (X-Tenant-ID vs Host vs path); schema-library IDs for structural tenant mapping;
  subdomain takeover → cookie-domain capture → session of any user (validate ONLY on
  operator-owned records; external dangling domains = third-party action — document
  feasibility instead).
- **DECISIVE PROOF:** a cross-tenant row read (`content-range: */1` on the foreign
  tenant), or proof-of-control page on an OWNED dangling record. Then STOP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
