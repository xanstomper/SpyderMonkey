# Host-header ACL bypass on Caddy `/metrics` + `/debug/pprof` — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hos.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `server: Caddy`. `GET /metrics` with `Host: wm.xplabs.ai` -> **403**, but
  `Host: 127.0.0.1` (or `localhost`) via `--resolve 127.0.0.1:443:<IP>` -> **200**.
- Same flip on `/debug/pprof`, `/debug/vars`, `/internal`, `/admin`. Bodies 0-byte but the
  **loopback-only ACL is Host-header/SNI-bound and remotely spoofable**.
- Class lesson: many Caddy/nginx vhosts protect internal/monitoring sites by Host-match.
  **Always try `Host: localhost`/`Host: 127.0.0.1` against 403/404 on internal hosts.**

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
