# Negatives & decay — firmware / low-priv

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-negatives-decay.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Negatives are results — exact test string in the ledger, never re-probed without a
  change (firmware version, access level, new kit).
- Findings decay: firmware updates kill rollback findings; radio state drifts; cloud
  trust changes. Re-verify before citing.

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
