# Regulator-leak archives (operator dossiers, public) — container / root

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-regulator-leak-archives.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Curaçao: the Casino Secrets leak (a researcher breached the CGA licensing system;
  filings published as public-interest journalism). Per-operator files at
  `curacaofiles.com/casinos/<license-number>-<entity>` — the license number on the target's
  own site footer is the file key (e.g. OGL/2024/1507/0838 -> file 1507).
- A file page lists applications, domains, related entities, and DOCUMENTS behind a
  download API (`/api/documents/<id>?key=...&name=...`). Pair the listing order with the
  hrefs to map names -> files, then download the priority classes.
- **Document priority order:** P&L/financial statements -> org chart (densest: dozens of
  real names + roles = the personnel map) -> group-structure charts -> M&A / share-purchase
  agreements (the ownership chain) -> signed personnel history disclosures -> AML/data-
  protection policies -> passport scans / bank references (last; PII-minimal handling).
- Extract with `pdftotext <file> -`. Scanned/image PDFs have no text layer = OCR ceiling —
  note "scanned, not read" rather than claiming content. Person-name extraction: regex
  capitalized name pairs, then filter against a corporate-word blacklist (Share, Director,
  Class, Meeting, ...) before calling anything a person.
- Check sibling-license files too: renames/amendments ("X thans Y") link the old and new
  entities = the fleet's corporate history.

## Probe adjustment (container × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
