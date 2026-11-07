# JWT & session-token crypto — mesh / federated

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-jwt-session-token-crypto.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **mesh** · auth **federated** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| alg=none | `jwt_tool -M none` on OWN issued token | none accepted |
| HS/RS confusion | `jwt_tool -X k` (own public key as HMAC) | signature verified with pubkey bytes |
| Weak HMAC | `hashcat -m 16500` on own token | secret cracked |
| kid/path trick | `jwt_tool` kid traversal (own token) | file-read marker |
| jku/x5u open | `jwt_tool -M pb` (own token) | attacker-supplied JWKS accepted (lab) |

## Probe adjustment (mesh × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
