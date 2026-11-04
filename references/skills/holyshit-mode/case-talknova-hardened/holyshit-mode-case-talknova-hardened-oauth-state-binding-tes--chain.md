# OAuth state-binding test (5 curls, decisive) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-oauth-state-binding-tes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. GET `/api/auth/google/start?attempt=x1` → capture state cookie A.
2. GET start again → cookie B. Then `callback?state=A&code=fake` with cookie B → hardened if `Invalid OAuth state`.
3. Matched cookie + fake code → expect token-exchange failure.
4. `returnTo=https://evil.com` on /start → hardened if Location still goes only to Google.
5. Callback with no cookie / no state → expect 400.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
