# Collection hygiene

- source canon: `spydermonkey/osint-deep-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Rate limits | 1 req/2s on scraping tools | no platform abuse |
| Data minimization | store only rows needed for the engagement | minimal corpus |
| PII handling | corpus dir chmod 600 + engagement tag | protected |
| Retention | purge corpus at engagement close | deleted/archived |
| Source ledger | every row carries source url + fetch date | reproducible |

Walls: no credentialed access anywhere in this layer — if a source requires
a login, it is out of reach by design (the family does not buy/steal access
to private data). Public-data scraping respects robots/ToS and rate limits;
PII is processed only for the authorized engagement and purged at close.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
