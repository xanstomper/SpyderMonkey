# Litigation dockets as a code-origin oracle (no-breach case) — container / high-priv

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-litigation-dockets-as-a.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
