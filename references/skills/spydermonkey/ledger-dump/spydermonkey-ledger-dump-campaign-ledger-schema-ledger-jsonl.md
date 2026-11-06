# Campaign ledger schema (ledger.jsonl rows)

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-06

## The technique

`{v:2, id:"SPY-NNN", title, cls (UPPERCASE), asset, severity (lowercase), cvss,
status (CONFIRMED|HYPOTHESIS), confidence, evidence_quality, proof, prev, hash}`
plus optional `cwe/wstg/attack/dedupe/evidence/request/at/updated`. Proof carries
literal `baseline: … attack: … diff: …` sections. Parse each line with json.loads,
skip non-dict or non-SPY rows.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
