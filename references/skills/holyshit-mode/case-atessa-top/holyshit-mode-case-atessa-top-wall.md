# Wall

- source canon: `holyshit-mode/case-atessa-top.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Signup + login captcha-gated server-side (operator declined account creation pre-auth; later supplied key). Remaining authed follow-ups needing a SESSION COOKIE: voucher brute (`/api/vouchers/redeem` + preview oracle), credit-transfer IDOR (`/user/transfer-credits`), key IDOR (`/user/keys/{id}`), reseller RS escalation, mass-assignment JWT persistence. Quota reset 2026-10-07 00:00 UTC gates completion-plane abuse tests.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
