# Identity layer

- source canon: `spydermonkey/osint-deep-canon.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Username mesh | `maigret`/`sherlock` (public profiles) | footprint across platforms |
| Email graph | `holehe` on OWN email (operator's) | signups enumerated |
| Phone intel | `phoneinfoga` on in-scope number | provider/geo (public) |
| Breach posture | `h8mail`/`breach-parse` on OWN corpus | creds in public breaches |
| Social media | `snscrape`/`instaloader` public profiles | timeline/posts corpus |
| Profile correlation | `social-analyzer` (public) | cross-platform identity |
| Avatar reverse | `exiftool`/`reverse image` (public) | same person across sites |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
