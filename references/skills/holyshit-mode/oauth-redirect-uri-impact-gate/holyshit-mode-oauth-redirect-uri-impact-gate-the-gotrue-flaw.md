# The GoTrue flaw (config-level, real but often unexploitable)

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

GoTrue (`/auth/v1/authorize?provider=X&redirect_uri=ATTACKER`) forwards ANY client-supplied `redirect_uri` verbatim to the OAuth provider. Variants all pass through:
- `https://evil.com/cb`
- `http://evil.com/cb` (no HTTPS enforcement)
- `/callback/../../evil` (path traversal, no normalization)
- `evil.com@legithost/cb` (userinfo confusion)

`redirect_to` is a DIFFERENT benign param — it passes as a dead provider query param (false-positive discriminator).

**The impact gate is provider-side, not GoTrue-side.** GoTrue being vulnerable is necessary but NOT sufficient. Rate the GoTrue-side flaw ~8.1 as a config finding; the kill-chain only fires if the provider also accepts the URI.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
