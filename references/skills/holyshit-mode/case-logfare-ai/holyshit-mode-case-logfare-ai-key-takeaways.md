# Key Takeaways

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. **FastAPI `openapi.json` exposure** gave full endpoint map including undocumented SSO flow
2. **CORS test on all endpoints** revealed arbitrary origin reflection with credentials — always test beyond login
3. **Rate limiter inconsistency** between rapid sequential vs. malformed requests — test both patterns
4. **Discord OAuth state cookie** properly implemented (HS256 JWT, 10-min expiry, secure nonce)
5. **Uniform error messages** prevented user enumeration via API key format
6. **postMessage with `window.location.origin`** is correct — don't false-alarm
7. **Subdomain CORS differential** — main API vulnerable, subdomains safe

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
