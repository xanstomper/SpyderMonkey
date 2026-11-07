# Next-session entry points

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Bundle hashes (2026-10-03): main B6Fhk0_W, siteRouting BaxhyiW5, chat DiezdlP6, platform D9-WxdCi, sse C_n6QzEY, api Cyn6IDlf, firstPartyOidc CY_Rj2cE — hash-diff before re-probing.
- If redeployed: re-run authorize redirect_uri probe + all three brute bursts (handoff/oauth-token/verify OTP) + auth-mode split chain.
- Browser leg pending: Discord authorize page acceptance of evil.com redirect (needs operator-supervised Discord login).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
