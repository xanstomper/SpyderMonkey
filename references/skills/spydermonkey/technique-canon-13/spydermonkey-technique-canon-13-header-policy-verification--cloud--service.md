# Header-policy verification — cloud / service

- source canon: `spydermonkey/technique-canon-13.md`
- base technique: `spydermonkey-technique-canon-13-header-policy-verification.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **cloud** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

CSP/HSTS/X-Frame/X-Content-Type/Referrer-Policy matrix (the header-posture canon). Decisive test: the posture matrix = the rows.

## Probe adjustment (cloud × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
