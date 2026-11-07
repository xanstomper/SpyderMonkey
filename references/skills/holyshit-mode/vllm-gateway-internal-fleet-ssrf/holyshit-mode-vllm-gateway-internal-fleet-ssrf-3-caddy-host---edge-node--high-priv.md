# 3. Caddy Host-header ACL flip (loopback-only intent defeat) — edge-node / high-priv

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-3-caddy-host-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge-node** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `server: Caddy` internal gateway. Public `Host: <host>` on `/metrics`, `/debug/pprof`, `/debug/vars`,
  `/admin`, `/internal` → **403** (loopback-only intent). With `Host: 127.0.0.1` (or `localhost`),
  via `--resolve 127.0.0.1:443:<gw-ip>`, those paths → **200** (empty body for non-existent routes,
  real content for real ones). The ACL is **Host/SNI-bound and remotely spoofable** = internet-reachable
  bypass of a loopback-only surface. Medium finding by itself; pairs with the SSRF above.

## Probe adjustment (edge-node × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
