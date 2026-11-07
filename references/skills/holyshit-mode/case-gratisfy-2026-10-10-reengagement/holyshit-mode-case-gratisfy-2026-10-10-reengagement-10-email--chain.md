# 10. Email delivery FIXED server-side + `/auth/v1/user` email bind (score 92, TOP FINDING) — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-10-email.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The session-3 "email delivery fully broken" negative is DEAD — "Confirm Email Change" from hello@verify.gratisfy.xyz lands in Mailinator in ~25s (second time this target invalidated a stored negative; re-test email paths before citing them as walls).
Full chain, ~90s total, zero payment:
1. `POST /auth/v1/signup {phone, password}` → full session (autoconfirm).
2. `PUT /auth/v1/user {"email": <mailinator>}` with Bearer AT → binds email. Root-level `email_verified` via PUT is REJECTED (Supabase /user only writes user_metadata) — the verify-email flow is the only way to flip the flag.
3. `POST /auth/v1/resend {"type":"signup","email":...}` → 200; email arrives at Mailinator.
4. Extract token from link: `GET /auth/v1/verify?token=...&type=email_change` → 303 with access_token fragment = confirmed.
5. Handoff to platform (code→JWT as before), then:
   - `POST /api/account/platform-keys {"name":"x"}` → 201, **plaintext key in the response body** (`key.plaintext`, format `gxyz-<long digits>`).
   - `POST /api/account/platform-keys/{id}/secret` → re-reveals full key anytime (`apiKey` field).
   - Param is `name` NOT `label` (400 `missing_key_name`).
6. Key authenticates `https://api.gratisfy.xyz/v1/*` — the real OpenAI-compat gateway (nginx 404 elsewhere on that host).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
