# Hashing & password storage — windows / federated

- source canon: `spydermonkey/crypto-canon.md`
- base technique: `spydermonkey-crypto-canon-hashing-password-storage.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **windows** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Hash identification | `name-that-hash` on OWN dump | plaintext-friendly scheme (md5, lm) |
| Salt presence | `hashid -m` + `john --show` on own dump | unsalted scheme |
| Fast-hash brute | `hashcat` benchmark on own dump (mode table) | runtime < policy floor |
| Length-extension | `hashpump`-class tool on own MAC | length-extendable construction (lab) |

## Probe adjustment (windows × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
