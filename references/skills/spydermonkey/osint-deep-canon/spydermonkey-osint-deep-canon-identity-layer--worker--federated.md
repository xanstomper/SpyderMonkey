# Identity layer — worker / federated

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-identity-layer.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Username mesh | `maigret`/`sherlock` (public profiles) | footprint across platforms |
| Email graph | `holehe` on OWN email (operator's) | signups enumerated |
| Phone intel | `phoneinfoga` on in-scope number | provider/geo (public) |
| Breach posture | `h8mail`/`breach-parse` on OWN corpus | creds in public breaches |
| Social media | `snscrape`/`instaloader` public profiles | timeline/posts corpus |
| Profile correlation | `social-analyzer` (public) | cross-platform identity |
| Avatar reverse | `exiftool`/`reverse image` (public) | same person across sites |

## Probe adjustment (worker × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
