# C. Wildcard certs hide hosts from CT logs — DNS wordlist instead

- source canon: `spydermonkey/spa-bundle-extraction.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

CT-log enumeration is blind to every subdomain NOT in a cert when a wildcard covers
it. After the CT pass, hand-probe a plausible-name DNS list (`api`, `ws`, `cashier`,
`wallet`, `my`, `auth`, `account`, `pay`, `download`, `client`, `update`, `admin`,
`test`, `dev`, `crm`...) against each in-scope apex. Prioritize hits on RAW (non-CF)
IPs — origin-visible hosts — and probe what they serve. A live payments app
(`cashier.<brand>`, Next.js) was invisible to 8 CT pulls and visible to one dig.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
