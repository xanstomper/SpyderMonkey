# Nginx alias traversal and off-by-slash

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`alias` directives without trailing slash make /path../ escape the root. Decisive test: the off-by-slash variant (location /x { alias /srv/x/; } → /x../secret) against a control path — distinct file content = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
