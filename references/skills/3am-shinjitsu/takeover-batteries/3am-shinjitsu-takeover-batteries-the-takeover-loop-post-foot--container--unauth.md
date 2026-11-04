# The takeover loop (post-foothold cadence) — container / unauth

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-the-takeover-loop-post-foot.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **unauth** · chain role **final**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

```
primitive confirmed → OP-ESCALATE consumer hunt → foothold landed →
T1..T7 applicable battery → decisive proof → chain hop recorded →
re-score remaining expansion vectors (§14) → next hop or TAKEOVER certification
```
Negatives are hops too: a key that fails on the next host is ledgered with the exact
test — never re-probed without a target change (canon).

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
