# Auth-provider redirect capture (before driving any login form) — chain composition

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-auth-provider-redirect-capture.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- When a login button hops to an external IdP, capture the FULL redirect URL from the
  click (don't just follow it): `openid.realm`, `openid.return_to`, and ticket params
  (`e`/`h`/`s` style) reveal the trust anchor and whether return_to is pinned to a
  dedicated login host.
- Rotating login-infra domains (`loginN.<brand>.com` series) are CF-fronted API-only
  hosts — root returns an empty 404. DNS + banner ONE, then probe adjacent numbers to
  map the series; realm-pinning to the series is an anti-phishing control, not a flaw.
- Record the IdP form's field layout before invoking vault save (Steam:
  steamcommunity.com/openid/loginform/, username id `«r3»`, password `«r4»`, guard code
  `authcode` — the guard prompt arrives after password submit; have the enter_code path
  ready).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
