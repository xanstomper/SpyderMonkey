# Cost-free discrimination (do NOT generate completions — every /invocations call bills the upstream) — wasm / low-priv

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-cost-free-dis.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **wasm** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Point `image_url` at a target and read the error, **not** a completion:

| `image_url` target | Error/echo | Meaning |
|---|---|---|
| `http://169.254.169.254/...` | `HTTP 404 error` | IMDS reachable; IMDSv2 → 404 without token (hardened, reach confirmed) |
| `http://127.0.0.1:8000/` | `HTTP 404 error` | a real HTTP service answers on that loopback port |
| `http://127.0.0.1:5432/` | `500 Cannot connect to host ... ssl:default [Connect call failed]` | loopback TLS listener there (Postgres etc.) |
| `http://127.0.0.1:9090/` | `500 Cannot connect to host` | closed/filtered |
| `http://<ext-host>:8000/` or `10.0.0.1` | hang/timeout | DNS resolves but connect blocked — SSRF is **loopback/IMDS-scoped**, not arbitrary-everywhere |

## Probe adjustment (wasm × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
