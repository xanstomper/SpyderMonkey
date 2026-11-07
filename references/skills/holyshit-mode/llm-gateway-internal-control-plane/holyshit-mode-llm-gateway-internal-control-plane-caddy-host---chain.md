# Caddy Host-header ACL bypass on monitoring/metrics — chain composition

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-caddy-host-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
