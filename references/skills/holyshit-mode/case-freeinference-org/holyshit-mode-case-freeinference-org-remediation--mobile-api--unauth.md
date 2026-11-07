# Remediation — mobile-api / unauth

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-remediation.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. **Rate-limit** `/api/export` and `/api/dashboard?refresh=1` — lockout after 5 failed password attempts
2. **Replace shared secret** `madsys` with per-user tokens or session-based auth
3. **Add MFA** for refresh/export operations
4. **Restrict unauthenticated `/api/dashboard`** (returns stale cache anyway — gate it)

## Probe adjustment (mobile-api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
