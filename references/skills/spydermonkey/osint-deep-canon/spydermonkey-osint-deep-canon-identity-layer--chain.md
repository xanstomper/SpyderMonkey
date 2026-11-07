# Identity layer — chain composition

- source canon: `spydermonkey/osint-deep-canon.md`
- base technique: `spydermonkey-osint-deep-canon-identity-layer.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Username mesh | `maigret`/`sherlock` (public profiles) | footprint across platforms |
| Email graph | `holehe` on OWN email (operator's) | signups enumerated |
| Phone intel | `phoneinfoga` on in-scope number | provider/geo (public) |
| Breach posture | `h8mail`/`breach-parse` on OWN corpus | creds in public breaches |
| Social media | `snscrape`/`instaloader` public profiles | timeline/posts corpus |
| Profile correlation | `social-analyzer` (public) | cross-platform identity |
| Avatar reverse | `exiftool`/`reverse image` (public) | same person across sites |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
