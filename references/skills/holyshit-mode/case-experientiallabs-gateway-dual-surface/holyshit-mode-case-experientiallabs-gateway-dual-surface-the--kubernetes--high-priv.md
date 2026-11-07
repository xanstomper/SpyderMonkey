# The dual-surface anatomy (reusable fingerprint) — kubernetes / high-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-the.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **high-priv** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

```
public edge   api.<domain>            -> /v1/* inference 401 (hardened) + /api/* mgmt 401 (hardened)
web root      platform.<domain>       -> Next.js + /api/* + /admin/* ALL server-side 401; Turnstile on every /auth bootstrap
internal fleet *.xplabs.ai            -> publicly IP-addressed (GCP/Azure ranges), WEAKER auth than public edge
```

The decisive discriminator repeated across engagements: **the public edge is hardened, the
internal serving fleet is not.** Attack the fleet, not the marketing host.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
