# The pivot table (confirmed seam → canon → next) — ci-cd / machine

- source canon: `holyshit-mode/surface-maps.md`
- base technique: `holyshit-mode-surface-maps-the-pivot-table-confirmed-seam-ca.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`pivot --target T` reads the family states (undercroft CONFIRMED seams, 3AM
chains) and matches them against the case canon by keyword score:

- CONFIRMED undercroft surface → which case file has this seam class → crown-class
  guess (PII/FIN/CRED/BACKUP/SRC/SASS) → `shukaku ingest`.
- CONFIRMED undercroft logic → value-flow recipes → `kairo compile` → 3AM promote.
- 3AM chains → takeover batteries → shukaku prices what the chain reaches.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
