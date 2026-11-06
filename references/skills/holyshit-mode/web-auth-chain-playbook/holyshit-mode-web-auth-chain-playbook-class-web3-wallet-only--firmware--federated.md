# Class: web3-wallet-only auth chains (casino/DeFi class) — firmware / federated

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-web3-wallet-only.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **firmware** · auth **federated** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

When the ONLY auth is a wallet signature (no email/password exists — mine the
`web3-sign-in-*` bundle chunk for the flow), the audit surface is the challenge + verify pair:

- **Read the challenge like a credential spec.** A flat personal_sign string with no
  timestamp, no expiry, and no domain binding signs a credential with NO intrinsic time
  bound — replay protection then depends entirely on server nonce consumption. Every absent
  binding field (domain, expiry, request id) is an audit finding in itself.
- **The operator's completed login IS the test artifact.** No wallet re-signing needed for
  the decisive tests: Network tab → the login's auth POST → "Copy as fetch" = byte-faithful
  replay primitive (real client headers included). Run twice for replay; edit the body
  address for the binding-swap test.
- **Test ladder (decisiveness order, all self-account):** signature replay ×2 →
  signature↔address binding swap → challenge determinism ×3 (identical = static challenge;
  rotating = sequence-check the nonce for counter/timestamp derivation) →
  registered-vs-fresh address oracle → extra-state-keys mass assignment on the auth POST.
- **Challenge TEMPLATE validation is a separate control from the signature — test it
  first.** Sign an ARBITRARY message string and send it as the message field with the hash
  appended: if verify accepts, only the hash binds and the message content is
  attacker-chosen (the login-template text is cosmetic, not a control).
- **Challenge hashes are single-use and often consumed by REJECTED attempts.** Each verify
  variant needs a FRESH initiate (new hash); a runner that reuses one hash across variants
  tests nothing after the first try, and hash-consumption-on-failure makes variant loops
  self-limiting — budget one initiate per variant.
- **Burned-vantage handoff:** when the WAF burns every agent vantage (scripted AND real CDP
  browser), stop probing and hand a numbered console kit to the operator — their logged-in
  console is same-origin, passes the challenge, and carries their real fingerprint. Include
  a token-redaction instruction so minted session tokens never ride back into the transcript.
- **Autonomous signup beats the console handoff when the exchange is open (ephemeral
  keypair):** wallet-only auth needs NO operator login if `POST <auth>/web3` (or the
  exchange) accepts requests from the probe vantage — generate a throwaway secp256k1
  keypair on the VM (`eth_account` in the probe venv), fetch the LIVE challenge for that
  address, sign it, and POST the exchange. No identity, no account fraud, fully
  shreddable. Rules: (1) challenge-issue endpoints return `201` not `200` — accept both
  and treat 201+message as open; (2) a cryptographically VALID signature that still gets
  403/500 = the WALL, not your signature — record the deny shape and stop churning
  variants; (3) on success the response answers the whole test in one request — decode
  the returned access JWT and diff the `user` object against the injected state keys,
  then replay the same signature (nonce-consumption) and the state-bomb in the same
  session; (4) shred key + artifacts from the RAM dir immediately after, never keep the
  key on disk.
- **Region walls change SHAPE between sessions — re-verify the deny, not the memory of
  it.** A clean `403 general.Forbidden` region-deny can become an unhandled `500 Internal
  server error` on the same endpoint without the route opening (challenge-issue stays
  open while the exchange 500s on a valid signature). Report the crash-shaped deny as an
  error-handling regression finding; do not read 500-as-soft-open until a valid
  credential proves otherwise (an empty body 401 vs signature-body 500 vs 403 across
  sessions is exactly this drift: first probe the body variants, then classify).
- **State-cookie injection mechanism (check for it BEFORE the login test):** auth
  middleware that serializes inbound context into cookies gives two things at once. A
  `header_state` cookie echoing the XFF chain / x-amzn-trace-id / CF geo = topology +
  geo-precision leak (observation; log it, don't chase it). A `query_state` cookie that
  persists the URL's `?state=` VERBATIM (arbitrary JSON accepted) = a state-injection
  primitive: the client's signIn JSON.parses `state` and spreads truthy keys into the auth
  POST body (`{..., ...state}`). The cookie is set on ANY `/auth/*` page — Google/Steam
  starters included, not just the wallet path — so the crafted-link → cookie → body chain
  reaches EVERY login method, including ones that are not region-gated. Prove the client
  side with one request (`?state={"isAdmin":true}` → read the Set-Cookie); the server
  DTO's acceptance of unknown keys is then the single remaining gate (console login test,
  then diff `/user/me`).
- **OAuth starter probing (302 = open, and the Location is the map):** fetch each login
  starter (`/auth/steam`, `/auth/google`, ...) with allow_redirects=False. The Location
  carries return_to/redirect_uri: retry with attacker values — echoed = override (hijack
  chain), hardcoded = fast negative. No `state` param in the Location = OAuth login-CSRF
  candidate (the victim's consent completes against the attacker's provider account). The
  REAL callback host lives inside the redirect_uri: callbacks almost never sit under
  `/auth/*/callback` on the main domain; the OAuth host serves them at top-level paths
  (`/google/redirect`, `/steam/redirect`) and may be entirely un-walled where the main
  domain is gated — probe those directly. Consumer fingerprint: garbage `code=`, `error=`
  param, and a well-formed OpenID `id_res` with a garbage `sig` — clean 401 on the error
  path plus 500 on every `id_res` variant = live consumer with unhandled exceptions, and
  sig validation exists (no forgery without the provider key); a 500 on garbage `code=`
  also proves the code-exchange handler is live and reachable pre-auth.

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
