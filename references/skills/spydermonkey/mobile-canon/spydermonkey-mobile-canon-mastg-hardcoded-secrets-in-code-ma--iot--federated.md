# MASTG Hardcoded Secrets in Code (MASTG-CRYPTO-RESILIENCE) — iot / federated

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-hardcoded-secrets-in-code-ma.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **iot** · auth **federated** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: api keys, jks keystores, endpoints in the binary
- probe: static strings dump of the lab build; compare against the known-good key list
- wall: read-only static analysis of the artifact the scope declares

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
