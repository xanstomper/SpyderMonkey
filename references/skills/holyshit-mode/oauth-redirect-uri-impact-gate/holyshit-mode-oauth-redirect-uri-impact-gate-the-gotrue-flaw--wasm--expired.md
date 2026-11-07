# The GoTrue flaw (config-level, real but often unexploitable) — wasm / expired

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-the-gotrue-flaw.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

GoTrue (`/auth/v1/authorize?provider=X&redirect_uri=ATTACKER`) forwards ANY client-supplied `redirect_uri` verbatim to the OAuth provider. Variants all pass through:
- `https://evil.com/cb`
- `http://evil.com/cb` (no HTTPS enforcement)
- `/callback/../../evil` (path traversal, no normalization)
- `evil.com@legithost/cb` (userinfo confusion)

`redirect_to` is a DIFFERENT benign param — it passes as a dead provider query param (false-positive discriminator).

**The impact gate is provider-side, not GoTrue-side.** GoTrue being vulnerable is necessary but NOT sufficient. Rate the GoTrue-side flaw ~8.1 as a config finding; the kill-chain only fires if the provider also accepts the URI.

## Probe adjustment (wasm × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
