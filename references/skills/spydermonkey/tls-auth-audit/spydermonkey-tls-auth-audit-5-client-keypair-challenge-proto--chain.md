# 5. Client-keypair challenge protocols (merchant / game-provider SDKs) — chain composition

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-5-client-keypair-challenge-proto.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When a bundled SDK authenticates sockets by generating a keypair in the browser,
audit the CHALLENGE TRANSPORT, not the crypto (RSA-2048 signing is fine — the
weakness is what you must possess to sign):

1. Grep the SDK chunk for `crypto.subtle.generateKey`, `auth-code`,
   `auth-token`, `recoverToken`, `connect-id` — these mark a client-keypair
   auth scheme on a merchant/provider socket namespace (`/merchants`-style).
2. Extract full function bodies with a balanced-brace sweep, never regex
   windows: find `function Name(`, then count `{}` depth to the close — regex
   `.\{0,N\}` snippets cut functions mid-body and hide the resolution chain.
3. Map the resolution: does the challenge (`code`/`recoverToken`) come from a
   server response, a prop, or `URLSearchParams(window.location.search)`? A
   URL-sourced challenge = the URL is the credential store; every referrer/log/
   analytics capture of that URL yields session takeover with an attacker-
   generated keypair (the server verifies the signature against the pubkey the
   CLIENT supplied, so possession of the challenge is the whole game).
4. Check the sibling identifier too (merchant `mkey` etc. often rides the same
   query string) and the recovery path (`auth-token` + recoverToken) — same
   class if it signs client-held material.
5. Severity honestly: transport design CONFIRMED from decompilation; live
   takeover needs one authenticated session to observe a real `?code=` URL —
   register the code-path as confirmed, the end-to-end takeover as a disclosure
   demand (name the transport fix), not as a claimed exploit.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
