# 8. Cross-brand (sibling-domain) drift — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-8-cross-brand-siblin.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Sister brands on the same stack (same error envelopes, CSP, cookies, CDN IPs): diff RPC method tables, namespace sets, endpoint literals, and gate behavior across brands. Older deployments expose different (usually smaller) surfaces and reveal which gates are new.
- Read the namespace init packet's `serverHost` — pods named `<brand>-rcc-slave-*` identify the INFRA OWNER and prove the fleet relationship at the socket level (a sister brand serving your sockets = same operator; their CSP cross-brand collectors corroborate).
- When the origin brand is geo-blocked from your vantage, its accessible sister brand usually runs the SAME shared data plane — the sister is the working vantage; probing the geo-walled brand's socket/API directly is wasted calls.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
