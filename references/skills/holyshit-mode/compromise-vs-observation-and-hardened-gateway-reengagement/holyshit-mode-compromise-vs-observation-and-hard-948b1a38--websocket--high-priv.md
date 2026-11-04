# Relationship to prior sessions — websocket / high-priv

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The obsidian ledger's top-scored items (cross-user poisoning 95, shared-buffer disclosure 85)
were genuine compromises on 2026-10-05 but are now PATCHED (PTOK constant). Re-asserting them
as current findings without a fresh PTOK-drift test would be a stale-finding error. The
data-plane session (case-obsidian-y-api-dataplane.md) added observation-class findings; this
is the compromise-scored companion.

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
