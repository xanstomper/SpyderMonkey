# T1 — Identity takeover (user · admin · tenant/IdP)

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
