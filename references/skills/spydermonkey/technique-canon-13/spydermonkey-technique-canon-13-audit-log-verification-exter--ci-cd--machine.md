# Audit-log verification (external signal) — ci-cd / machine

- source canon: `spydermonkey/technique-canon-13.md`
- base technique: `spydermonkey-technique-canon-13-audit-log-verification-exter.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Missing log coverage inferred from unlogged test actions visible server-side — provable only from the operator's own visibility; characterize as hypothesis-grade from client-visible traces. Decisive test: none without operator logs — the honest ceiling row.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
