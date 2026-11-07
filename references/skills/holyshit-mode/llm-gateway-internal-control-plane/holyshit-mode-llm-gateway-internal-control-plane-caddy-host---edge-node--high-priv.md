# Caddy Host-header ACL bypass on monitoring/metrics — edge-node / high-priv

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-caddy-host-.md`
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

Internal gateways serve via Caddy. Monitoring paths (`/metrics`, `/debug/pprof*`, `/debug/vars`,
`/internal`, `/admin`) that return **403 for the public hostname** often flip to **200 with
`Host: 127.0.0.1`** (or `localhost`) — the loopback-only ACL is keyed on Host/SNI, not the
client IP, so it's spoofable remotely:

```
curl -k --resolve 127.0.0.1:443:<ip> -H 'Host: 127.0.0.1' https://127.0.0.1/metrics   # 403→200
```

`server: Caddy` in the response header confirms the stack. Note the 200 may be an empty shell
(0 bytes) if the real data binds to a different internal vhost — the status flip is still the
finding (defeats the loopback-only intent).

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
