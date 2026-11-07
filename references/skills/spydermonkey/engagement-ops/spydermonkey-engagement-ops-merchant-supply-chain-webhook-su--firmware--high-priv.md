# Merchant / supply-chain webhook surface: the session+fund mint primitive — firmware / high-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-merchant-supply-chain-webhook-su.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **firmware** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

A target that runs a merchant ecosystem (integrators pushing player balance and redeeming
one-time login codes) exposes a supply-chain webhook surface that is a genuine session+fund
mint class — far stronger than recon telemetry. Recover it from the operator's own SDK or
from third-party repos that integrated the merchant API (`gh search code "<socket/API host>"`),
then reproduce the EXACT serving implementation read-only:

1. **Map the two primitives.** Typical names: `create-code` (return a one-time login code for a
   `playerId`) and `push/balance/change` (`{playerId, currencyName, changeAmount,
   beforeChangeAmount}` — directly sets a player's balance in the platform). `create-code` is
   redeemed at a public path like `/api/merchants/auth/?code=X&path=Y` → **code possession =
   session control on the NEXT party's platform**. `push/balance/change` is **fund forgery at the
   supply-chain boundary** (an integrator tells the platform "this player's balance changed by X"
   and the platform trusts it).
2. **Read the signing scheme — it is the ONLY gate.** Reproduce the SDK's `Signature()` and read
   what it binds: a scheme like `HMAC-SHA256("POST\n{url}\n{timestamp}\n{MD5UPPER(body)}",
   securityKey)` + `mkey` + `t` (ms+5min) means the request is authorized purely by possession of
   the shared `securityKey`/`mkey`. Identify where those live (a DB config dictionary row named
   after the merchant) and flag that a leak of that row = the whole primitive.
3. **State the real impact, not the inventory.** A leaked/predictable `securityKey` becomes
   (a) mint unlimited one-time login codes for arbitrary `playerId` → account takeover, and
   (b) push arbitrary `changeAmount` balance changes → fund theft. That is a HIGH-class
   supply-chain trust finding (CWE-306 into AUTHZ, WSTG-SUPL-01), NOT a recon inventory row.
4. **Characterize, don't exploit — and be honest about the blockers.** Probe the real gateway
   host read-only (e.g. `provider.<brand>.<tld>` — a CloudFront-fronted 502 `Error from
   cloudfront` means the origin is down/geo-fenced, still a real live public surface worth
   registering). No key leaked in the repo (dummy test values) + origin down = the vulnerability
   is characterized but NOT live-exploitable; say so. Never mint/validate a real code or push a
   balance — those are state-changing. Fix demands: high-entropy + rotated securityKey, never
   logged/committed/DB-serialized in the clear; webhook rate-limited and player-identity
   server-bound; `push/balance/change` validated against an independent ledger.
5. **Register with the IN-ESTATE asset** (the merchant gateway host is often a subdomain the
   scope gate refuses — put the target's own asset in `--asset`, the gateway host in
   title/proof with third-party-or-operator attribution).

This is the shape of a real-vuln class — a trust boundary that, if the one secret leaks,
becomes takeover + fund forgery — versus an RTP number or a namespace handshake.

**Proving a merchant-key hunt is EXHAUSTIVE (so the "no leaked key" negative is decisive) requires
sweeping the WHOLE integrator/operator account, not just the repo you remembered.** When the
credential you need is held in a DB config row (never in code), enumerate the merchant-API
integrator's entire GitHub account (`gh api users/<u>/repos?per_page=100`) and grep EACH repo for
the key patterns — plus `git log --all -p` the repo(s) that DO reference the API for committed
values (real `securityKey`/`mkey`/host, AWS/ak/DP keys, DSN creds). Many operator repos are EMPTY
skeletons (a `warning: you appear to have cloned an empty repository` means zero content — that is a
non-leak, not a miss). A clean result across the full account + full history is what upgrades the
hunt from "we checked some repos" to a citable negative-with-value; an empty history and only
code-level (`url := ...create-code`) references with dummy test values is the decisive no-key-leak
evidence. Also `gh search code "<merchant gateway host>"` — if it returns ONLY the integrator's
own repo, no other party has reimplemented or commented the scheme, which independently confirms the
key stays in-house. This discipline closes the "there must be a leaked key somewhere" assumption
that would otherwise re-cost future sessions.

## Probe adjustment (firmware × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
