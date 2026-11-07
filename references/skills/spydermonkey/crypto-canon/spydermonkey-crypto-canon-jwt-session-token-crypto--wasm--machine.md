# JWT & session-token crypto — wasm / machine

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-jwt-session-token-crypto.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **wasm** · auth **machine** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| alg=none | `jwt_tool -M none` on OWN issued token | none accepted |
| HS/RS confusion | `jwt_tool -X k` (own public key as HMAC) | signature verified with pubkey bytes |
| Weak HMAC | `hashcat -m 16500` on own token | secret cracked |
| kid/path trick | `jwt_tool` kid traversal (own token) | file-read marker |
| jku/x5u open | `jwt_tool -M pb` (own token) | attacker-supplied JWKS accepted (lab) |

## Probe adjustment (wasm × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
