# 5. Client-keypair challenge protocols (merchant / game-provider SDKs) — host / low-priv

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-5-client-keypair-challenge-proto.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **host** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

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

## Probe adjustment (host × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
