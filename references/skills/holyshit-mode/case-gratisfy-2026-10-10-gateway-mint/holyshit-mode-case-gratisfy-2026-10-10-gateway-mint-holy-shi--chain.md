# HOLY SHIT: full platform key mint chain (score 92) — email-verify gate walked through the front door — chain composition

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-holy-shi.md`
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

The "broken email delivery" was FIXED server-side (or uses a different transport per flow).
Chain, all plain urllib:
1. Phone signup (`phone_autoconfirm: true`, 2s session mint) — known.
2. **Email bind without verification**: `PUT /auth/v1/user` `{"email": "<mailinator>"}` → 200.
   (Root-level `email_verified` flag is NOT writable via /user — only `user_metadata`. Don't retry that.)
3. `POST /auth/v1/resend` → 200; **verification email ("Confirm Email Change" from
   hello@verify.gratisfy.xyz) landed in Mailinator in ~25s**.
4. Extract token from mail body → `GET /auth/v1/verify?token=…&type=email_change` → **303**
   with `#access_token=…` fragment = confirmed.
5. Platform handoff (chat → platform, code → JWT) with the now-verified account.
6. **`POST https://platform.gratisfy.xyz/api/account/platform-keys` `{"name": "…"}`** → 201,
   key created **AND plaintext returned in the create response**. Bonus: `POST …/{id}/secret`
   re-reveals the full key anytime (no re-mask discipline at all).
7. Key shape: `gxyz-<48 digits>`, scope `inference`, all models, all routes, free tier.

Lesson: "email delivery is broken" findings rot. Always re-test the verify-mail path before
concluding an email-gated chain is dead — one Mailinator inbox check flipped a hard wall into
full API-key issuance.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
