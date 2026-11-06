# XXE out-of-band and local-file

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV-07** · **CWE-611** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

DOCTYPE + external entity to your DNS/HTTP listener = OOB proof; file:///etc/hostname echoed = local-file proof. Decisive test: OOB marker arrival at your listener; file read limited to hostname/ident material.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
