# Next-session entry points — kubernetes / machine

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-next-session-entry-points.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Bundle hashes (2026-10-03): main B6Fhk0_W, siteRouting BaxhyiW5, chat DiezdlP6, platform D9-WxdCi, sse C_n6QzEY, api Cyn6IDlf, firstPartyOidc CY_Rj2cE — hash-diff before re-probing.
- If redeployed: re-run authorize redirect_uri probe + all three brute bursts (handoff/oauth-token/verify OTP) + auth-mode split chain.
- Browser leg pending: Discord authorize page acceptance of evil.com redirect (needs operator-supervised Discord login).

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
