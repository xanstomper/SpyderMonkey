# Rate-limit key rotation (X-Forwarded-For trust) — firmware / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-rate-limit-key-rotation-x-forwa.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **firmware** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Limits keyed on a client-supplied header = limit-free access. Decisive test: same request 6× with rotating X-Forwarded-For — all 200 past the documented limit = the class (the arithmetic, not a brute).

## Probe adjustment (firmware × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
