# Ghost-route discrimination — mobile-api / low-priv

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-ghost-route-discriminat.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

404s returning `application/json` = real routing layer (not SPA fallback). Only `text/html`
404/200s are ghosts. Check `/openapi.json`, `/docs`, `/api/docs` — but expect them genuinely absent on hardened non-FastAPI targets.

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
