# 4. Confirm the ONE surviving compromise (bounded, never drain) — container / low-priv

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **low-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

The unauthenticated unlimited proxy is the crown jewel when the other compression classes
hold. Re-verify it is STILL live with tiny max_tokens-capped bursts (3 x ~12 tokens) — the
proof is the amount an attacker CAN burn, not the amount you burn. If still 200 no-key, 0
429, max_tokens honored → the drain is a REAL compromise (financial+avail DoS of operator's
own upstream billing accounts, which /status?json=1 already leak: crypto-billing, Anthropic
fleet, etc.). Score it as a genuine compromise, not just "free AI."

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
