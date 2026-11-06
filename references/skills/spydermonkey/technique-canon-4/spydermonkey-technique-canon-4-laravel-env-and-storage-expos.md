# Laravel .env and storage exposure

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

/.env fetch (already HARVEST), /storage path listing, APP_KEY in artifacts. Decisive test: control-path differential fetch — distinct content = the harvest.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
