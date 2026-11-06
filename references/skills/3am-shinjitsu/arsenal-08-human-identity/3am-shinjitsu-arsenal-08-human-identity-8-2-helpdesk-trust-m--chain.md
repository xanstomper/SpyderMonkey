# 8.2 Helpdesk trust model (score 60, documentation only) — chain composition

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-2-helpdesk-trust-m.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Public-facing support channels, documented identity-verification requirements (or their
  absence), password-reset-over-phone policy in public docs.
- Findings are PROSE ratings: "helpdesk reset requires account number only = MFA bypass
  exposure" — no contact is ever made.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
