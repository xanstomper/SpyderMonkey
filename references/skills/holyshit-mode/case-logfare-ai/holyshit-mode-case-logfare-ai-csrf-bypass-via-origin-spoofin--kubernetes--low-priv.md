# CSRF Bypass via Origin Spoofing — kubernetes / low-priv

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-csrf-bypass-via-origin-spoofin.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The server's CSRF validation accepts `Origin: https://logfare.ai`. While browsers cannot set
this from a cross-origin context, this reveals the CSRF check is **Origin-only** with no token:
- `POST /v1/auth/logout` → 200, **NO CSRF CHECK AT ALL** (confirmed: works cross-origin from any origin)
- `POST /connections/revoke` → Origin check only (bypassable via curl with `Origin: https://logfare.ai`)
- `POST /v1/me/delete` → Origin check only
- `POST /v1/auth/regenerate-key` → Origin check only

**Logout endpoint is the critical CSRF gap: zero protection.** A malicious page can call
`fetch('https://logfare.ai/v1/auth/logout', {method:'POST', credentials:'include'})` and log out
any logged-in user who visits. CORS headers on the 200 response let the attacker confirm success.

If Origin check is ever bypassed (via Origin spoofing, Referer manipulation, or another bug),
the full destructive chain is exposed: account deletion, connection revocation, API key regeneration,
force logout — all reachable cross-origin with victim's session.

## Probe adjustment (kubernetes × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
