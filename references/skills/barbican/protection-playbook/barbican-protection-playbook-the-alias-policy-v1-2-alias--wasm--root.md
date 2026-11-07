# The alias policy (v1.2 — `alias`) — wasm / root

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-alias-policy-v1-2-alias.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **wasm** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Derivation: `ghost-` + first 6 hex of sha256(`target#epoch`) — deterministic
  per target+epoch, stable across sessions, no randomness to lose.
- Rotation: `--rotate` bumps the epoch → new alias per engagement window. The
  posture's `--alias` (human-chosen) always wins over the derived suggestion.
- Artifacts carry the alias, NEVER the operator identity — and `sanitize` is the
  enforcement pass that makes it true on disk.

## Probe adjustment (wasm × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
