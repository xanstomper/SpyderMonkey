# The sendable disclosure variant (Obsidian/client-ready) — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-the-sendable-disclos.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When the operator wants findings documented **to send to the target** (bounty, responsible
disclosure, or leverage), write a SECOND document distinct from the internal report — same
facts, different framing:

- **Professional disclosure tone, no tooling or vantage reveals** beyond what reproduces the
  bug: PoC links/requests a defender can run, code citations from THEIR OWN bundle, fixes per
  finding. No operator infrastructure names, no burner identities, no attack-tooling names.
- **Severity-ranked with honest credit**: state mitigations that work (a respected opt-out, a
  held gate) inside the finding — credibility with the target's security team is leverage,
  padding is not.
- **Claim-channel check BEFORE promising a bounty** (and before burning hours): fetch
  `/.well-known/security.txt`, grep the ToS for disclosure/bounty language, and search the
  platforms (Bugcrowd/HackerOne/Intigriti/Immunefi/YesWeHack/Cantina) for the target or its
  family. No program + no security.txt + silent ToS = **no payout channel exists** — say so
  early and frame the work as a disclosure package or portfolio, never as income. Never
  promise a bounty for a target with no claim channel.
- Deliverable placement: the operator's Obsidian vault (`~/Documents/Obsidian Vault/<Target>
  Redteam/`) as one markdown note per engagement, named for sending. Link the internal case
  file by name, not by content — the internal report keeps tooling/vantage detail; the sendable
  doc keeps only what the target may see.
- If raw evidence exists (socket captures, header dumps), say where it is preserved and offer
  the walkthrough — an offer to reproduce on demand is what converts a report into a bounty
  conversation.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
