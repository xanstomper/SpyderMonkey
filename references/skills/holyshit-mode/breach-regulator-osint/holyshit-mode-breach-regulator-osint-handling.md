# Handling

- source canon: `holyshit-mode/breach-regulator-osint.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Regulator-leak data is published journalism / public interest — accessing it is
  legitimate OSINT. The SCOPE GATE for live probing is unchanged by it: history informs,
  it does not authorize.
- PII minimality: pull the minimum documents needed for the finding; report the CLASSES
  exposed (passports, financials, personnel rosters) with counts, not the personal data
  itself. Keep downloaded PDFs in /tmp scratch, not the workspace or reports.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
