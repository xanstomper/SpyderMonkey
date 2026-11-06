# CORS on Error Responses — kubernetes / low-priv

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-cors-on-error-responses.md`
- bindings: **WSTG-CLNT-03** · **CWE-942** · **ATT&CK T1557**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The CORS headers (`access-control-allow-origin: <any>`, `access-control-allow-credentials: true`)
are present on ALL response codes including 401/403/404/405/429. This means a malicious site
can send requests to destructive endpoints and read the error responses, confirming server-side
processing even when blocked.

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
