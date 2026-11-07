# T1 — Identity takeover (user · admin · tenant/IdP) — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t1-identity-takeover-user-a.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **User account:** reset-flow abuse (no-secret reset path, rate-limit absence),
  credentials in accessible logs/env/backup/CI, session fixation or cookie-carrier,
  OAuth consent-abuse feasibility (document), password reuse across surfaced services
  (owned identity lists only).
- **Admin/privileged:** privilege claim persistence (mass-assignment gate — real only if
  a CONSUMER authorizes on the planted claim), role escalation via IDOR on role-grant
  endpoints, helpdesk reset trust (documentation only).
- **Tenant/IdP:** shared IdP secret leak (backup/firmware/CI), SAML signing key from
  artifacts, tenant-locator enumeration → cross-tenant account match, tenant-admin via
  OAuth app over-grant.
- **DECISIVE PROOF:** one authenticated session as the target identity or a token minted
  for the target `sub`. Then STOP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
