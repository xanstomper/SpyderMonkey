# 3b. CONFIRMED — Host-header ACL bypass on `/metrics` + `/debug/pprof` (Caddy) (score 55) — windows / high-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3b-confirmed-host-hea.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **windows** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (windows × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
