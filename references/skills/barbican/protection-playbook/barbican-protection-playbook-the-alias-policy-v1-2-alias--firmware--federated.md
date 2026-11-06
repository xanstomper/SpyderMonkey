# The alias policy (v1.2 — `alias`) — firmware / federated

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-alias-policy-v1-2-alias.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **firmware** · auth **federated** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Derivation: `ghost-` + first 6 hex of sha256(`target#epoch`) — deterministic
  per target+epoch, stable across sessions, no randomness to lose.
- Rotation: `--rotate` bumps the epoch → new alias per engagement window. The
  posture's `--alias` (human-chosen) always wins over the derived suggestion.
- Artifacts carry the alias, NEVER the operator identity — and `sanitize` is the
  enforcement pass that makes it true on disk.

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
