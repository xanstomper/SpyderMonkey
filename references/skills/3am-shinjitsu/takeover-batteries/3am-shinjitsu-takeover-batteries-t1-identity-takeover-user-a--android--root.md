# T1 — Identity takeover (user · admin · tenant/IdP) — android / root

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t1-identity-takeover-user-a.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **android** · auth **root** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (android × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
