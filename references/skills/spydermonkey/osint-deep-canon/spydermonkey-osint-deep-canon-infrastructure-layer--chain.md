# Infrastructure layer — chain composition

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-infrastructure-layer.md`
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
| Cert transparency | `ctfr`/`crt.sh` (public) | subdomain inventory |
| Passive dns | `subfinder -passive`/`chaos` (needs key) | historic records |
| Tech stack | `whatweb`/`wappalyzer` (public) | stack fingerprint |
| Document meta | `metagoofil` on PUBLIC docs | author/software meta |
| Git exposure | `gitleaks`/`gitdorker` on public repos | indexed secrets |
| Maps/geo | GeoVision pipeline on public imagery | location context |
| Wayback archaeology | `waybackurls`/`waymore` (public) | dead endpoints/old versions |
| Archive chats/forums | `pagodo` dorks (public index) | mentions/credentials chatter |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
