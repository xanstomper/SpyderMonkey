# Credential Access Credentials from Password Stores (T1555) — ios / high-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-credential-access-credentials-from.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: browser/keychain credential extraction
- probe: REFUSED on any live endpoint; the class exists as a detection pattern
- wall: kage rule only

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
