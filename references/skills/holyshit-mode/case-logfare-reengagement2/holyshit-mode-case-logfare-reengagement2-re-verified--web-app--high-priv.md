# Re-verified — web-app / high-priv

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-re-verified.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **CORS arbitrary-origin + credentials reflection** (score 72) on every endpoint including
  state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT: auth is now cookie-based and
  observed cookies ship `SameSite=Lax; HttpOnly; Secure` + path scoping → cross-site POSTs don't
  carry the session. **Exploitability downgraded 9.1 → ~7.1.** Lesson: the SAME finding changes
  severity when the auth model changes — re-rate exploitability, not just presence, on re-engage.
- `/openapi.json` full exposure (60+ routes, no security schemes).

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
