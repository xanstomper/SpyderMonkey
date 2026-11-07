# 1. Build the brief from breach-OSINT

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Search: `<target> breach leak <year>` — hit Breachsense, ransomware.live, and 2-3 news writeups.
- Record from the attacker's leak-site statement: claimed initial access, claimed data
  holdings, escalation promises. This is the engagement brief — the attacker documents
  their own kill-chain.
- Corroborate against the victim's public statements. The mechanism is confirmed when the
  victim's own PR admits it ("unauthorized withdrawal requests were added to the database"
  = proven DB-level WRITE). Disputed scale ≠ disputed method.
- The two datasets (attacker holdings vs victim confirmations) define what remains open.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
