# 4. Schema-library extraction — proving the auth gate WITHOUT a session — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-4-schema-library-ex.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The SPA client ships the complete zod/io-ts request-shape library, derived from the
backend's shared types. Exploit it:

1. Pool all code-split chunks, grep for the schema-definition chunk (look for
   `intersection([type({...}), partial({...})])`, `refinement(Integer,`, `union([...])`).
2. Extract the target RPC's full arg schema + every referenced enum (WalletUnit:
   COINS|USDT|USDC|USD1|FIAT_*|BTC_SATOSHI|...).
3. Build a COMPLETE valid shape and fire it unauth: the uniform `Invalid parameters` wall
   becomes an explicit error (`Not logged in`) = validation→auth order proven, pre-auth
   question closed.
4. Read the trust model from the schemas:
   - `*_requested` field naming and OPTIONAL client-supplied fields (`userExpectedFeeCoins`)
     = the server recomputes; client amounts are requests, not truths.
   - A money-transfer shape with NO cross-user identifier (no walletId/ownerId) means
     IDOR is structurally impossible on that surface — only self-inflation (trusted
     amount) could be a vuln, and that gets caught by ledger reconciliation.
   - Asymmetry worth flagging: a tip endpoint using generic `number` where withdrawals
     use `refinement(Integer, e=>e>0)` — the loose side is where unit-conversion edges live.
5. Deliver the verdict with a confidence number (~92%) + the named residual edges.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
