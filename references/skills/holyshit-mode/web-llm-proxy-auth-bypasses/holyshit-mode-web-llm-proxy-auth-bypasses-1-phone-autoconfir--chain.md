# 1. Phone autoconfirm = instant confirmed accounts — chain composition

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-1-phone-autoconfir.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `GET /auth/v1/settings` reveals `phone_autoconfirm: true`, `mailer_autoconfirm: false`.
- `POST /auth/v1/signup` with `{"phone":"+1...","password":"..."}` returns a FULL session
  (access_token + refresh_token) with NO SMS/OTP step. Accounts mint in ~2s.
- Rate limits on the AI proxy (~6 req/min) are defeated by minting fresh accounts and rotating.
- Pitfall: response shape differs by flow — email signup nests the session under `session`,
  phone signup may return access_token at top level. Parse both.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
