# MASTG Deep Links and Intent Redirection (MASTG-PLATFORM-06)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: hijackable deep links, intent passthrough
- probe: static link inventory; am-probe the lab app with crafted intents
- wall: lab device

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
