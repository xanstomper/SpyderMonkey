# MASTG Data in Clipboard and Keyboard Cache (MASTG-STORAGE-04)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- class: clipboard sync + keyboard autocorrect retaining secrets
- probe: paste a marker, inspect the keyboard cache db
- wall: lab only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
