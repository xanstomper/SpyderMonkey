# 1. vLLM `image_url` SSRF + COST-FREE status oracle (the big one)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

On vLLM-backed OpenAI-compatible inference endpoints, `POST {api}/invocations` (and some
`/v1/chat/completions`) accept an `image_url` content part that the worker **fetches server-side**
and — crucially — **reports the fetched HTTP status / connect result in the error message**.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
