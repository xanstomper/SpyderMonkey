# Collection hygiene — chain composition

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-collection-hygiene.md`
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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
