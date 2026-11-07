# 3. Caddy Host-header ACL flip (loopback-only intent defeat)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `server: Caddy` internal gateway. Public `Host: <host>` on `/metrics`, `/debug/pprof`, `/debug/vars`,
  `/admin`, `/internal` → **403** (loopback-only intent). With `Host: 127.0.0.1` (or `localhost`),
  via `--resolve 127.0.0.1:443:<gw-ip>`, those paths → **200** (empty body for non-existent routes,
  real content for real ones). The ACL is **Host/SNI-bound and remotely spoofable** = internet-reachable
  bypass of a loopback-only surface. Medium finding by itself; pairs with the SSRF above.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
