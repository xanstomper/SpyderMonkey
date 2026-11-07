# Cookie jar depth

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

__Host- enforcement (canon-I), SameSite=None sprawl, cookie-count overflow eviction (forced-logout class), chstate/confusion via name collisions. Decisive test: your own cookie jar manipulations in the lab browser — the eviction/collision behavior is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
