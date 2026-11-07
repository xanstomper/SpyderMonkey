# Flaw-family key — ios / guest

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-flaw-family-key.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ios** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| # | Family | Canonical primitive |
|---|---|---|
| 1 | Validation-order | gate runs after the protected step |
| 2 | Trust-in-client-params | server adopts client-supplied claims |
| 3 | Type-coercion | parser accepts what the validator counted differently |
| 4 | Rate-limiter scope/keying | limiter keys on the wrong identity axis |
| 5 | State-machine gaps | steps skippable / order-forgeable |
| 6 | Identifier trust | client-controlled or predictable IDs |
| 7 | Cache/edge separation | edge caches or mutates what origin didn't |
| 8 | Session/cookie confusion | cookie scoping/semantics diverge from intent |
| 9 | Header/parser differential | the two ends disagree on the message |
| 10 | Entropy/forge | tokens/keys weaker than claimed |
| 11 | Observable-oracle | errors/timing leak what should stay hidden |
| 12 | LLM data-plane | model state leaks or mutates across callers |
| 13 | **Cloud-misconfig** | identity/policy/object-store misconfiguration grants access |
| 14 | **Network-protocol** | the service protocol trusts the anonymous client |
| 15 | **Database-exposure** | a data engine is reachable without a valid identity |
| 16 | **Mobile-device** | package/deep-link/update-path trust abuse |
| 17 | **Firmware-hardware** | device trust-chain gaps (console, OTA, vendor defaults) |
| 18 | **Wireless-RF** | the medium's trust assumptions (WPS, pairing, broadcast) |
| 19 | **Collab-webhook** | app-to-app trust (webhooks, grants, bots) abused |
| 20 | **Operational-planes** | monitoring/orchestration plane reachable unauthenticated |

## Probe adjustment (ios × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
