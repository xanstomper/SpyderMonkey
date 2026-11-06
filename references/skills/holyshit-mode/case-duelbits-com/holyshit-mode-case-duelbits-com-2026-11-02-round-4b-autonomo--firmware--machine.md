# 2026-11-02 round-4b: autonomous mass-assignment attempt — wall re-verified, shape changed — firmware / machine

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-4b-autonomo.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **firmware** · auth **machine** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

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

## Probe adjustment (firmware × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
