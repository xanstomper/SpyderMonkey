# Phrasing template — web-app / federated

- source canon: `holyshit-mode/adhoc-verification-loop.md`
- base technique: `holyshit-mode-adhoc-verification-loop-phrasing-template.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **web-app** · auth **federated** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

> **Ad-hoc verification passed: 7/7, exit 0** (not a suite green — no canonical test/lint config exists here; focused temp script, created/run/cleaned).
> - compile ✓ / synthetic fixture roundtrip ✓ / domain-window sanity ✓ / live end-to-end run ✓
> - First attempt failed on the harness (fixture omitted <field>), not the changed code; fixed and all green.

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
