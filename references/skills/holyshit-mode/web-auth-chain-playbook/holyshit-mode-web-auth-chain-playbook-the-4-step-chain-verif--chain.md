# The 4-step chain (verified end-to-end, ~60s) — chain composition

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-the-4-step-chain-verif.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Confirmed session with zero verification.** If `phone_autoconfirm: true`,
   `POST /auth/v1/signup` with a phone number returns a full session (access_token +
   refresh_token, `phone_confirmed_at` set) — no SMS delivered or checked. Also test
   arbitrary `data:` fields (mass assignment) but VERIFY against the full response: GoTrue
   strips `user_metadata`/`app_metadata` from the body in recent versions — retract the
   finding if fields are not echoed back.
2. **RLS write escalation on trust flags.** With the session JWT as
   `Authorization: Bearer` + anon key as `apikey`, try
   `PATCH /rest/v1/profiles?user_id=eq.<self>` with `{"email_verified": true}`. Row-owner
   RLS often permits writing user-controlled boolean trust flags the backend then gates on.
   Check constraint errors (pg 23514) reveal allowed column value sets.
3. **Key/feature minting behind the trust gate.** Retest the previously-401 backend
   endpoints (`/api/account/platform-keys` POST → real `gxyz-...` plaintext key;
   `/api/account/settings` PATCH accepts rate-limit increases, clamped server-side).
4. **Free inference.** `POST /v1/chat/completions` on the API host with the minted key.
   Proxy error bodies leak upstream provider state (e.g. Z.ai 403 USER_BLOCKED with
   upstream user_id) — inventory which paid models actually return 200.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
