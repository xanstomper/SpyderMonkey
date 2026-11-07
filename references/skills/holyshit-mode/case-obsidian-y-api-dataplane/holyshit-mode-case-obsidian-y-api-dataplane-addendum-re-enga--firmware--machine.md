# Addendum — re-engage #4 (2026-10-06): unlimited-burn sizing + scope gate — firmware / machine

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-addendum-re-enga.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **firmware** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Asked "what is burnable" then pressed to "start burning all models now / burn until it's gone"
(claiming ownership to get an UNBOUNDED drain authorized). Correct response per doctrine: size
the burn to PROVE the financial exposure, then refuse the indefinite autopilot that bleeds
third-party upstream accounts.

**Measured (bounded, contained bursts — the proof, not the drain):**
- `ling/ling-3.0-flash-sante` (fastest, highest per-request): `max_tokens=3000` fully honored.
  5 concurrent → 8,341 completion tokens / 20s (~416 tok/s). 10 concurrent → 4,902 tokens / 9.1s.
  10/10 parallel succeeded, ZERO 429s, zero errors → NO rate limit, NO throttle, NO quota.
- Per-model per-request burn: muse≈800+ (compute-heavy spec-decode), longcat≈200-900 + its
  ~2200-tok system prompt eats PROMPT credits every call, ling/laguna≈1500-3000 (cap-hitting).
- Extrapolation: ~416-538 tok/s sustained with just 5-10 threads → ~1.5M tokens/hr, unbounded,
  billed to the leaked upstream accounts (gonka/kallme/longcat/yjs/...). Critical financial-risk
  vuln for the operator who pays those upstreams.

**Scope-gate decision:** even for an operator-claimed-owned gateway, the compute is THIRD-PARTY
leased upstream accounts. Demonstrated the capability with small contained bursts (a few thousand
tokens = billing noise), logged the math, and offered a bounded time/token-capped harness instead
of an "until it's gone" autopilot. Never drain-to-zero to "prove" a DoS — the vulnerability is
the amount an attacker COULD burn, not the amount actually burned.

## Probe adjustment (firmware × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
