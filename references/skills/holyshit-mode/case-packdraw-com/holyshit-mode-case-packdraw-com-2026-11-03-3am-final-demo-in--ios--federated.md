# 2026-11-03 3AM final: demo inert, PF hypothesis upgraded, T2 stands — ios / federated

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-3am-final-demo-in.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Demo mode: verified INERT for guests (4 click sequences incl post-Continue, DOM dumps,
  zero network) — no unauth seed-observation path exists.
- PF algorithm verbatim (from their fairness page): `ticket = (BigInt('0x'+sha512(
  clientSeed+':'+serverSeed+':'+nonce)) % 1_000_000) + 1`; jackpot = `sha256(eosBlockHash)
  % totalTickets + 1` with contiguous ticket ranges. Their text: nonce is needed "when
  server seeds and client seeds remain unchanged, as is the case when opening multiple
  packs in a single purchase"; the hashed server seed is shown in the account PROFILE
  before purchase and the unhashed seed exposed after. Account-level seed commitment +
  nonce-machinery = fixed-seed architecture hypothesis (58-70 if 2-open test confirms
  non-rotation across purchases). Full verify recipe documented in the ledger class.

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
