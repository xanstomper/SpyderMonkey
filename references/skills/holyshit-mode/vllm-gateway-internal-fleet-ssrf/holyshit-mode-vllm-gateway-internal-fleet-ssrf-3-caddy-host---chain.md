# 3. Caddy Host-header ACL flip (loopback-only intent defeat) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-3-caddy-host-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `server: Caddy` internal gateway. Public `Host: <host>` on `/metrics`, `/debug/pprof`, `/debug/vars`,
  `/admin`, `/internal` → **403** (loopback-only intent). With `Host: 127.0.0.1` (or `localhost`),
  via `--resolve 127.0.0.1:443:<gw-ip>`, those paths → **200** (empty body for non-existent routes,
  real content for real ones). The ACL is **Host/SNI-bound and remotely spoofable** = internet-reachable
  bypass of a loopback-only surface. Medium finding by itself; pairs with the SSRF above.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
