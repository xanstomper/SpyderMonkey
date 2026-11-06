# 2. user_metadata injection (limited value) — chain composition

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-2-user-metadata-in.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Arbitrary `user_metadata` (role, is_admin, credits) PERSISTS into the JWT via signup/update.
- Backends authorize on their own DB (`profiles` / `app_metadata`), NOT client metadata →
  admin bypass fails. Expect `email_not_verified` middleware on all privileged routes.
- Don't burn turns re-testing metadata escalation against a well-built backend.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
