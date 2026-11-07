# CAPTCHA-gate anatomy (the Fastly _fs-ch class family) — mesh / service

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-captcha-gate-anatomy-the-fast.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **mesh** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

The challenge SVG/logo-strip is NOT the captcha — the form-adjacent JPEG is (engagement-ops). Decisive test: challenge-object inventory on the live edge — the anatomy map is the finding; solving is NOT attempted (the wall).

## Probe adjustment (mesh × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
