# Container registry anonymous pull

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

Private registries allowing anonymous catalog/list. Decisive test: /v2/_catalog 200 = the inventory finding; image contents stay uncrowned beyond the manifest listing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
