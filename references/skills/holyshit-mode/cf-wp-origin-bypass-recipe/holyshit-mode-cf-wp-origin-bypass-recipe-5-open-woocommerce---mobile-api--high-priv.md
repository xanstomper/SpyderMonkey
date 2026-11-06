# 5. Open WooCommerce store API behind the mask — mobile-api / high-priv

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-5-open-woocommerce-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile-api** · auth **high-priv** · chain role **final**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`/wp-json/wc/store/v1/products` (full catalog), `/cart`, `/products/attributes` serve openly
with no auth/no nonce. Checkout (`/checkout`) is POST-reachable and responds to validation
(400 `Missing parameter(s): billing_address`) but **cart add-item and checkout need a nonce**
(`woocommerce_rest_missing_nonce`) — so no order can be created without an authenticated
session. This is the boundary for "customer info" on a masked WC shop: catalog open, orders
gated.

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
