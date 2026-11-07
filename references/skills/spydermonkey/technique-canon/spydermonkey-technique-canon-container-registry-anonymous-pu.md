# Container registry anonymous pull

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Private registries allowing anonymous catalog/list. Decisive test: /v2/_catalog 200 = the inventory finding; image contents stay uncrowned beyond the manifest listing.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
