# Turnstile harvesting — azure / federated

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-turnstile-harvesting.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **azure** · auth **federated** · chain role **final**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Headless Playwright (firefox) often fails to render the widget:
`[Cloudflare Turnstile] Unable to find onload callback 'onloadTurnstileCallback'`. The target's own
integration can be half-broken — if the widget never mints tokens for real users either,
server-side enforcement may be flaky. Test `?turnstile=garbage` once the rate limit allows.

## Probe adjustment (azure × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
