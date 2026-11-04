# Auth-provider redirect capture (before driving any login form)

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
