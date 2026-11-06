# Score: 92 (High) — chain composition

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-score-92-high.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **E** (Exploitability): 9 — trivial wordlist brute, no tooling required
- **I** (Impact): 9 — full infra topology + live utilization + traffic volumes
- **L** (Likelihood): 8 — password `madsys` found on 7th attempt; real password likely equally weak
- **R** (Reproducibility): 9 — single curl with correct password returns 6.3MB
- **N** (Novelty): 7 — shared-secret telemetry endpoint is a distinct pattern, but brute-without-rate-limit is classic OWASP

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
