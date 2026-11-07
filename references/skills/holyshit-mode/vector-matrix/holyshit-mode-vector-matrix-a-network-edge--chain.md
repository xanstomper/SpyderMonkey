# A. NETWORK / EDGE — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-a-network-edge.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- TLS: weak ciphers/certs, SAN leaks, hostname mismatch, cert pinning gaps — sslscan output
- HSTS/CSP/XFO/Referrer-Policy/CORS misconfig — `Origin: evil.test` reflection on authed endpoints = cred theft
- Request smuggling (CL.TE / TE.CL / TE.TE) — differential timing on front/back servers
- HTTP/2 & HTTP/3 quirks — rapid reset, header-name case desync, QPACK smuggling
- Host-header injection — password-reset poisoning, cache poisoning, SSRF pivot
- Web cache poisoning/deception — unkeyed input reflection (params, headers), X-Forwarded-* trust
- IP honoring — X-Forwarded-For / X-Real-IP / CF-Connecting-IP acceptance = limiter bypass + log poisoning
- Origin exposure — direct IP hit on discovered origin bypassing CDN protections entirely

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
