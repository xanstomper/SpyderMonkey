# Structure (each section's purpose) — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-structure-each-secti.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Header** — target, generation timestamp, counts (classes tracked / confirmed /
  hypothesis / negative / chains). Compliance + scope-evidence at a glance.
- **`## Confirmed Holy Shits`** — the money section. Each confirmed class, ranked by score
  desc (then status tier), with score / technique / probe-count / last-probed. **Severity
  high first.** This is what clients read first.
- **`## Hypotheses (need proof)`** — unproven-but-higher-probability classes with score +
  probe-count. Not Holy Shits (mandate §29 strictness: a finding needs provable req+resp,
  kill-chain phase + ATT&CK id, one-sentence impact, non-destructive validation) — flagged
  as the highest-priority NEXT decisive tests.
- **`## Ruled Out (negative)`** — classes tested and cleared. Evidence of test coverage
  (valuable for scope/compliance), excluded from remediation.
- **`## Attack Paths`** — each recorded chain (crown jewel, steps joined with `→`, impact).
  Chains the isolated findings into exploit narratives.
- **`## Remediation Priority`** — the standing ordering: (1) confirmed holyshits first
  (RCE/admin-bypass/cross-tenant/cloud-cred), (2) confirmed chains (fix the base primitive
  step first), (3) hypotheses (prove or dismiss), (4) re-verify confirmed on every deploy
  (findings decay).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
