# Technique: rate-limit brute test (reusable) — websocket / high-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-technique-rate-limit-brute-t.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

For any code-exchange/token endpoint: 15–20 rapid POSTs with garbage codes in a shell loop, collect `-w "%{http_code}"`. All 401/400 with zero 429 = brute surface open. Confirm uniform error strings (no oracle), note entropy/TTL as the unknown.

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
