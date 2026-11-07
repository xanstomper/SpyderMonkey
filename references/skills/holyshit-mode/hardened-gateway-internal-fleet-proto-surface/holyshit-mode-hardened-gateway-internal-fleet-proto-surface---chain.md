# Contrast vs the vulnerable GoTrue variant (gratisfy/gonka) — chain composition

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The earlier findings (redirect_uri forwarded verbatim, anon key client-exposed, unthrottled code
exchange) come from an **un-hardened GoTrue deployment**. Always fingerprint BEFORE assuming: server-side
PKCE + no client anon key + hardcoded redirect_to ⇒ the gratisfy chain does not apply; pivot.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
