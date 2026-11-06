# MASTG Weak Cryptography (MASTG-CRYPTO-02) — ios / high-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-weak-cryptography-mastg-cryp.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: ECB mode, MD5/SHA1, hardcoded IVs, predictable random
- probe: decompile the lab build, inventory the crypto primitives per MASVS-CRYPTO
- wall: static inventory; no crypto oracle execution

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
