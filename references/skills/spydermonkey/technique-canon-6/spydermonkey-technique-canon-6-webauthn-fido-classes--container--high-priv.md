# WebAuthn/FIDO classes — container / high-priv

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-webauthn-fido-classes.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Origin/RP-ID scoping gaps, challenge entropy, credential-id enumeration, the SPY-101 allowCredentials:[] mint class. Decisive test: ceremony parameters observed on your own enrollment — the scoping delta is the finding.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
