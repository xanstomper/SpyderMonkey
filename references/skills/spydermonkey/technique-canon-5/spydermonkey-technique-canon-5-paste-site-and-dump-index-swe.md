# Paste/site and dump-index sweeps

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Paste-site keyword sweeps and dump-index catalogs tied to the estate (LeakRadar-class sources) — the row-level rule applies. Decisive test: source URL + correlated row count per source, distinct leading words per title (dedupe discipline).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
