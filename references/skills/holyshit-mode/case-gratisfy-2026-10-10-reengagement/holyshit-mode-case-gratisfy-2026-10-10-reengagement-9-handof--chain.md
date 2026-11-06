# 9. Handoff refinements (score 78) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-9-handof.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `POST /api/auth/platform-handoff/start` accepts ANY target string (admin/platform/internal/dashboard/mission-control all mint codes for unverified users — no role check) with body `{refresh_token, next, target}` + Bearer AT.
- Codes: 32-hex UUID-v4 (128-bit — brute dead, confirmed again). **Replayable within 60s TTL** (single-use only after expiry). Cross-host exchange: code minted at gratisfy.xyz exchanges at platform.gratisfy.xyz.
- Exchange mints a session for the CODE OWNER's account (no takeover by itself — it's self-minted).
- /api/account/session works for unverified accounts (200); every privileged route 403 `email_not_verified`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
