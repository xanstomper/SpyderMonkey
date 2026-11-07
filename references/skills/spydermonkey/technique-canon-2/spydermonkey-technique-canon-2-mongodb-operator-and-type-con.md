# MongoDB operator and type confusion

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`$ne`/`$regex`/`$where` and array-typed params accepted server-side. Decisive test: operator body on your own login/owner field — acceptance without the secret = the class; `$where` acceptance is the JS-execution variant (reported, never weaponized).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
