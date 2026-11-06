# Phase 2: TLS + SAN Extraction — host / federated

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-2-tls-s.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **host** · auth **federated** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- OpenSSL `s_client -connect` cert SAN revealed: `openinfra.freeinference.org`, `*.opendata.freeinference.org`
- These internal infra hosts are not linked from the public site — SAN extraction is the only discovery vector
- Technique: `openssl s_client -connect freeinference.org:443 -servername freeinference.org`

## Probe adjustment (host × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
