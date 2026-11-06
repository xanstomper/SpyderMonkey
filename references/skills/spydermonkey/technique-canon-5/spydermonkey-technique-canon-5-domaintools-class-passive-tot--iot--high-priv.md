# Domaintools-class passive-total and sibling-brand mapping — iot / high-priv

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-domaintools-class-passive-tot.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Registration-tree expansion (registrant org → sibling brands) feeding the shared-backend hypothesis (the error-taxonomy canon-I test confirms). Decisive test: whois org field + the sibling's confirmed shared taxonomy.

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
