# Jinja2 and Jinja-flavored arithmetic

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`{{7*7}}`→49, `{{7*'7'}}`→7777777 fingerprints jinja2; `{{config}}` exposure = the crown. Decisive test: arithmetic marker reflected exactly.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
