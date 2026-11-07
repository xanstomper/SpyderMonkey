# Not every publicly-pushed value is a leak

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

A "next round" field can be the REFERENCE state the game publishes for gameplay:
hilo announces `apriori: {color, number}` = the CURRENT card players bet
higher/lower against (public BY DESIGN). Check the game rules before reporting
an outcome leak — the genuinely hidden value arrives only in an authed event.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
