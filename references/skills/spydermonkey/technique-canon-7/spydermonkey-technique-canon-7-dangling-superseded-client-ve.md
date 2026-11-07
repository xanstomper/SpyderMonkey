# Dangling/superseded client versions

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Older app versions still served (APK mirrors, cached chunks) exposing retired endpoints/auth shapes. Decisive test: old-version bundle diff against live — retired-surface presence = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
