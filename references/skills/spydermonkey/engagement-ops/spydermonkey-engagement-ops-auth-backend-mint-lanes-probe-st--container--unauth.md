# Auth-backend mint lanes: probe state-creation oracles; clear the captcha-free ATO primitives with evidence — container / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-auth-backend-mint-lanes-probe-st.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Sites that captcha-wall their registration/login UI still expose **login-handshake mint endpoints that allocate server-side state per request, unauthenticated** — the ATO funnel's "open mint / gated verify" asymmetry. Two oracle classes to hunt, both on the same shared auth backend:

1. **WebAuthn/passkey ceremony mints.** `POST .../passkey/get_auth_challenge_for_login/` (or any challenge-mint route) may return `{sessionId, challenge, timeout, rpId, allowCredentials, extensions}` with `credentials:'omit'` — no auth, no captcha, no rate limit, and **`allowCredentials:[]` = the server accepts ANY credential ID at the assertion step (no user/credential scoping at mint)**. Measure the flood: N rapid mints (20 in ~15ms is easy) counting distinct sessionIds — every mint allocates a server-side ceremony session (180s timeout), so the flood is an auth-backend session-store DoS plus attacker-initiated ceremonies against any user. Follow the assertion endpoint read-only to prove the VERIFY side validates (bean errors like "must not be blank" / "must be a well-formed base64" = server-side validation exists — the mint side still has none; that asymmetry is the finding).
2. **ECIES/fingerprint handshake mints.** `.../login-pre/?p=<anything>` (garbage works) returns `{random, publicKey, eciesKey:{keyVersion, keyId, pubKey}}`. **A 19-digit snowflake `keyId` that increases per call = a persistent DB row written per request** — mint 8x and list the keyIds; unique snowflakes each time proves an unbounded DB-write flood (row/disk exhaustion) on the auth backend, NOT just ephemeral state. A valid t1-format `p` also returns a protobuf `random` — the full password-login handshake material for an attacker-chosen fingerprint.

Both classes register as HIGH (CWE-799/400 availability + ceremony misuse on the shared auth backend), with the exact mint rate + state-creation proof (unique sessionIds/keyIds) in the evidence. Fix demands: session-bind the mint, rate-limit per IP/session, cap outstanding sessions/rows per caller, populate allowCredentials from the claimed user.

**Test the classic captcha-free ATO primitives and BANK the cleared lanes** — a cleared lane is evidence, not a dead end, and proves the estate's auth surface holds:

- **Wallet-sign auto-register test.** Crypto-casino claim: "sign any message with any wallet → auto-created account." Recipe: GET the signing message (`/account/wallet/login/message/` → bare `bc.game <random>` template), sign it locally with a FRESH keypair (`pip install eth-account` in the hermes venv; `Account.create()`, `acct.sign_message(encode_defunct(text=msg))` — `sign_message_text` does NOT exist), POST `varify` with `{address, signature, message}` (and 0x-prefixed/variant shapes). A `Wallet signature error` on BOTH the empty body and a valid ECDSA signature means the field format or a registered-wallet binding is required — do NOT read the catch-all error as "format wrong" alone; the decisive observation is whether a fresh-address signature is ever accepted (auto-register present) or always rejected (binding required).
- **Member-gate oracle differential.** When a resource route answers unauth with an identical
  gate page (`Member only.` alert-redirect), differential-test resource ID variants
  (real-format provider codes, numerics, garbage, quote payloads) and compare BODY BYTES +
  TIMING: a uniform response = the auth check PRECEDES resource resolution — no enumeration
  oracle, no pre-auth processing, the route is sealed; register the sweep as the decisive
  negative. A size/timing differential on valid vs invalid IDs would instead be the oracle.
- **Social login-callback gating.** A telegram/OAuth `login-callback` that returns flow-state errors (`5999 login timeout` / `1001 Service error` / `5001 login info expired`) for forged params is FLOW-STATE + auth_date-freshness gated BEFORE any hash validation — cite the gating, never claim "no HMAC validation" from a flow error (the hash is never reached). Popup-bind/auth endpoints that answer `6002 user info expired` are login-gated — that is the gate, record it.

Register all three as one AUTHN row: wallet-sign crypto-validated (auto-register absent), telegram flow-gated, popup-bind login-gated — the social/wallet ATO surface holds against the standard primitives.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
