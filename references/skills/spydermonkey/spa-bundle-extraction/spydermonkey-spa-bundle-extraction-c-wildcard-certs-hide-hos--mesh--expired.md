# C. Wildcard certs hide hosts from CT logs — DNS wordlist instead — mesh / expired

- source canon: `spydermonkey/spa-bundle-extraction.md`
- base technique: `spydermonkey-spa-bundle-extraction-c-wildcard-certs-hide-hos.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

CT-log enumeration is blind to every subdomain NOT in a cert when a wildcard covers
it. After the CT pass, hand-probe a plausible-name DNS list (`api`, `ws`, `cashier`,
`wallet`, `my`, `auth`, `account`, `pay`, `download`, `client`, `update`, `admin`,
`test`, `dev`, `crm`...) against each in-scope apex. Prioritize hits on RAW (non-CF)
IPs — origin-visible hosts — and probe what they serve. A live payments app
(`cashier.<brand>`, Next.js) was invisible to 8 CT pulls and visible to one dig.

## Probe adjustment (mesh × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
