# Regulator-leak archives (operator dossiers, public) — chain composition

- source canon: `holyshit-mode/breach-regulator-osint.md`
- base technique: `holyshit-mode-breach-regulator-osint-regulator-leak-archives.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
