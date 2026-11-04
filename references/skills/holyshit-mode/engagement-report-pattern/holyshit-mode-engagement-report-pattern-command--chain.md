# Command — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-command.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```bash
export HOLYSHIT_TARGET=example.com
python3 scripts/holyleadger.py report                 # stdout
python3 scripts/holyleadger.py report --out engagement-report.md   # write to file
```

Reads the ledger at `~/.hermes/scripts/holyleadger/<target>.json` (override home via
`HOLYSHIT_SCRIPT_DIR`).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
