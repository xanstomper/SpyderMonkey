# PHASE 5 — AUTH & FLOW ANALYSIS — ios / federated

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-5-auth-flow-analy.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ios** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Session model**: where tokens live (cookie vs localStorage), flags (HttpOnly/Secure/
  SameSite), rotation on privilege change, fixation vectors, ?token= URL params (HOLY SHIT:
  session fixation via referrer/history).
- **OAuth flows**: state validation, redirect_uri validation, token-in-fragment leakage,
  PKCE enforcement.
- **Password/account flows**: enumeration via response/timing divergence, reset-token
  entropy and single-use enforcement.
- **Verification gates**: server-side verification or stateless claim gate? (hash-verify →
  empty-body claim + no server-to-server callback = farm hypothesis; CVSS ~7.5 documented).
- Deliverable: session/OAuth/reset findings, stateless-verification hypotheses.

## Probe adjustment (ios × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
