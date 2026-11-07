# Cost-free discrimination (do NOT generate completions — every /invocations call bills the upstream)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Point `image_url` at a target and read the error, **not** a completion:

| `image_url` target | Error/echo | Meaning |
|---|---|---|
| `http://169.254.169.254/...` | `HTTP 404 error` | IMDS reachable; IMDSv2 → 404 without token (hardened, reach confirmed) |
| `http://127.0.0.1:8000/` | `HTTP 404 error` | a real HTTP service answers on that loopback port |
| `http://127.0.0.1:5432/` | `500 Cannot connect to host ... ssl:default [Connect call failed]` | loopback TLS listener there (Postgres etc.) |
| `http://127.0.0.1:9090/` | `500 Cannot connect to host` | closed/filtered |
| `http://<ext-host>:8000/` or `10.0.0.1` | hang/timeout | DNS resolves but connect blocked — SSRF is **loopback/IMDS-scoped**, not arbitrary-everywhere |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
