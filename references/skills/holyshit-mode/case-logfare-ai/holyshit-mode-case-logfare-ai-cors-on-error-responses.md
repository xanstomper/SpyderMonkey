# CORS on Error Responses

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-CLNT-03** · **CWE-942** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

The CORS headers (`access-control-allow-origin: <any>`, `access-control-allow-credentials: true`)
are present on ALL response codes including 401/403/404/405/429. This means a malicious site
can send requests to destructive endpoints and read the error responses, confirming server-side
processing even when blocked.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
