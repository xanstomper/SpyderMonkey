# Contrast vs the vulnerable GoTrue variant (g***REDACTED***/g***REDACTED***) — api / low-priv

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The earlier findings (redirect_uri forwarded verbatim, anon key client-exposed, unthrottled code
exchange) come from an **un-hardened GoTrue deployment**. Always fingerprint BEFORE assuming: server-side
PKCE + no client anon key + hardcoded redirect_to ⇒ the g***REDACTED*** chain does not apply; pivot.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
