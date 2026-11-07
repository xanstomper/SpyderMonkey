# Key-material-in-code classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Hardcoded keys/salts in bundles (the crash-verifier salt class, SPY-067 repo prefill) — the string context proves it is KEY MATERIAL (used in a live crypto op), not decoration. Decisive test: the key string + its use-site in the decompiled path — the pairing is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
