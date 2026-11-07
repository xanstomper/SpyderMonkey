# Platform-handoff flow — mesh / high-priv

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-platform-handoff-flow.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mesh** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`POST /api/auth/platform-handoff/start` with `{refresh_token, next, target}` + `Authorization: Bearer <session>` mints handoff codes:
- Codes: 32-hex chars (~128 bits, UUIDv4-like), 60s TTL, replayable WITHIN TTL (single-use after expiry).
- `target` accepts arbitrary values (admin, platform, internal, chat, sillytavern...) even for unverified low-priv users; codes are host-specific on exchange (platform.* host exchanges platform-target codes).
- Use for session-fixation / code-theft chains when a victim URL fragment can be intercepted.

## Probe adjustment (mesh × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
