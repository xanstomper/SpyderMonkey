# Litigation dockets as a code-origin oracle (no-breach case) — chain composition

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-litigation-dockets-as-a.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When a target has NO breach record, run its corporate entities (from the site footer:
foreign parents + US LLCs + any additional vehicles like payments companies) through
CourtListener RECAP (`storage.courtlistener.com/recap/...` PDFs), Justia Dockets, and
govinfo USCOURTS PDFs. Complaints are technical documents:

- IP/code-misappropriation complaints name the PREDECESSOR codebase and the engineers
  ("used software code belonging to the Partnership to develop <target> for <casino>")
  — that codebase's public audits and brand lineage answer architecture questions the
  live site won't answer unauth (RNG/seed policy, ownership chain, who built what).
- The judge's order rules on which claims survive dismissal — surviving fiduciary /
  misappropriation claims carry the best-supported factual allegations: dev timelines
  ("first assets imported <date> from the predecessor Figma"), domains seized, code
  origin, deposit volumes in user-facing filings.
- Harvest the entity map (extra corporate vehicles), financial scale (deposit figures
  named in complaints), licensing status ("operates without a license"), and adjacent
  litigation (the target named as defendant in laundering/impersonation suits) — all
  public, all report-class.
- `web_search "<entity> lawsuit OR complaint OR docket"` to find the cases, then pull
  the PDFs directly from the PACER mirrors above (free, no account).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
