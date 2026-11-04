# Litigation dockets as a code-origin oracle (no-breach case)

- source canon: `holyshit-mode/breach-regulator-osint.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
