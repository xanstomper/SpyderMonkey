# Autonomous ephemeral-wallet signup test — chain composition

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-autonomous-ephemera.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
