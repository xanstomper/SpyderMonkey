# DKIM key length and selector hygiene — cloud / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-dkim-key-length-and-selector-hy.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

DKIM RSA key < 1024 bits or stale selectors pointing at dead infra. Decisive test: selector DNS lookup + published key size parse = the posture finding.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
