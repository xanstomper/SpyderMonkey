# TL;DR — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-tl-dr.md`
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

The operator's public gateway (`api.experientiallabs.ai`) is well-hardened — every `/v1/*`
inference route 401s without a valid `xpl_` key, the management API is session/org-gated, and
the Next.js admin console is auth-routed. However, the **internal serving fleet** under
`*.xplabs.ai` leaks heavily and exposes an **unauthenticated elastic-scaling control-plane
write** on the DeepSeek lane — a real compromise.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
