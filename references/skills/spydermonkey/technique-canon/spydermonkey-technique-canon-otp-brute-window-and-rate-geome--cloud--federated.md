# OTP brute window and rate geometry — cloud / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-otp-brute-window-and-rate-geome.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

OTP validation with per-request cost < lockout threshold is enumerable (6-digit, 10 tries/lockout, no window reset = 1-in-10000 per lockout cycle). Decisive test: measure the exact counters — wrong-OTP responses until lock, lock TTL, and whether attempts decrement on resend. Register the arithmetic; never extract a live OTP.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
