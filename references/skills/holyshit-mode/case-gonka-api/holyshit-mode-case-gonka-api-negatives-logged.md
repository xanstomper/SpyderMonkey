# Negatives logged

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

19 admin/secret path probes on the edge function → all 404 (no admin panel, no
key-management endpoint). `/v1/credits` is the only metadata leak.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
