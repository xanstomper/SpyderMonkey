# 4. Confirm the ONE surviving compromise (bounded, never drain) — browser / high-priv

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **browser** · auth **high-priv** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The unauthenticated unlimited proxy is the crown jewel when the other compression classes
hold. Re-verify it is STILL live with tiny max_tokens-capped bursts (3 x ~12 tokens) — the
proof is the amount an attacker CAN burn, not the amount you burn. If still 200 no-key, 0
429, max_tokens honored → the drain is a REAL compromise (financial+avail DoS of operator's
own upstream billing accounts, which /status?json=1 already leak: crypto-billing, Anthropic
fleet, etc.). Score it as a genuine compromise, not just "free AI."

## Probe adjustment (browser × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
