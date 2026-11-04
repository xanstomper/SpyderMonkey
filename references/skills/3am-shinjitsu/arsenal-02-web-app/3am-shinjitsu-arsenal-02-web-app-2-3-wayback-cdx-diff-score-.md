# 2.3 Wayback CDX diff (score 75, zero target traffic)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- DECISIVE: `curl -s 'https://web.archive.org/cdx/search/cdx?url=<domain>/*&fl=original&collapse=urlkey'`
- EXTRACT: removed routes vs live; id-format oracle (`user=`, `token=`, `r=`, `stag=` shapes);
  removed auth methods; old affiliate formats. Run BEFORE brute-formatting any id oracle.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
