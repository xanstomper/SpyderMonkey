# Walls (verified, not assumed) — chain composition

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-walls-verified-not-assumed.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `staging`/`dashboard`/`ds`/`aiostaging` = Cloudflare Access walls.
- `slot-integrations.rainbet.com` = NestJS, `/docs` → CF Access; all guessed paths 404
  (real routing, "Cannot GET").
- `api.rainbet.com` + `staging-api` = IP-reputation hard block (even real chromium).
- Sign-up = Turnstile `secure_token` + edge managed challenge on the auth plane.
- `staging-mono`/`dev-mono` = AWS ELB (`awselb/2.0`) 504 — orphaned backends.
- Game verifier = fully client-side (no bet-lookup oracle).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
