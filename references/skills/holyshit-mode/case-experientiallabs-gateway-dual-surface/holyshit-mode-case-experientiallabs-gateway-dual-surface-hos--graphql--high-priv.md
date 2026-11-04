# Host-header ACL bypass on Caddy `/metrics` + `/debug/pprof` — graphql / high-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hos.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `server: Caddy`. `GET /metrics` with `Host: wm.xplabs.ai` -> **403**, but
  `Host: 127.0.0.1` (or `localhost`) via `--resolve 127.0.0.1:443:<IP>` -> **200**.
- Same flip on `/debug/pprof`, `/debug/vars`, `/internal`, `/admin`. Bodies 0-byte but the
  **loopback-only ACL is Host-header/SNI-bound and remotely spoofable**.
- Class lesson: many Caddy/nginx vhosts protect internal/monitoring sites by Host-match.
  **Always try `Host: localhost`/`Host: 127.0.0.1` against 403/404 on internal hosts.**

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
