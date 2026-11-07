# 6. Bet/settlement layer inspection — chain composition

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-6-bet-settlement-layer-inspectio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Game bundles with an anti-exploit layer (`bet-guard`, `betGate`, `revealPacer`)
expose what the platform thinks its attack surface is. Look for client-side
pacing of money-relevant commits: `commitGuardMs` setTimeout deferrals,
`maxInflight`/`minIntervalMs` reveal pacing, client-held `txId`, `settle(payout)`
on bet objects, `commitWallet` called on client timers. Client-parametrized bet
APIs (`game.bet(amount, payout)` in public betting-script repos) put the
cashout target in client hands — that is the client-trust surface a
game-exploiter rides, and the shape to cite when reconstructing a disclosed
breach.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
