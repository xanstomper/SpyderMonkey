# Sister brands have no own files

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

A sister brand (perabet under gamdom; cocogamebox/dogcrash under bc.game) does
NOT get its own holyleadger file or campaign dir. Its rows live in the parent
brand's ledger + holyleadger JSON. To dump one brand: filter BOTH stores for the
brand string, case-insensitive, across title/asset/proof (holyleadger: class
`technique` too); sort rows by cvss desc; report severity/status counters plus
the chains whose steps/impact mention the brand. Proven scale: perabet = 26
rows, ALL CONFIRMED (4 high / 8 med / 10 low / 4 info), inside gamdom's ledger.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
