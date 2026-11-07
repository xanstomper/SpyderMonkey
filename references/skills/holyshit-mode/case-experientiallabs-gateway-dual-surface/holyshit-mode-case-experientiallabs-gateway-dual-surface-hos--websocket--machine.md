# Host-header ACL bypass on Caddy `/metrics` + `/debug/pprof` — websocket / machine

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hos.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **websocket** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `server: Caddy`. `GET /metrics` with `Host: wm.xplabs.ai` -> **403**, but
  `Host: 127.0.0.1` (or `localhost`) via `--resolve 127.0.0.1:443:<IP>` -> **200**.
- Same flip on `/debug/pprof`, `/debug/vars`, `/internal`, `/admin`. Bodies 0-byte but the
  **loopback-only ACL is Host-header/SNI-bound and remotely spoofable**.
- Class lesson: many Caddy/nginx vhosts protect internal/monitoring sites by Host-match.
  **Always try `Host: localhost`/`Host: 127.0.0.1` against 403/404 on internal hosts.**

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
