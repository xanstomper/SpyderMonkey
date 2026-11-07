# The GoTrue flaw (config-level, real but often unexploitable) — chain composition

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-the-gotrue-flaw.md`
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

GoTrue (`/auth/v1/authorize?provider=X&redirect_uri=ATTACKER`) forwards ANY client-supplied `redirect_uri` verbatim to the OAuth provider. Variants all pass through:
- `https://evil.com/cb`
- `http://evil.com/cb` (no HTTPS enforcement)
- `/callback/../../evil` (path traversal, no normalization)
- `evil.com@legithost/cb` (userinfo confusion)

`redirect_to` is a DIFFERENT benign param — it passes as a dead provider query param (false-positive discriminator).

**The impact gate is provider-side, not GoTrue-side.** GoTrue being vulnerable is necessary but NOT sufficient. Rate the GoTrue-side flaw ~8.1 as a config finding; the kill-chain only fires if the provider also accepts the URI.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
