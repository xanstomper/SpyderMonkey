# 4.9 Web3-wallet auth chain (score 75) — chain composition

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-9-web3-wallet-auth-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Read the challenge SPEC from the bundle: flat `personal_sign` with NO timestamp/expiry/
  nonce-binding = replayable challenge (hypothesis ~65 until replay test on own wallet).
- Ephemeral keypair signup when the exchange is open = autonomous self-account (no identity
  fraud, shred the key from RAM after). State-cookie carrier (`state` cookie, never the
  `?state=` URL param — query_state mirror may be unread).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
