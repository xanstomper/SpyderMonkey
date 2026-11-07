# 3. Handoff-code flow = credential minting without gates

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `POST /api/auth/platform-handoff/start` with body `{refresh_token, next, target}` +
  Bearer session accepts ANY target (`admin`, `platform`, `chat`, `sillytavern`, ...).
- Returns 32-hex one-time codes, 60s TTL, redirect to subdomain you may not have recon'd
  (chat./platform./sillytavern. subdomains appeared here — always enumerate from handoff targets).
- Exchange: `POST /api/auth/platform-handoff/exchange {code}` — works cross-host, is
  unthrottled, and DOES NOT check email verification. Replay works within TTL, single-use after.
- Codes look UUIDv4 (128-bit) — not brute-forceable; value is the bypass + new hosts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
