# 3b. CONFIRMED — Host-header ACL bypass on `/metrics` + `/debug/pprof` (Caddy) (score 55) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3b-confirmed-host-hea.md`
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

- Serve is **Caddy** (`server: Caddy`). `wm.xplabs.ai/metrics` returns **403** for the public
  hostname, but with `Host: 127.0.0.1` (or `localhost`) it returns **200** — same for
  `/debug/pprof`, `/debug/pprof/*`, `/debug/vars`, `/internal`, `/admin`.
- **EVIDENCE:** `GET /metrics` with `Host: 127.0.0.1` (via `--resolve 127.0.0.1:443:34.44.95.184`)
  → HTTP/2 200 (vs 403 for `Host: wm.xplabs.ai`). Bodies currently 0-byte, but the **ACL is
  Caddy Host-header/SNI-bound and remotely spoofable** — the loopback-only intent for
  metrics/pprof is defeated from the internet.
- **IMPACT:** Exposes an intended-loopback-only surface (metrics/pprof) to remote attackers via
  trivial Host-spoofing → internal site discovery + potential data scrape. MEDIUM.
- **CONFIDENCE:** High (status-code flip is deterministic).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
