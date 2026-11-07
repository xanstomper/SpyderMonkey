# ERB/Mako/pebble/nunjinjucks

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`<%= 7*7 %>` (erb), `${7*7}` (mako/pebble/nunjucks ambiguity resolved by error text). Decisive test: marker + engine-error cross-read.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
