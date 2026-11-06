# MASTG Insecure Random (MASTG-CRYPTO-03) — ios / unauth

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-insecure-random-mastg-crypto.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ios** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: java.util.Random / non-CSPRNG for tokens
- probe: static scan + session-token structure check (the SESSION class on mobile)
- wall: read-only

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
