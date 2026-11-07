# The purple contract — wasm / machine

- source canon: `kage/mirror-playbook.md`
- base technique: `kage-mirror-playbook-the-purple-contract.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **wasm** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. mirror: family CONFIRMED → rule (id, ATT&CK, log source, Sigma YAML)
2. telemetry: the registry of what the operator CAN see
3. validate: rc=1 while any rule lacks a live source — the gap list is the deliverable
4. report: the handoff artifact (rules + telemetry map)

## Probe adjustment (wasm × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
