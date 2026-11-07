# The purple contract — chain composition

- source canon: `kage/mirror-playbook.md`
- base technique: `kage-mirror-playbook-the-purple-contract.md`
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

1. mirror: family CONFIRMED → rule (id, ATT&CK, log source, Sigma YAML)
2. telemetry: the registry of what the operator CAN see
3. validate: rc=1 while any rule lacks a live source — the gap list is the deliverable
4. report: the handoff artifact (rules + telemetry map)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
