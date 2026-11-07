# Withdrawal threshold and fee dodge — mesh / expired

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-withdrawal-threshold-and-fee-do.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mesh** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

Min-withdrawal/fee logic enforced client-side (button disable, computed fee in JS) while the API accepts the raw request. Decisive test: submit the raw withdrawal POST for 1 cent below threshold on a test account — acceptance = the class; the payload is never the point, the server's acceptance is.

## Probe adjustment (mesh × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
