# Key Takeaways — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-key-takeaways.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **FastAPI `openapi.json` exposure** gave full endpoint map including undocumented SSO flow
2. **CORS test on all endpoints** revealed arbitrary origin reflection with credentials — always test beyond login
3. **Rate limiter inconsistency** between rapid sequential vs. malformed requests — test both patterns
4. **Discord OAuth state cookie** properly implemented (HS256 JWT, 10-min expiry, secure nonce)
5. **Uniform error messages** prevented user enumeration via API key format
6. **postMessage with `window.location.origin`** is correct — don't false-alarm
7. **Subdomain CORS differential** — main API vulnerable, subdomains safe

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
