# SPYDERMONKEY — Deep OSINT Canon (v6.0)

Open-source intelligence classes — public data only, no credentialed access,
no scraping of private accounts. Every query target is either public by
design or named in the engagement scope. Bindings: ATT&CK T1593/T1596.

## Identity layer

| Probe | Test | Confirmed-when |
|---|---|---|
| Username mesh | `maigret`/`sherlock` (public profiles) | footprint across platforms |
| Email graph | `holehe` on OWN email (operator's) | signups enumerated |
| Phone intel | `phoneinfoga` on in-scope number | provider/geo (public) |
| Breach posture | `h8mail`/`breach-parse` on OWN corpus | creds in public breaches |
| Social media | `snscrape`/`instaloader` public profiles | timeline/posts corpus |
| Profile correlation | `social-analyzer` (public) | cross-platform identity |
| Avatar reverse | `exiftool`/`reverse image` (public) | same person across sites |

## Infrastructure layer

| Probe | Test | Confirmed-when |
|---|---|---|
| Cert transparency | `ctfr`/`crt.sh` (public) | subdomain inventory |
| Passive dns | `subfinder -passive`/`chaos` (needs key) | historic records |
| Tech stack | `whatweb`/`wappalyzer` (public) | stack fingerprint |
| Document meta | `metagoofil` on PUBLIC docs | author/software meta |
| Git exposure | `gitleaks`/`gitdorker` on public repos | indexed secrets |
| Maps/geo | GeoVision pipeline on public imagery | location context |
| Wayback archaeology | `waybackurls`/`waymore` (public) | dead endpoints/old versions |
| Archive chats/forums | `pagodo` dorks (public index) | mentions/credentials chatter |

## Discovery layer (authorized/bfe)

| Probe | Test | Confirmed-when |
|---|---|---|
| BreachCLI | `pwned`-style check on own corpus | leaked accounts |
| Credential stuffing Feasibility | count of unique creds in OWN corpus | reaching attack material |
| Suppliers chain | public vendor docs (in scope) | third-party attack surface |
| Social graph | `maigret` mutuals (public) | trusted-personas map |

## Collection hygiene

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