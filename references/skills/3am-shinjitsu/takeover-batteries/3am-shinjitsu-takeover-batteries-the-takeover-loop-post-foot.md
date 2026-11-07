# The takeover loop (post-foothold cadence)

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

```
primitive confirmed → OP-ESCALATE consumer hunt → foothold landed →
T1..T7 applicable battery → decisive proof → chain hop recorded →
re-score remaining expansion vectors (§14) → next hop or TAKEOVER certification
```
Negatives are hops too: a key that fails on the next host is ledgered with the exact
test — never re-probed without a target change (canon).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
