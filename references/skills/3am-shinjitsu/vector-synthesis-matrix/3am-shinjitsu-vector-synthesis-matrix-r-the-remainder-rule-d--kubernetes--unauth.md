# §R — the remainder rule (derive any unlisted pair) — kubernetes / unauth

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-r-the-remainder-rule-d.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Pair (F, S) not in the table → derive mechanically, 60 seconds:

1. Take F's canonical primitive shape (flaw-family key).
2. Substitute S's boundary as the attacker-controlled input position (seam key).
3. Write the one-liner: `[primitive shape] at [seam's input position]`.
4. Score §14. ≥60 → run; else ledger as rejected-with-reason.

Derivation example: (3 Type-coercion × H Multi-host) → "send the object-where-string
payload to the mirror host's twin endpoint, where the validator is one version older" —
this is exactly how the gamdom mirrors got probed.

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
