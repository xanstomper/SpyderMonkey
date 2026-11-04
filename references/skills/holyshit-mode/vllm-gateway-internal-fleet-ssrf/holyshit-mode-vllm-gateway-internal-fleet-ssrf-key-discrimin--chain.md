# Key discriminators learned — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-key-discrimin.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Open-service vs closed vs TLS-listener** is fully distinguishable from the error echo → this IS
  a working internal **port scanner** with no token burn.
- **Content-received signal:** when the fetched response is valid HTTP 200 but not an image, the
  error becomes `Failed to load image: cannot identify ...` (NOT connect/404) → you retrieved real
  **content** from an internal endpoint. On the target, `127.0.0.1:8000/{docs,metrics,openapi.json,health}`
  returned this = **loopback-only internal `/docs` + `/metrics` + `/openapi.json` readable via SSRF**
  that the public Host-header ACL hid.
- **401 echo:** `image_url: http://127.0.0.1:8000/v1/models` → `HTTP 401 error` — internal route
  auth-matches public; tells you the internal service still enforces keys (log as coverage).
- ICMP/random external hosts hang (000 timeout) → the fetch egress is filtered beyond loopback/IMDS.
  Run enough targets to characterize the ceiling honestly, then state it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
