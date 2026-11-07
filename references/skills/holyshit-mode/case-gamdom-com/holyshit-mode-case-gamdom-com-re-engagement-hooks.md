# Re-engagement hooks

- source canon: `holyshit-mode/case-gamdom-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Post-auth chain READY (payload shapes extracted from the schema library in
   `util.JkhQEYLZ.js`): `tipUser {toId, reason, walletInfo:{amount≥0, unit:WalletUnit enum,
   displayCurrency}, antiFraudSession}` — the walletInfo-trust forge test (amount=999999999999
   on a 0-balance session) is built: `~/gamdom-wallet-claim-test.py` (operator's box, needs
   GD_COOKIE). Reasoned verdict ~92% secure (walletInfo cannot name foreign wallets;
   `amount_coins_requested` naming = request-not-trust; anti-fraud pipeline; reconciliation
   catches mints) — residual risk: FIAT unit-conversion edges + `wallet_type` override + tips
   use looser `number` typing than withdrawals' `Integer>0` refinement.
2. Watch for `forced:true` crash rounds — the PF escape hatch = part-2 material.
3. The fossil box: re-check 3306/8083 exposure; whether golvar8/sieveunem/a.info got registered
   or the dead login CTA fixed. Note any new funnel target.
4. Bundle-hash diff BOTH brands on re-engage (perabet chunks ≠ gamdom chunks; namespaces
   chat/dice/general only on perabet).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
