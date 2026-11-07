# Next-session entry points — kubernetes / high-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-next-session-entry-points.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Bundle hashes (2026-10-03): main B6Fhk0_W, siteRouting BaxhyiW5, chat DiezdlP6, platform D9-WxdCi, sse C_n6QzEY, api Cyn6IDlf, firstPartyOidc CY_Rj2cE — hash-diff before re-probing.
- If redeployed: re-run authorize redirect_uri probe + all three brute bursts (handoff/oauth-token/verify OTP) + auth-mode split chain.
- Browser leg pending: Discord authorize page acceptance of evil.com redirect (needs operator-supervised Discord login).

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
