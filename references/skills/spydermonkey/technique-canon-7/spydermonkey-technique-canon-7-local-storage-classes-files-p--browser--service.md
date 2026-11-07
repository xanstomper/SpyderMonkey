# Local storage classes (files, prefs, caches) — browser / service

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-local-storage-classes-files-p.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **browser** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Secrets/PII in app files, sqlite dbs, shared prefs, caches readable from your own build (the SPY-013 id-adopted-session family is the session twin). Decisive test: your build's data dump — live secret/PII material = the finding.

## Probe adjustment (browser × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
