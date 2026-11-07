# Scope-gate notes — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-scope-gate-notes.md`
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

- Operator demanded "destructive level" holy shits → refused (bill-drain/DoS on third-party prod = sabotage). Clarified to read-only → everything above proven with ~10 requests total, no abuse. Free-AI reported as bill-drain RISK, never demonstrated by draining.
- Operator then claimed ownership ("this is my app and inference") → treated as authorized finding report; probes stayed non-destructive regardless; takeover-style "for control" actions still not run without verifiable infra proof.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
