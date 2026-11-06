# Re-engagement hooks — cloud / high-priv

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-re-engagement-hooks.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
