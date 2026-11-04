# Platform-handoff flow — chain composition

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-platform-handoff-flow.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`POST /api/auth/platform-handoff/start` with `{refresh_token, next, target}` + `Authorization: Bearer <session>` mints handoff codes:
- Codes: 32-hex chars (~128 bits, UUIDv4-like), 60s TTL, replayable WITHIN TTL (single-use after expiry).
- `target` accepts arbitrary values (admin, platform, internal, chat, sillytavern...) even for unverified low-priv users; codes are host-specific on exchange (platform.* host exchanges platform-target codes).
- Use for session-fixation / code-theft chains when a victim URL fragment can be intercepted.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
