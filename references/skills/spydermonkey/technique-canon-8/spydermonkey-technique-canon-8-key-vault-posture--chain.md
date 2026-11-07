# Key Vault posture — chain composition

- source canon: `spydermonkey/technique-canon-8.md`
- base technique: `spydermonkey-technique-canon-8-key-vault-posture.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Vaults with public network access + soft-delete absent. Decisive test: public reachability of the vault endpoint = the posture row.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
