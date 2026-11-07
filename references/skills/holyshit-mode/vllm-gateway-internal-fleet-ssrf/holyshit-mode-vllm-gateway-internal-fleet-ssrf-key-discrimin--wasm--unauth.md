# Key discriminators learned — wasm / unauth

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-key-discrimin.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wasm** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (wasm × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
