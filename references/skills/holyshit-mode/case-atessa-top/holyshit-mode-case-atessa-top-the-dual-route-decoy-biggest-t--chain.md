# The dual-route decoy (biggest time sink — learn it) — chain composition

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-the-dual-route-decoy-biggest-t.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Bare paths (`/auth/login`, `/vouchers/redeem`) 422 with `"input":null` on EVERY field despite valid JSON = SPA-fallback router where the body never reaches Pydantic. Looks like "captcha strips the body" — it isn't.
- Real API lives under `/api/*`: `/api/auth/login` → `CAPTCHA verification required`; `/api/auth/signup` 422 echoes `input:{...your body...}` back.
- **Rule:** any 422 with `input:null` on all fields → immediately re-probe the same path under `/api` + `/api/v1` prefixes.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
