# 6. Bet/settlement layer inspection — linux / federated

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-6-bet-settlement-layer-inspectio.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **linux** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Game bundles with an anti-exploit layer (`bet-guard`, `betGate`, `revealPacer`)
expose what the platform thinks its attack surface is. Look for client-side
pacing of money-relevant commits: `commitGuardMs` setTimeout deferrals,
`maxInflight`/`minIntervalMs` reveal pacing, client-held `txId`, `settle(payout)`
on bet objects, `commitWallet` called on client timers. Client-parametrized bet
APIs (`game.bet(amount, payout)` in public betting-script repos) put the
cashout target in client hands — that is the client-trust surface a
game-exploiter rides, and the shape to cite when reconstructing a disclosed
breach.

## Probe adjustment (linux × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
