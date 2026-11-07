# U16 Human & process — cloud / machine

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u16-human-process.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- [ ] Authorization and approval chains documented; no unapproved human testing
- [ ] Helpdesk, recovery, exception, and break-glass processes reviewed
- [ ] Awareness/reporting controls assessed through documentation and tabletop
- [ ] Third-party onboarding/offboarding and access reviews measured
- [ ] Findings framed as process improvements, never as coercion or deception

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
