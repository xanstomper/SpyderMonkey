# Citations rot: check the current manifest before testing a claimed artifact — ios / federated

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-citations-rot-check-the-current-.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **ios** · auth **federated** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Public claims name files by build hash (`Crash.route.BBLHNSNC.js`). Builds rotate weekly;
resolve CURRENT chunk names from the live index/route manifest (`grep -oE
"[A-Za-z]+\.route\.[A-Za-z0-9_-]{8}\.js" client.<hash>.js`) before declaring a file
missing or testing its contents. A cited artifact's absence after rotation is a finding
(evidence rotated post-exposure); scanning ~800KB of current chunks for the claimed math
(sha256/2**52/slice(0,13)/hardcoded 64-hex) and finding none is the testable half.

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
