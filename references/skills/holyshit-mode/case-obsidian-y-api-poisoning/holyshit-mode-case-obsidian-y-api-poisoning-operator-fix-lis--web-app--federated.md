# Operator fix list (delivered) — web-app / federated

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-operator-fix-lis.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **federated** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. Per-user/per-session conversation state (random session key per browser or no history); flush the poisoned buffer on deploy. Collapses findings 95/85.
2. Session-gate + IP rate-limit /pg/*. Collapses 90/70.
3. Move character/persona data out of system prompt into per-request injection.
4. Auth-gate /status?json=1.

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
