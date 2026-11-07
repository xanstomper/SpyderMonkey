# 5. Register + report — chain composition

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-5-register-report.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Ledger rows: flat v2 schema (see SKILL.md State & Egress), proof carrying
  literal `baseline: … attack: … diff: …` sections.
- Report shape: TLS table (host × protocol × cert × headers) + auth-architecture
  summary (bearer type, storage, rotation, WS auth material) + hypothesis
  section clearly separated from confirmed findings.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
