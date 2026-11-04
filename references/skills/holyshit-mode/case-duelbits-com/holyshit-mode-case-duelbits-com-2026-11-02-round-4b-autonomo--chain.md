# 2026-11-02 round-4b: autonomous mass-assignment attempt — wall re-verified, shape changed — chain composition

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-4b-autonomo.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Operator asked to test the query_state mass-assignment without a console. Executed the
full autonomous equivalent on the VM:
1. Ephemeral secp256k1 keypair generated in RAM (`eth_account` on the VM venv).
2. Live challenge issued by the target (201, rotating 6-digit nonce) — message endpoint
   provably OPEN from DE.
3. Signature generated with the throwaway key — cryptographically valid for that exact
   challenge, byte-exact client flow.
4. `POST /auth/web3` with the valid pair: **500 Internal server error** — and 500 for the
   state-bomb variant and the replay variant; empty body = 401; the same-session resubmit
   also 500.

Conclusion: the region wall on the auth exchange has CHANGED SHAPE (round-1: clean 403
deny; now: unhandled 500 crash) but still stands from the DE vantage — the handler never
reaches account/state logic even with a provably valid signature. The state key-acceptance
test is therefore NOT completable from any datacenter/residential-DE vantage without a
real identity: web3 = wall (500), Google/Steam = needs a live identity-provider consent.
Cleanup: ephemeral key + artifacts shredded from VM RAM immediately after.

New ledger class: web3_exchange_500_regioncrash (region-deny regression: 500 instead of
403 = unhandled exception on the deny path; also a broken-error-handling flag across the
fleet's OAuth consumers).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
