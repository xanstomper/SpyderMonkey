# What lives where — mobile-api / federated

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-what-lives-where.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- VM (`ssh vermes`, opc@92.5.99.31): `~/holyshit-mode/` (full repo) + `~/.hermes/scripts/holyleadger/` (all 15 ledger JSONs, chmod 700 dir / 600 files).
- Home: same paths (authoritative copy for git pushes — VM has no GitHub creds).
- Sync out: `rsync -az ~/holyshit-mode/ vermes:~/holyshit-mode/` + ledger dir.
- Sync back: reverse rsync after engagement, then relay to GitHub from home.

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
