# 9. Handoff refinements (score 78)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `POST /api/auth/platform-handoff/start` accepts ANY target string (admin/platform/internal/dashboard/mission-control all mint codes for unverified users — no role check) with body `{refresh_token, next, target}` + Bearer AT.
- Codes: 32-hex UUID-v4 (128-bit — brute dead, confirmed again). **Replayable within 60s TTL** (single-use only after expiry). Cross-host exchange: code minted at gratisfy.xyz exchanges at platform.gratisfy.xyz.
- Exchange mints a session for the CODE OWNER's account (no takeover by itself — it's self-minted).
- /api/account/session works for unverified accounts (200); every privileged route 403 `email_not_verified`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
