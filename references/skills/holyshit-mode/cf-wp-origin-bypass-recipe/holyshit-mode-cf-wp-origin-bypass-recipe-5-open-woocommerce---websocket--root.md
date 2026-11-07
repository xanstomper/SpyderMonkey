# 5. Open WooCommerce store API behind the mask — websocket / root

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-5-open-woocommerce-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **websocket** · auth **root** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

`/wp-json/wc/store/v1/products` (full catalog), `/cart`, `/products/attributes` serve openly
with no auth/no nonce. Checkout (`/checkout`) is POST-reachable and responds to validation
(400 `Missing parameter(s): billing_address`) but **cart add-item and checkout need a nonce**
(`woocommerce_rest_missing_nonce`) — so no order can be created without an authenticated
session. This is the boundary for "customer info" on a masked WC shop: catalog open, orders
gated.

## Probe adjustment (websocket × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
