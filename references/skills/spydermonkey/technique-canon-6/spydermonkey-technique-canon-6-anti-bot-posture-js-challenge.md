# Anti-bot posture (JS challenges, managed challenge)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Which lanes get challenged (curl/requests vs headless vs real browser) — the differential map is the recon crown (drives all lane strategy). Decisive test: same endpoint three clients — the treatment matrix.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
