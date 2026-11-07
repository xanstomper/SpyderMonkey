# 4. Schema-library extraction — proving the auth gate WITHOUT a session — container / unauth

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-4-schema-library-ex.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **container** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
