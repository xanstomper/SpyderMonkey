# 3b. CONFIRMED — Host-header ACL bypass on `/metrics` + `/debug/pprof` (Caddy) (score 55) — container / unauth

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3b-confirmed-host-hea.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
