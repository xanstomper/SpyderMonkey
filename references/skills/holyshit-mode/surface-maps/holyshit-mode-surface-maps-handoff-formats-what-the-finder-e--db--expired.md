# Handoff formats (what the finder emits) — db / expired

- source canon: `holyshit-mode/surface-maps.md`
- base technique: `holyshit-mode-surface-maps-handoff-formats-what-the-finder-e.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **db** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the engine's own handshake/banner first — auth-stage reachability is the inventory row
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- `--to undercroft` — findings registered as PROBED logic seams (the descent's map).
- `--to 3am` — (flaw 11, seam A) observable-oracle rows: finder-confirmed leads
  the sweep verifies.
- `--to shukaku` — findings ingested into the harvest register WITH crown-class
  suggestions, derived from the family's CONFIRMED states when `--findings` is
  omitted. The harvester reasons/hunts from there.

## Probe adjustment (db × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
