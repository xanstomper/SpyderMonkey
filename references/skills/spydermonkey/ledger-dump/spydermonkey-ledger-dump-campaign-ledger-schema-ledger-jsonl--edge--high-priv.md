# Campaign ledger schema (ledger.jsonl rows) — edge / high-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-campaign-ledger-schema-ledger-jsonl.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **edge** · auth **high-priv** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`{v:2, id:"SPY-NNN", title, cls (UPPERCASE), asset, severity (lowercase), cvss,
status (CONFIRMED|HYPOTHESIS), confidence, evidence_quality, proof, prev, hash}`
plus optional `cwe/wstg/attack/dedupe/evidence/request/at/updated`. Proof carries
literal `baseline: … attack: … diff: …` sections. Parse each line with json.loads,
skip non-dict or non-SPY rows.

## Probe adjustment (edge × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
