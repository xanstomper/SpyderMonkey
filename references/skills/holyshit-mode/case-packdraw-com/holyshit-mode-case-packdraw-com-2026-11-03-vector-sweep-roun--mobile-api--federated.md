# 2026-11-03 vector sweep round (customer info / control panels / wallet) — mobile-api / federated

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-vector-sweep-roun.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **federated** · chain role **entry**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Customer info:** NOT reachable unauth. Public `pack-result`/`created` stream verified =
  product+price only (live DOM + RSC checked); private channels 403; SSR anonymized.
- **Control panels:** absent on every plane (prod 404/ghost, alias host-level-405, staging
  Vercel-auth 401; admin staff dashboard internal names all 404).
- **Wallet/drain plane:** money APIs = server actions behind auth; deposit/cashout
  mechanics invisible unauth. The only drain-class chain remains PF seed-prediction
  (operator 2-open test). Alias = static shell, POST blocked host-level (405 everywhere =
  Vercel frozen deployment, NOT routes - discriminator: 405-on-all-paths means host-level
  block, not route existence).

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
