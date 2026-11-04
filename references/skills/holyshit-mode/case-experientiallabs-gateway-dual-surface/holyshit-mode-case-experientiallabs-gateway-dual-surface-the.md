# The dual-surface anatomy (reusable fingerprint)

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

```
public edge   api.<domain>            -> /v1/* inference 401 (hardened) + /api/* mgmt 401 (hardened)
web root      platform.<domain>       -> Next.js + /api/* + /admin/* ALL server-side 401; Turnstile on every /auth bootstrap
internal fleet *.xplabs.ai            -> publicly IP-addressed (GCP/Azure ranges), WEAKER auth than public edge
```

The decisive discriminator repeated across engagements: **the public edge is hardened, the
internal serving fleet is not.** Attack the fleet, not the marketing host.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
