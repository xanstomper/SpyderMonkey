# Lessons — web-app / unauth

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-lessons.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. CORS finding severity is a function of auth model + cookie SameSite, not the reflection
   alone. Read raw Set-Cookie flags before rating; re-derive severity when auth model churns.
2. Targets get rebuilt between sessions (SPA → server-rendered). Diff the openapi route list
   across re-engagements like bundle hashes; don't grep a stale bundle.
3. Marketing copy about signup friction is not evidence — probe the register endpoint.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
