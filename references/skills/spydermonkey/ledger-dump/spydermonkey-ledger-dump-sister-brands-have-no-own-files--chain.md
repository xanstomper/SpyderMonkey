# Sister brands have no own files — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-sister-brands-have-no-own-files.md`
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

A sister brand (perabet under gamdom; cocogamebox/dogcrash under bc.game) does
NOT get its own holyleadger file or campaign dir. Its rows live in the parent
brand's ledger + holyleadger JSON. To dump one brand: filter BOTH stores for the
brand string, case-insensitive, across title/asset/proof (holyleadger: class
`technique` too); sort rows by cvss desc; report severity/status counters plus
the chains whose steps/impact mention the brand. Proven scale: perabet = 26
rows, ALL CONFIRMED (4 high / 8 med / 10 low / 4 info), inside gamdom's ledger.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
