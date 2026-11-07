# Detection & hygiene classes — web-app / root

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-detection-hygiene-classes.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **web-app** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Entropy scan | `ent`/`rabin2 -e` on own carrier | high-entropy region |
| Fingerprint | `exiftool` hash-consistency (own set) | retouched carrier |
| Batch sweep | `stegextract` over own corpus | hits inventory |

Walls: carriers and payloads are the operator's own; if the file comes from
an engagement, its analysis is within the engagement scope and the payload is
never published without the engagement's disclosure terms.

## Probe adjustment (web-app × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
