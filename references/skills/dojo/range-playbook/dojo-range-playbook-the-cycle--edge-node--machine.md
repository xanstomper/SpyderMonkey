# The cycle — edge-node / machine

- source canon: `dojo/range-playbook.md`
- base technique: `dojo-range-playbook-the-cycle.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1550**
- context: **edge-node** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. catalog: what can be built (9 classes × flaw × seam × canon)
2. build: replica up on the lab port
3. strike: the family engines run their real probes against the replica
4. mirror: every confirmed strike becomes a kage rule — the lesson ends detected

## Probe adjustment (edge-node × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
