# 9.1 Breach-context search (score 80) — browser / machine

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-1-breach-context-sea.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **browser** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `web_search <target> breach leak ransomware` + ransomware.live + Breachsense-class trackers
  + news. Corroborate what the victim CONFIRMED ("withdrawal requests were added to the
  database" = proven DB-write access) before theorizing.
- FULL WORKED CASE: `case-example-target-adjacent-infra.md` (holyshit refs, normative by reference).

## Probe adjustment (browser × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
