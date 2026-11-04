# A. NETWORK / EDGE — api / high-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-a-network-edge.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- TLS: weak ciphers/certs, SAN leaks, hostname mismatch, cert pinning gaps — sslscan output
- HSTS/CSP/XFO/Referrer-Policy/CORS misconfig — `Origin: evil.test` reflection on authed endpoints = cred theft
- Request smuggling (CL.TE / TE.CL / TE.TE) — differential timing on front/back servers
- HTTP/2 & HTTP/3 quirks — rapid reset, header-name case desync, QPACK smuggling
- Host-header injection — password-reset poisoning, cache poisoning, SSRF pivot
- Web cache poisoning/deception — unkeyed input reflection (params, headers), X-Forwarded-* trust
- IP honoring — X-Forwarded-For / X-Real-IP / CF-Connecting-IP acceptance = limiter bypass + log poisoning
- Origin exposure — direct IP hit on discovered origin bypassing CDN protections entirely

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
