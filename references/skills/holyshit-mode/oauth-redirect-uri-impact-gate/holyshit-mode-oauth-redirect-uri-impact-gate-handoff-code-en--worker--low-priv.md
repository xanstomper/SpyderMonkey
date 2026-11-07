# Handoff-code entropy — unbruteforceable to size blind — worker / low-priv

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-handoff-code-en.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **low-priv** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

A one-time handoff code exchanged at `/api/auth/platform-handoff/exchange` (code → Supabase access+refresh tokens) is a juicy target, but you CANNOT size its entropy without observing one real code. Uniform `401 invalid_handoff_code` on garbage gives no format/length oracle. The `/start` endpoint requires a valid refresh_token to mint a code — pre-auth you can't generate one.

Log it as "brute surface open, entropy unknown" and move on. Sizing needs one authenticated session to trigger a real handoff and observe the code format in the redirect URL.

## Probe adjustment (worker × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
