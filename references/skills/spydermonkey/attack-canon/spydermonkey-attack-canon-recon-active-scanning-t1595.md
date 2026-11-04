# Recon Active Scanning (T1595)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- class: adversarial scanning of the victim surface — port sweeps, vuln scans, wordlist strikes
- probe: rate-limited sweep of the declared scope only; masscan-class first, then app layer
- wall: in-scope only — the scope authority refuses everything else (rc=1)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
