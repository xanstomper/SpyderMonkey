# AS-REP roastable and kerberoastable ENUMERATION

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Accounts without preauth or with SPNs are ENUMERABLE read-only (the class inventory); the offline crack is the no-gain wall — register the account list, never the cracked material. Decisive test: the enum response naming the accounts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
