# Host-header ACL bypass on Caddy `/metrics` + `/debug/pprof`

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `server: Caddy`. `GET /metrics` with `Host: wm.xplabs.ai` -> **403**, but
  `Host: 127.0.0.1` (or `localhost`) via `--resolve 127.0.0.1:443:<IP>` -> **200**.
- Same flip on `/debug/pprof`, `/debug/vars`, `/internal`, `/admin`. Bodies 0-byte but the
  **loopback-only ACL is Host-header/SNI-bound and remotely spoofable**.
- Class lesson: many Caddy/nginx vhosts protect internal/monitoring sites by Host-match.
  **Always try `Host: localhost`/`Host: 127.0.0.1` against 403/404 on internal hosts.**

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
