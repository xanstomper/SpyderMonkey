# Infrastructure layer

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
| Cert transparency | `ctfr`/`crt.sh` (public) | subdomain inventory |
| Passive dns | `subfinder -passive`/`chaos` (needs key) | historic records |
| Tech stack | `whatweb`/`wappalyzer` (public) | stack fingerprint |
| Document meta | `metagoofil` on PUBLIC docs | author/software meta |
| Git exposure | `gitleaks`/`gitdorker` on public repos | indexed secrets |
| Maps/geo | GeoVision pipeline on public imagery | location context |
| Wayback archaeology | `waybackurls`/`waymore` (public) | dead endpoints/old versions |
| Archive chats/forums | `pagodo` dorks (public index) | mentions/credentials chatter |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
