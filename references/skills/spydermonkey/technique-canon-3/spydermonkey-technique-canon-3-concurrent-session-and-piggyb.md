# Concurrent-session and piggyback policy

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

No session revocation on password change / unlimited parallel sessions = replay-window classes. Decisive test: old session alive after rotation on YOUR accounts — the window is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
