# Ledger

- source canon: `holyshit-mode/case-atessa-top.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`holyleadger/atessa.top.json` — confirmed: routing-oracle 45, count_tokens-DoS 50, forgot 40, resend 35, trust-split 30, quota-429 10; negatives: turnstile 20, oauth 15, stripe 15, cors 10, admin 10, ghosts 5; chain `preauth-routing-oracle` (hypothesis).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
