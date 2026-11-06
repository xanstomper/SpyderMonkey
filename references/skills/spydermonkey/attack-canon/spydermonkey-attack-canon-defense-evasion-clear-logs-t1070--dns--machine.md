# Defense Evasion Clear Logs (T1070) — dns / machine

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-defense-evasion-clear-logs-t1070.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **dns** · auth **machine** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: log tampering to erase the trail
- probe: NEVER; the estate memory + tamper-evident hash chain exists to resist this
- wall: REFUSED — the ledger is append-only, hash-chained, tamper-evident

## Probe adjustment (dns × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
