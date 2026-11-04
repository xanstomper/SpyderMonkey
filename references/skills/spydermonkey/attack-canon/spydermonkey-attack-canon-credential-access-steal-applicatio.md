# Credential Access Steal Application Access Token (T1528)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- class: OAuth/app token theft
- probe: token-handling review of the in-scope app — where tokens land in logs/artifacts
- wall: read-only analysis

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
