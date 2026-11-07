# Infrastructure layer — gateway / root

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-infrastructure-layer.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

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

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
