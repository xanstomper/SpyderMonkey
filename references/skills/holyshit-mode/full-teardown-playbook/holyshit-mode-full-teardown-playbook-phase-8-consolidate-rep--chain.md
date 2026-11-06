# PHASE 8 — CONSOLIDATE & REPORT — chain composition

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-8-consolidate-rep.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Severity ranking**: HOLY SHIT tier = RCE, auth bypass on admin, full PII access, cloud
  cred theft, takeover chains, stateless payment/claim gates. Then high → med → low.
- **Attack-path chains**: combine findings into kill-chain narratives (recon→impact).
- **Detection gaps** (if purple-team scope): per-finding, propose analytic coverage.
- **Disclosure**: host abuse contact, upstream provider ToS, regulator — for anything
  outside own-infrastructure boundary.
- Deliverable: executive summary, technique-mapped findings, chains, remediations, evidence appendix.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
