# Shipping and tax zeroing — wireless / root

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-shipping-and-tax-zeroing.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **wireless** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

The shipping/tax line recomputed per address/region can be zeroed by a region string the tax table lacks. Decisive test: region=XX-UNKNOWN at checkout — total drops the tax line = the finding (characterize, don't purchase).

## Probe adjustment (wireless × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
