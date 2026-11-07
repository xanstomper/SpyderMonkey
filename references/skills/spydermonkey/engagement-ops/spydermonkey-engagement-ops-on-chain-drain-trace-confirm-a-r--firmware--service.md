# On-chain drain trace: confirm a reported breach/drain actually moved money — firmware / service

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-on-chain-drain-trace-confirm-a-r.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **firmware** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

When a target (or its parent brand) has a publicly-reported exploit/drain that names a wallet
address, VALIDATE it on the public ledger before reporting the fund movement as fact. "The wallet
took it" is a claim; "the wallet held X and is now empty, last outflow to Y" is a finding. Public
read-only blockchain data is catalog-legal (no corpus wall). Recipe (works for ETH/ERC-20/BSC/TRON):

1. **Keyless ETH RPCs are rate-limited** — Etherscan V1 is deprecated (returns `NOTOK` telling you
to switch to V2); `eth.llamarpc.com`/`rpc.ankr.com`/`cloudflare-eth.com` refuse or rate-limit anonymous
calls. `https://ethereum.publicnode.com` tolerated anonymous `eth_getBalance`/`eth_getTransactionByHash`
in practice — use it first. For BSC use `bsc-dataseed1.binance.org`.
2. **ETH balance**: `eth_getBalance [addr,latest]` — convert hex wei → ETH.
3. **ERC-20 balance**: `eth_call` the token contract's `balanceOf(addr)`. Method selector is `0x70a08231`
+ 32-byte zero-padded address: `data="0x70a08231" + "0"*24 + addr(40 hex)`. USDC =
`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`, USDT = `0xdAC17F958D2ee523a2206206994597C13D831ec7`. A wiped
ERC-20 balance is the drain-confirmation signal even when native balance is trivial.
4. **Volume + tx count**: Blockcypher `api.blockcypher.com/v1/eth/main/addrs/<addr>?limit=N` returns
`total_received`/`total_sent` (in ETH units in the JSON, not wei for `-limit=1`; the `?limit=` form
returns full-volume per tx before summarising), `n_tx`, `balance`. High nonce (`eth_getTransactionCount`)
+ near-zero balance + a `final_balance` that is ~$10 of dust = the wallet processed and emptied itself.
5. **Where it ended**: pull the newest `txrefs`, take the last `tx_hash`, then
`api.blockcypher.com/v1/eth/main/txs/<hash>` → `outputs[].addresses` gives the FINAL recipient.
6. **Report both interpretations**: an exploit wallet that's fully drained (0 ETH/0 USDC/0 USDT, high nonce,
last outflow weeks ago) means the proceeds are laundered and NOT recoverable at that address — the
on-chain trace turns "drain X" into a concrete closed finding and may DISPROVE a recovery claim. Pair
it with any documented victim-receiver wallets (from forum reports) — if those are also swept, the
drain-onward is confirmed. Register as FINANCIAL_EXPLOIT with the traced address + balances + threshold
in the proof; a standard-account drain that already moved is a finding that closes the lane, not a dead end.
Also note: the [background-delegation provider pitfall](#background-delegation-pin-a-working-provider-or-the-fan-out-dies-silently) applies when parallelizing this.

## Probe adjustment (firmware × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
