# Campaign ledger schema (ledger.jsonl rows) — dns / low-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-campaign-ledger-schema-ledger-jsonl.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **dns** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`{v:2, id:"SPY-NNN", title, cls (UPPERCASE), asset, severity (lowercase), cvss,
status (CONFIRMED|HYPOTHESIS), confidence, evidence_quality, proof, prev, hash}`
plus optional `cwe/wstg/attack/dedupe/evidence/request/at/updated`. Proof carries
literal `baseline: … attack: … diff: …` sections. Parse each line with json.loads,
skip non-dict or non-SPY rows.

## Probe adjustment (dns × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
