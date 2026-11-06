# 3.13 CORS severity discipline — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-13-cors-severity-discipline.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Reflection `ACAO: <evil>` + `ACAC: true` on cookie-auth endpoints = critical. On Bearer-
  header APIs = config flaw ONLY (no credentials ride CORS). Cookie era: read raw `Set-Cookie`
  — `SameSite=Lax` blocks cross-site POST → downgrade ~7.1. Severity is f(auth-model, SameSite),
  not reflection alone.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
