# Cost-free discrimination (do NOT generate completions — every /invocations call bills the upstream) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-cost-free-dis.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Point `image_url` at a target and read the error, **not** a completion:

| `image_url` target | Error/echo | Meaning |
|---|---|---|
| `http://169.254.169.254/...` | `HTTP 404 error` | IMDS reachable; IMDSv2 → 404 without token (hardened, reach confirmed) |
| `http://127.0.0.1:8000/` | `HTTP 404 error` | a real HTTP service answers on that loopback port |
| `http://127.0.0.1:5432/` | `500 Cannot connect to host ... ssl:default [Connect call failed]` | loopback TLS listener there (Postgres etc.) |
| `http://127.0.0.1:9090/` | `500 Cannot connect to host` | closed/filtered |
| `http://<ext-host>:8000/` or `10.0.0.1` | hang/timeout | DNS resolves but connect blocked — SSRF is **loopback/IMDS-scoped**, not arbitrary-everywhere |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
