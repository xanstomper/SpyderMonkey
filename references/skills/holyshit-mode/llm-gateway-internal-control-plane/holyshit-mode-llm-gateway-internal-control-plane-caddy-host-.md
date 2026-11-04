# Caddy Host-header ACL bypass on monitoring/metrics

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
