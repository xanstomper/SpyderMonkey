# MASTG Weak Cryptography (MASTG-CRYPTO-02) — chain composition

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-weak-cryptography-mastg-cryp.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: ECB mode, MD5/SHA1, hardcoded IVs, predictable random
- probe: decompile the lab build, inventory the crypto primitives per MASVS-CRYPTO
- wall: static inventory; no crypto oracle execution

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
