# Mobile deep-link and app-link hijack (depth) — android / high-priv

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-mobile-deep-link-and-app-link.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- context: **android** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

App-links without domain verification (assetlinks absent) = hijack-prep. Decisive test: the verification file's absence on the domain — 404/missing = the class.

## Probe adjustment (android × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
