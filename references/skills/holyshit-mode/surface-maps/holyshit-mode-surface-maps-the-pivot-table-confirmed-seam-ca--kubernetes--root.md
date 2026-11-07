# The pivot table (confirmed seam → canon → next) — kubernetes / root

- source canon: `holyshit-mode/surface-maps.md`
- base technique: `holyshit-mode-surface-maps-the-pivot-table-confirmed-seam-ca.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **kubernetes** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

`pivot --target T` reads the family states (undercroft CONFIRMED seams, 3AM
chains) and matches them against the case canon by keyword score:

- CONFIRMED undercroft surface → which case file has this seam class → crown-class
  guess (PII/FIN/CRED/BACKUP/SRC/SASS) → `shukaku ingest`.
- CONFIRMED undercroft logic → value-flow recipes → `kairo compile` → 3AM promote.
- 3AM chains → takeover batteries → shukaku prices what the chain reaches.

## Probe adjustment (kubernetes × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
