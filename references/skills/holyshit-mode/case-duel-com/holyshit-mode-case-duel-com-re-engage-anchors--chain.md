# Re-engage anchors — chain composition

- source canon: `holyshit-mode/case-duel-com.md`
- base technique: `holyshit-mode-case-duel-com-re-engage-anchors.md`
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

- `VITE_BUILD_COMMIT` in the env object (this session: `22aa5245`) = the bundle-hash diff oracle.
- Re-verify first: profile financial fields, socket anon streaming, PaymentIQ test flag. `next --target duel.com` surfaces them.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
