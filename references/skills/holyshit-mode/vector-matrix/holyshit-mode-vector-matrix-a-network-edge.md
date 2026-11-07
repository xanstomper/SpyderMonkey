# A. NETWORK / EDGE

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- TLS: weak ciphers/certs, SAN leaks, hostname mismatch, cert pinning gaps — sslscan output
- HSTS/CSP/XFO/Referrer-Policy/CORS misconfig — `Origin: evil.test` reflection on authed endpoints = cred theft
- Request smuggling (CL.TE / TE.CL / TE.TE) — differential timing on front/back servers
- HTTP/2 & HTTP/3 quirks — rapid reset, header-name case desync, QPACK smuggling
- Host-header injection — password-reset poisoning, cache poisoning, SSRF pivot
- Web cache poisoning/deception — unkeyed input reflection (params, headers), X-Forwarded-* trust
- IP honoring — X-Forwarded-For / X-Real-IP / CF-Connecting-IP acceptance = limiter bypass + log poisoning
- Origin exposure — direct IP hit on discovered origin bypassing CDN protections entirely

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
