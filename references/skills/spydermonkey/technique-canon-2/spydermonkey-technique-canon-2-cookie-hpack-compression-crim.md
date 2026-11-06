# Cookie/HPACK compression crimes-shape

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

Cross-origin compression oracles (length-differential on secrets echoed into compressed structures). Decisive test: lab replica with a secret + compressed echo — the byte-length oracle is the proof.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
