# MASTG Weak Cryptography (MASTG-CRYPTO-02)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- class: ECB mode, MD5/SHA1, hardcoded IVs, predictable random
- probe: decompile the lab build, inventory the crypto primitives per MASVS-CRYPTO
- wall: static inventory; no crypto oracle execution

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
