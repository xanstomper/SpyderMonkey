# Campaign ledger schema (ledger.jsonl rows) — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-campaign-ledger-schema-ledger-jsonl.md`
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

`{v:2, id:"SPY-NNN", title, cls (UPPERCASE), asset, severity (lowercase), cvss,
status (CONFIRMED|HYPOTHESIS), confidence, evidence_quality, proof, prev, hash}`
plus optional `cwe/wstg/attack/dedupe/evidence/request/at/updated`. Proof carries
literal `baseline: … attack: … diff: …` sections. Parse each line with json.loads,
skip non-dict or non-SPY rows.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
