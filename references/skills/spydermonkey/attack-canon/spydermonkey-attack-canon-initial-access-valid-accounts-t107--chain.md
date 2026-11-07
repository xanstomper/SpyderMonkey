# Initial Access Valid Accounts (T1078) — chain composition

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-initial-access-valid-accounts-t107.md`
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

- class: default/leaked/reused credentials
- probe: only credentials the SCOPE FILE declares; never a live brute against prod
- wall: brute classes run against the dojo replica; prod runs are refusals

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
