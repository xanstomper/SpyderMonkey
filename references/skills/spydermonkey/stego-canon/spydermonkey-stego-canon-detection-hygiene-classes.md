# Detection & hygiene classes

- source canon: `spydermonkey/stego-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Entropy scan | `ent`/`rabin2 -e` on own carrier | high-entropy region |
| Fingerprint | `exiftool` hash-consistency (own set) | retouched carrier |
| Batch sweep | `stegextract` over own corpus | hits inventory |

Walls: carriers and payloads are the operator's own; if the file comes from
an engagement, its analysis is within the engagement scope and the payload is
never published without the engagement's disclosure terms.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
