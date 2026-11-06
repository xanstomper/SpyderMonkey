# Walls (verified, not assumed) — iot / federated

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-walls-verified-not-assumed.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot** · auth **federated** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `staging`/`dashboard`/`ds`/`aiostaging` = Cloudflare Access walls.
- `slot-integrations.rainbet.com` = NestJS, `/docs` → CF Access; all guessed paths 404
  (real routing, "Cannot GET").
- `api.rainbet.com` + `staging-api` = IP-reputation hard block (even real chromium).
- Sign-up = Turnstile `secure_token` + edge managed challenge on the auth plane.
- `staging-mono`/`dev-mono` = AWS ELB (`awselb/2.0`) 504 — orphaned backends.
- Game verifier = fully client-side (no bet-lookup oracle).

## Probe adjustment (iot × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
