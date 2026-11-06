# OAuth start URL (recovered via `urllib r.url` + `allow_redirects=False` pattern) — api / federated

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-oauth-start-url-re.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`GET /api/auth/discord` returns 302 to:

```
https://discord.com/oauth2/authorize
  ?client_id=1555444770552152085
  &redirect_uri=https%3A%2F%2Fdirectrouter.pages.dev%2Fapi%2Fauth%2Fdiscord%2Fcallback
  &response_type=code
  &scope=identify+email
  &state=1bd11b87-fe48-49b5-9ba3-a473d3f7ac4d   (server-issued nonce)
```

Recon takeaways (no OAuth completion required):

- **client_id** = 1555444770552152085 — fingerprint the DirectRouter Discord OAuth app.
- **redirect_uri** is hardcoded to the directrouter.pages.dev callback — open-redirect via
  state/redirect_uri params NOT possible from the start URL itself. The `?ref=` query param
  is the referral code, not a redirect target.
- **scope = identify+email** (no `guilds`) — the OAuth flow does NOT request Discord guild
  membership, so `/api/auth/membership` must check membership via a separate server-side
  call (likely a Discord bot token calling the Discord API with the user's access token).
  Server-side check is correct because it can't be bypassed by the client; test the actual
  endpoint with a Bearer to confirm the gate holds.
- **state** is server-issued (UUIDv4 nonce) — CSRF protection on the OAuth callback is
  correctly implemented at the server level. The client-side `urlParams.get('discord_token')`
  fallback in `app.js` is demoted to a no-op when the primary
  `POST /api/auth/discord/exchange` succeeds; client-side fallback alone is NOT
  exploitable.

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
