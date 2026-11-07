# Collection hygiene — browser / federated

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-collection-hygiene.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (browser × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
