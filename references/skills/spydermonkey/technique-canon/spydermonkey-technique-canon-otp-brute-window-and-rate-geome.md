# OTP brute window and rate geometry

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

OTP validation with per-request cost < lockout threshold is enumerable (6-digit, 10 tries/lockout, no window reset = 1-in-10000 per lockout cycle). Decisive test: measure the exact counters — wrong-OTP responses until lock, lock TTL, and whether attempts decrement on resend. Register the arithmetic; never extract a live OTP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
