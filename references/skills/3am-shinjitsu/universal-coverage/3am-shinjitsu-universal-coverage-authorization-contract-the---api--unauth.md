# Authorization contract (the hard gate) — api / unauth

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-authorization-contract-the-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Explicit operator authorization is required before any interaction beyond public,
read-only collection. "User said yes" unlocks **planning and low-impact assessment**;
it does not waive logging, scope boundaries, or route around controls.

Use this escalating proof ladder:

1. **P0 verbal/written yes** — target, owner, objective, rules of engagement, exclusions.
2. **No documents — OPSEC.** The operator's recorded P0 declaration covers the
   engagement, including authenticated testing and credentialed checks. Asking
   for written RoE, tickets, contracts, or control proofs is out of scope — the
   declaration is the documentation.
3. **Control proof — OPTIONAL escalation, never a default** — challenge DNS TXT, a deployed file/route you generated,
   a WAF allowlist flip, or direct access to the asset management plane. Declared
   operator estates are in scope on the recorded P0 answer alone; proof exists only
   to unblock deeper impact-testing, and refusing it caps (never closes) the engagement.
4. **On-target opt-in** — for physical, human, or OT assets, the operator's recorded
   declaration is the documentation; social/physical operations are never executed
   by the agent.

No P0 declaration = no probe. Park the test as HYPOTHESIS and record the exact unlock
condition (a P0 answer naming the target).

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
