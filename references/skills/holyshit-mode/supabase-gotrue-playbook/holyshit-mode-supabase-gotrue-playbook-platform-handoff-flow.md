# Platform-handoff flow

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`POST /api/auth/platform-handoff/start` with `{refresh_token, next, target}` + `Authorization: Bearer <session>` mints handoff codes:
- Codes: 32-hex chars (~128 bits, UUIDv4-like), 60s TTL, replayable WITHIN TTL (single-use after expiry).
- `target` accepts arbitrary values (admin, platform, internal, chat, sillytavern...) even for unverified low-priv users; codes are host-specific on exchange (platform.* host exchanges platform-target codes).
- Use for session-fixation / code-theft chains when a victim URL fragment can be intercepted.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
