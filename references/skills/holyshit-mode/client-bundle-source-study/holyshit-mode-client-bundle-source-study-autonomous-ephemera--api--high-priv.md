# Autonomous ephemeral-wallet signup test — api / high-priv

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-autonomous-ephemera.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

For web3-wallet login targets where the exchange is region-walled from every vantage you
control, complete the register + mass-assignment probe without the operator console:

1. Generate keypair on the probe box: `eth_account.Account.create()` (venv on disk —
   /dev/shm is often noexec).
2. Challenge: `POST <auth>/web3/message/?publicAddress=<addr>` — accept 200 AND 201
   (non-200 success statuses are common); response `.message`.
3. Sign: `Account.sign_message(encode_defunct(text=msg), key)` — `hex_signature` is
   65-byte r||s||v, directly recoverable by web3.js `personal.ecRecover`.
4. `POST <auth>/web3` body `{address, signature, ...injected-keys}` — 200/201 returns the
   session + user object; diff the user object for stuck keys (role/VIP class/verified).
5. Hygiene: key stays in RAM; shred the artifacts dir immediately; the account is
   throwaway and non-destructive.
6. Scope note: a vanity keypair is an operator-directed self-account test, NOT identity
   fraud — no real identity, no funds, no third-party accounts touched.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
