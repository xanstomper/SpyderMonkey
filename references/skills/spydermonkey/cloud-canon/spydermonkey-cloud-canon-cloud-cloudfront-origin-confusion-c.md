# Cloud CloudFront Origin Confusion (CLOUD-EDGE-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: origin that answers any Host — the edge/cache chain opener
- probe: Host-header differentials through the declared distribution
- wall: read-only; cache-poisoning classes are proven lab-side only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
