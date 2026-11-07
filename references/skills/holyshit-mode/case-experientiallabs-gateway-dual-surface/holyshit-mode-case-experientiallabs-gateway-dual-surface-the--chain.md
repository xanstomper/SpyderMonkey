# The dual-surface anatomy (reusable fingerprint) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-the.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```
public edge   api.<domain>            -> /v1/* inference 401 (hardened) + /api/* mgmt 401 (hardened)
web root      platform.<domain>       -> Next.js + /api/* + /admin/* ALL server-side 401; Turnstile on every /auth bootstrap
internal fleet *.xplabs.ai            -> publicly IP-addressed (GCP/Azure ranges), WEAKER auth than public edge
```

The decisive discriminator repeated across engagements: **the public edge is hardened, the
internal serving fleet is not.** Attack the fleet, not the marketing host.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
