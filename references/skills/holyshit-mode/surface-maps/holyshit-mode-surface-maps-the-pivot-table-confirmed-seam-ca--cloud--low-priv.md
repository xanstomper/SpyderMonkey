# The pivot table (confirmed seam → canon → next) — cloud / low-priv

- source canon: `holyshit-mode/surface-maps.md`
- base technique: `holyshit-mode-surface-maps-the-pivot-table-confirmed-seam-ca.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`pivot --target T` reads the family states (undercroft CONFIRMED seams, 3AM
chains) and matches them against the case canon by keyword score:

- CONFIRMED undercroft surface → which case file has this seam class → crown-class
  guess (PII/FIN/CRED/BACKUP/SRC/SASS) → `shukaku ingest`.
- CONFIRMED undercroft logic → value-flow recipes → `kairo compile` → 3AM promote.
- 3AM chains → takeover batteries → shukaku prices what the chain reaches.

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
