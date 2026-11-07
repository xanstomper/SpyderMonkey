# Clickjacking without X-Frame-Options / frame-ancestors

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Framable state-changing pages. Decisive test: local framing harness — the frame renders the sensitive control = the class (register per-endpoint).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
